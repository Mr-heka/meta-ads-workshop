# Render and QA

## Composition checks

Before the full render:

- Build and inspect each card’s static hero frame when all content is visible.
- Confirm video, cards, subtitles/captions, and diagrams do not overlap unintentionally.
- Confirm the frame clips hidden video areas.
- Confirm every timed element, including card hosts and sub-compositions, has `clip`, `data-start`, `data-duration`, and the intended `data-track-index`.
- Use `data-track-index`, not `data-layer`; use `data-duration`, not `data-end`.
- Register exactly one paused master timeline at `window.__timelines["graphic-overlays"]`.
- Build timelines synchronously at page load. Keep render paths deterministic and synchronous by using direct timeline statements instead of `async`, Promises, `setTimeout`, media `play()`, `Math.random()`, or `Date.now()`.
- Calculate finite repeats from media duration rather than an infinite `repeat:-1`.
- Prefer transforms and opacity (`x`, `y`, `scale`, `rotation`, `opacity`) over layout-property motion. Tween wrappers such as `#video-wrap`, not video element dimensions.
- Give each animated property one timeline owner at a given time.
- Use concrete global font names with matching local `@font-face` files when present. The current bundle has no font assets, so a concrete system stack is the working default.
- Confirm card end times and composition duration do not exceed probed media duration.

## Snapshot

Capture a representative frame before committing to the full render:

```bash
npx hyperframes snapshot public --at 5
```

This writes `public/snapshots/frame-00-at-5s.png`. A single `--at` ignores `--out`. Inspect multiple meaningful timestamps as needed: entrance, fully readable hold, exit, layout transition, dense data, and final frame.

## Render

```bash
cd "$WORK_DIR"
PRODUCER_BROWSER_GPU_MODE=hardware npx hyperframes render public \
  -o output.mp4 \
  --fps 30
```

`hyperframes render <dir>` reads `<dir>/index.html`. Match `--fps` to the storyboard and dense-keyframe encode. On macOS, `PRODUCER_BROWSER_GPU_MODE=hardware` or `--browser-gpu` is strongly recommended because software-only Chrome rendering times out on many laptops.

Verify the real MP4: duration, dimensions, frame rate, audio presence, readable frames, continuous source video, card timing, and no black tail or frozen seek frames.

## Optional preview

The source clip remains unchanged inside `public/index.html`, so the HTML is a faithful overlay preview. Do not open it during the run. If the user requests a live preview, start it after the render:

```bash
(cd "$WORK_DIR/public" && npx hyperframes preview)
```

For a shareable link:

```bash
(cd "$WORK_DIR/public" && npx hyperframes play)
```

Report the resulting URL.

## Final report

Give the user:

- Work directory.
- `storyboard.json`.
- `public/cards/*.html`.
- `public/index.html`.
- `output.mp4`.
- ASR provider: local Whisper.
- Final card count and one-sentence pacing rationale.
- Missing assets or quality caveats.

Retain the work directory unless the user explicitly asks for deletion.
