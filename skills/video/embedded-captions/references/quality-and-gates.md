# Quality and gates

## Preview contract

```bash
node scripts/preview-frames.cjs <project> [t…]
```

The preview tool produces faithful composites in about 2 seconds per frame: seek-time caption screenshots + real video frame + matte occlusion + rail overlay. Defaults sample every group/climax window. Inspect `<project>/preview/sheet.png` before a full render; previews cost seconds, while a full render costs minutes.

Fix:

1. Washout: move the plane or select a scene-fitting identity; use `ink` for a bright surface.
2. Text-on-text: clear scene graphics and collisions between caption groups.
3. Reading order: match vertical order to speech; keep the hero above later words.
4. Hero presence: make the climax large and visibly behind the subject, about 30–55% occluded.
5. Balance: form one coherent column/band with breathing margins and no clipping.

Then run `references/reference-bar.md`’s poster test, timid test, one-glance hierarchy, scene handshake, and dead-air audit. Ship only when both sets pass. For user-facing work, a fresh-eyes agent may receive only the preview sheet and checklist, return PASS or a specific fix per frame, then the author recompiles and re-previews.

## Output contracts

- Prevent 100% continuous face coverage by preserving at least 30% of the face bbox uncovered in every 0.3s window.
- Pass final-render WCAG contrast lint; fix palette failures through identity choice or supported configuration.
- Keep generation deterministic: omit `Math.random()`, `Date.now()`, and `repeat:-1`.
- Preserve the a-roll image. Keep scanlines, duotone, darkening, vignettes, cyberpunk, and CRT texture inside caption elements rather than over the full frame; Theme PLATE reactions are the defined exception.
- Use rail-first treatment for talking-head/explainer work. Space embeds by beat; use at most one embed per sentence/beat, one APEX total, and no adjacent or co-visible embeds. “Climax” means the peak of a beat, not necessarily the clip’s single payoff.
- Keep every caption visible for at least 0.5s.

## Matte and placement

The matte represents the person via hyperframes `remove-background` with `u2net_human_seg` (Apache-2.0). Thin offset furniture such as mic booms is usually excluded, so captions can render over it while remaining behind the person. Large nearby objects such as telescopes or desk rigs can leak into the matte; held products/phones can disappear intermittently and let captions pass in front.

Sample `frames_fg/` at 2–3 timestamps and cross-check `frames_bg/`. Prefer hero positions clear of leaked furniture because leaks can skew `heroAnchor`.

Safe zones are prop-blind: they score subject occlusion and luminance; `peakLuma` catches only moving bright objects, and automatic prop saliency remains a known gap. Extract one frame from every intended band. If a prop occupies it, measure its bbox and move or shrink the plane. Two real deliveries stayed clean because this manual check caught the issue. A leaked prop may skew `heroAnchor.centerXPct`.

## Geometry and timing

- Cinematic frame overflow is a hard gate. Standard `check-overflow.cjs` emits a warning; intentional bleed is the accepted case after reviewing that warning.
- Word timing must match `transcript.json` within 80ms. Cinematic runs `check-timing.cjs --strict` through `render-and-composite.sh`; Theme uses the sequential transcript matcher and verbatim-completeness compile gate.
- Store each transcript word separately with its own start/end. For a visual line such as `"FUTURE OF"` or an `IT`/`ALL` stack, use natural wrap or CSS `white-space`, not one shared timed entry or `<br>`. A shared entry can fire the second word `500ms` early.
- Register creative substitutions such as `"15%"` for `"fifteen percent"` in `CREATIVE_SUBS` inside `check-timing.cjs`.
- Envelop words with their group: `group.in ≤ min(word.start)` and `group.out ≥ max(word.end)`. The validator prevents the container-mount delay that has caused 800ms lag.
- Separate caption groups that overlap in time by non-overlapping vertical bands. Alternatives are a handoff (`earlier.out ≤ next.in`) or deliberate layering with `"allow_overlap": true` on one group. The validator estimates vertical bboxes from CSS; spatial separation produces memory-wall-style poem accumulation rather than subtitle replacement.

## Scene and style gates

- Screen blend washes out above luminance 180. Locked cream+`screen` cinematic styling should route to `ink` or opaque-rail `anchor` on bright scenes.
- Animate stable transforms. `letter-spacing` and `filter:blur` on inline-block word entrance cause reflow and line jumps.
- Run matting on CPU. The onnxruntime CoreML execution provider’s mixed-precision partitioning corrupted face alpha with the prior RVM engine.
- CPU matting runs about 2 fps at 1080p, roughly 2–3 minutes per `10s` clip; budget long clips accordingly.

## Render and hand-off

`render-and-composite.sh` runs timing, occlusion/hero, overflow, and hand-off gates, then writes `final.mp4` plus a `history/` snapshot. Theme writes `final_fx.mp4` after its plate pass. Inspect the real video before delivery, including frame alignment, readability, occlusion, untouched source appearance, and expected audio.
