#!/usr/bin/env python3
"""
smart-reframe - headless, shot-aware horizontal->vertical reframe (no NLE).

QUALITY-BAR rule 11: the crop must FOLLOW the subject. A static centre-crop
loses the person the moment they move; a pan that tracks the subject keeps them
framed. This script:

  1. Splits the source into SHOTS  (PySceneDetect AdaptiveDetector) so the crop
     never pans across a hard cut.
  2. Finds the SUBJECT per frame   (YOLOv11 person box -> MediaPipe face if a
     model is present; falls back to a motion-energy centroid, then to centre).
  3. Smooths the path per shot      (deadband + EMA + max-velocity clamp) so the
     crop glides, never jitters, and snaps to a new centre only at a cut.
  4. Crops + pans headlessly        (ffmpeg crop with a time-keyed x/y expression
     driven by sendcmd) into 9:16 / 1:1 / 4:5, scaled to the target canvas.

Deterministic, local, free. No Resolve, no Premiere, no cloud, no credits.
The cloud subject-aware fallback (Higgsfield `reframe` MCP) is documented in
SKILL.md and is what to reach for when no GPU/models are available.

Deps (auto-installable with --auto-install):
  ffmpeg/ffprobe (system, Homebrew)              REQUIRED
  pip: scenedetect>=0.7  opencv-python  numpy    REQUIRED (shot + motion path)
  pip: ultralytics (YOLOv11)                      OPTIONAL (best subject lock)
  pip: mediapipe                                  OPTIONAL (face refine)
Without ultralytics/mediapipe the script still tracks via motion energy, which
is good for a single talking subject; it degrades gracefully to centre-crop only
if even OpenCV is missing.

Usage:
  reframe.py --in input.mov --out out_916.mp4 --ar 9:16
  reframe.py --in input.mov --outdir ./vert --ar 9:16,1:1,4:5
  reframe.py --in input.mov --out out.mp4 --ar 9:16 --auto-install
  reframe.py --in input.mov --out out.mp4 --ar 9:16 --static   # disable tracking

Self-heal / version-gate (QUALITY-BAR rule 14): every output is read back with
ffprobe and the dimensions + duration are asserted against the request. A wrong
size or a truncated file STOPS loudly instead of shipping a broken vertical.
"""

import argparse
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile

# ----------------------------------------------------------------------------
# small helpers
# ----------------------------------------------------------------------------

AR_MAP = {
    "9:16": (9, 16),
    "1:1": (1, 1),
    "4:5": (4, 5),
}

# --- tracking / smoothing tunables (defaults; --best lock is the precise tier) -
# YOLO person-box confidence floor: drop weak boxes so background clutter, a
# poster, or a half-frame edge artefact can't forge a false person lock. 0.40 is
# conservative; a clean talking head sits well above it (~0.85-0.90 measured).
YOLO_MIN_CONF = 0.40
# Path smoother defaults (one profile; documented, not magic):
EMA_ALPHA = 0.35           # two-pass centred EMA strength (higher = snappier)
DEADBAND_FRAC = 0.05       # ignore subject wobble under 5% of the crop span
MAX_VEL_FRAC = 0.45        # per-axis pan speed cap as a fraction of source size/s
# --best YOLO subject lock is the precise path; these constants only govern the
# motion-energy tier and the smoother that sits in front of either source.


def die(msg):
    print(f"\n[smart-reframe] STOP: {msg}\n", file=sys.stderr)
    sys.exit(1)


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def ensure_ffmpeg():
    for b in ("ffmpeg", "ffprobe"):
        if not shutil.which(b):
            die(f"{b} not found. Install with: brew install ffmpeg")


def pip_install(pkg):
    """
    pip-install one package, surviving PEP 668 'externally-managed' Pythons
    (Homebrew / modern macOS+Linux) WITHOUT crashing.

    Order of attempts:
      1. plain `pip install` (works on venvs / non-managed Pythons)
      2. `--break-system-packages --user` (the documented PEP 668 escape hatch)
    Returns True on success, False if every attempt failed -> caller degrades
    to the next tracking tier instead of throwing a traceback.
    """
    base = [sys.executable, "-m", "pip", "install", "-q", pkg]
    attempts = [base, base + ["--break-system-packages", "--user"]]
    for cmd in attempts:
        try:
            subprocess.run(cmd, check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    return False


def maybe_install(auto, best=False):
    """
    Import the python deps; pip-install the missing ones if --auto-install is set.
    --best also pulls the YOLOv11 + MediaPipe person-lock tier. A failed install
    never crashes: it prints a one-line note and the caller degrades a tier.
    """
    mods = {}
    wanted = [("scenedetect", "scenedetect>=0.7"),
              ("cv2", "opencv-python"),
              ("numpy", "numpy")]
    if best:
        wanted += [("ultralytics", "ultralytics"),
                   ("mediapipe", "mediapipe")]
    for mod, pkg in wanted:
        try:
            mods[mod] = __import__(mod)
            continue
        except ImportError:
            pass
        if not auto:
            continue
        print(f"[smart-reframe] installing {pkg} ...")
        if not pip_install(pkg):
            print(f"[smart-reframe] could not install {pkg} "
                  f"(continuing without it - tracking will degrade a tier)")
            continue
        try:
            mods[mod] = __import__(mod)
        except ImportError:
            print(f"[smart-reframe] {pkg} installed but not importable yet "
                  f"(continuing without it)")
    return mods


def ffprobe_stream(path):
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height,r_frame_rate,nb_frames",
             "-show_entries", "format=duration",
             "-of", "json", path],
            capture_output=True, text=True, check=True).stdout
        j = json.loads(out)
        st = j["streams"][0]
    except (subprocess.CalledProcessError, json.JSONDecodeError,
            KeyError, IndexError):
        die(f"could not read a video stream from {path} "
            f"(corrupt file, or no video track?)")
    num, den = st["r_frame_rate"].split("/")
    fps = float(num) / float(den) if float(den) else 25.0
    dur = float(j.get("format", {}).get("duration") or 0.0)
    if dur <= 0:
        die(f"{path}: zero/unknown duration (corrupt or unreadable)")
    return int(st["width"]), int(st["height"]), fps, dur


# ----------------------------------------------------------------------------
# 1. shots  (PySceneDetect) -- never pan a crop across a hard cut
# ----------------------------------------------------------------------------

def detect_shots(path, dur, mods):
    """Return list of (start_s, end_s). One element = whole clip if unavailable."""
    if "scenedetect" not in mods or "cv2" not in mods:
        return [(0.0, dur)]
    from scenedetect import open_video, SceneManager
    from scenedetect.detectors import AdaptiveDetector
    video = open_video(path)
    sm = SceneManager()
    sm.add_detector(AdaptiveDetector())          # KB: PySceneDetect 0.7 Adaptive
    sm.detect_scenes(video)
    scenes = sm.get_scene_list()
    if not scenes:
        return [(0.0, dur)]
    return [(s.get_seconds(), e.get_seconds()) for s, e in scenes]


# ----------------------------------------------------------------------------
# 2. subject centre per sampled frame
# ----------------------------------------------------------------------------

def load_yolo(mods):
    if "ultralytics" not in mods:
        return None
    try:
        from ultralytics import YOLO
        return YOLO("yolo11n.pt")               # KB: YOLOv11 (nano, auto-pulls)
    except Exception:
        return None


def load_face(mods):
    """
    MediaPipe face detector for the face-refine step (best tier), wrapped so it
    works across the two MediaPipe API generations and degrades cleanly if
    neither is usable:
      - legacy Solutions API (`mp.solutions.face_detection`) on builds that
        still ship it (<=Python 3.12 wheels),
      - new Tasks API (`mediapipe.tasks.python.vision.FaceDetector`) on newer
        builds (e.g. mediapipe 0.10.x on Python 3.13/3.14) where `mp.solutions`
        was dropped. The Tasks detector needs a .tflite model bundle; if it is
        not present and cannot be fetched, we skip face-refine rather than crash.
    Returns a callable refine(roi_bgr) -> (cx_frac, cy_frac) in [0,1] of the
    ROI, or None when no face is found. Returns None (the whole loader) when
    face-refine is unavailable, in which case the Best tier is YOLO-box-only -
    still a real person lock, just centred on the body box rather than the head.
    """
    if "mediapipe" not in mods:
        return None
    # --- legacy Solutions API ------------------------------------------------
    try:
        import mediapipe as mp
        if hasattr(mp, "solutions") and hasattr(mp.solutions, "face_detection"):
            det = mp.solutions.face_detection.FaceDetection(
                model_selection=1, min_detection_confidence=0.5)

            def refine_legacy(roi_rgb):
                fr = det.process(roi_rgb)
                if fr and fr.detections:
                    rb = fr.detections[0].location_data.relative_bounding_box
                    return (rb.xmin + rb.width / 2.0, rb.ymin + rb.height / 2.0)
                return None
            return ("legacy", refine_legacy)
    except Exception:
        pass
    # --- new Tasks API -------------------------------------------------------
    try:
        from mediapipe.tasks import python as mp_python
        from mediapipe.tasks.python import vision as mp_vision
        import mediapipe as mp
        model_path = _ensure_face_model()
        if not model_path:
            return None
        opts = mp_vision.FaceDetectorOptions(
            base_options=mp_python.BaseOptions(model_asset_path=model_path),
            min_detection_confidence=0.5)
        det = mp_vision.FaceDetector.create_from_options(opts)

        def refine_tasks(roi_rgb):
            mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=roi_rgb)
            res = det.detect(mp_img)
            if res and res.detections:
                bb = res.detections[0].bounding_box
                rh, rw = roi_rgb.shape[0], roi_rgb.shape[1]
                cx = (bb.origin_x + bb.width / 2.0) / rw
                cy = (bb.origin_y + bb.height / 2.0) / rh
                return (cx, cy)
            return None
        return ("tasks", refine_tasks)
    except Exception:
        return None


# MediaPipe Tasks face detector model (BlazeFace short-range). Cached once.
_FACE_MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/"
                   "face_detector/blaze_face_short_range/float16/1/"
                   "blaze_face_short_range.tflite")


def _ensure_face_model():
    """Return a local path to the Tasks FaceDetector model, fetching it once;
    None if it cannot be obtained (face-refine then silently skipped)."""
    cache = os.path.join(os.path.expanduser("~"), ".cache", "smart-reframe")
    dst = os.path.join(cache, "blaze_face_short_range.tflite")
    if os.path.exists(dst) and os.path.getsize(dst) > 0:
        return dst
    try:
        os.makedirs(cache, exist_ok=True)
        import urllib.request
        urllib.request.urlretrieve(_FACE_MODEL_URL, dst)
        return dst if os.path.getsize(dst) > 0 else None
    except Exception:
        return None


def _motion_centroid(diff, np, prev_xy, w, h):
    """
    Subject-gated motion centroid. Plain column/row sums get yanked off the
    person by ANY background motion (a window, a screen, camera shake). We gate
    the motion map so a clear single mover still wins, but competing background
    motion can't drag the lock away:
      - a GENTLE centre prior (wide Gaussian on a high floor) - it barely biases a
        single dominant subject, but breaks ties toward the middle when motion is
        scattered,
      - temporal continuity: strong extra weight near the PREVIOUS subject
        position so the lock sticks to one blob instead of jumping between movers.
    Returns (cx_norm, cy_norm) or None if there isn't enough motion to trust.
    """
    if diff.sum() < 1e3:
        return None
    ys = np.arange(h, dtype="float64").reshape(h, 1)
    xs = np.arange(w, dtype="float64").reshape(1, w)
    # GENTLE centre prior: wide sigma + 0.6 floor -> ranges only 0.6..1.0, so a
    # clear single subject dominates; it only matters when motion is ambiguous.
    sx, sy = w / 1.5, h / 1.5
    prior = 0.6 + 0.4 * np.exp(-(((xs - w / 2.0) ** 2) / (2 * sx * sx)
                                 + ((ys - h / 2.0) ** 2) / (2 * sy * sy)))
    weight = prior
    # temporal continuity dominates once we have a lock: weight motion near the
    # last known subject far more than anywhere else.
    if prev_xy is not None:
        px, py = prev_xy[0] * w, prev_xy[1] * h
        tx, ty = w / 4.0, h / 4.0
        cont = np.exp(-(((xs - px) ** 2) / (2 * tx * tx)
                        + ((ys - py) ** 2) / (2 * ty * ty)))
        weight = prior * (0.25 + 1.5 * cont)
    m = diff.astype("float64") * weight
    tot = m.sum()
    if tot < 1e3:
        return None
    cx = float((m.sum(axis=0) * np.arange(w)).sum() / tot) / w
    cy = float((m.sum(axis=1) * np.arange(h)).sum() / tot) / h
    return (cx, cy)


def subject_path(path, w, h, fps, mods, use_static):
    """
    Sample ~6 fps and return [(t_seconds, cx_norm, cy_norm)] where (cx,cy) in
    [0,1] is the subject centre. Tracking precedence:
      YOLOv11 person box (+ MediaPipe face refine) -> subject-gated motion
      centroid -> frame centre.
    We track BOTH axes so the squarer crops (1:1, 4:5) can also pan vertically
    when the source is tall enough to need it.
    """
    if use_static or "cv2" not in mods:
        return [(0.0, 0.5, 0.5)]
    import cv2
    import numpy as np

    yolo = load_yolo(mods)
    face = load_face(mods)
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        return [(0.0, 0.5, 0.5)]

    step = max(1, int(round(fps / 6.0)))         # ~6 samples/sec
    idx = 0
    prev_gray = None
    prev_xy = None
    pts = []
    try:
        while True:
            ok = cap.grab()
            if not ok:
                break
            if idx % step == 0:
                ok, frame = cap.retrieve()
                if not ok:
                    break
                fh, fw = frame.shape[0], frame.shape[1]
                cx = cy = None
                if yolo is not None:
                    res = yolo.predict(frame, classes=[0], verbose=False)  # person
                    best, ba, bbox = None, 0.0, None
                    for r in res:
                        for b in r.boxes:
                            conf = float(b.conf[0]) if b.conf is not None else 1.0
                            if conf < YOLO_MIN_CONF:        # gate weak detections
                                continue                    # so noise/clutter can't
                            x1, y1, x2, y2 = b.xyxy[0].tolist()   # forge a false lock
                            a = (x2 - x1) * (y2 - y1)
                            if a > ba:
                                ba = a
                                best = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)
                                bbox = (x1, y1, x2, y2)
                    if best is not None:
                        cx, cy = best[0] / fw, best[1] / fh
                        # face refine: pull the lock toward the head inside the box
                        if face is not None and bbox is not None:
                            _, refine = face
                            x1, y1, x2, y2 = (int(max(0, bbox[0])),
                                              int(max(0, bbox[1])),
                                              int(min(fw, bbox[2])),
                                              int(min(fh, bbox[3])))
                            roi = frame[y1:y2, x1:x2]
                            if roi.size:
                                rc = refine(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
                                if rc is not None:
                                    fcx = x1 + rc[0] * (x2 - x1)
                                    fcy = y1 + rc[1] * (y2 - y1)
                                    cx, cy = fcx / fw, fcy / fh
                if cx is None:                   # subject-gated motion fallback
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    if prev_gray is not None:
                        diff = cv2.absdiff(gray, prev_gray)
                        cen = _motion_centroid(diff, np, prev_xy, fw, fh)
                        if cen is not None:
                            cx, cy = cen
                    prev_gray = gray
                if cx is None:
                    cx, cy = (prev_xy if prev_xy else (0.5, 0.5))
                cx = max(0.0, min(1.0, cx))
                cy = max(0.0, min(1.0, cy))
                prev_xy = (cx, cy)
                pts.append((idx / fps, cx, cy))
            idx += 1
    finally:
        cap.release()
    return pts or [(0.0, 0.5, 0.5)]


# ----------------------------------------------------------------------------
# 3. smooth the path PER SHOT  (deadband + EMA + velocity clamp)
# ----------------------------------------------------------------------------

def _shot_index(shots):
    def shot_of(t):
        for i, (s, e) in enumerate(shots):
            if s - 1e-6 <= t < e + 1e-6:
                return i
        return len(shots) - 1
    return shot_of


def _smooth_axis(targets, max_lo, max_hi, span, max_vel, dt):
    """
    Zero-lag smoother for ONE axis over ONE shot's target positions.

    The old forward-only EMA + hard velocity clamp lagged the subject by ~200px
    on a real sweep and never caught up (it can only ever look backwards). This
    runs a TWO-PASS centred smoother: an EMA forward, an EMA backward, then the
    average. A centred filter has no phase lag, so the crop sits ON the subject,
    not trailing it. A deadband first removes micro-jitter; a per-step velocity
    cap (generous, eased) kills whip pans without re-introducing lag.
    """
    n = len(targets)
    if n == 0:
        return []
    deadband = span * DEADBAND_FRAC
    alpha = EMA_ALPHA
    # deadband pre-pass: hold inside small wobble
    held = [targets[0]]
    for i in range(1, n):
        prev = held[-1]
        held.append(targets[i] if abs(targets[i] - prev) > deadband else prev)
    # forward EMA
    fwd = [held[0]]
    for i in range(1, n):
        fwd.append(fwd[-1] + alpha * (held[i] - fwd[-1]))
    # backward EMA
    bwd = [held[-1]] * n
    for i in range(n - 2, -1, -1):
        bwd[i] = bwd[i + 1] + alpha * (held[i] - bwd[i + 1])
    # centred average = no phase lag
    cen = [(fwd[i] + bwd[i]) / 2.0 for i in range(n)]
    # velocity cap (generous) so the pan is smooth, never a whip
    step_cap = max_vel * dt
    out = [max(max_lo, min(max_hi, cen[0]))]
    for i in range(1, n):
        v = cen[i]
        d = v - out[-1]
        if d > step_cap:
            v = out[-1] + step_cap
        elif d < -step_cap:
            v = out[-1] - step_cap
        out.append(max(max_lo, min(max_hi, v)))
    return out


def smooth_per_shot(pts, shots, crop_w, src_w, fps, crop_h=None, src_h=None):
    """
    Produce smoothed crop top-left (x_px, y_px) per sampled point:
      - resets at every shot boundary (snap, don't pan across a cut),
      - within a shot, a zero-lag two-pass smoother keeps the crop on the
        subject (no trailing lag), deadbanded and velocity-capped.
    Returns sendcmd-ready [(t, x_px, y_px)]. y is tracked only when the source
    is tall enough that the crop doesn't already take the full height.
    """
    pts = [(p[0], p[1], p[2] if len(p) > 2 else 0.5) for p in pts]
    half_w = crop_w / 2.0
    max_x = max(0.0, src_w - crop_w)
    track_y = crop_h is not None and src_h is not None and crop_h < src_h
    half_h = (crop_h / 2.0) if track_y else 0.0
    max_y = max(0.0, (src_h - crop_h)) if track_y else 0.0
    # generous velocity caps: fast enough for a walking subject, still smooth
    max_vel_x = src_w * MAX_VEL_FRAC
    max_vel_y = (src_h * MAX_VEL_FRAC) if track_y else 0.0
    dt = 1.0 / 6.0                       # sampling cadence (~6 fps)
    shot_of = _shot_index(shots)

    out = []
    i = 0
    n = len(pts)
    while i < n:
        sh = shot_of(pts[i][0])
        j = i
        while j < n and shot_of(pts[j][0]) == sh:
            j += 1
        seg = pts[i:j]
        tx = [max(0.0, min(max_x, p[1] * src_w - half_w)) for p in seg]
        sx = _smooth_axis(tx, 0.0, max_x, crop_w, max_vel_x, dt)
        if track_y:
            ty = [max(0.0, min(max_y, p[2] * src_h - half_h)) for p in seg]
            sy = _smooth_axis(ty, 0.0, max_y, crop_h, max_vel_y, dt)
        else:
            sy = [0.0] * len(seg)
        for k, p in enumerate(seg):
            out.append((p[0], sx[k], sy[k]))
        i = j
    return out


def write_sendcmd(path_pts, cmdfile):
    """ffmpeg sendcmd script: re-set crop's x (and y) at each sampled time."""
    with open(cmdfile, "w") as f:
        for (t, x, y) in path_pts:
            f.write(f"{t:.3f} crop x {x:.1f};\n")
            f.write(f"{t:.3f} crop y {y:.1f};\n")


# ----------------------------------------------------------------------------
# 4. crop + pan + scale headlessly with ffmpeg
# ----------------------------------------------------------------------------

def target_canvas(ar, src_h):
    """Vertical/square canvas keyed to source height, even dims, 1080-class out."""
    arw, arh = AR_MAP[ar]
    out_h = src_h if src_h % 2 == 0 else src_h - 1
    out_w = int(round(out_h * arw / arh))
    out_w -= out_w % 2
    # normalise to a 1080-wide-class master where it makes sense
    if ar == "9:16":
        out_w, out_h = 1080, 1920
    elif ar == "1:1":
        out_w, out_h = 1080, 1080
    elif ar == "4:5":
        out_w, out_h = 1080, 1350
    return out_w, out_h


def reframe_one(src, out, ar, w, h, fps, dur, pts, shots, use_static):
    arw, arh = AR_MAP[ar]
    # take the tallest crop window that fits the target ratio inside the source:
    # full height if it fits, else full width with a shorter crop (lets us pan
    # vertically on the squarer 1:1 / 4:5 ratios from a wide source).
    crop_w = int(round(h * arw / arh))
    crop_h = h
    if crop_w > w:
        crop_w = w
        crop_h = int(round(w * arh / arw))
    crop_w -= crop_w % 2
    crop_h -= crop_h % 2
    out_w, out_h = target_canvas(ar, h)

    # upscale-softness gate: the crop window is the real pixel budget. If it is
    # narrower than the 1080-class canvas, ffmpeg lanczos blows it up and the
    # result is visibly soft - a true $5k deliverable needs source pixels >=
    # target, or generative edge-fill. Warn loudly (don't silently ship soft).
    if crop_w < out_w:
        ratio = out_w / float(crop_w)
        print(f"[smart-reframe] WARNING {ar}: crop window is {crop_w}px wide but "
              f"the {out_w}px canvas needs more - this {ratio:.2f}x upscale will "
              f"look soft. Feed a higher-res source (>= {out_w}px after crop), or "
              f"use the Higgsfield 'reframe' cloud fallback for generative "
              f"edge-fill. (SKILL.md -> Cloud fallback.)", file=sys.stderr)

    if use_static or len(pts) <= 1:
        x_expr = f"(in_w-{crop_w})/2"            # static centre column
        y_expr = f"(in_h-{crop_h})/2"            # static centre row
        vf = (f"crop={crop_w}:{crop_h}:{x_expr}:{y_expr},"
              f"scale={out_w}:{out_h}:flags=lanczos,setsar=1")
        filtergraph = vf
        cmdfile = None
    else:
        path_pts = smooth_per_shot(pts, shots, crop_w, w, fps,
                                   crop_h=crop_h, src_h=h)
        cmdfile = tempfile.NamedTemporaryFile(
            "w", suffix=".cmd", delete=False).name
        write_sendcmd(path_pts, cmdfile)
        x0, y0 = path_pts[0][1], path_pts[0][2]
        # crop with runtime-settable x/y, driven by the sendcmd timeline
        vf = (f"sendcmd=f={cmdfile},"
              f"crop={crop_w}:{crop_h}:{x0:.1f}:{y0:.1f},"
              f"scale={out_w}:{out_h}:flags=lanczos,setsar=1")
        filtergraph = vf

    cmd = ["ffmpeg", "-y", "-i", src,
           "-vf", filtergraph,
           "-c:v", "libx264", "-preset", "slow", "-crf", "18",
           "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "256k",
           "-movflags", "+faststart", out]
    run(cmd)
    if cmdfile:
        try:
            os.unlink(cmdfile)
        except OSError:
            pass

    # ---- self-heal / version-gate (QUALITY-BAR rule 14) -------------------
    ow, oh, _, odur = ffprobe_stream(out)
    if (ow, oh) != (out_w, out_h):
        die(f"{out}: got {ow}x{oh}, expected {out_w}x{out_h} (reframe failed)")
    if odur < dur * 0.92:
        die(f"{out}: duration {odur:.2f}s < source {dur:.2f}s (truncated)")
    print(f"[smart-reframe] OK {ar:>4}  {ow}x{oh}  {odur:.1f}s  -> {out}")


# ----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="headless shot-aware H->V reframe")
    ap.add_argument("--in", dest="src", required=True)
    ap.add_argument("--out", help="single output path (with --ar X:Y)")
    ap.add_argument("--outdir", help="dir for multi-AR output")
    ap.add_argument("--ar", default="9:16",
                    help="comma list of 9:16,1:1,4:5")
    ap.add_argument("--static", action="store_true",
                    help="disable subject tracking -> centre column crop")
    ap.add_argument("--auto-install", action="store_true",
                    help="pip-install scenedetect/opencv/numpy if missing")
    ap.add_argument("--best", action="store_true",
                    help="also install/use the YOLOv11 + MediaPipe person-lock "
                         "tier (implies --auto-install)")
    a = ap.parse_args()
    if a.best:
        a.auto_install = True

    if not os.path.exists(a.src):
        die(f"input not found: {a.src}")
    ars = [x.strip() for x in a.ar.split(",") if x.strip()]
    for ar in ars:
        if ar not in AR_MAP:
            die(f"unsupported aspect ratio {ar}; use 9:16, 1:1 or 4:5")
    if len(ars) > 1 and not a.outdir:
        die("multiple --ar values need --outdir")
    if len(ars) == 1 and not (a.out or a.outdir):
        die("need --out or --outdir")

    ensure_ffmpeg()
    mods = maybe_install(a.auto_install, best=a.best)
    if "cv2" not in mods and not a.static:
        print("[smart-reframe] opencv/scenedetect missing -> static centre crop. "
              "Re-run with --auto-install for subject tracking.")
        a.static = True

    w, h, fps, dur = ffprobe_stream(a.src)
    print(f"[smart-reframe] source {w}x{h} @ {fps:.2f}fps {dur:.1f}s")

    shots = detect_shots(a.src, dur, mods) if not a.static else [(0.0, dur)]
    print(f"[smart-reframe] {len(shots)} shot(s) detected")
    pts = subject_path(a.src, w, h, fps, mods, a.static)
    print(f"[smart-reframe] {len(pts)} subject sample(s)")

    base = os.path.splitext(os.path.basename(a.src))[0]
    for ar in ars:
        if a.out and len(ars) == 1:
            out = a.out
        else:
            tag = ar.replace(":", "x")
            os.makedirs(a.outdir, exist_ok=True)
            out = os.path.join(a.outdir, f"{base}_{tag}.mp4")
        reframe_one(a.src, out, ar, w, h, fps, dur, pts, shots, a.static)


if __name__ == "__main__":
    main()
