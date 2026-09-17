# Pipeline and authoring

## Caption model

| Role | Content | Surface |
|---|---|---|
| `drop` | um/uh, stutters, self-corrections | omitted |
| `rail` | ordinary verbatim speech | readable foreground lower-third; optional inline `emphasis` accent/active-word pop |
| `embed` | promoted headline peak | large word behind the subject with designed entrance and exit |

Scarcity is per thought block: at most one hero per block, no two heroes co-visible, and at least one beat of air between hero windows; the compiler warns below 0.6s. A short clip usually earns 1–2 embeds; a long explainer roughly one per section. The largest authored hero is the sole APEX, with full lockup embed and width-fit raise. MINOR peaks stay foreground, oversized in their column, with damped motion.

Standard uses `rail.html` for rail + the `index.html` climax embed. Column-flow omits the rail and uses embed-style composition throughout. Theme supports rail, panel, poem, and takeover paradigms. The a-roll stays visually untouched in Standard/Cinematic. Theme’s registry-gated PLATE budget is the sanctioned reaction layer: charge-dim, punch, shake, or grain runs after matte compositing so subject, text, and plate move as one frame.

## End-to-end commands

```bash
hyperframes init <project> --non-interactive --video <video.mp4>
bash scripts/prepare.sh <project>
node scripts/preview-frames.cjs <project>
bash scripts/render-and-composite.sh <project>
```

Skip `hyperframes init` when the project already contains the video; `matte.cjs` and `transcribe.cjs` adopt it as `source.mp4`. `init` checks installed skills against GitHub and updates the global set when stale.

`prepare.sh` runs matte, transcription, and audio envelope in parallel, then safe-zones v2. Outputs include `frames_fg/`, `transcript.json`, and `safe-zones.json`.

## Cinematic authoring

Read `safe-zones.json` first. Put narration in `zones.hugLeft` or `zones.hugRight`, abutting the silhouette; distant text floats instead of feeling embedded, and far corners are fallback. Place the hero at `heroAnchor` / `heroBands.best`, centered on the subject with roughly 30–55% occlusion. `recommendation:"fg"` moves narration forward for legibility; keep the hero embedded while `heroBands.feasible`, using hero-fg only as last resort.

Preferred authoring file: `<project>/cinematic.json` with `"dna": "<name>"` and thought blocks. Each block contains transcript-ordered lines grouped 2–5 words at clause boundaries, a stacking plane, per-line `css` limited to size/weight/style, and at most one `"hero": true`; use `"text"` for its display form. The schema header lives in `scripts/make-cinematic.cjs`.

Compile:

```bash
node scripts/make-cinematic.cjs <project>
```

The compiler lowers blocks to `plan.json` and `index.html`; sequences transcript timings; accumulates within blocks; page-flips between blocks; enforces reading order; resolves fg fallback; and builds the hero lockup. Pre-context, HERO, and post-context form one subject-centered composition in spoken top-to-bottom order. Context sits foreground while the hero embeds behind the subject; a mass rule keeps the hero dominant. It also separates apex from minor heroes.

For layouts the block model cannot express, hand-author `plan.json`, then run:

```bash
node scripts/fill-timings.cjs <project>
node scripts/fit-fonts.cjs <project>
node scripts/make-composition.cjs <project>
```

Legacy `plan.template:"cinematic-cream"` maps automatically to `dna:"cream"`.

## Theme authoring

Read `themes/README.md` first for paradigm/setpiece registries, linkages, hard rules, and exact schema. Select the catalog-routed theme DNA using each `themes/<name>.json` `voice` and `when`.

Author `<project>/theme.json`:

- `dna`
- `lines`: verbatim transcript order, 1–5 words each; in `takeover`, each line is one card
- `minors`: emphasis words
- `hero:{match}`: climax word/phrase; omit it from `lines` for embed setpieces, retain it for inline setpieces and panel+redact

Compile and render:

```bash
bash scripts/render-theme.sh <project>
```

This invokes `make-theme.cjs`, runs the verbatim-completeness compile gate, renders both layers, composites, and applies plate reaction. The deliverable is `final_fx.mp4`; `final.mp4` is the pre-plate-reaction file. Use `preview-frames.cjs` after compile and before the paid render. Theme replaces the generic final render step because `render-theme.sh` already runs compile, `render-and-composite`, and `_postfx.sh`.
