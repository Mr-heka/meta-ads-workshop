---
name: embedded-captions
description: 'Use when the user asks to add captions or subtitles to a single-subject talking-head video, says “embed captions,” “cinematic captions,” “VFX captions,” “炸,” “特效,” or “酷炫字幕,” names an embedded-captions identity, or asks for top-tier motion-graphics captions.'
metadata:
  tags: captions, embedded-captions, occlusion, matting, talking-head, rembg-matting, whisper, ffmpeg, cinematic
---

# Embedded Captions

Build local, scene-aware captions for a talking-head clip. Route through one of the 36 catalog identities; engine names remain implementation detail.

**Requirements:** this skill runs on HyperFrames. Install HyperFrames per its own docs and confirm `npx hyperframes doctor` passes before running any stage.

## Use when

- A single human subject speaks on camera and needs readable subtitles, embedded typography, or a themed VFX treatment.
- The user names an identity or asks for cinematic, motion-graphics, or “炸 / 特效 / 酷炫” captions.

## Do not use when

- The clip has no speaker, no usable speech, hard cuts or multiple speakers that have not been split, an unreliable transcript, heavy motion that breaks the matte, or existing burned-in captions/heavy text graphics.
- The job is ordinary captions with no talking-head or scene-integration need.

## Recipe

| Stage | Action | Read |
|---|---|---|
| 1. Refresh and admit | Update the skill, probe the clip, and run every admission check. | [Routing and intake](references/routing-and-intake.md) |
| 2. Choose | Shortlist 2–3 catalog identities, recommend one, then resolve the preference gate. | [CATALOG.md](CATALOG.md) |
| 3. Prepare | Initialize the project; generate matte, transcript, audio envelope, and safe zones. | [Pipeline and authoring](references/pipeline-and-authoring.md) |
| 4. Author | Read `safe-zones.json`; create `cinematic.json`, direct `plan.json`, or `theme.json` for the catalog-selected engine. | [Pipeline and authoring](references/pipeline-and-authoring.md) |
| 5. Prove | Preview composites, fix visual failures, run gates, render once, and inspect the deliverable. | [Quality and gates](references/quality-and-gates.md) |

For dependencies, resolver order, deliverables, and legacy compatibility, read [Runtime and legacy](references/runtime-and-legacy.md). Use [Reference map](references/reference-map.md) to load craft guidance only when its stage requires it. For brand values, use the user's own brand guide.

## Common mistakes

- Keep ordinary speech on the rail; promote only earned peaks to embeds.
- Give every transcript word its own timing and make group windows envelop those timings.
- Inspect matte and background frames before trusting safe zones around props.
- Judge the faithful preview sheet with geometric gates and human visual checks.
- Choose an identity that suits scene luminance; keep locked identity styling intact.

## Example

User: “Add cinematic captions to this explainer, surprise me.” Probe the clip, shortlist identities, select and explain one in autonomous mode, prepare it, author from `safe-zones.json`, preview until checks pass, then render the catalog-derived deliverable.
