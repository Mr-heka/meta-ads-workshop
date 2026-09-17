# Workflow and CLI

## Runtime

This skill uses the HyperFrames CLI plus system `ffmpeg` and `ffprobe`. Transcription is local Whisper through `hyperframes transcribe`; it needs no third-party service, API key, rate-limited proxy, or credential record.

Refresh and inspect the runtime:

```bash
npx hyperframes skills update talking-head-recut
npx hyperframes --help
npx hyperframes doctor
ls "<SKILL_DIR>/assets/fonts" "<SKILL_DIR>/assets/vendor/gsap.min.js"
```

Required assets are `<SKILL_DIR>/assets/fonts/*.woff2` and `<SKILL_DIR>/assets/vendor/gsap.min.js`. The host injects `SKILL_DIR` as “Base directory for this skill: …”. On macOS, use hardware browser rendering:

```bash
export PRODUCER_BROWSER_GPU_MODE=hardware
```

## Work directory and source analysis

Keep the workspace root as the current directory. All output lives in one subdirectory, matching `product-launch-video`, `faceless-explainer`, and `pr-to-video`:

```bash
VIDEO_PATH="/absolute/path/input.mp4"
WORK_DIR="videos/$(basename "$VIDEO_PATH" | sed 's/\.[^.]*$//')"
mkdir -p "$WORK_DIR"

ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate \
  -show_entries format=duration -of json "$VIDEO_PATH" > "$WORK_DIR/metadata.json"

ffmpeg -y -i "$VIDEO_PATH" -vn -acodec libmp3lame -q:a 2 "$WORK_DIR/audio.mp3"

npx hyperframes transcribe "$WORK_DIR/audio.mp3" \
  -d "$WORK_DIR" --json --model small.en
```

`metadata.json` contains `width`, `height`, `duration`, and `r_frame_rate`; evaluate the fraction, for example `30000/1001 → 29.97`. `transcript.json` is the flat word array `[{ "text": "...", "start": s, "end": s }, …]`, with no `segments` array or `words` wrapper.

Correct obvious homophones, product names, technical terms, and punctuation by editing `text` in place while preserving `start` and `end`. Group words into sentences at terminal punctuation or pauses when segment-like chunks are useful.

Clamp every card `endSec` and `composition.durationSeconds` to the media duration from `metadata.json`; Whisper can place the final word slightly beyond the clip and create a black tail.

## Artifact contract

| Path | Purpose |
| --- | --- |
| `metadata.json` | duration, width, height, and fps source |
| `audio.mp3` | extracted transcription audio |
| `transcript.json` | corrected word-level Whisper output |
| `storyboard.json` | agent-authored timing/content plan; no CLI consumes it |
| `public/cards/card-XX.html` | one scoped HTML fragment per card |
| `public/index.html` | assembled composition |
| `public/input-video.mp4` | seek-safe staged source |
| `output.mp4` | final render |

## Stage and render

Stage bundled assets and re-encode the input with dense keyframes. A source GOP above roughly 1 second can freeze during renderer seeks. Set `-g` and `-keyint_min` to the composition fps; `30` is shown and `24`, `25`, or `60` should match those timelines.

```bash
SKILL_DIR="<SKILL_DIR>"
mkdir -p "$WORK_DIR/public/fonts" "$WORK_DIR/public/vendor" "$WORK_DIR/public/cards"
cp -n "$SKILL_DIR/assets/fonts/"* "$WORK_DIR/public/fonts/"
cp -n "$SKILL_DIR/assets/vendor/gsap.min.js" "$WORK_DIR/public/vendor/"

ffmpeg -y -i "$VIDEO_PATH" -c:v libx264 -crf 18 -g 30 -keyint_min 30 \
  -pix_fmt yuv420p -movflags +faststart -c:a aac \
  "$WORK_DIR/public/input-video.mp4"
```

Snapshot a representative hero frame before the full render:

```bash
cd "$WORK_DIR"
npx hyperframes snapshot public --at 5
# public/snapshots/frame-00-at-5s.png
# A single --at ignores --out.

PRODUCER_BROWSER_GPU_MODE=hardware npx hyperframes render public \
  --skill=talking-head-recut \
  -o output.mp4 \
  --fps 30
```

`hyperframes render <dir>` reads `<dir>/index.html`. `--browser-gpu` is the CLI alternative to `PRODUCER_BROWSER_GPU_MODE=hardware`; software-only Chrome rendering times out on most Mac laptops.

Inspect the rendered MP4, then report the work directory, `storyboard.json`, `public/cards/*.html`, `public/index.html`, `output.mp4`, ASR provider, card count and its one-sentence rationale, plus missing keys or quality caveats.

Start live preview only after render and only when requested:

```bash
(cd "$WORK_DIR/public" && npx hyperframes preview)
# npx hyperframes play creates a shareable link.
```

The source clip remains unchanged inside `public/index.html`, so this preview is faithful. Retain the work directory until the user explicitly asks for deletion.
