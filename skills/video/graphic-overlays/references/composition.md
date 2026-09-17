# Composition Assembly

## Stage assets and media

The current bundle has GSAP but no fonts:

```bash
SKILL_DIR="<SKILL_DIR>"
mkdir -p "$WORK_DIR/public/vendor" "$WORK_DIR/public/cards"
cp -n "$SKILL_DIR/assets/vendor/gsap.min.js" "$WORK_DIR/public/vendor/"

# Copy only font files that actually exist:
mkdir -p "$WORK_DIR/public/fonts"
find "$SKILL_DIR/assets/fonts" -maxdepth 1 -type f -name '*.woff2' \
  -exec cp -n {} "$WORK_DIR/public/fonts/" \; 2>/dev/null || true

# Dense keyframes prevent sparse-GOP sources freezing during renderer seeks.
# Set -g and -keyint_min to composition fps: 24, 25, 30, or 60.
ffmpeg -y -i "$VIDEO_PATH" -c:v libx264 -crf 18 -g 30 -keyint_min 30 \
  -pix_fmt yuv420p -movflags +faststart -c:a aac \
  "$WORK_DIR/public/input-video.mp4"
```

## Composition template

Write `$WORK_DIR/public/index.html`. Match canvas dimensions, durations, card bounds, and selectors to the storyboard:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <style>
    /*
    Intended font roles if these optional files are supplied:
    Caveat = handwriting; LXGW WenKai TC = Chinese hand-script;
    Inter = modern sans; Virgil = geometric hand.
    Optional only when these exact local files exist:
    @font-face{font-family:"Caveat";src:url("fonts/Caveat-400-latin.woff2") format("woff2");font-weight:400;font-display:block}
    @font-face{font-family:"Caveat";src:url("fonts/Caveat-700-latin.woff2") format("woff2");font-weight:700;font-display:block}
    @font-face{font-family:"LXGW WenKai TC";src:url("fonts/LXGWWenKaiTC-400-latin.woff2") format("woff2");font-weight:400;font-display:block}
    @font-face{font-family:"Inter";src:url("fonts/Inter-400-latin.woff2") format("woff2");font-weight:400;font-display:block}
    @font-face{font-family:"Inter";src:url("fonts/Inter-700-latin.woff2") format("woff2");font-weight:700;font-display:block}
    @font-face{font-family:"Virgil";src:url("fonts/Virgil.woff2") format("woff2");font-display:block}
    */
    :root {
      --bg:#fff9e3; --text:#1e1e1e;
      --accent-0:#1971c2; --accent-1:#e03131; --accent-2:#2f9e44;
      --accent-3:#e8590c; --accent-4:#9c36b5;
      --font-family:Inter,Arial,sans-serif;
    }
    *{box-sizing:border-box}
    html,body{
      margin:0;padding:0;width:100%;height:100%;overflow:hidden;background:#000;
      font-family:Inter,Arial,sans-serif;
    }
    #stage{position:relative;width:100%;height:100%;overflow:hidden}
    .video-wrapper{
      position:absolute;left:0;top:0;width:1920px;height:1080px;
      overflow:hidden;border-radius:0;box-shadow:none;
    }
    .video-wrapper video{width:100%;height:100%;object-fit:cover}
    .video-wrapper.framed,.video-wrapper.pip-pill{
      border-radius:16px;box-shadow:0 12px 40px rgba(0,0,0,.35);
    }
    .card-host{position:absolute;pointer-events:none;overflow:hidden}
    .card-host .card{position:relative;width:100%;height:100%;overflow:hidden}
    .card-host .char{display:inline-block;visibility:visible}
  </style>
</head>
<body>
<div id="stage"
     data-composition-id="graphic-overlays"
     data-start="0" data-duration="121.2" data-fps="30"
     data-width="1920" data-height="1080">

  <div class="video-wrapper" id="video-wrap">
    <video id="bg-video" src="input-video.mp4" muted playsinline
           data-start="0" data-duration="121.2" data-track-index="1"></video>
  </div>

  <div class="card-host clip" data-card-id="card-01"
       data-start="1.0000" data-duration="6.5000" data-track-index="2"
       style="left:0;top:0;width:1920px;height:1080px;visibility:hidden;opacity:0">
    <!-- inline public/cards/card-01.html -->
  </div>

  <div class="card-host clip" data-card-id="card-02"
       data-start="8.0000" data-duration="12.0000" data-track-index="2"
       style="left:0;top:0;width:960px;height:1080px;visibility:hidden;opacity:0">
    <!-- inline public/cards/card-02.html -->
  </div>

  <script src="vendor/gsap.min.js"></script>
  <script>
  (function(){
    window.__fmt=function(v,fmt){
      if(typeof fmt==="string" && /^\.[0-9]+f$/.test(fmt))
        return Number(v).toFixed(Number(fmt.slice(1,-1)));
      if(fmt===",d") return Math.round(v).toLocaleString();
      return String(Math.round(v));
    };

    const tl=window.gsap.timeline({paused:true});

    tl.set('.card-host[data-card-id="card-01"]',{visibility:"visible"},1.0);
    tl.fromTo('.card-host[data-card-id="card-01"]',
      {opacity:0},{opacity:1,duration:.4,ease:"power2.out"},1.0);
    tl.from('.card[data-card-id="card-01"] #card-01-title .char',
      {opacity:0,y:8,scale:.8,duration:.5,ease:"power2.out",stagger:.04},1.3);
    tl.fromTo('.card[data-card-id="card-01"] #card-01-line',
      {width:0},{width:420,duration:.5,ease:"power2.out"},1.65);
    tl.to('.card-host[data-card-id="card-01"]',
      {opacity:0,duration:.35,ease:"power2.in"},7.15);
    tl.set('.card-host[data-card-id="card-01"]',{visibility:"hidden"},7.5);

    tl.set("#video-wrap",{className:"video-wrapper framed"},7.5);
    tl.to("#video-wrap",
      {left:960,top:0,width:960,height:1080,duration:.6,ease:"power2.inOut"},7.5);

    tl.set('.card-host[data-card-id="card-02"]',{visibility:"visible"},8.0);
    tl.fromTo('.card-host[data-card-id="card-02"]',
      {opacity:0},{opacity:1,duration:.4,ease:"power2.out"},8.0);

    window.__timelines=window.__timelines||{};
    window.__timelines["graphic-overlays"]=tl;
  })();
  </script>
</div>
</body>
</html>
```

Every host needs both `card-host` and `clip`. HyperFrames uses `.clip` to enforce `data-start` through `data-start + data-duration`; the `timed_element_missing_clip_class` lint identifies a host that would otherwise remain visible for the full video.

Name concrete fonts in the body/global `font-family`. Static analysis does not expand CSS variables, so `font_family_without_font_face` identifies a var-only chain. Cards may use `var(--font-family)`.

## Compile declarations into GSAP

For every declaration:

```text
absoluteSeconds = card.startSec + data-anim-at
T = Math.round(absoluteSeconds × fps) / fps
```

At 30fps the smallest step is `1/30 ≈ 0.0333s`; four decimal places are sufficient. Use `.card[data-card-id="X"] #elementId`.

```js
// fade-in
tl.fromTo(SEL,{opacity:0},{opacity:1,duration:D,ease:"power2.out"},T);
// fade-out
tl.to(SEL,{opacity:0,duration:D,ease:"power2.in"},T);
// slide-in from left by 80
tl.fromTo(SEL,{opacity:0,x:-80},{opacity:1,x:0,duration:D,ease:"power2.out"},T);
// kinetic-chars pop
tl.from(SEL+" .char",{opacity:0,y:8,scale:.8,duration:D,ease:"power2.out",stagger:S},T);
// count-up
(function(){const o={v:FROM};tl.to(o,{v:TO,duration:D,ease:"power2.out",
  onUpdate:function(){const el=document.querySelector(SEL);if(el)el.textContent=__fmt(o.v,"FMT");}},T);})();
// draw-path
(function(){const el=document.querySelector(SEL);if(el){const L=el.getTotalLength();
  tl.set(SEL,{strokeDasharray:L,strokeDashoffset:L},T);
  tl.to(SEL,{strokeDashoffset:0,duration:D,ease:"power2.inOut"},T);}})();
// grow-x / grow-y
tl.fromTo(SEL,{width:0},{width:W,duration:D,ease:"power2.out"},T);
tl.fromTo(SEL,{height:0},{height:H,duration:D,ease:"power2.out"},T);
// scale-pop
tl.fromTo(SEL,{opacity:0,scale:.6},{opacity:1,scale:1,duration:D,ease:"back.out(1.6)"},T);
// mask-reveal from left
tl.fromTo(SEL,{clipPath:"inset(0 100% 0 0)"},
  {clipPath:"inset(0 0 0 0)",duration:D,ease:"power2.inOut"},T);
```

`typewriter`, `blur-in`, and `morph-to` follow their declaration semantics with a deterministic `tl.fromTo` or `tl.to`.

## Video transitions

Set initial inline bounds to the first card layout. Between cards, tween `#video-wrap` for `0.5–0.7s` with `power2.inOut`. Animate the wrapper, not video dimensions:

```js
// Enter landscape PiP
tl.set("#video-wrap",{className:"video-wrapper pip-pill"},T);
tl.to("#video-wrap",
  {left:1480,top:760,width:400,height:300,duration:.6,ease:"power2.inOut"},T);

// Leave PiP for clean full bleed
tl.set("#video-wrap",{className:"video-wrapper"},T_NEXT);
tl.to("#video-wrap",
  {left:0,top:0,width:1920,height:1080,duration:.6,ease:"power2.inOut"},T_NEXT);
```

Resolve each `card.zone` to pixels and write those bounds into the host’s inline `left`, `top`, `width`, and `height`. A `video-overlay` host fills the canvas; its inner CSS positions the visible glass card.
