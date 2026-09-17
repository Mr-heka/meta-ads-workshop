# Routing and intake

## Refresh

Run silently before relying on the skill:

```bash
npx hyperframes skills update embedded-captions
```

This is a fast no-op when current; otherwise it refreshes this skill and its core domain dependencies.

## One identity surface

`CATALOG.md` is the only front-end: 36 identities, comprising 10 classic and 26 themed identities. Ask for an identity, not Standard/Cinematic/Theme; catalog lookup derives the engine, compiler, authoring file, reading surface, voice, scene needs, and adjacency notes for loud↔ordnance, neon↔neonsign, and cream↔stardust. Opening an identity is a validation event and identities are engine-locked.

- Rail-surface/default: a restrained verbatim lower-third rail carries most speech; one or more earned peaks become behind-subject embeds. `anchor` is the quiet, scene-safe default.
- Column-flow/pure embed: every caption uses embed-style composition with no rail. Recommend it for mood-over-verbatim work.
- Themed constitution: body paradigm × hero setpiece × front FX × plate reaction, composed from registries. `ordnance`, `terminal`, `neonsign`, `stardust`, and `stomp` are representative VFX-grade choices for requests such as “炸”, “特效”, or “像 AE 做的”.

Selection contract: probe the clip, classify tone/shot/platform, shortlist 2–3 identities using `CATALOG.md`, recommend one with a one-line reason, then let the user pick before authoring. In autonomous mode such as “surprise me” or “decide for me”, choose from the shortlist and state the reason. This is the preference gate defined by the **hyperframes-core** skill’s brief contract §1. When uncertain, recommend `anchor`.

Shortlist by what should carry the effect: explainer/interview/must-read words → rail or panel surfaces; poetic/social/“cinematic” → column-flow by register; VFX/named-world asks → themed identities. The direction matrix informs the shortlist; `CATALOG.md` remains the router.

Classify:

- Tone: documentary, conversational, energetic, poetic, keynote, investigative, music-video.
- Shot: close-up (head + shoulders), mid-shot (torso+), wide (full body+), cut-montage (mixed shots).
- Platform: 9:16 portrait (TikTok/IG/Shorts), 16:9 landscape (YouTube/web), 1:1 square, broadcast export.

## Admission gate

Probe specs and frames at 20%, 50%, and 80%:

```bash
ffprobe <video.mp4>
ffmpeg -ss <t> -i <video.mp4> -vframes 1 sample.png
```

Split per shot or decline the clip when it has multiple speakers/hard cuts, no human subject, duration under 3 seconds, no speech, a face that is never clear, or busy handheld motion that makes the matte flicker. Near-silent audio can make Whisper invent phrases such as “Thank you.”; heed the `transcribe.cjs` warning.

Find mid-clip burned captions and text graphics with a 1 fps contact sheet:

```bash
ffmpeg -i in.mp4 -vf "fps=1,scale=160:-1,tile=10x5" sheet.png
```

The source ships without covering or inpainting, so existing burned text is an admission failure. Sanity-read `transcript.json`; for confident gibberish from non-native or heavy-accent speech, retry once with `WHISPER_MODEL=medium`, then decline if it still does not parse as language.

## Free pre-flight probes

1. Shot cuts: compare 20/50/80% frames and trim before any changed subject or scene.
2. Letterbox/pillarbox: detect black bars on the first frame, compute the safe content rectangle, and keep captions inside it.
3. Caption-region luminance: under 60 → light text as-is; `60-180` → glyph scrim; 180+ → opaque text plus scrim. Locked cream+`screen` cinematic styling is selected, not recolored: bright scenes favor `ink` or opaque-rail `anchor`.
4. Props: safe zones score subject occlusion and luminance, not static props. Inspect the bands that authoring will use.

## Classic DNA lookup

`safe-zones.json` fields `heroAnchor.bandLuma` and `palette.temperature`, plus content register, select the DNA:

| DNA | Register and scene fit | Locked voice |
|---|---|---|
| cream | premium-warm; dark/mid warm | Inter, warm cream, screen blend, glowing-emergence hero |
| ink | premium; bright, luma >150 | near-black multiply, printed-on-wall |
| editorial | editorial-luxe; introspective/fashion/poetic | Bodoni Moda, lowercase italic hero |
| keynote | tech-premium; product/launch | opaque white Inter 800, centered stillness |
| documentary | formal; serious interview | burn-in reveals, no hero |
| loud | hype/sport/social | Anton, scene accent, `bodyLayer: fg`, slam+ripple |
| neon | cyber/nightlife/tech-noir; dark | electric-cyan sign ignition |
| glitch | digital/hacker/AI | RGB-split echoes snapping together |
| chrome | Y2K/fashion-tech/music | liquid-metal hero, one hold-phase sheen |
| velocity | sport/auto/fitness | vector arrivals, streak/skew, hero speed trails |

The chosen DNA locks type, palette, blend, motion, and hero three-act. Safe-zones v2 adapts `palette`, `optics`, and `lighting` to the scene using footage-sampled accent, light-direction contact shadow, depth-match blur, and RMS-coupled hero amplitude. The engine generates: co-visible captions dim for setup; per-letter impact amplitude follows spoken loudness; the hero breathes/glows through afterglow.
