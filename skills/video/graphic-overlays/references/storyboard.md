# Storyboard and Decision Contract

## Storyboard shape

`storyboard.json` is an inspectable planning artifact. No HyperFrames command parses it. Keep this v3 shape stable so card IDs, timing, content, and the HTML assembly stay aligned:

```json
{
  "schemaVersion": 3,
  "composition": {
    "fps": 30,
    "width": 1080,
    "height": 1920,
    "durationSeconds": 121.2,
    "layout": "portrait",
    "themeId": "noir",
    "seed": 42
  },
  "videoTrack": {
    "sourcePath": "input-video.mp4",
    "startSec": 0,
    "endSec": 121.2,
    "bounds": { "x": 0, "y": 0, "width": 1080, "height": 1920 }
  },
  "subtitles": { "enabled": false },
  "cards": [
    {
      "id": "card-01",
      "intent": "Hook with the speaker's anxious midnight question",
      "startSec": 0.5,
      "endSec": 13,
      "accentIndex": 0,
      "zone": "fullscreen",
      "contentHints": {
        "kicker": "AN HONEST QUESTION",
        "title": "The soul-searching question at 11 PM",
        "detail": "Client's 60-second voice message: 'If the RMB appreciates, does that mean my USD policy is a terrible loss?'"
      }
    }
  ]
}
```

`composition` owns `fps`, `width`, `height`, `durationSeconds`, `layout`, `themeId`, and `seed`; none belongs at the top level. `videoTrack.bounds` defaults to the full canvas. `subtitles` is explicit. Each card requires:

| Field | Contract |
|---|---|
| `id` | Stable string used by HTML and GSAP selectors |
| `intent` | Natural-language design purpose |
| `startSec`, `endSec` | Seconds; `endSec > startSec`; stay within composition duration |
| `accentIndex` | Integer `0` through `4` |
| `zone` | `fullscreen`, `whiteboard-area`, `lower-third`, `side-panel`, or `video-overlay` |
| `contentHints` | Free-form string or JSON data such as kicker, title, detail, data, or quote |

Optional: free-form `archetype`, and `transition` from `cut`, `fade`, `slide`, or `wipe`. A planning content payload may be a plain string such as `"Title: annualized 5.69%\nNotes: ..."` or any JSON shape. Cards may overlap only intentionally; use `data-track-index` for z-order. Visual styling belongs in the card HTML, not `contentHints`. Style/layout/frame choices stay in working memory, not this schema. There is no `card.layout` field.

## Card count

Cards follow transcript ideas, not a prescribed role list or narrative arc. The minimum is five; there is no upper clamp.

| Duration | Medium-density base pace |
|---|---|
| `<60s` | `6–8s/card` |
| `60s–3m` | `8–12s/card` |
| `3–10m` | `12–20s/card` |
| `10–30m` | `20–35s/card` |
| `>30m` | `30–60s/card` |

Choose a representative point in the range, then multiply by transcript density:

| Density | Signal | Multiplier |
|---|---|---|
| High | Many numbers or claims, staccato/list pacing, a new idea every 1–2 sentences | `0.7` |
| Medium | Mixed data and narrative | `1.0` |
| Low | Extended story, repeated reframing, slow reflection, one unfolding argument | `1.5` |

```text
secPerCard = basePace × densityMultiplier
autoCount  = max(5, round(videoDurationSec / secPerCard))
```

Calibration examples:

- 30s reel, low density: `7 × 1.5 = 10.5`, `round(30/10.5)=3`, floor to **5**.
- 60s reflective monologue: `10 × 1.5 = 15`, `4`, floor to **5**.
- 121s rich-data talking head: `10 × 0.7 = 7`, about **17**.
- 5m mixed interview: `16 × 1.0`, about **19**.
- 10m high-density deep dive: `16 × 0.7 = 11`, about **55**.
- 30m medium lecture: `28 × 1.0`, about **64**.
- 1h low-density podcast: `45 × 1.5 = 67.5`, about **53**.

A static one-liner becomes dull after 8 seconds. For cards longer than about 15 seconds, plan a data block, multi-step reveal, or staggered sub-points. When many cards exceed 30 seconds, split chapters into separate HTML sub-compositions mounted with `data-composition-src`; this also prevents HyperFrames `timeline_track_too_dense`.

The bundle has no fixed brand outro. If the user requests one, add a neutral wordmark plus one-line tagline for about `1.5–2s`, fade in, hold briefly, fade out, append it to `cards[]`, and extend duration to its `endSec`.

## Confirm visual direction

Before designing cards or bounds, compute:

```text
sourceAspect = sourceWidth / sourceHeight
sourceAspect >= 1.5  -> recommend 16:9 (about 3:2 or wider)
sourceAspect <= 0.7  -> recommend 9:16 (about 9:13 or taller)
otherwise            -> recommend 4:5
```

Also compute `autoCount`. Ask once for ratio, overall layout, style group, and card count. Use `AskUserQuestion` when available, otherwise another native clarification tool such as `ask_question` or `request_user_input`, otherwise one plain-text message with four numbered questions. Keep each round to 2–5 questions. Put the recommendation first and explain that it matches source dimensions.

Options:

| Decision | Choices |
|---|---|
| Ratio | `16:9` `1920×1080` for TV/YouTube/desktop; `9:16` `1080×1920` for TikTok/Reels/mobile; `4:5` `1080×1350` for Instagram feed/WeChat Moments |
| Layout | `split` side-by-side 50/50; `stack` video top/card bottom; `pip` card-led with rounded video window; `overlay` full-bleed video with glass card |
| Style group | `warm-paper`: academic/editorial/whiteboard/xhs; `clinical`: audit/swiss/terminal/minimal; `experimental`: geom/spotlight |
| Count | Auto `autoCount`; fewer `max(5, round(autoCount × 0.6))`; more `round(autoCount × 1.5)`; or an integer floored at 5 |

Structured-question contract:

```js
AskUserQuestion({
  questions: [
    { question: "Output video aspect ratio (canvas):", header: "Aspect ratio", multiSelect: false, options: RATIO_OPTIONS_RECOMMENDED_FIRST },
    { question: "Choose the overall layout: how should the video and cards coexist on the canvas?", header: "Layout", multiSelect: false, options: LAYOUT_OPTIONS },
    { question: "Choose the card visual style (style):", header: "Style group", multiSelect: false, options: STYLE_GROUP_OPTIONS },
    { question: "Card count (takeaway pacing): how many cards to cut?", header: "Card count", multiSelect: false, options: COUNT_OPTIONS }
  ]
})
```

Native `AskUserQuestion` supplies an `Other` choice. Parse an integer and floor it at five; non-integer input falls back to auto.

Plain-text fallback:

```text
I need to confirm four visual decisions:
1) Ratio: A 16:9, B 9:16, C 4:5. Recommendation: <recommendedRatio>, matches <sourceW>×<sourceH>.
2) Layout: A split, B stack, C pip, D overlay.
3) Style: A warm-paper, B clinical, C experimental.
4) Count: A auto ≈<autoCount>, B fewer ≈round(N×0.6), C more ≈round(N×1.5), D a number.
Reply “1A 2C 3B 4A”, natural language, or “default”.
```

Accept loose replies such as `A C B A`, `16:9 / pip / data / auto`, full sentences, `default`, `auto`, or `use all recommendations`. Re-ask only ambiguous decisions. If defaults were pre-approved or questions were declined, use the recommended ratio, `stack`, the most neutral transcript-matched editorial/data style, and `autoCount`; state the choices and continue.

Map canvas exactly:

| Ratio | Width × height | `composition.layout` |
|---|---|---|
| `16:9` | `1920×1080` | `landscape` |
| `9:16` | `1080×1920` | `portrait` |
| `4:5` | `1080×1350` | `portrait` |

For 4:5, keep portrait horizontal values and scale vertical values by `1350/1920 ≈ 0.703`. Example: `{x:24,y:1280,w:1032,h:564}` becomes `{x:24,y:900,w:1032,h:397}`.

Within the chosen style group, select the specific style from transcript tone. If two remain genuinely tied, ask one 2–4-option follow-up. Free-text style names are design hints outside the 10-style library; keep the chosen layout bounds.

Auto-pick the frame:

| Layout | Warm-paper | Clinical | Experimental |
|---|---|---|---|
| `split` | `polaroid` | `hairline` | `clean` |
| `stack` | `polaroid` | `hairline` | `clean` |
| `pip` | `clean` | `clean` | `clean` |
| `overlay` | `clean` | `clean` | `clean` |

Tell the user the ratio and canvas, layout, specific style, frame, and final card count in one sentence. Retain those five values in working memory.
