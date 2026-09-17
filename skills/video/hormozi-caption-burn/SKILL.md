---
name: hormozi-caption-burn
description: "Use when the user says \"add captions\", \"burn captions\", \"Hormozi captions\", \"MrBeast captions\", \"caption this video\", \"add animated word captions\", or \"put bouncing captions on this\" for a vertical video. Route editable NLE caption tracks to the relevant NLE tool."
---

# Hormozi Caption Burn⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

Takes a finished vertical video and stamps animated word-by-word captions onto
it - the punchy, one-or-two-words-at-a-time style where the word you're hearing
right now pops in a bright colour. No video editor open, no clicking. It listens
to the speech (automatic transcription - turns talking into timed text), lines
each word up to the exact frame it's spoken, then bakes the captions into the
picture (burns them in - permanent, plays everywhere). Out comes a
ready-to-post MP4 plus the editable subtitle file if a human wants to tweak the
wording later.

This is the **headless caption layer** of the video-edit suite. It is the
only path to the locked Hormozi look that does NOT need DaVinci Resolve or
Premiere running - captions are computed from word timestamps and burned with
ffmpeg + libass. (Resolve's `CreateSubtitlesFromAudio` and Premiere have no
scriptable word-level karaoke caption API, which is exactly why captions are
done here, outside the NLE.)

## When to use

- A vertical reel is cut, graded, audio-mastered - last step is captions.
- Drop any talking-head / b-roll MP4 and says "caption this" / "add the
  Hormozi captions" / "subtitle this for IG".
- The last stage of a headless reel pipeline, after reframe, so captions are
  burned onto each final canvas.

## When NOT to use

- The reel already gets captions from an in-composition caption layer (for
  example a Remotion kinetic-caption pipeline). This skill is the **generic,
  any-video, any-suite** burner - use it for footage that isn't going through
  such a pipeline (conformed AI b-roll reels, NLE-graded reels, one-off client
  clips).
- You need captions as a live editable track inside a delivered `.prproj`/`.drt`
  - burn-in is permanent. Use the NLE caption track for that case.

## What it produces

- `<name>-captioned.mp4` - same video, captions burned in, `yuv420p`, audio
  copied through untouched.
- `<name>.ass` - the Advanced SubStation Alpha file (the editable caption
  source: every word, its timing, and the karaoke highlight). Re-burn after a
  hand-edit without re-transcribing.
- `<name>.words.json` - the raw word timestamps, cached so re-runs skip
  transcription.

## Setup / dependencies

**Feasibility: full-auto.** One command, no human in the loop once deps are in.

| Need | What | One-time install |
|------|------|------------------|
| Transcription | openai-whisper `--word_timestamps True` is the **default path** (installed with `brew install openai-whisper` (or `pip install openai-whisper`), model `small.en`). WhisperX is an **optional upgrade** for tighter word alignment via forced alignment | works out of the box on whisper; `pip install whisperx` (pulls torch) only if you want sharper sync |
| Width measurement | **Pillow** - measures real glyph widths so captions never clip (the no-overflow guard). Soft dep: falls back to a calibrated heuristic if absent | `pip install Pillow` (usually already present) |
| Burn engine | **ffmpeg built WITH libass** | `brew install ffmpeg-full` - see the libass gate below. The mainline `ffmpeg` formula is libass-LESS; `ffmpeg-full` is the build that ships it |
| Font | Montserrat 900 (Black) or Anton or Impact | auto-installed by the script: `brew install --cask font-montserrat font-anton` |

**Sync honesty:** word timing comes from the transcriber. With plain
openai-whisper `small.en` (the default here) word timestamps are good but not
frame-perfect on fast speech; WhisperX forced alignment tightens them. The
caption *layout* (wrap, scale, travel, pop) is identical either way - only the
per-word timing precision improves with WhisperX. Install it only if you see
words landing slightly early/late on rapid delivery.

### ⚠️ libass gate - the load-bearing self-heal

The caption burn is `ffmpeg -vf "ass=..."`. That filter only exists if ffmpeg
was compiled with **libass**. The mainline Homebrew `ffmpeg` formula ships
**zero** libass (verified with `brew cat ffmpeg` - no `--enable-libass`, no
freetype/fontconfig deps), so `ass` is reported as `Unknown filter`. The build
that actually carries libass is **`ffmpeg-full`** (confirmed: depends on
libass + fontconfig + freetype). It is **keg-only**, so it installs to
`/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg` and does NOT shadow the PATH ffmpeg.

The script handles all of this itself:

1. It probes the PATH `ffmpeg -filters` for the `ass` filter. If present, uses it.
2. If not, it auto-finds the keg-only `ffmpeg-full` binary (no symlink needed)
   and uses that for extract + burn.
3. If neither has libass, it prints the exact fix and exits non-zero rather
   than producing a silently caption-less file:

```bash
brew install ffmpeg-full      # ships libass + fontconfig + freetype
# keg-only: the script auto-finds /opt/homebrew/opt/ffmpeg-full/bin/ffmpeg
```

No "ask a human" path - the message tells Claude to run the install and retry.
Self-healing by design. (Reinstalling the mainline `ffmpeg` would
loop forever - it never ships libass.)

### ⚠️ font gate - presence-check + self-heal

The locked look needs a heavy display font. The script checks the requested
font is on disk before building the .ass. If missing, it runs the Homebrew cask
(`font-montserrat` / `font-anton`); if the cask isn't available it falls back
to the first installed caption font (Montserrat Black → Anton → Impact →
Arial Black) and says so, so the burn never renders in a wrong thin default.

Note on Montserrat: the `font-montserrat` cask ships a **variable** font
(`Montserrat[wght].ttf`) whose default master is Thin. libass + fontconfig
resolve the by-name request **"Montserrat Black"** to the Black (900) named
instance correctly (verified by rendering a frame - the burn comes out heavy,
not thin). Anton is a single static heavy face and is the safest fallback.

### Cost

- **Free.** WhisperX/whisper run locally on CPU/GPU. ffmpeg is free. No
  Higgsfield credits, no API spend. (GPU optional - speeds WhisperX up, not
  required.)

## The exact automation path (named calls)

`scripts/burn_captions.py <video.mp4>` runs four stages:

1. **Extract speech** - `ffmpeg -i video.mp4 -ac 1 -ar 16000 -c:a pcm_s16le
   /tmp/audio.wav` (mono 16 kHz, what the ASR wants).

2. **Word timestamps** - try `whisperx <wav> --model large-v3 --align_model
   WAV2VEC2_ASR_LARGE_LV60K_960H --output_format json` (forced alignment gives
   true per-word start/end). Fallback: `whisper <wav> --model small.en
   --word_timestamps True --output_format json`. Either way we parse
   `segments[].words[] -> {word, start, end}` and cache to `<name>.words.json`.

3. **Build the .ass karaoke** - group words into 1-3-word phrase chunks (the
   Hormozi cadence). Each word is its OWN `\pos`'d Dialogue line at a measured
   centre, which buys three things a single shared line can't:
   - **Fit-to-frame (no clipping).** Every word's pixel width is measured from
     the real font file (Pillow reads the actual glyph advances; a calibrated
     heuristic if Pillow is absent). A too-wide chunk **wraps** onto stacked
     rows (`EXTRAORDINARY / DEVELOPMENT / OPPORTUNITY`); a single word wider than
     the frame (`INTERNATIONALIZATION`) is **scaled down** to fit. A caption can
     never run off the edge - the round-2 overflow defect.
   - **Per-word vertical pop.** On its spoken frame the word `\move`s up a few %
     and settles - real Y-axis motion, plus the scale bounce
     (`\fscx/\fscy` 70% → 118% → 100% over ~130ms).
   - **Travelling highlight.** The spoken word pops to the accent colour and
     **stays accent until the next word pops** (the last word holds to chunk
     end). No mid-chunk revert-to-white - the most-recently-spoken word is always
     the coloured one, which is the real Hormozi behaviour (round-2 colour
     defect). Pattern from `unconv/captacity` and `Nutlope/ai-subtitles`; ASS
     animation per the williamhuster.com Whisper→.ass recipe.

4. **Burn** - `ffmpeg -i video.mp4 -vf "ass=<name>.ass:fontsdir=<fonts>"
   -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a copy <name>-captioned.mp4`
   (run via the resolved libass-capable ffmpeg). Audio is stream-copied so the
   mastered track is untouched. `yuv420p` forced for QuickTime/IG compatibility.

ASS style values are hard-coded to the locked preset (below), positioned in the
caption safe zone (a fixed `MarginV` ≈ 28% up from the bottom, clear of the
top/bottom 12%). This is a fixed lower-third position, NOT face detection - it
sits where a talking-head subject's face almost never is. If a subject sits low
in frame, raise `MarginV` (or run `smart-reframe` first so the subject is
upper-centre).

## QUALITY-BAR rules this skill enforces

- **Rule 9 - CAPTIONS (the core of this skill).** Word-level karaoke, active-word
  scale-bounce + vertical pop + a colour highlight that **travels** word to word,
  fixed on-brand Hormozi preset: **Montserrat 900 / Anton / Impact**, **#f7c204
  yellow + #02fb23 green** highlights, **white fill, black outline+shadow**;
  burned from Whisper word timestamps; fixed lower-third safe zone. All locked in
  the ASS `[V4+ Styles]` + per-word `\pos`/`\move`/`\t` spans. (ASS colours are
  `&HAABBGGRR` - yellow `#f7c204` → `&H0004C2F7`, green `#02fb23` →
  `&H0023FB02`.) A font presence-check installs the cask or falls back to an
  installed caption font.
- **Rule 9b - NO OVERFLOW (the load-bearing fix).** Every word's width is
  measured against the frame before placement. A chunk too wide for one line
  wraps to stacked rows; a single word too wide scales down. Captions never clip
  off the edge. `--check` self-tests this on a known fixture (the exact
  `INTERNATIONALIZATION` / 3-long-word cases) and exits non-zero if any word's
  measured edge lands outside the safe band, if the scale-to-fit fails to fire,
  or if the highlight reverts to white mid-chunk - a broken asset can't pass.
- **Rule 1 - PACING.** Captions are chunked 1-3 words and re-timed to the
  spoken word, so the on-screen text changes every beat - a visual change well
  inside the 3-5s rule. Never a static full-sentence block.
- **Rule 14 - SELF-HEAL / VERSION-GATE.** The libass gate above: probe
  `ffmpeg -filters` for `ass`, auto-fall-back to the keg-only `ffmpeg-full`
  build (which actually ships libass), and **read back** the output (ffprobe the
  burned file's dimensions + duration match the source) to ground-truth the burn
  actually happened - captions failing silently is the classic
  undocumented-surface trap.
- **Rule 12 - DELIVERY.** Output is `yuv420p` H.264, audio stream-copied,
  dimensions preserved - a true platform-ready master, not a re-encode that
  drifts the grade.

Rules this skill deliberately does NOT own (handled upstream): grade/colour,
loudness/clean audio, and reframe (`smart-reframe`). Caption-burn assumes it receives an already-finished picture +
mastered audio.

## Locked caption preset (do not relitigate)

- **Font:** Montserrat Black (900) primary, Anton / Impact fallback. All-caps.
  Auto-installed by the script's font gate; Anton is the safest single-file
  static face.
- **Size:** scaled to frame height - ~7-8% of height (≈ 130-150px at 1080×1920).
- **Fill:** white `&H00FFFFFF`. **Outline + shadow:** black, outline 6-8,
  shadow 3-4 (the thick black stroke that survives any background).
- **Active-word pop:** yellow `#f7c204` default highlight; green `#02fb23` as the
  alternate accent for emphasis words (numbers, claims). One pop colour per
  reel unless an emphasis word earns the green.
- **Position:** vertically centred-low, inside the safe zone (Alignment 2,
  `MarginV` ≈ 28% of height up from bottom). Clear of the top/bottom 12%. This
  is a fixed lower-third, not face-aware - if the subject sits low in frame,
  raise `MarginV` or reframe first so the face is upper-centre.
- **Cadence:** 1-3 words per on-screen chunk, break on a speech pause ≥ 0.4s.
  The chunk sits on screen for its span; the spoken word springs up + scale-pops
  (70→118→100%) and takes the accent colour on its own frame, holding the accent
  until the next word takes it. A chunk wider than the safe zone wraps to stacked
  rows (or scales down if it's a single huge word) so nothing clips.

## Run it

```bash
# basic - Hormozi yellow, auto-transcribe, burn
python3 scripts/burn_captions.py ~/Desktop/reel.mp4

# pick the accent colour + force a font + reuse cached words
python3 scripts/burn_captions.py reel.mp4 --accent green --font Anton
python3 scripts/burn_captions.py reel.mp4 --words reel.words.json   # skip ASR

# transcribe + write .ass only (hand-edit wording, then re-burn)
python3 scripts/burn_captions.py reel.mp4 --ass-only
python3 scripts/burn_captions.py reel.mp4 --ass reel.ass --burn-only

# self-test the .ass builder (no video, no ffmpeg, no ASR) - asserts no
# overflow, the long-word scale-to-fit fires, and the highlight travels
# without a mid-chunk white flash. Exits non-zero on a broken asset.
python3 scripts/burn_captions.py --check
```

## Pairs with

- **Your cut and audio master** → cut the reel and master the audio FIRST
  (captions stream-copy that audio through untouched); this captions the
  rendered result.
- **smart-reframe** → reframe to 9:16 BEFORE captioning so the safe-zone maths
  hold for vertical.
- **An in-composition caption layer** (for example Remotion kinetic captions) is
  the *other* caption path. This skill is the headless generic burner; a
  composition pipeline owns its own in-comp captions. They do not overlap.

## Provenance (OSS wrapped, with licence)

- **WhisperX** - m-bain/whisperX, **BSD-4-Clause** - forced-alignment word
  timestamps.
- **openai-whisper** - openai/whisper, **MIT** - fallback ASR with
  `--word_timestamps`.
- **ffmpeg + libass** - **LGPL/GPL** (libass ISC) - the `ass` burn filter.
- **Caption pattern refs:** `unconv/captacity` (**MIT**), `Nutlope/ai-subtitles`
  (**MIT**) - Whisper→styled-caption-burn approach; ASS `\k` karaoke recipe per
  williamhuster.com. The Hormozi preset values (Montserrat 900, #f7c204 +
  #02fb23) are this skill's locked spec, not copied from any one repo.

Router key `sk-5h4enu` — resolved by the skills index on load.
