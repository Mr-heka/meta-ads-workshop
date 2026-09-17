---
name: talking-head-recut
description: Use when the user says “add graphic overlays,” “add on-screen graphics,” “package my video,” or “dress up my talking-head video,” or asks to recut an existing interview or podcast with timed designed cards while keeping the clip itself unchanged.
---

# Talking Head Recut

Package a local talking-head, interview, or podcast video with transcript-timed graphic cards. The source clip plays in full; the deliverable is an inspectable HyperFrames composition and MP4.

## Use this route

Use it for kinetic titles, lower-thirds, data callouts, quotes, side panels, and picture-in-picture over an existing clip.

Route plain spoken-word subtitles to `embedded-captions`, one short unnarrated logo sting or lower-third to `motion-graphics`, and videos built from a URL, topic, or PR to the relevant creation skill such as `product-launch-video` or `faceless-explainer`. Use `hyperframes` when overlays versus captions remains unclear. NLE work such as retiming, recoloring, reframing, reordering, or audio editing is outside this route.

## Core recipe

| Step | Action | Read |
| --- | --- | --- |
| 1 | Silently run `npx hyperframes skills update talking-head-recut`, check the environment, create `videos/<project-name>/`, extract metadata/audio, transcribe locally, and correct ASR text without changing timestamps. | [workflow.md](references/workflow.md) |
| 2 | Read `metadata.json` and `transcript.json`; infer card timing, ask once for ratio/layout/style/count, and write the v3 storyboard. | [storyboard.md](references/storyboard.md) |
| 3 | Read the matching inherited style, layout, and frame files; author one scoped HTML fragment per card. For brand values, read the user's own brand guide. | [DESIGN_INDEX.md](references/DESIGN_INDEX.md), [cards.md](references/cards.md) |
| 4 | Stage local assets and a seek-safe input video, assemble one deterministic paused GSAP timeline, snapshot-check hero frames, render, inspect the MP4, and report artifacts. | [composition.md](references/composition.md), [workflow.md](references/workflow.md) |

Artifacts: `metadata.json`, `audio.mp3`, flat word-array `transcript.json`, `storyboard.json`, `public/cards/card-XX.html`, `public/index.html`, and `output.mp4`.

## Common mistakes

- Treating `storyboard.json` as CLI input; it is the authoring plan.
- Expecting transcript `segments` or `words`; the file itself is `[{text,start,end}, …]`.
- Letting Whisper or cards exceed media duration, which creates a black tail.
- Using sparse-keyframe source video, unscoped card CSS, untimed hosts, remote assets, CSS-variable-only global fonts, or nondeterministic timelines.
- Painting an opaque full-card background where video should remain visible.
- Previewing before render or deleting the work directory without a user request.
