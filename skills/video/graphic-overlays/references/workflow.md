# Workflow, Files, and Media Preparation

## Runtime and artifacts

The workflow uses the HyperFrames CLI plus system `ffmpeg` and `ffprobe`. `hyperframes transcribe` runs local Whisper, so there is no third-party transcription service, API key, proxy, or rate limit.

```bash
npx hyperframes --help
npx hyperframes doctor
```

On macOS, use hardware browser rendering:

```bash
export PRODUCER_BROWSER_GPU_MODE=hardware
```

Keep the workspace root as the current directory. Put every artifact under `videos/<project-name>/`:

```bash
VIDEO_PATH="/absolute/path/input.mp4"
WORK_DIR="videos/$(basename "$VIDEO_PATH" | sed 's/\.[^.]*$//')"
mkdir -p "$WORK_DIR"
```

Expected files:

| Path | Purpose |
|---|---|
| `metadata.json` | Duration, width, height, and frame rate |
| `audio.mp3` | Extracted audio |
| `transcript.json` | Flat word array: `[{ "text": "...", "start": s, "end": s }, …]` |
| `storyboard.json` | Agent-authored planning outline; no CLI consumes it |
| `public/cards/card-XX.html` | One HTML fragment per card |
| `public/index.html` | Assembled composition |
| `output.mp4` | Final render |

## Probe and extract

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate \
  -show_entries format=duration -of json "$VIDEO_PATH" > "$WORK_DIR/metadata.json"

ffmpeg -y -i "$VIDEO_PATH" -vn -acodec libmp3lame -q:a 2 "$WORK_DIR/audio.mp3"
```

Read `width`, `height`, and `duration`. Evaluate the `r_frame_rate` fraction, for example `30000/1001 → 29.97`.

## Transcribe and correct

```bash
npx hyperframes transcribe "$WORK_DIR/audio.mp3" -d "$WORK_DIR" --json --model small.en
```

`transcript.json` has no `segments` array and no `words` wrapper. Each word uses the key `text`. Correct obvious homophones, names, product names, technical terms, and punctuation in place while preserving every `start` and `end`. Group words into sentences yourself at terminal punctuation or pauses when planning cards.

Whisper may place the last word slightly past the media. Clamp every card `endSec` and `composition.durationSeconds` to `metadata.json` duration so the render has no black tail.

## Asset reality

The current bundle contains:

```text
assets/vendor/gsap.min.js
references/DESIGN_INDEX.md
references/styles/{academic,editorial,minimal,spotlight,geom,whiteboard,audit,terminal,swiss,xhs}.html
references/layouts/{split,stack,pip,overlay}.html
references/frames/{clean,hairline,polaroid}.html
```

It currently does **not** contain `assets/fonts/`. Check what actually exists:

```bash
test -f "<SKILL_DIR>/assets/vendor/gsap.min.js"
find "<SKILL_DIR>/assets" -maxdepth 2 -type f -print
```

Stage GSAP as documented in [composition.md](composition.md). If a future bundle adds local `.woff2` files, stage only those present and declare matching `@font-face` entries. Until then, use a concrete system-font stack. For brand color and type decisions, read the user's own brand guide.

## Deliverables

Report:

- Work-directory path.
- `storyboard.json`, `public/cards/*.html`, `public/index.html`, and `output.mp4`.
- ASR provider: local Whisper.
- Card count and its one-sentence rationale.
- Any missing assets or quality caveats.

Keep the work directory. Delete it only if the user asks.
