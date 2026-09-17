# Visual System and Card Contract

## Reference library

The shipped library has three orthogonal dimensions:

```text
Style (10) × Layout (4) × Video frame (3)
```

| Dimension | Keys | Controls |
|---|---|---|
| Style | `academic editorial minimal spotlight geom whiteboard audit terminal swiss xhs` | Card language: type, color, ornament, and internal composition |
| Layout | `split stack pip overlay` | How video and card share the canvas |
| Frame | `clean hairline polaroid` | Decorative video chrome |

Skim `references/DESIGN_INDEX.md` for its matrix and use-case guide. Once chosen, read only the matching files:

- `references/styles/<key>.html`: copy `.card[data-card-id="ref-<key>"]`, rename `data-card-id`, and replace placeholder content.
- `references/layouts/<key>.html`: exact landscape and portrait video/card bounds.
- `references/frames/<key>.html`: sibling HTML, CSS, and placement notes.

The style files are inspiration, not archetypes. Their tokens live in card HTML; `themeId` remains composition-level. Style, layout, and frame can change per card when transitions remain coherent. One valid sequence is `editorial × overlay × clean`, `audit × split × hairline`, then `whiteboard × pip × polaroid`.

For brand values, read the user's own brand guide. The neutral composition themes below are retained as runnable configuration:

```js
const themes = {
  classic: { accents: ["#1971c2","#e03131","#2f9e44","#e8590c","#9c36b5"], bg:"#FFF9E3", text:"#1e1e1e" },
  noir:    { accents: ["#4cc9f0","#f72585","#4ade80","#fb923c","#a78bfa"], bg:"#1a1a1a", text:"#f1f1f1" },
  mint:    { accents: ["#0077b6","#d62828","#2d6a4f","#e76f51","#7209b7"], bg:"#e8faf0", text:"#1b4332" },
  craft:   { accents: ["#bf5700","#d62728","#6c757d","#e9b54a","#3d5a80"], bg:"#f6efe1", text:"#2d2d2d" },
  slate:   { accents: ["#0ea5e9","#ef4444","#22c55e","#f97316","#a855f7"], bg:"#1e293b", text:"#f1f5f9" },
  mono:    { accents: ["#000","#555","#888","#aaa","#ccc"], bg:"#fff", text:"#000" }
};
```

Expose the selected theme as `--bg`, `--text`, and `--accent-0` through `--accent-4`. Vary `accentIndex` for rhythm; reuse it across one narrative beat.

## Zones and video layouts

`card.zone` resolves the card-host bounds. Video bounds are set once in `videoTrack.bounds`; apparent movement is GSAP applied to `#video-wrap`.

| Zone | Resolved area | Use |
|---|---|---|
| `fullscreen` | Full canvas | Hero, number, mantra; video may hide or become PiP |
| `whiteboard-area` | 40px inset in landscape, or bottom 45% in portrait | Dense data and annotations |
| `lower-third` | Bottom 30% | Annotation over visible video |
| `side-panel` | Right 42% in landscape, bottom 40% in portrait | Split/sidebar |
| `video-overlay` | Full canvas with a mostly transparent root | Glass/annotation over full-bleed video |

The four coordinated recipes are:

| Layout | Recommended zone | Landscape `1920×1080` target for `#video-wrap` | Portrait `1080×1920` target | Use |
|---|---|---|---|---|
| `split` | `side-panel` | `{left:960,top:0,width:960,height:1080}` | `{left:0,top:960,width:1080,height:960}` | Equal 50:50 speaker/data weight |
| `stack` | `lower-third` | `{left:14,top:14,width:1892,height:548}` (top 52%) | `{left:0,top:0,width:1080,height:844}` (top 44%) | Speaker above summary |
| `pip` | `fullscreen` | `{left:1480,top:760,width:400,height:300}` | `{left:690,top:28,width:360,height:203}` | Card-led scene; add `.framed`/PiP chrome |
| `overlay` | `video-overlay` | `{left:0,top:0,width:1920,height:1080}` | `{left:0,top:0,width:1080,height:1920}` | Full-bleed cinematic video |

For 4:5, scale portrait `y` and `height` by `0.703`; keep horizontal values. A second landscape PiP option is top-left at `{left:40,top:40,width:400,height:300}`. A pure-graphic moment can hide video with `{opacity:0}` or move it off-canvas.

Use `object-fit: cover` inside the tweened wrapper. For no cropping, target a rectangle matching the source aspect and let the canvas/card/backdrop fill the remainder. Decorative frames are siblings of `#video-wrap`; suppress them for `overlay`. PiP already has pill chrome, so additional decorative frames normally belong to `split` or `stack`.

When video remains visible behind or beside a `lower-third`, `video-overlay`, overlay, or PiP moment, use a transparent card root. A side-panel may be opaque because its host already occupies only its half:

```css
html, body { background: var(--bg); }
.card[data-card-id="card-overlay"] .root { background: transparent; }
.card[data-card-id="card-hero"] .root { background: var(--bg); }
```

## Card fragment

Create `$WORK_DIR/public/cards/{card-id}.html` with one rooted fragment:

```html
<div class="card" data-card-id="card-01">
  <style>
    .card[data-card-id="card-01"] .root {
      width:100%; height:100%; display:flex;
      color:var(--text); background:transparent;
      font-family:Inter, Arial, sans-serif;
    }
    .card[data-card-id="card-01"] .title { font-size:84px; }
  </style>
  <div class="root">
    <h1 id="card-01-title" class="title"
        data-anim="kinetic-chars" data-anim-at="0.3"
        data-anim-duration="0.5" data-anim-stagger="0.04"
        data-anim-pattern="pop">
      <span class="char">S</span><span class="char">u</span>
    </h1>
    <div id="card-01-line" data-anim="grow-x"
         data-anim-at="0.65" data-anim-duration="0.5"
         data-anim-target-w="420"
         style="width:0;height:8px;background:var(--accent-0);border-radius:4px"></div>
  </div>
</div>
```

HyperFrames lint contract:

- One root `.card[data-card-id="<id>"]`.
- Prefix every inline CSS rule with that card selector.
- Use relative paths within `public/`.
- Use theme CSS variables for portable colors.
- Express animation with `data-anim-*`; compile it into the master composition timeline.
- Keep card fragments to scoped HTML and CSS. Load assets from local relative `src`/`href` values, keep event handling in the composition, and put animation in the master timeline.

## Sizing

The style references preview at `1920×1080`. For portrait, use:

| Token | Landscape | Portrait | Scale |
|---|---|---|---|
| Hero title | `64–96px` | `88–132px` | `1.35×`, up to `1.4×` |
| Body/detail | `24–30px` | `30–40px` | `1.30×` |
| Kicker/chip | `14–16px` | `18–22px` | `1.30×` |
| Timecode/meta | `12–14px` | `16–18px` | `1.20–1.30×` |
| Primary number | `48–60px` | `64–88px` | `1.40×` |
| Line-height | `1.05–1.5` | Same | Do not scale |

Rule: `portraitPx = round(landscapePx × 1.3)`, then floor to a nearby 4px multiple. Use `24–36px` portrait horizontal padding instead of landscape `40–64px`.

For one fragment that serves both layouts, use container-aware fluid sizing or explicit `@container` variants:

```css
.card[data-card-id="X"] .root { container-type:inline-size; }
.card[data-card-id="X"] .title { font-size:clamp(64px,8.5cqi,132px); }
.card[data-card-id="X"] .detail { font-size:clamp(24px,3.2cqi,40px); }
```

## Animation declarations

Choose two or three repeated patterns for visual coherence. `data-anim-at` is seconds relative to `card.startSec`.

| Kind | Purpose | Parameters |
|---|---|---|
| `fade-in`, `fade-out` | Opacity entrance/exit | `at duration ease?` |
| `slide-in` | Directional entrance | `at duration from=left|right|top|bottom distance` |
| `kinetic-chars` | Character pop/fade; needs `.char` children | `at duration stagger pattern=pop|fade` |
| `typewriter` | Slower character fade | Same character parameters |
| `count-up` | Number animation | `at duration from to format=.0f|.1f|.2f|,d` |
| `draw-path` | SVG path reveal | `at duration`; target is a `<path>` |
| `grow-y`, `grow-x` | Bar size from zero | `target-h` or `target-w` in px |
| `scale-pop`, `blur-in` | Pop or focus entrance | `at duration` |
| `mask-reveal` | Directional clip | `at duration direction=left|right|top|bottom` |
| `morph-to` | Arbitrary CSS tween | `at duration props='{...JSON...}'` |

Build the fully visible static hero frame first, then add motion.
