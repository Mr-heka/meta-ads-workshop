# Composition and render QA

## Assembly contract

Write `$WORK_DIR/public/index.html` after staging fonts, GSAP, and the dense-keyframe `input-video.mp4` from [workflow.md](workflow.md).

The page contains:

1. One `#stage` with `data-composition-id="talking-head-recut"`, `data-start`, `data-duration`, `data-fps`, `data-width`, and `data-height`.
2. One `#video-wrap` around the muted, inline source video on `data-track-index="1"`.
3. One `.card-host.clip` per storyboard card on `data-track-index="2"`, with inline resolved bounds, `data-start`, and `data-duration`.
4. The card fragments copied inside their hosts.
5. Bundled `vendor/gsap.min.js` and one synchronously constructed paused timeline registered as `window.__timelines["talking-head-recut"]`.

This complete composition is the canonical example:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <style>
    @font-face {
      font-family: "Caveat";
      src: url("fonts/Caveat-400-latin.woff2") format("woff2");
      font-weight: 400;
      font-display: block;
    }
    @font-face {
      font-family: "Caveat";
      src: url("fonts/Caveat-700-latin.woff2") format("woff2");
      font-weight: 700;
      font-display: block;
    }
    @font-face {
      font-family: "LXGW WenKai TC";
      src: url("fonts/LXGWWenKaiTC-400-latin.woff2") format("woff2");
      font-weight: 400;
      font-display: block;
    }
    @font-face {
      font-family: "Inter";
      src: url("fonts/Inter-400-latin.woff2") format("woff2");
      font-weight: 400;
      font-display: block;
    }
    @font-face {
      font-family: "Inter";
      src: url("fonts/Inter-700-latin.woff2") format("woff2");
      font-weight: 700;
      font-display: block;
    }
    @font-face {
      font-family: "Virgil";
      src: url("fonts/Virgil.woff2") format("woff2");
      font-display: block;
    }

    :root {
      --bg: #fff9e3;
      --text: #1e1e1e;
      --accent-0: #1971c2;
      --accent-1: #e03131;
      --accent-2: #2f9e44;
      --accent-3: #e8590c;
      --accent-4: #9c36b5;
      --font-family: "Caveat", "LXGW WenKai TC", serif;
    }
    * { box-sizing: border-box; }
    html, body {
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      background: #000;
      font-family: "Inter", "Caveat", "LXGW WenKai TC",
        ui-sans-serif, system-ui, sans-serif;
    }
    #stage { position: relative; width: 100%; height: 100%; overflow: hidden; }
    .video-wrapper {
      position: absolute;
      left: 0;
      top: 0;
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      border-radius: 0;
      box-shadow: none;
    }
    .video-wrapper video { width: 100%; height: 100%; object-fit: cover; }
    .video-wrapper.framed {
      border-radius: 16px;
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.35);
    }
    .card-host { position: absolute; pointer-events: none; overflow: hidden; }
    .card-host .card { position: relative; width: 100%; height: 100%; overflow: hidden; }
    .card-host .char { display: inline-block; visibility: visible; }
  </style>
</head>
<body>
  <div id="stage"
       data-composition-id="talking-head-recut"
       data-start="0" data-duration="121.2" data-fps="30"
       data-width="1920" data-height="1080">
    <div class="video-wrapper" id="video-wrap">
      <video id="bg-video" src="input-video.mp4" muted playsinline
             data-start="0" data-duration="121.2"
             data-track-index="1"></video>
    </div>

    <div class="card-host clip"
         data-card-id="card-01"
         data-start="1.0000" data-duration="6.5000"
         data-track-index="2"
         style="left:0;top:0;width:1920px;height:1080px;
                visibility:hidden;opacity:0">
      <!-- contents of public/cards/card-01.html -->
    </div>

    <div class="card-host clip"
         data-card-id="card-02"
         data-start="8.0000" data-duration="12.0000"
         data-track-index="2"
         style="left:0;top:0;width:960px;height:1080px;
                visibility:hidden;opacity:0">
      <!-- contents of public/cards/card-02.html -->
    </div>

    <script src="vendor/gsap.min.js"></script>
    <script>
      (function () {
        window.__fmt = function (v, fmt) {
          if (typeof fmt === "string" && /^\.[0-9]+f$/.test(fmt)) {
            return Number(v).toFixed(Number(fmt.slice(1, -1)));
          }
          if (fmt === ",d") return Math.round(v).toLocaleString();
          return String(Math.round(v));
        };

        const tl = window.gsap.timeline({ paused: true });

        tl.set('.card-host[data-card-id="card-01"]',
          { visibility: "visible" }, 1.0);
        tl.fromTo('.card-host[data-card-id="card-01"]',
          { opacity: 0 },
          { opacity: 1, duration: 0.4, ease: "power2.out" }, 1.0);
        tl.from('.card[data-card-id="card-01"] #card-01-title .char',
          { opacity: 0, y: 8, scale: 0.8, duration: 0.5,
            ease: "power2.out", stagger: 0.04 }, 1.3);
        tl.fromTo('.card[data-card-id="card-01"] #card-01-line',
          { width: 0 },
          { width: 420, duration: 0.5, ease: "power2.out" }, 1.65);
        tl.to('.card-host[data-card-id="card-01"]',
          { opacity: 0, duration: 0.35, ease: "power2.in" }, 7.15);
        tl.set('.card-host[data-card-id="card-01"]',
          { visibility: "hidden" }, 7.5);

        tl.set("#video-wrap",
          { className: "video-wrapper framed" }, 7.5);
        tl.to("#video-wrap",
          { left: 960, top: 0, width: 960, height: 1080,
            duration: 0.6, ease: "power2.inOut" }, 7.5);

        tl.set('.card-host[data-card-id="card-02"]',
          { visibility: "visible" }, 8.0);
        tl.fromTo('.card-host[data-card-id="card-02"]',
          { opacity: 0 },
          { opacity: 1, duration: 0.4, ease: "power2.out" }, 8.0);

        window.__timelines = window.__timelines || {};
        window.__timelines["talking-head-recut"] = tl;
      })();
    </script>
  </div>
</body>
</html>
```

The example shows card 01 from `1.0` to `7.5`, a 0.4-second entrance, internal motion at `1.3` and `1.65`, a 0.35-second exit beginning at `7.15`, and a 0.6-second video transition at `7.5` before card 02 begins at `8.0`.

## Compile declarative animation

For selector `.card[data-card-id="X"] #elementId`, calculate:

```js
const T = Math.round((card.startSec + relativeAt) * fps) / fps;
```

At 30fps, the minimum step is `1/30 ≈ 0.0333s`; four decimal places are sufficient.

| Declaration | GSAP statement |
| --- | --- |
| `fade-in` | `tl.fromTo(SEL,{opacity:0},{opacity:1,duration:D,ease:"power2.out"},T);` |
| `fade-out` | `tl.to(SEL,{opacity:0,duration:D,ease:"power2.in"},T);` |
| `slide-in`, left, 80 | `tl.fromTo(SEL,{opacity:0,x:-80},{opacity:1,x:0,duration:D,ease:"power2.out"},T);` |
| `kinetic-chars`, pop | `tl.from(SEL+" .char",{opacity:0,y:8,scale:.8,duration:D,ease:"power2.out",stagger:S},T);` |
| `count-up` | `(function(){const o={v:FROM};tl.to(o,{v:TO,duration:D,ease:"power2.out",onUpdate:function(){const el=document.querySelector(SEL);if(el)el.textContent=__fmt(o.v,"FMT");}},T);})();` |
| `draw-path` | `(function(){const el=document.querySelector(SEL);if(el){const L=el.getTotalLength();tl.set(SEL,{strokeDasharray:L,strokeDashoffset:L},T);tl.to(SEL,{strokeDashoffset:0,duration:D,ease:"power2.inOut"},T);}})();` |
| `grow-x` | `tl.fromTo(SEL,{width:0},{width:W,duration:D,ease:"power2.out"},T);` |
| `grow-y` | `tl.fromTo(SEL,{height:0},{height:H,duration:D,ease:"power2.out"},T);` |
| `scale-pop` | `tl.fromTo(SEL,{opacity:0,scale:.6},{opacity:1,scale:1,duration:D,ease:"back.out(1.6)"},T);` |
| `mask-reveal`, left | `tl.fromTo(SEL,{clipPath:"inset(0 100% 0 0)"},{clipPath:"inset(0 0 0 0)",duration:D,ease:"power2.inOut"},T);` |

Implement `typewriter`, `blur-in`, and `morph-to` with their declared parameters in the same timeline.

## Video framing

Set `#video-wrap` inline to card 01’s bounds. Between cards, tween the wrapper rather than the video element. Use a 0.5–0.7-second `power2.inOut` transition.

Landscape 1920×1080 targets:

| Recipe | Typical zone | `#video-wrap` target |
| --- | --- | --- |
| `split` | `side-panel` | `{left:960,top:0,width:960,height:1080}` |
| `stack` | `lower-third` | `{left:14,top:14,width:1892,height:548}`; top 52% |
| `pip`, bottom-right | `fullscreen` | `{left:1480,top:760,width:400,height:300}` plus `pip-pill` |
| `pip`, top-left | `fullscreen` | `{left:40,top:40,width:400,height:300}` plus `pip-pill` |
| `overlay` | `video-overlay` | `{left:0,top:0,width:1920,height:1080}` |
| pure graphic | `fullscreen` | `{opacity:0}` or move the wrapper off canvas |

Portrait targets include `split {left:0,top:960,width:1080,height:960}`, `stack {left:0,top:0,width:1080,height:844}` for the top 44%, `pip {left:690,top:28,width:360,height:203}`, and full-bleed overlay `{left:0,top:0,width:1080,height:1920}`. Use the inherited layout files for source-aspect variants and exact 4:5 values.

PiP chrome toggles through the wrapper class:

```js
tl.set("#video-wrap", { className: "video-wrapper pip-pill" }, T);
tl.to("#video-wrap",
  { left: 1480, top: 760, width: 400, height: 300,
    duration: 0.6, ease: "power2.inOut" }, T);

tl.set("#video-wrap", { className: "video-wrapper" }, T_NEXT);
tl.to("#video-wrap",
  { left: 0, top: 0, width: 1920, height: 1080,
    duration: 0.6, ease: "power2.inOut" }, T_NEXT);
```

Decorative frame markup sits beside `#video-wrap` and follows its transitions. Resolve each `card.zone` to pixel bounds and write them into the host’s inline `left`, `top`, `width`, and `height`. A `video-overlay` host fills the canvas; the visible card placement comes from `.card .root`.

## Deterministic QA contract

- Build and inspect each static hero frame before motion.
- Check that video, cards, subtitles/captions, and diagrams overlap only by design; clip hidden video areas to their frames.
- Register exactly one paused `window.__timelines["talking-head-recut"]` and build it synchronously at page load.
- Keep render paths deterministic: synchronous statements, fixed values, and finite repeats calculated from duration. Omit `async`, `setTimeout`, Promises, media `play()` calls, `Math.random()`, `Date.now()`, and `repeat:-1`.
- Prefer transform/opacity motion (`x`, `y`, `scale`, `rotation`, `opacity`). Use layout-property tweens only for deliberate wrapper reframing.
- Animate `#video-wrap`, avoid simultaneous timelines changing the same property on the same element, and keep video dimensions controlled by the wrapper.
- Use `data-track-index` rather than `data-layer`, and `data-duration` rather than `data-end`.
- Give every timed element, including card hosts and sub-compositions, a `clip` class so HyperFrames gates visibility to `data-start … data-start+data-duration`; otherwise lint reports `timed_element_missing_clip_class`.
- Declare concrete font names on `html` and `body`. The static font resolver does not expand CSS variables there and reports `font_family_without_font_face`; card internals may still use `var(--font-family)`.
