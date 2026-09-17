---
name: social-safe-zones
description: Plan and check placement of social text, logos, captions and graphics against local platform templates and measured subject boxes. Use for reels, ads, Shorts, TikToks, carousels and covers before rendering or when content is being cropped or obscured.
---

# Social safe zones

Select the actual placement, measure the content and inspect the render. These local tools check declared geometry and export properties. They do not detect faces, certify current platform UI, upload files or authorize publishing.

## Choose a profile before placing content

Read [platform profiles](references/platform-safe-zones.md) and the matching entry in `data/social-safe-zones.json`. Official downloaded artwork is under `vendor/`; authored Instagram planning overlays are under `overlays/instagram/`.

- Confirm platform, canvas, direction, anchor/add-ons and caption layout. TikTok templates differ across those conditions. Do not reuse a standard LTR profile for RTL or an anchor placement.
- The legacy key `universal_vertical_9x16_1080x1920` remains for compatibility. Its corrected rectangle is `{x:120,y:288,w:660,h:960}`. It covers only the intersection of the downloaded Google vertical and TikTok standard LTR templates, without an anchor. It does not establish safe placement on Meta or an unknown destination.
- All rectangles use half-open bounds: `right=x+w`, `bottom=y+h`. Every important pixel must fall before the right/bottom boundary. Contained rectangles exclude notches in the template; the transparent area's bounding box is insufficient.
- Instagram crop guides and center-80 profiles are Selr composition presets based on historical observations. Verify the current intended crop. The reel-cover face zone now ends at y=1168, inside its parent safe rectangle.

## Prepare, render and inspect

1. Read the requested source, relevant brand/rendering skill and [production flow](references/production-flow.md). Choose the talking-head, above-head, split-screen, cutaway, motion or static route based on the material.
2. Measure face/body/product boxes from actual representative frames. Use [content styles](references/content-styles.md). Missing detection is unresolved; a default face box cannot substitute for measurement.
3. Declare the exact profile, its conditions, overlays and video timing in a placement plan. Check every moving subject and overlay, including transition frames. Static plans do not require audio or video export fields.
4. Run the relevant local checks below, then inspect actual images/frames and listen to the audio. A geometric pass does not prove readability, an accurate measurement or platform acceptance.
5. For video, read [export and delivery](references/export-upload-quality.md). Check the real file; do not certify bitrate, codec or quality from manifest claims. Follow existing authorization when delivering or publishing. A file-size rule never grants permission to upload to a public host.

## Commands

Run from this skill directory. Requires Python 3, Pillow and NumPy; export measurement also needs `ffprobe`. No script installs dependencies or reads credentials.

```bash
python3 scripts/check-safe-zones.py
python3 scripts/check-subject-framing.py --style talking_head_full_1080x1920 \
  --face 360,600,360,360 --body 260,560,560,980
python3 scripts/check-production-manifest.py examples/production-manifest.example.json
python3 scripts/check-tile-safe-zone.py /absolute/tile.png --profile post \
  --expect ink --out /absolute/new-safecheck.png
python3 scripts/check-tile-safe-zone.py /absolute/cover.png --profile reel \
  --expect pill --pill-box 200,500,500,150 --out /absolute/new-cover-check.png
python3 scripts/check-export-quality.py /absolute/final.mp4 \
  --profile phone_ready_vertical_reel_1080x1920 --source-fps 25
```

Tile inputs must match the exact canvas. Ink detection is a color heuristic. Pill bounds must come from the renderer or manual measurement; a dark photo feature is not a detected pill. Missing expected content fails. A declared pill box proves only its geometry, not that a pill exists there. Outputs require a new path unless `--overwrite` is explicit; the source image cannot be replaced.

Rebuild authored Instagram overlays from canonical data with `python3 scripts/make-instagram-overlays.py --out /absolute/new-directory`. `profiles.json` there is a generated compatibility copy. Imports do not write. Do not edit or stamp the official vendor assets.

Regression suite: `python3 -B scripts/test_safe_zones.py`. Report the selected scenario, commands/results, actual artifacts inspected and remaining uncertainty. A plan pass, metadata pass or provenance marker is never end-to-end publishing proof.

<!-- Provenance marker: sk-1wzolr2 --><!-- Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠ -->
