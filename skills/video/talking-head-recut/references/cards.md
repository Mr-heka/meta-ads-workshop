# Card authoring and visual library

## Read the inherited library first

The inherited `references/` library separates three orthogonal dimensions:

```text
Style (10) × Layout (4) × VideoFrame (3)
```

`DESIGN_INDEX.md` contains the decision guide, ratio behavior, portrait sizing, and copying constraints. Read it, then read only the selected files:

- `references/styles/<key>.html`: `academic`, `editorial`, `minimal`, `spotlight`, `geom`, `whiteboard`, `audit`, `terminal`, `swiss`, or `xhs`.
- `references/layouts/<key>.html`: `split`, `stack`, `pip`, or `overlay`, with exact landscape, portrait, and 4:5 bounds.
- `references/frames/<key>.html`: `clean`, `hairline`, or `polaroid`, with placement HTML and CSS.

The style controls card typography, colors, ornament, and internal layout. The layout controls how card and video share the canvas. The frame supplies video chrome. Copy a selected style’s scoped block, rename its `data-card-id`, and replace the placeholder takeaway. These style tokens live in each card rather than `storyboard.composition`.

Mix dimensions between cards when transitions remain legible. Decorative frames are siblings of `#video-wrap`; use them with `split` and `stack`. `overlay` stays clean because its video is full-bleed. PiP already has a rounded pill treatment; `polaroid` becomes cramped in portrait PiP.

For brand values such as brand hex codes, typefaces, or prices, read the user's own brand guide. The following palettes and fonts are renderer configuration bundled with this skill.

## Composition theme configuration

Use a composition palette as `--accent-0` through `--accent-4`, `--bg`, and `--text`:

```js
const themes = {
  classic: { accents: ["#1971c2", "#e03131", "#2f9e44", "#e8590c", "#9c36b5"], bg: "#FFF9E3", text: "#1e1e1e" },
  noir:    { accents: ["#4cc9f0", "#f72585", "#4ade80", "#fb923c", "#a78bfa"], bg: "#1a1a1a", text: "#f1f1f1" },
  mint:    { accents: ["#0077b6", "#d62828", "#2d6a4f", "#e76f51", "#7209b7"], bg: "#e8faf0", text: "#1b4332" },
  craft:   { accents: ["#bf5700", "#d62728", "#6c757d", "#e9b54a", "#3d5a80"], bg: "#f6efe1", text: "#2d2d2d" },
  slate:   { accents: ["#0ea5e9", "#ef4444", "#22c55e", "#f97316", "#a855f7"], bg: "#1e293b", text: "#f1f5f9" },
  mono:    { accents: ["#000", "#555", "#888", "#aaa", "#ccc"], bg: "#fff", text: "#000" }
};
```

Bundled WOFF2 fonts under `<SKILL_DIR>/assets/fonts/` are Caveat handwriting, LXGW WenKai TC Chinese hand-script, Inter modern sans, and Virgil geometric hand. Stage them into `public/fonts/` and declare them with `@font-face`.

## Fragment contract

Create `$WORK_DIR/public/cards/{card-id}.html` for every card. Each file contains one `.card` root, scoped inline CSS, local relative assets, and declarative animation attributes:

```html
<div class="card" data-card-id="card-01">
  <style>
    .card[data-card-id="card-01"] .root {
      width: 100%;
      height: 100%;
      display: flex;
      font-family: "Caveat", "LXGW WenKai TC", serif;
      color: var(--text);
      background: var(--bg);
    }
    .card[data-card-id="card-01"] .title { font-size: 84px; }
  </style>
  <div class="root">
    <h1 id="card-01-title" class="title"
        data-anim="kinetic-chars" data-anim-at="0.3"
        data-anim-duration="0.5" data-anim-stagger="0.04"
        data-anim-pattern="pop">
      <span class="char">S</span><span class="char">u</span>
    </h1>
    <div id="card-01-line"
         data-anim="grow-x" data-anim-at="0.65"
         data-anim-duration="0.5" data-anim-target-w="420"
         style="width:0;height:8px;background:var(--accent-0);border-radius:4px">
    </div>
  </div>
</div>
```

HyperFrames’ fragment contract:

| Concern | Required shape |
| --- | --- |
| Root | One `<div class="card" data-card-id="{cardId}">` |
| CSS scope | Every rule begins `.card[data-card-id="{cardId}"]` |
| Motion | `data-anim-*` declarations compiled into the master timeline |
| Code | Fragment contains HTML/CSS and omits `<script>` and inline event handlers |
| Assets | Relative paths inside `public/`; omit CDN, remote fonts, and external `src`/`href` URLs |
| Color | Theme variables such as `var(--accent-N)`, `var(--bg)`, and `var(--text)` |

For layouts that keep video visible (`overlay`, `pip`, `lower-third`, or `video-overlay`), make `.root` transparent. A fullscreen card may paint `var(--bg)`. A `side-panel` host may be opaque because it covers only its own half.

```css
html, body { background: var(--bg); }
.card[data-card-id="card-overlay"] .root { background: transparent; }
.card[data-card-id="card-hero"] .root { background: var(--bg); }
```

## Portrait sizing

Inherited style cards target 1920×1080. For a 1080×1920 mobile composition, scale visual type up while narrowing horizontal padding:

| Token | Landscape | Portrait | Scale |
| --- | --- | --- | --- |
| hero title | 64–96px | 88–132px | about 1.35 |
| detail/body | 24–30px | 30–40px | about 1.30 |
| kicker/chip | 14–16px | 18–22px | about 1.30 |
| timecode/meta | 12–14px | 16–18px | about 1.30 |
| primary number | 48–60px | 64–88px | about 1.40 |
| line-height | 1.05–1.5 | unchanged | 1.0 |

Use `portraitPx = round(landscapePx × 1.3)`, then floor near a 4px multiple. Hero text can reach `×1.4`; small meta can stay near `×1.2`. Use 24–36px portrait horizontal padding instead of 40–64px landscape padding.

For one fragment that must span layouts:

```css
.card[data-card-id="X"] .root { container-type: inline-size; }
.card[data-card-id="X"] .title { font-size: clamp(64px, 8.5cqi, 132px); }
.card[data-card-id="X"] .detail { font-size: clamp(24px, 3.2cqi, 40px); }
```

## Declarative animation vocabulary

`data-anim-at` is relative to the card’s `startSec`. During composition assembly, calculate absolute time as `card.startSec + data-anim-at` and quantize to `1/fps`.

| Kind | Purpose | Attribute keys |
| --- | --- | --- |
| `fade-in` | entrance | `data-anim-at`, `data-anim-duration`, optional `data-anim-ease` |
| `fade-out` | exit | `data-anim-at`, `data-anim-duration`, optional `data-anim-ease` |
| `slide-in` | directional entrance | `data-anim-at`, `data-anim-duration`, `data-anim-from=left|right|top|bottom`, `data-anim-distance` |
| `kinetic-chars` | per-character pop/fade | `data-anim-at`, `data-anim-duration`, `data-anim-stagger`, `data-anim-pattern=pop|fade`; element has `.char` spans |
| `typewriter` | slower per-character fade | kinetic-character attributes with a slower default stagger |
| `count-up` | number tween | `data-anim-at`, `data-anim-duration`, `data-anim-from`, `data-anim-to`, `data-anim-format=.0f|.1f|.2f|,d` |
| `draw-path` | SVG reveal | `data-anim-at`, `data-anim-duration`; target is a `<path>` |
| `grow-y` | bar height | `data-anim-at`, `data-anim-duration`, `data-anim-target-h`; starts at `height:0` |
| `grow-x` | bar width | `data-anim-at`, `data-anim-duration`, `data-anim-target-w`; starts at `width:0` |
| `scale-pop` | pop entrance | `data-anim-at`, `data-anim-duration` |
| `blur-in` | unfocused to focused | `data-anim-at`, `data-anim-duration` |
| `mask-reveal` | directional clip reveal | `data-anim-at`, `data-anim-duration`, `data-anim-direction=left|right|top|bottom` |
| `morph-to` | arbitrary CSS tween | `data-anim-at`, `data-anim-duration`, `data-anim-props='{...JSON...}'` |
