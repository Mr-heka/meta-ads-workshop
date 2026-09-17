# Storyboard, pacing, and visual decisions

## Storyboard contract

Read `metadata.json` and the corrected `transcript.json`, then author `storyboard.json`. It is an agent-internal plan; no CLI parses it.

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
  "cards": [{
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
  }]
}
```

The stable v3 shape keeps `fps`, `width`, `height`, `durationSeconds`, `layout`, `themeId`, and `seed` inside `composition`; `videoTrack` contains `sourcePath`, `startSec`, `endSec`, and optional `bounds`; `subtitles` contains `enabled` and any subtitle settings.

Each card has:

| Field | Contract |
| --- | --- |
| `id` | Stable string shared by HTML and GSAP selectors |
| `intent` | Natural-language design intent |
| `startSec`, `endSec` | Seconds, with `endSec > startSec`, inside composition duration |
| `accentIndex` | `0`, `1`, `2`, `3`, or `4` |
| `zone` | One of the five zones below |
| `contentHints` | Free-form prompt data such as kicker, title, detail, data, or quote |
| `archetype` | Optional free-form memory label; free-form is the default |
| `transition` | Optional `cut`, `fade`, `slide`, or `wipe` |

`contentHints` can also be a plain string such as `Title: annualized 5.69%\nNotes: ...`; visual details belong in card HTML. Card times are normally non-overlapping; intentional overlap uses `data-track-index` for z-order. Style, layout recipe, and frame choices stay in working memory because there is no `card.layout` field. `videoTrack.bounds` is one composition-level value; GSAP moves `#video-wrap` between cards.

| Zone | Resolved bounds | Typical use |
| --- | --- | --- |
| `fullscreen` | whole canvas | hero, big number, mantra, quote |
| `whiteboard-area` | 40px inset in landscape, or bottom 45% in portrait | dense or annotated content |
| `lower-third` | bottom 30% | annotation over visible video |
| `side-panel` | right 42% in landscape, or bottom 40% in portrait | split/sidebar |
| `video-overlay` | whole canvas with mostly transparent card root | overlay on full-bleed video |

Cards follow the transcript rather than fixed roles or a prescribed narrative arc.

## Card count

Choose a medium-density base pace, multiply by density, then calculate:

```text
secPerCard = basePace × densityMultiplier
cardCount  = max(5, round(videoDurationSec / secPerCard))
```

There is a five-card floor and no upper clamp.

| Duration | Base seconds/card | Reason |
| --- | --- | --- |
| under 60s | 6–8 | short-form viewers expect fast cuts |
| 60s–3m | 8–12 | normal social pace |
| 3–10m | 12–20 | breathing room for richer cards |
| 10–30m | 20–35 | lecture/interview rhythm |
| over 30m | 30–60 | episodic, near-chapter rhythm |

| Density | Signal | Multiplier | Effect |
| --- | --- | --- | --- |
| High | many numbers or claims, staccato/list pacing, new idea every 1–2 sentences | `0.7` | faster cuts, more cards |
| Medium | mixed data and narrative | `1.0` | base pace |
| Low | one extended story, repeated reframing, reflective pacing, one unfolding argument | `1.5` | slower cuts, fewer cards |

Reference calculations: `30 / (7 × 1.5) → 3 → 5`; `60 / (10 × 1.5) → 4 → 5`; `121 / (10 × 0.7) → 17`; `300 / (16 × 1.0) → 19`; `600 / (16 × 0.7) → 55`; `1800 / (28 × 1.0) → 64`; `3600 / (45 × 1.5) → 53`.

A card held beyond roughly 15 seconds needs a data block, multiple sub-points, or staggered reveals; a static one-liner becomes dull beyond 8 seconds. When many cards exceed 30 seconds, split the timeline into chapter HTML sub-compositions mounted with `data-composition-src`; this also addresses the HyperFrames `timeline_track_too_dense` warning.

An optional neutral outro is a wordmark plus one-line tagline held for about 1.5–2 seconds with fade in, short hold, and fade out. Append it to `cards[]` and extend `composition.durationSeconds` to its `endSec`; otherwise end on the last content card. The skill carries no fixed brand outro.

## Ask once for visual direction

Before card design and bounds, resolve ratio, overall layout, style group, and count. Precompute:

```text
sourceAspect = metadata.width / metadata.height
sourceAspect >= 1.5           → recommend 16:9 (about 3:2 or wider)
sourceAspect <= 0.7           → recommend 9:16 (about 9:13 or taller)
0.7 < sourceAspect < 1.5      → recommend 4:5 (near-square)
autoCount = max(5, round(videoSec / (basePace × densityMultiplier)))
```

Put the recommended ratio first and label it `recommended · matches source video W×H`. Put the concrete `autoCount` in the Auto label. Use the available structured question tool (`AskUserQuestion`, `request_user_input`, `ask_question`, or IDE equivalent); otherwise ask all four in one plain-text message. Keep each round within 2–5 questions.

| Decision | Options and meaning |
| --- | --- |
| Ratio | `16:9` 1920×1080 for TV/YouTube/desktop; `9:16` 1080×1920 for TikTok/Reels/mobile; `4:5` 1080×1350 for Instagram feed/WeChat Moments and cross-platform use |
| Layout | `split` side-by-side 50/50; `stack` video top about 52% and card below; `pip` card-led canvas with rounded corner video; `overlay` full-bleed video with floating glass card |
| Style group | `warm-paper`: academic, editorial, whiteboard, xhs; `clinical`: audit, swiss, terminal, minimal; `experimental`: geom, spotlight |
| Count | Auto `N`; Fewer `round(N × 0.6)`; More `round(N × 1.5)`; or a typed integer |

For a native `AskUserQuestion` channel, preserve its field names and make each decision single-select:

```js
AskUserQuestion({
  questions: [
    {
      question: "Output video aspect ratio (canvas):",
      header: "Aspect ratio",
      multiSelect: false,
      options: [
        { label: "16:9 (1920×1080) landscape", description: "TV / YouTube / desktop playback; widest canvas." },
        { label: "9:16 (1080×1920) portrait", description: "TikTok / Reels / short-form mobile." },
        { label: "4:5 (1080×1350) near-portrait", description: "Instagram feed / WeChat Moments; covers both platforms." }
      ]
    },
    {
      question: "Choose the overall layout: how should the video and cards coexist on the canvas?",
      header: "Layout",
      multiSelect: false,
      options: [
        { label: "side-by-side (split)", description: "Video and card each take half; stable interview/data separation." },
        { label: "top-bottom (stack)", description: "Video on top around 52%, card below; cross-ratio default." },
        { label: "picture-in-picture (pip)", description: "Card fills canvas; video becomes a rounded corner window." },
        { label: "full-screen overlay (overlay)", description: "Video is full-bleed; card floats as a glass layer." }
      ]
    },
    {
      question: "Choose the card visual style (style):",
      header: "Style group",
      multiSelect: false,
      options: [
        { label: "warm paper (warm-paper)", description: "Academic, editorial, whiteboard, or xhs for reflections, launches, lifestyle, and emotional stories." },
        { label: "clinical / cold (clinical)", description: "Audit, swiss, terminal, or minimal for finance, investigations, technical tutorials, and serious presentations." },
        { label: "experimental / avant-garde (experimental)", description: "Geom or spotlight for highlights, launches, strong emotion, and cinematic work." }
      ]
    },
    {
      question: "Card count (takeaway pacing): how many cards to cut?",
      header: "Card count",
      multiSelect: false,
      options: [
        { label: "Auto (recommended) · approx N cards", description: "Use duration and information density; substitute autoCount for N." },
        { label: "Fewer · approx round(N × 0.6) cards", description: "Sparse, longer holds for reflective or slow content." },
        { label: "More · approx round(N × 1.5) cards", description: "Tight, fast cuts for staccato, data-dense, or highlight content." }
      ]
    }
  ]
});
```

Accept loose replies such as `1A 2C 3B 4A`, `A C B A`, `16:9 / pip / data / auto`, natural language, or `default`. Re-ask only ambiguous decisions. `AskUserQuestion` supplies an Other option: parse an entered count as an integer, apply the five-card floor, and fall back to Auto on parse failure.

When the user has already approved defaults, asked for no questions, or said “surprise me” or “decide for me,” use the recommended ratio, `stack`, the transcript-appropriate style from the neutral editorial/data group, and Auto. This follows the `hyperframes` brief contract. State the choice in one sentence and continue.

Resolve the answers:

| Choice | Result |
| --- | --- |
| `16:9` | `1920 × 1080`, storyboard `layout: "landscape"` |
| `9:16` | `1080 × 1920`, storyboard `layout: "portrait"` |
| `4:5` | `1080 × 1350`, storyboard `layout: "portrait"` because height exceeds width |
| Fewer | `max(5, round(autoCount × 0.6))` |
| More | `round(autoCount × 1.5)` with no upper clamp |
| Integer Other | `max(5, parseInt(n))` |
| Non-integer Other | `autoCount` |

The inherited layout files contain exact bounds for all three ratios. The proportional fallback for 4:5 keeps horizontal values and scales portrait `y` and `h` by `1350/1920 ≈ 0.703`; for example `{x:24,y:1280,w:1032,h:564}` becomes `{x:24,y:900,w:1032,h:397}`.

Pick a specific style from the selected group based on transcript tone. If two remain genuinely tied, ask a second question with 2–4 specific options. A free-text style outside the ten-style library is a design hint anchored to the selected layout bounds.

Auto-pick frames:

| Layout | Warm paper | Clinical | Experimental |
| --- | --- | --- | --- |
| `split` | `polaroid` | `hairline` | `clean` |
| `stack` | `polaroid` | `hairline` | `clean` |
| `pip` | `clean` | `clean` | `clean` |
| `overlay` | `clean` | `clean` | `clean` |

PiP already has chrome; full-bleed overlay uses clean framing. State ratio/canvas, layout, specific style, frame, and final count in one sentence, then keep those five values in working memory.

## Per-card decisions

- Map the main recipe to a zone: `split → side-panel`, `stack → lower-third`, `pip → fullscreen`, `overlay → video-overlay`; use `fullscreen` or `whiteboard-area` for one-off hero/data moments.
- Keep `object-fit: cover` when cropping is acceptable. To preserve the full source, tween `#video-wrap` to a source-aspect-matched rectangle and let the card or backdrop fill remaining canvas.
- Vary `accentIndex` for rhythm and reuse it within one narrative beat.
- Choose 2–3 recurring `data-anim` patterns for coherence.
- Read the matching inherited `references/styles/<key>.html`, `references/layouts/<key>.html`, and `references/frames/<key>.html` before authoring.
