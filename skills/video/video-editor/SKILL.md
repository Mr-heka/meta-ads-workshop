---
name: video-editor
description: "Edits recorded video locally with the free ffmpeg and auto-editor CLIs - trims, joins, cuts silences, adds captions, reframes, overlays, compresses - nothing uploaded. Use when the user wants footage they already have (podcast, vlog, ad) edited, not AI-generated."
allowed-tools: Bash, Read, Write
metadata:
  category: Content & Writing
  tags:
    - video-editing
    - ffmpeg
    - auto-editor
    - podcast
    - vlog
    - captions
    - local
  pairs-with:
    - skill: hyperframes-media
      reason: Auto-generate captions - its Whisper transcription turns speech into an SRT this skill then burns in with FFmpeg
    - skill: hyperframes-cli
      reason: Sibling local video tool - HyperFrames for programmatic/templated React video, this skill for editing recorded footage
    - skill: higgsfield-connector
      reason: Generate AI B-roll / intro clips, then cut them into your recorded edit here
    - skill: ad-creative
      reason: Write the ad/script, then assemble and caption the video with this skill
---

# Video Editor (local, free)

> **Tooling:** `ffmpeg` + `ffprobe` (the engine) and `auto-editor` (automatic silence-cutting). All local, all free, nothing uploaded to any cloud. Grounded against FFmpeg n8.1.1 and auto-editor 29.3.1.

## Overview

This skill does **proper, scriptable video editing on the user's own machine** - the right tool when they've *recorded* footage (vlogs, ads, tutorials, podcasts, talking-head) and want to edit it, as opposed to AI-*generating* new footage. Two tools, both CLI:

- **FFmpeg / FFprobe** - the universal engine: trim, join, captions, overlays, reframe/resize, audio, speed, thumbnails, compression.
- **auto-editor** - analyses loudness and **automatically cuts silences / dead air**, the single biggest time-saver for podcasts and vlogs.

There is no account, no API key, no upload, and no per-render cost - it's free and offline.

### What this skill is NOT for

- **AI-generating** new video/images → use `higgsfield-connector`.
- **Programmatic / templated** React-rendered video (data-driven ads, animated lower-thirds at scale) → use `hyperframes-cli`.
- A visual timeline GUI (this is CLI-driven; Claude composes the commands).

## PHASE 0 - Tooling check (silent)

```bash
ffmpeg -version | head -1 && ffprobe -version | head -1     # the engine
command -v auto-editor && auto-editor --version             # silence-cutter (optional until needed)
```

- FFmpeg present → ready for everything except auto silence-cut.
- `auto-editor` missing → only needed for the silence-cut workflow; install it on demand (Phase 1).

## PHASE 1 - Install (only what's missing)

**FFmpeg** (almost always preinstalled; install per OS if not):
```bash
# macOS:        brew install ffmpeg
# Debian/Ubuntu: sudo apt install ffmpeg
# Arch:          sudo pacman -S ffmpeg
# Windows:       winget install Gyan.FFmpeg
```

**auto-editor** - it's a Python app; **do not** use bare `pip install` (modern distros like Arch block it via PEP 668). Prefer, in order:
```bash
uv tool install auto-editor        # cleanest if `uv` is present (recommended)
pipx install auto-editor           # else pipx  (Arch: sudo pacman -S python-pipx first)
# fallback (isolated venv):
python3 -m venv ~/.venvs/auto-editor && ~/.venvs/auto-editor/bin/pip install auto-editor
# then call ~/.venvs/auto-editor/bin/auto-editor
```
auto-editor downloads a small platform binary on first run - that's expected.

## PHASE 2 - Operations (grounded recipes)

> **Golden rule: never overwrite the source.** Always write to a NEW file (and confirm before replacing anything the user can't regenerate). Keep originals.

### Inspect first

```bash
ffprobe -v error -show_entries format=duration,size:stream=index,codec_type,codec_name,width,height,r_frame_rate -of default=noprint_wrappers=1 INPUT.mp4
auto-editor info INPUT.mp4        # quick stream summary
```

### Trim / cut a section

```bash
# Fast & lossless (cuts on keyframes; -c copy = no re-encode):
ffmpeg -ss 00:00:05 -to 00:00:20 -i INPUT.mp4 -c copy OUT_trim.mp4
# Frame-accurate (re-encodes; use when the lossless cut lands slightly off):
ffmpeg -ss 00:00:05 -to 00:00:20 -i INPUT.mp4 -c:v libx264 -crf 18 -c:a aac OUT_trim.mp4
```

### Join / concatenate clips

```bash
# SAME codec/resolution/fps → fast concat demuxer (lossless):
printf "file '%s'\n" clip1.mp4 clip2.mp4 clip3.mp4 > /tmp/list.txt
ffmpeg -f concat -safe 0 -i /tmp/list.txt -c copy OUT_joined.mp4
# DIFFERENT formats → normalise with the concat filter (re-encodes):
ffmpeg -i a.mp4 -i b.mov -filter_complex \
  "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" OUT_joined.mp4
```

### Auto-cut silences / dead air (podcasts & vlogs) - `auto-editor`

```bash
auto-editor INPUT.mp4 --stats                      # DRY RUN: shows how much will be cut, then halts
auto-editor INPUT.mp4 -o OUT_tightened.mp4         # do it (cuts silent sections)
auto-editor INPUT.mp4 -o OUT.mp4 --margin 0.3s     # keep 0.3s padding around speech (less jarring)
auto-editor INPUT.mp4 -o OUT.mp4 --edit audio:threshold=4%   # sensitivity (higher = cut more)
auto-editor INPUT.mp4 -o OUT.mp4 --when-silent speed:8       # speed up silences 8x instead of removing
```
Always run `--stats` first and tell the user the projected length change before rendering.

### Captions / subtitles

```bash
# Burn IN a provided .srt (hardcoded, always visible):
ffmpeg -i INPUT.mp4 -vf "subtitles=subs.srt:force_style='FontSize=24,OutlineColour=&H80000000,BorderStyle=3'" -c:a copy OUT_captioned.mp4
# Soft subtitles (toggleable, smaller file):
ffmpeg -i INPUT.mp4 -i subs.srt -c copy -c:s mov_text OUT_softsub.mp4
```
**Auto-generate captions from speech:** this skill doesn't transcribe - hand the audio to **`hyperframes-media`** (Whisper transcription → `.srt`), then burn that SRT in with the command above. (Reuse, don't reinvent.)

### Reframe / resize aspect ratio (e.g. 16:9 → 9:16 for Reels/Shorts, or → 1:1)

```bash
# Crop-to-fill 9:16 (1080x1920), centered:
ffmpeg -i INPUT.mp4 -vf "scale=-2:1920,crop=1080:1920" -c:a copy OUT_vertical.mp4
# Fit-with-blurred-bars (no cropping; keeps whole frame):
ffmpeg -i INPUT.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" OUT_padded.mp4
```

### Overlay a logo / watermark / lower-third (PNG)

```bash
ffmpeg -i INPUT.mp4 -i logo.png -filter_complex "overlay=W-w-20:20" -c:a copy OUT_branded.mp4   # top-right, 20px margin
```

### Audio: extract, replace, add a music bed

```bash
ffmpeg -i INPUT.mp4 -vn -c:a libmp3lame audio.mp3                                   # extract audio
ffmpeg -i INPUT.mp4 -i voiceover.wav -map 0:v -map 1:a -c:v copy -shortest OUT.mp4  # replace audio
# Mix a background music bed under the original audio (music at 25%):
ffmpeg -i INPUT.mp4 -i music.mp3 -filter_complex "[1:a]volume=0.25[m];[0:a][m]amix=inputs=2:duration=first" -c:v copy OUT.mp4
```

### Speed up / slow down

```bash
ffmpeg -i INPUT.mp4 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" OUT_2x.mp4   # 2x faster
```

### Thumbnail / frame grab

```bash
ffmpeg -ss 00:00:03 -i INPUT.mp4 -vframes 1 -q:v 2 thumbnail.jpg
```

### Compress / export for web

```bash
ffmpeg -i INPUT.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k -movflags +faststart OUT_web.mp4
```
(`-crf` 18 = high quality/larger, 28 = smaller/lower; `+faststart` = streams/plays before fully downloaded.)

## Prompt-to-recipe mapping

| What the user says | Recipe |
|---|---|
| "Cut the boring/silent bits from my podcast/vlog" | `auto-editor --stats` (preview) → `auto-editor -o … --margin 0.3s` |
| "Trim from 0:05 to 0:20" | ffmpeg `-ss … -to … -c copy` |
| "Stitch these clips together" | concat demuxer (same codec) or concat filter (mixed) |
| "Add captions / subtitles" | burn-in `subtitles=`; auto-gen via `hyperframes-media` → SRT first |
| "Make it vertical for Reels/TikTok" | scale+crop to 1080x1920 |
| "Put my logo in the corner" | `overlay=` a PNG |
| "Add background music" | `amix` with `volume=` |
| "Speed it up 2x" | `setpts`/`atempo` |
| "Grab a thumbnail" | `-ss … -vframes 1` |
| "Make the file smaller / web-ready" | `libx264 -crf -preset … +faststart` |

## Behaviour Guidelines

- **Never overwrite the source.** Always output a new file; confirm before replacing anything irreplaceable.
- **Dry-run destructive edits.** For auto-editor, run `--stats` and report the projected length change before rendering. For big cuts, confirm.
- **Prefer lossless** (`-c copy`) for plain trims/joins; only re-encode when needed (codec mismatch, filters, frame-accuracy).
- **Inspect before acting** (`ffprobe`) so you match resolution/codec/fps when joining.
- **Report the result** - output path, new duration, and file size - and offer to preview a frame (`-vframes 1`) or open it.
- **Long renders:** run in the background and poll; show progress, don't block silently.
- **Deliver.** Once the final export is accepted, deliver the finished file to
  wherever the user keeps rendered video.

## Error Handling

| Symptom | Cause | Fix |
|---|---|---|
| `ffmpeg: command not found` | not installed | Phase 1 (OS package manager) |
| `auto-editor: command not found` | not installed | `uv tool install auto-editor` / pipx (not bare pip - PEP 668) |
| Concat output glitches / desync | clips have different codec/res/fps | use the concat **filter** (re-encode), not `-c copy` |
| Trim starts at the wrong spot | `-c copy` cut to nearest keyframe | re-encode for frame accuracy |
| Burned captions don't show | wrong path / style | check `subtitles=` path; escape special chars; verify the `.srt` is valid |
| Huge output file | no compression | re-export with `-crf 23 -preset medium` |

## Scope Limitations

- **CLI, not a GUI timeline** - Claude composes commands; there's no drag-and-drop editor here.
- **Captions need a transcript** - auto-generation is delegated to `hyperframes-media` (Whisper); this skill burns in / attaches the resulting SRT.
- **auto-editor cuts by loudness** (and a few other `--edit` methods), not by understanding content - review the `--stats` preview before committing.
- For **transcript-based editing UX** (edit by deleting words, like Descript) there is no free CLI equivalent - that's a GUI-app workflow.

## Related Skills

- **hyperframes-media** - Whisper transcription (→ SRT for captions), TTS, background removal
- **hyperframes-cli** - programmatic/templated React video (data-driven ads, animated graphics)
- **higgsfield-connector** - generate AI images/clips and B-roll to edit in
- **ad-creative** / **copywriting** - script and plan the video before you cut it

<!-- Provenance marker: sk-1mkueot --><!-- Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠ -->

Made by Selr AI.⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠
<!-- srk:z4nwj5 -->
