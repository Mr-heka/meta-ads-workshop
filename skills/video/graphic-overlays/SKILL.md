---
name: graphic-overlays
description: Use when the user asks to add graphic overlays, overlay cards, lower-thirds, data callouts, kinetic titles, quotes, side panels, picture-in-picture, or to “package” or “dress up” an existing talking-head, interview, or podcast video.
---

# Graphic Overlays

Package an existing video without changing its edit: keep the clip playing in full and place transcript-timed HTML graphic cards above it. HyperFrames handles local Whisper transcription and deterministic HTML-to-MP4 rendering.

## Route

Use for designed titles, callouts, quotes, lower-thirds, panels, PiP, or graphic packaging over an existing talking-head, interview, or podcast.

Use `embedded-captions` for plain spoken-word subtitles, `motion-graphics` for one short unnarrated sting or lower-third, and creation skills such as `product-launch-video`, `faceless-explainer`, or `pr-to-video` for a video built from a URL, topic, or PR. Re-timing, recoloring, reframing, reordering, and audio editing belong in an NLE.

## Recipe

| Stage | Contract | Read |
|---|---|---|
| Inspect | Run doctor; probe media; extract audio; transcribe locally; correct words without moving timestamps. | [workflow.md](references/workflow.md) |
| Plan | Infer card count, confirm ratio/layout/style/count, then write the v3 storyboard. | [storyboard.md](references/storyboard.md) |
| Design | Choose style × layout × frame; author one scoped, script-free HTML fragment per card. | [visual-system.md](references/visual-system.md) |
| Assemble | Stage real assets, re-encode the video with dense keyframes, inline cards, and compile one paused GSAP timeline. | [composition.md](references/composition.md) |
| Verify | Lint through render, inspect snapshots and MP4, then report artifacts and caveats. | [render-qa.md](references/render-qa.md) |

For brand colors and typography, read the user's own brand guide. The shipped design library remains the source for its neutral reference styles, layouts, and frames.

## Example

For a 121-second, high-density portrait interview: recommend 9:16, infer about 17 cards, confirm a layout and style group, then build transcript-aligned cards while the original speaker video remains continuous.

## Common mistakes

- Treating `storyboard.json` as CLI input; it is an agent planning contract.
- Inventing `card.layout`; the schema uses `card.zone`, while video movement is GSAP on `#video-wrap`.
- Copying the old font command; this bundle currently has no `assets/fonts/`.
- Omitting `clip`, concrete body font names, timeline registration, duration clamping, or dense keyframes.
- Opening a preview during the run; preview only after render and only when requested.
