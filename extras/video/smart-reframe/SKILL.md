---
name: smart-reframe
description: "Use when the user says \"make this vertical\", \"reframe this for Reels\", \"crop this to 9:16\", \"auto-reframe this\", \"make a vertical version that follows me\", or reports that a centre crop cuts off heads. Use for headless landscape-to-9:16, 1:1, or 4:5 reframing. Route live Premiere work to Premiere's own Auto Reframe."
---

# Smart Reframe⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

## What it does (plain English)

- Takes a **wide video** (filmed landscape, like a YouTube interview or a
  webcam recording) and makes a **tall phone version** for Reels, TikTok and
  Shorts - without opening a video editor.
- The trick: it **follows the person**. It looks at where the subject is in each
  shot and slides the crop ("camera framing") to keep them centred, so a head
  never drifts off the edge when they lean or walk. A normal crop just takes the
  middle of the frame and loses them.
- For social videos, tracking alone is not enough. After reframing, run the
  `social-safe-zones` subject-framing gate so the person lands in the intended
  talking-head, above-head-graphic, or split-screen target.
- One run gives you **all three social shapes** - 9:16 (Reels/TikTok/Shorts),
  1:1 (square feed), 4:5 (the tall LinkedIn/IG feed crop).
- It's the headless (no-app) twin of the NLE auto-reframe. A junior would open
  Premiere, run Auto Reframe, wait, babysit it per platform. This does it from
  one command and proves the output is the right size before it hands
  it back.

## Feasibility

**FULL-AUTO (local).** One Python script, ffmpeg under the hood, runs in a loop
over a folder. No NLE, no GUI, no subscription.

Honest about the tracking tiers - the crop quality depends on what's installed:

| Tier | What's installed | How it tracks the subject |
|------|------------------|---------------------------|
| **Best** | `ultralytics` (YOLOv11) [+ `mediapipe`] | locks onto the **person box** (a real person detector, holds the lock even over a busy/moving background); MediaPipe then pulls the lock onto the **face** when available |
| **Good** | `opencv` + `scenedetect` only | motion-energy centroid - **one talking subject on a calm background.** It chases the biggest mover, so a busy/animated background, two subjects, or heavy hand/screen motion can pull it off the head. Use `--best` for those. |
| **Floor** | ffmpeg only | static centre column (no tracking - still produces all 3 shapes) |

**Best tier is the real person lock and it is the tested one.** On a 6s clip of a real person sweeping across a *busy* `testsrc2` background, the YOLOv11 path tracked the person to within 0.002-0.008 (normalised) of ground truth while the motion-energy tier drifted - so for anything that isn't a single subject on a calm background, reach for `--best`. MediaPipe face-refine is optional polish on top: the loader supports BOTH the legacy `mp.solutions` API and the newer `mediapipe.tasks` API (the only one present on Python 3.13/3.14 builds, where it fetches a small BlazeFace model once), and if neither is usable it silently runs YOLO-box-only - still a genuine person lock, just centred on the body box rather than the head.

`--auto-install` pulls scenedetect / opencv / numpy on first run. Add `--best`
to also pull YOLOv11 + mediapipe for the tightest person lock. Both flags are
**PEP 668-safe**: on a modern Homebrew/managed Python they retry the install
with `--break-system-packages --user`, and if an install still fails the script
prints one line and **degrades a tier** instead of crashing. The motion-energy
path (Good tier) already follows a single talking head well on its own.

**What costs money:** nothing local. The optional **cloud fallback** is
Higgsfield's `reframe` MCP tool (subject-aware reframe + edge-fill in the
cloud) - that **spends Higgsfield credits** and is only worth it when you have
no GPU/models locally OR you want generative edge-fill instead of a crop. See
*Cloud fallback* below.

**Resolution honesty (this is a crop, not a magnifier).** The vertical is cut
*out* of the source, so the sharpest 9:16 you can make is bounded by the source
height: a 9:16 crop is ~0.56x the source height wide. From 1080p that crop is
only ~404px wide and gets blown up to the 1080-wide master = visibly soft. The
script now **warns loudly** whenever the crop window is narrower than the 1080
canvas and tells you to feed a higher-res source (4K/UHD gives a ~1215px crop -
sharp) or switch to the Higgsfield cloud fallback, which paints the missing
edges in generatively instead of upscaling a small crop. It will still produce
the file, it just won't pretend a soft upscale is sharp.

## Setup / dependencies

**One-time:**
- `ffmpeg` + `ffprobe` (Homebrew: `brew install ffmpeg`). Install if missing.
  The script `die()`s with the install line if missing.
- Python deps, auto-installed with `--auto-install` (or `pip install
  scenedetect opencv-python numpy`):
  - `scenedetect>=0.7` - shot detection (AdaptiveDetector), so the crop never
    pans across a hard cut.
  - `opencv-python` + `numpy` - frame sampling + the motion-energy fallback.
- **For the best lock:** add `--best` (installs `ultralytics` + `mediapipe`) or
  `pip install ultralytics mediapipe` yourself. YOLOv11 auto-pulls `yolo11n.pt`
  on first predict.

The installer survives PEP 668 ("externally-managed-environment", the default on
recent macOS/Linux Homebrew Python): it tries a plain `pip install`, then retries
with `--break-system-packages --user`, and if that still fails it logs one line
and runs on the tier below instead of throwing a traceback.

**Imports / pairs upstream:** none. This is a pure headless transform - it does
NOT need an NLE bridge or an NLE MCP server. That's the whole point: it's
the reframe you reach for when an NLE isn't in the loop. (The NLE routes are
Premiere's Auto Reframe and Resolve's `item.SmartReframe()`.)

**No keys, no MCP server** for the local path. The cloud fallback needs the
Higgsfield MCP connected (`higgsfield-connector`).

## The exact automation path

Core script: **`scripts/reframe.py`** (real, runnable, tested locally).

```bash
# one vertical, subject-tracked:
python3 scripts/reframe.py --in interview.mov --out reel_916.mp4 --ar 9:16 --auto-install

# all three social shapes at once:
python3 scripts/reframe.py --in interview.mov --outdir ./vert --ar 9:16,1:1,4:5 --auto-install

# tightest person lock (YOLOv11 + MediaPipe, auto-installed):
python3 scripts/reframe.py --in interview.mov --out reel_916.mp4 --ar 9:16 --best

# disable tracking (fast static centre column):
python3 scripts/reframe.py --in interview.mov --out reel.mp4 --ar 9:16 --static

# prove the tracking actually centres the subject (golden-frame self-test):
python3 scripts/selftest.py

# prove a measured 9:16 frame lands in the selected subject target
# (path is relative to this skill folder; social-safe-zones ships in this kit):
python3 ../../safe-zones/social-safe-zones/scripts/check-subject-framing.py \
  --style talking_head_full_1080x1920 \
  --face 360,600,360,360 \
  --body 260,560,560,980
```

The pipeline, with the real primitives:

1. **Shots** - `scenedetect.open_video()` + `SceneManager` +
   `AdaptiveDetector()` (PySceneDetect 0.7) → list of shot spans. The crop
   **snaps** to a new centre at each cut and only pans *within* a shot. Panning
   across a hard cut is the classic auto-reframe tell; this avoids it.
2. **Subject centre** - sample ~6 fps with OpenCV. Precedence:
   **YOLOv11** person box (`ultralytics.YOLO("yolo11n.pt").predict(frame,
   classes=[0])`, biggest box above a `YOLO_MIN_CONF=0.40` floor wins, so
   background clutter can't forge a false lock) + **MediaPipe face refine**
   (pulls the crop toward the head inside the box) → **subject-gated motion
   centroid** (inter-frame `cv2.absdiff`, weighted by a gentle centre prior +
   strong temporal continuity so background motion can't yank the lock off the
   subject)
   → frame centre. It tracks **both** `cx` and `cy`, so the squarer 1:1 and 4:5
   crops pan vertically too when the source is tall enough to need it.
3. **Smooth the path per shot** - a deadband removes micro-jitter, then a
   **two-pass centred smoother** (forward EMA + backward EMA, averaged) keeps the
   crop ON the subject with **no trailing lag** - the old forward-only EMA could
   only look backwards, so it lagged a walking subject by ~200px and never caught
   up; the centred filter has zero phase lag. A generous velocity cap kills whip
   pans without re-introducing lag. Reset at every shot boundary. The three
   smoother constants live as named defaults at the top of `reframe.py`
   (`EMA_ALPHA=0.35`, `DEADBAND_FRAC=0.05`, `MAX_VEL_FRAC=0.45`) - one profile,
   tuned for a talking head / slow walk and validated by the self-test sweep. A
   very fast subject wants a higher `MAX_VEL_FRAC`; edit the constant rather than
   hand-patching the maths. There is one profile, not a per-footage auto-tuner -
   that's the honest scope.
4. **Crop + pan + scale headlessly** - ffmpeg, the only headless route to a
   moving crop: a **`sendcmd` script keys `crop`'s `x` and `y` over time**, then
   `crop` takes the tracked window and `scale=…:flags=lanczos,setsar=1` fits the
   target canvas. Output `libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart`,
   audio passed through as 256k AAC. The static path drops `sendcmd` and uses a
   fixed centre `x`/`y`. (Verified locally: both the static crop+scale and
   the dynamic `sendcmd=f=…,crop=W:H:x:y` filtergraphs render correct
   1080×1920 / 1080×1080 / 1080×1350.)
5. **Self-heal / version-gate** - every output is read back with `ffprobe`; the
   script asserts the dimensions match the requested aspect ratio and the
   duration isn't truncated (≥92% of source), and **STOPs loudly** otherwise. A
   corrupt or audio-only input also STOPs with a clean message (no traceback).
   `scripts/selftest.py` goes further with **three rendered checks**, each
   skipping cleanly if its deps aren't present: (a) **motion tier** - a box
   sweeps over a clean background, proves the centroid keeps it framed; (b)
   **best tier** (when `ultralytics` is installed) - a **real person** sweeps
   over a **busy** background, proves YOLOv11 locks the person to within ~0.01
   of ground truth where the motion tier can't; (c) **cut-snap** - a 2-shot
   clip with a hard cut, proves the crop *jumps* to the new subject at the cut
   instead of panning across it. The cut-snap check reports honestly whether
   PySceneDetect saw the cut or it fell back to a fixed split (AdaptiveDetector
   can miss flat synthetic colour cuts; it fires reliably on real footage where
   luma/edges actually change). Exit 0 = every available check held.

Canvas sizes are fixed to the social masters: 9:16 → **1080×1920**, 1:1 →
**1080×1080**, 4:5 → **1080×1350**.

### Cloud fallback (no GPU / want generative edge-fill)

The Higgsfield connector's reframe tool - subject-aware reframe + AI edge-fill
in the cloud. Discover the exact tool name at run time from the live tool list
(the connector notes that tool names are unstable; `mcp__higgsfield__reframe`
is only an example). `params.aspect_ratio` is one of `16:9 | 9:16 | 4:3 | 3:4 | 1:1 |
21:9` (verified against the live tool schema). **Note: 4:5 is NOT a Higgsfield
option** - the cloud fallback can deliver the 9:16 and 1:1 masters but not 4:5;
do 4:5 locally (it's just a crop, no edge-fill needed). Pass exactly one source
`{role:"video", value:<confirmed media_id or completed job_id>}` (never a raw
URL - `media_import_url` first); for clips >15s pass `duration_seconds` +
`resolution` and ONLY the source video; set `params.get_cost=true` (with
`duration_seconds` + `resolution`) first to price the credits before submitting.
Use this when the local models aren't installed or you want the edges *painted
in* rather than cropped away (the cure for the upscale-softness case above).
**Costs Higgsfield credits.**

## QUALITY-BAR rules this skill enforces

- **Rule 11 - REFRAME (this skill's whole job).** Horizontal→vertical is
  **subject-tracked** (the crop pans when the subject moves), never a static
  centre-crop, and framed in **9:16, 1:1 and 4:5**. The shot-split + per-shot
  smoothing is what makes it read as an intentional reframe, not a sliding
  window. (Static centre-crop is available via `--static` but is the explicit
  fallback, not the default.)
- **Rule 11b - SUBJECT POSITION.** For reels, the tracked crop must also
  pass the chosen `social-safe-zones` `subject_framing` profile. A centered
  subject can still be wrong if the head is too high, too low, or blocking the
  b-roll/graphic zone.
- **Rule 14 - SELF-HEAL / VERSION-GATE.** Reframe lives on an undocumented,
  flaky surface (NLE auto-reframe famously *returns before analysis finishes*).
  This skill side-steps that by being deterministic, then **ground-truths every
  output with ffprobe** (dimensions + duration) and STOPs on a wrong size or a
  truncated file. It degrades through named fallbacks (YOLO → motion → centre;
  local → cloud) instead of failing hard.
- **Rule 12 - DELIVERY (multi-platform masters from one edit).** One source →
  the three platform-correct shapes in one run, each at the right canvas size.

It does NOT grade, master audio, or burn captions - grade and audio happen
upstream; captions are `hormozi-caption-burn`. For generic
vertical finishing, reframe runs **before** caption burn so captions land on the
final 9:16, 1:1, or 4:5 canvas. Burning captions on a wide master and cropping
later can clip long phrases.

## Where it sits in a headless reel pipeline

**REFRAME in headless vertical mode.** After audio, before caption
burn. Captions are burned onto each reframed canvas.

`... -> AUDIO -> REFRAME (9:16 + 1:1 + 4:5) -> CAPTIONS per canvas -> QA+DELIVER ...`

## Pairs with

- **hormozi-caption-burn** - burn karaoke captions AFTER this reframe step for
  generic vertical finishing, so captions are placed on the final canvas.
- **Your grade and audio master** - the look and the −14 LUFS audio are
  baked before this; reframe just changes the shape.
- **Premiere Auto Reframe** - the NLE sibling. Use that when you're already in
  a live Premiere; use this when you're not.
- **higgsfield-connector** - its reframe tool is the cloud fallback for
  generative edge-fill.

## Provenance

- **FFmpeg** (`crop`, `sendcmd`, `scale`, `ffprobe`) - LGPL-2.1+ / GPL-2+ per
  build. Calls the system binary; the `sendcmd`-driven moving-crop is the
  documented headless pan route.
- **PySceneDetect** 0.7 (Brandon Castellano) - **BSD-3-Clause**. AdaptiveDetector
  for shot splitting.
- **Ultralytics YOLOv11** - **AGPL-3.0** (optional; person detection). Only
  pulled if you opt in with `pip install ultralytics`; not vendored.
- **MediaPipe** (Google) - **Apache-2.0** (optional; face refine).
- Approach references: **KazKozDev/auto-vertical-reframe** (YOLOv11 + MediaPipe
  framing) and **Google AutoFlip** (shot-aware tracked reframe). No fork, no
  vendored code - this is a clean reimplementation of the pattern.

Made by Selr AI.

Router key `sk-16rtxrx` — resolved by the skills index on load.
