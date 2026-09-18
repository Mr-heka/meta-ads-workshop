#!/usr/bin/env python3
"""
smart-reframe self-test: proves the crop CENTRES ON A KNOWN SUBJECT (not just
that the output is the right size), across the tracking tiers that are actually
installed, and that the crop SNAPS at a hard cut instead of panning across it.

Three checks (each skips cleanly if its deps aren't present):

  1. MOTION tier (opencv): a bright box sweeps left->right over a DARK frame
     (clean background). Proves the motion-energy centroid keeps the box framed.
     This is the floor the motion tier is honestly sold for: one mover, clean bg.

  2. BEST tier (ultralytics installed): a REAL person cut-out sweeps over a BUSY
     moving background (testsrc2). This is the hard case the motion tier can't
     do - it proves YOLOv11 LOCKS A PERSON and follows them even with competing
     background motion. Skipped (not failed) when ultralytics is absent.

  3. CUT-SNAP (opencv): a 2-shot clip (subject on the LEFT in shot 1, on the
     RIGHT in shot 2, with a hard cut between). Proves the crop jumps to the new
     subject at the cut rather than smearing across it - the per-shot reset that
     differentiates this from a dumb sliding window. Falls back to a fixed split
     if PySceneDetect can't see the cut, so the snap logic is exercised either
     way and we report which path ran.

Run:  python3 scripts/selftest.py
Exit: 0 = every available check passed; 1 = a regression in any check.

Needs: ffmpeg/ffprobe + opencv + numpy. ultralytics enables check 2.
"""

import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def sh(cmd):
    subprocess.run(cmd, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def run_reframe(src, out, extra=None):
    cmd = [sys.executable, os.path.join(HERE, "reframe.py"),
           "--in", src, "--out", out, "--ar", "9:16"]
    if extra:
        cmd += extra
    subprocess.run(cmd, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def bright_centroid_norm(frame, np, cv2, thresh=180):
    """Brightest-region centre as (cx_norm, cy_norm), or None if nothing bright."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = (gray > thresh).astype("float64")
    tot = mask.sum()
    if tot < 50:
        return None
    h, w = gray.shape
    cx = float((mask.sum(axis=0) * np.arange(w)).sum() / tot) / w
    cy = float((mask.sum(axis=1) * np.arange(h)).sum() / tot) / h
    return (cx, cy)


def worst_off_centre(out, np, cv2, finder):
    """Max horizontal distance of the detected subject from crop centre over the
    sampled output frames. 0 = dead centre, 0.5 = at the crop edge, 1.0 = gone."""
    cap = cv2.VideoCapture(out)
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 150
    worst, checked = 0.0, 0
    for f in range(10, n - 10, 12):
        cap.set(cv2.CAP_PROP_POS_FRAMES, f)
        ok, frame = cap.read()
        if not ok:
            break
        cen = finder(frame, np, cv2)
        if cen is None:
            worst = max(worst, 1.0)          # subject missing = worst-case drift
        else:
            worst = max(worst, abs(cen[0] - 0.5))
        checked += 1
    cap.release()
    return worst, checked


# ---------------------------------------------------------------------------
# check 1 - MOTION tier on a clean background
# ---------------------------------------------------------------------------

def check_motion(work, np, cv2):
    src = os.path.join(work, "sweep.mp4")
    out = os.path.join(work, "sweep_9x16.mp4")
    sh(["ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=black:s=1280x720:d=6:r=25",
        "-f", "lavfi", "-i", "color=c=white:s=160x320:d=6:r=25",
        "-f", "lavfi", "-i", "sine=frequency=300:duration=6",
        "-filter_complex", "[0:v][1:v]overlay=x='160+800*t/6':y=200[v]",
        "-map", "[v]", "-map", "2:a",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
        "-shortest", src])
    run_reframe(src, out)
    if not os.path.exists(out):
        print("[selftest] motion: FAIL (no output)")
        return False
    worst, checked = worst_off_centre(out, np, cv2, bright_centroid_norm)
    print(f"[selftest] motion (clean bg): {checked} frames, "
          f"worst off-centre {worst:.3f} (gate 0.30)")
    if worst > 0.30:
        print("[selftest] motion: FAIL - subject drifted toward the crop edge")
        return False
    print("[selftest] motion: PASS")
    return True


# ---------------------------------------------------------------------------
# check 2 - BEST tier: real person over a BUSY background (needs ultralytics)
# ---------------------------------------------------------------------------

def check_best(work, np, cv2):
    try:
        import ultralytics  # noqa: F401
    except ImportError:
        print("[selftest] best (person lock): SKIP - ultralytics not installed "
              "(run reframe.py --best to install + exercise this tier)")
        return None
    # cut one real person out of the ultralytics sample, sweep over testsrc2.
    import urllib.request
    bus = os.path.join(work, "bus.jpg")
    try:
        urllib.request.urlretrieve("https://ultralytics.com/images/bus.jpg", bus)
    except Exception as e:
        print(f"[selftest] best: SKIP - could not fetch person fixture ({e})")
        return None
    cut = os.path.join(work, "person.png")
    # the highest-confidence person box in bus.jpg
    sh(["ffmpeg", "-y", "-i", bus, "-vf", "crop=140:484:671:395", cut])
    src = os.path.join(work, "person_sweep.mp4")
    out = os.path.join(work, "person_9x16.mp4")
    sh(["ffmpeg", "-y",
        "-f", "lavfi", "-i", "testsrc2=s=1280x720:d=6:r=25",
        "-i", cut,
        "-f", "lavfi", "-i", "sine=frequency=220:duration=6",
        "-filter_complex",
        "[1:v]scale=140:484[p];[0:v][p]overlay=x='80+900*t/6':y=120[v]",
        "-map", "[v]", "-map", "2:a",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
        "-shortest", src])
    run_reframe(src, out, extra=["--best"])
    if not os.path.exists(out):
        print("[selftest] best: FAIL (no output)")
        return False
    # the person cut-out is darker/textured, not a bright box -> detect via the
    # output crop following the person: a correctly-locked crop keeps the person
    # near centre. We re-run the tracker and compare to ground truth directly.
    sys.path.insert(0, HERE)
    import reframe as R
    mods = R.maybe_install(True, best=True)
    w, h, fps, dur = R.ffprobe_stream(src)
    pts = R.subject_path(src, w, h, fps, mods, False)
    if "ultralytics" not in mods:
        print("[selftest] best: SKIP - ultralytics import failed after install")
        return None
    xs = [p[1] for p in pts]
    # ground truth: person centre sweeps (80+70)/1280=0.117 -> (980+70)/1280=0.820
    err_start = abs(xs[0] - 0.117)
    err_end = abs(xs[-1] - 0.820)
    print(f"[selftest] best (person/busy bg): tracked cx {xs[0]:.3f}->{xs[-1]:.3f} "
          f"vs truth 0.117->0.820 (err {err_start:.3f}/{err_end:.3f}, gate 0.08)")
    if err_start > 0.08 or err_end > 0.08:
        print("[selftest] best: FAIL - YOLO lock did not follow the person")
        return False
    print("[selftest] best: PASS - person locked through a busy background")
    return True


# ---------------------------------------------------------------------------
# check 3 - CUT-SNAP: crop jumps at a hard cut, doesn't pan across it
# ---------------------------------------------------------------------------

def check_cut_snap(work, np, cv2):
    src = os.path.join(work, "cut.mp4")
    out = os.path.join(work, "cut_9x16.mp4")
    # shot 1 (0-3s): bright box jittering on the LEFT.  shot 2 (3-6s): box
    # jittering on the RIGHT. Hard cut at 3s. The small jitter gives the
    # motion-energy tier something to lock (a dead-static box has zero motion),
    # while the box stays firmly in its half so a correct per-shot crop sits
    # left then right. A crop that pans across the cut lands mid-frame instead.
    sh(["ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=black:s=1280x720:d=3:r=25",
        "-f", "lavfi", "-i", "color=c=white:s=200x360:d=3:r=25",
        "-filter_complex", "[0:v][1:v]overlay=x='120+30*sin(8*t)':y=180[a]",
        "-map", "[a]", "-c:v", "libx264", "-pix_fmt", "yuv420p",
        os.path.join(work, "s1.mp4")])
    sh(["ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=black:s=1280x720:d=3:r=25",
        "-f", "lavfi", "-i", "color=c=white:s=200x360:d=3:r=25",
        "-filter_complex", "[0:v][1:v]overlay=x='930+30*sin(8*t)':y=180[a]",
        "-map", "[a]", "-c:v", "libx264", "-pix_fmt", "yuv420p",
        os.path.join(work, "s2.mp4")])
    # concat (re-encode so the cut is a real hard boundary) + add audio
    sh(["ffmpeg", "-y",
        "-i", os.path.join(work, "s1.mp4"),
        "-i", os.path.join(work, "s2.mp4"),
        "-f", "lavfi", "-i", "sine=frequency=300:duration=6",
        "-filter_complex", "[0:v][1:v]concat=n=2:v=1:a=0[v]",
        "-map", "[v]", "-map", "2:a", "-shortest",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", src])

    # how many shots did the tracker actually see?
    sys.path.insert(0, HERE)
    import reframe as R
    mods = R.maybe_install(False)
    w, h, fps, dur = R.ffprobe_stream(src)
    shots = R.detect_shots(src, dur, mods)
    via = "PySceneDetect" if len(shots) > 1 else "fixed-split fallback"
    if len(shots) <= 1:
        # AdaptiveDetector can miss a flat-colour cut; force the known split so
        # the SNAP logic is still exercised and reported honestly.
        shots = [(0.0, 3.0), (3.0, dur)]

    pts = R.subject_path(src, w, h, fps, mods, False)
    crop_w = int(round(h * 9 / 16)); crop_w -= crop_w % 2
    sm = R.smooth_per_shot(pts, shots, crop_w, w, fps, crop_h=h, src_h=h)
    # crop CENTRE per sample, normalised
    centres = [((x + crop_w / 2.0) / w, t) for (t, x, _y) in sm]
    early = [c for c, t in centres if t < 2.5]          # settled in shot 1
    late = [c for c, t in centres if t > 3.5]           # settled in shot 2
    if not early or not late:
        print("[selftest] cut-snap: SKIP - too few samples per shot")
        return None
    # shot1 box centre ~= (120+30+100)/1280=0.195 ; shot2 ~= (930+30+100)/1280=0.828
    e_med = sorted(early)[len(early) // 2]
    l_med = sorted(late)[len(late) // 2]
    jump = abs(l_med - e_med)
    print(f"[selftest] cut-snap (via {via}): crop centre {e_med:.3f} (shot1) -> "
          f"{l_med:.3f} (shot2), jump {jump:.3f} (gate >=0.30)")
    if e_med > 0.45 or l_med < 0.55 or jump < 0.30:
        print("[selftest] cut-snap: FAIL - crop did not snap to the new subject")
        return False
    print("[selftest] cut-snap: PASS - crop snapped at the cut, no pan across it")
    return True


def main():
    try:
        import cv2
        import numpy as np
    except ImportError:
        print("[selftest] SKIP: opencv/numpy not installed "
              "(run reframe.py --auto-install first)")
        return 0

    work = tempfile.mkdtemp(prefix="srselftest_")
    results = []
    for name, fn in (("motion", check_motion),
                     ("best", check_best),
                     ("cut-snap", check_cut_snap)):
        try:
            results.append((name, fn(work, np, cv2)))
        except Exception as e:
            print(f"[selftest] {name}: ERROR {e}")
            results.append((name, False))

    ran = [r for _, r in results if r is not None]
    failed = [n for n, r in results if r is False]
    skipped = [n for n, r in results if r is None]
    print(f"\n[selftest] ran {len(ran)} check(s); "
          f"skipped {skipped or 'none'}; failed {failed or 'none'}")
    if failed:
        return 1
    if not ran:
        print("[selftest] nothing ran (no deps) - inconclusive")
        return 0
    print("[selftest] PASS: every available tracking check held")
    return 0


if __name__ == "__main__":
    sys.exit(main())
