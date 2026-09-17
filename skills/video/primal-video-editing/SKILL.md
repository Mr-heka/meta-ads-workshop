---
name: primal-video-editing
description: Use when the user says "edit this talking-head video", "plan my YouTube edit", "use an audio-first workflow", "give me a beginner edit pipeline", "Primal Video", "Justin Brown", "9-step edit", or "edit backwards", or when a talking-head edit needs planning or review. Route Remotion build questions to the Remotion documentation.
---

# Primal Video Editing Method⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

Justin Brown's talking-head video workflow, reverse-engineered from his Primal Video YouTube tutorials. Apply it to plan, record, edit, and structure talking-head content video, and to codify those rules into Remotion.

## Who Justin Brown is

- Founder of **Primal Video**, an Australian YouTube channel (1.8M+ subscribers, approximate) that teaches creators and business owners "how to grow an audience and scale your revenue with online video".
- He repeatedly frames his audience as "entrepreneurs and business owners" who want to "amplify their business and brand with video", not film students. The whole method is built for non-experts who need speed and a repeatable process.
- His flagship asset is the **Primal Video Method**: a downloadable, printable step-by-step editing process (now also shipped as an AI prompt). The core belief behind it: "the most efficient way to edit and to learn to edit is by following a specific process so that you know that you're doing the right things in the right order and not unnecessarily wasting your time."
- Primal Video's own production stack as of 2026: records and edits in **Descript**, plans in **ClickUp**, validates topics with **VidIQ**, scripts with **Claude**, tracks business impact with **Video Stats**, automates with **n8n**, runs email on **Bento**. They cut editing time from "14 to 20 hours" per video down to "1 to two hours maximum" by systemising and using AI.

## When to use this skill

Use it for any talking-head video work: deciding what video to make, structuring the edit, sequencing the editing pass, deciding when and how to cut, adding b-roll or captions or music or color, or translating those rules into Remotion. This skill decides **how** to edit and structure a talking-head video. It pairs with the Remotion documentation (the React build) and the user's own brand voice rules. Reach for it the moment a talking-head video needs an edit plan or a Remotion structure.

## The core mental model: editing is a process, not an art project

Stop treating an edit as one big creative blob. Justin's central diagnosis of why editing feels slow and painful:

> "Most people that are doing this are either treating this as one big project, which becomes overwhelming, or they're jumping into the wrong things first. Too many people jump in and try to make their videos look good first instead of doing what they actually need to do. So they end up jumping all over the place, adding to their frustration and burning a lot of time."

Three fixes run through everything below:

1. **Follow a fixed step order.** The Primal Video Method is "literally step 1 do this, step 2 do this". Same order every time. This is exactly what makes it codifiable into Remotion.
2. **Edit in iterative passes.** "Editing is an iterative process so we'll do a pass, we'll clean things up, tidy it up a bit, and there'll be further refining on the next pass." Never try to make a section final on the first touch.
3. **Content first, polish last.** "Focus on the story first." Brightness, color, effects, and "making it pretty" come at the END, because doing them early "slows down your computer and makes the editing process more frustrating" and you may cut the very footage you spent time beautifying.

## The Primal Video Method: the 9-step editing order

Every talking-head edit moves through these nine steps **in this order**. This is the spine of the whole skill. Full detail and verbatim quotes in `references/editing-method.md`.

1. **Set up the project.** Pick the format (16:9 widescreen or 9:16 portrait). Let the tool auto-detect resolution, frame rate, and color space from the **first clip you import** (so import primary camera footage first). Delete any auto-added end-card or watermark.
2. **Import and lay down primary footage.** Bring the main talking-head footage into the timeline first. This is "the thing that's going to make up the bulk of our edit".
3. **Trim down: remove bad takes and mistakes.** Cut everything you do not want. Use the **audio waveforms** to see where speech is and is not. "Remove all the bad takes, all the mistakes, all the things that we actually don't want."
4. **Add b-roll / overlay footage.** Drop b-roll, screen recordings, and graphics onto a layer **above** the primary footage. Mute b-roll audio unless you need it.
5. **Add text and titles.** Names, lower-thirds, subscribe prompts. Each title behaves like its own clip with a start and end.
6. **Add transitions and effects.** Transitions go between clips; effects (speed change, stabilisation, fancy stuff) go on clips. Use transitions sparingly (see philosophy below).
7. **Add music and sound effects.** Use properly licensed music (Justin uses Artlist and Epidemic Sound), never the tool's built-in tracks unless you are sure of the license. Match cuts to the beat.
8. **Adjust volume levels.** Spoken word first, music and SFX second. Speech sits in green-to-yellow on the meters, never red. Music typically starts around -25 to -30 dB.
9. **Color correct, then export.** Color is the LAST creative step. Adjust the first clip, then apply to all. Export with the platform preset or the project's native settings.

## The signature techniques (the high-leverage rules)

These are the techniques worth codifying. Full detail in `references/editing-method.md`.

- **Edit backwards on talking-head footage.** When filming a piece to camera, only move to the next point "when I am happy with the last take". That makes the **last take the keeper** every time. Then in the edit, start at the END of the timeline and work back, hitting the good take immediately instead of scrubbing through every failed attempt. Justin: "This tip is an absolute game changer." (Note: with transcript-based editors like Descript that auto-remove retakes, editing forward is fine because the bad takes are already gone.)
- **Trim by the waveform, not by ear.** "I like to use the visual representation here." The audio waveform shows speech vs silence at a glance, so you cut silences and dead air fast.
- **The fake second-camera-angle cut.** Two near-identical talking-head clips will have a jarring jump cut between them. Instead of a transition, **zoom in on one of the two clips** so it reads as a second angle. Critical detail: "if you make sure the person's eyes are in a very similar position it's going to be way less jarring". Do not zoom so far you lose quality. This is the move Primal Video uses on YouTube "instead of just having a bunch of transitions every couple of seconds".
- **Set effects on the first clip, then apply to all.** Volume and color get dialled in on the first clip, then copied or "apply to all" across the timeline. Then handle b-roll separately.
- **Save backup versions of the timeline.** Save a new version at every milestone, ideally every time you move to the next step of the method, so you can go backwards if a project corrupts or you need an earlier state.

## The editing philosophy: do not over-edit

Justin's strongest review principle. Over-editing is mistake #7 in his beginner-mistakes video:

> "Over editing your videos: making way too many cuts, removing out every little pause or every little breath, just adding cuts for the sake of adding cuts, or going the other way and adding in way too many transitions and too many effects. All that does is annoy the viewers and make it distracting."

- **Stick to simple cuts.** "Remove the mistakes, tighten up stuff if it needs it. For the most part the more you simplify your videos the easier they're going to be for you to edit, but also the easier for your viewers to watch."
- **Transitions are for change, not for sameness.** A transition works "if we're transitioning from one clip or one style of footage to something totally different". Between two similar talking-head shots, do NOT add a transition. Either leave the hard cut or use the fake-second-angle zoom.
- **Tight but not robotic.** Cut dead air and pauses, but keep natural breath and rhythm. For YouTube, Justin wants "the edits to be relatively tight".

## The 10 beginner mistakes (use as a review checklist)

Run any talking-head edit against this. Full list with quotes in `references/mistakes-and-review.md`.

1. Not considering the edit while filming (capturing footage you will never use).
2. Editing without a plan: no goal for what the viewer should think, feel, know, or do.
3. No process: dumping footage in the timeline and color grading first.
4. Poor file management: assets not in one logical folder structure.
5. Not learning keyboard shortcuts (JKL playback, ripple trim, split).
6. Wrong or too-loud music that fights the intended feeling.
7. Over-editing: too many cuts, too many transitions, too many effects.
8. Not saving backup versions of the timeline.
9. Software-hopping ("the grass is greener") instead of finishing videos.
10. Editing front-to-back instead of editing backwards from the best last take.

## Step 1 of any video: deciding what to make

Before editing, decide the topic. Justin uses **five overlapping lenses**; the best videos sit where several overlap. Full detail in `references/mistakes-and-review.md`.

1. **Excitement.** "What am I excited about right now that my audience would also see value in." Excitement flows into the video and kills procrastination.
2. **What has already worked.** Look at existing videos that performed and decide what to update or remake. Roundups especially ("best editing software 2026").
3. **Adjacent ideas.** Given what worked, what related content would the same viewer want next.
4. **The viewer's lens.** Their biggest pains and problems, what they search, what competitors' top videos prove there is demand for.
5. **Search volume.** Real keyword search data validates demand, both to find topics and to validate ones you already have.

Critical business point from Justin: **views are not the success metric.** "The videos that YouTube is rewarding aren't the ones that are building the business." Judge a video by whether it drove the real business goal (for example: leads, DMs, calls), not raw view count. "When the only metrics you see are algorithm metrics, then you're likely going to make algorithm content."

## Captions, gear, and recording baselines

- **Captions.** Add subtitles: "captions are great for attention spans, accessibility, and SEO." Auto-generate, then correct mistakes. Style fonts, colors, sizes to the brand. Tools Justin names: Descript, Adobe Premiere, CapCut, YouTube Studio (free), Rev, Captions.
- **Recording resolution.** Shoot **4K** for the highest quality and so footage holds up when reframed to vertical shorts. 1080p is the lighter-weight fallback.
- **Frame rate.** **24fps** for a cinematic look, **30fps** for a richer "YouTube" look. Pick one and lock it.
- **The exposure triangle.** Shutter speed = roughly 2x the frame rate (24fps -> 1/50s, 30fps -> 1/60s). Aperture as low as the lens allows for a blurred background and more light. ISO as low as possible to avoid digital noise.
- **White balance.** Use a grey card, or match the Kelvin of your lights (around 4500-5000K), then adjust by eye. White balance "impacts your skin tone way more than most people think".
- **Audio.** Shotgun mic within an arm's length; lapel/wireless mic if further away. "Just make sure that your audio sounds good."
- **Ship it.** "If you do make some mistakes, publish your video anyway, and then in the very next video make small improvements at every iteration."

## Applying it to talking-head video and Remotion

The Primal Video Method is unusually well suited to Remotion because both are **fixed, ordered, repeatable pipelines**. Full mapping table and rule set in `references/remotion-application.md`.

- **Encode the 9 steps as the build order** of a Remotion talking-head composition: project setup, primary track, trimmed cuts, b-roll layer, text layer, transitions, audio, audio mix, color. Build them in that order; do not jump to color/polish first.
- **Edit-backwards becomes a cut list.** Because the keeper is always the last take, a transcript or cut list can be generated programmatically and fed to Remotion as trim in/out points. Codify "last instance of a repeated sentence wins" as the retake-removal rule.
- **The fake second-angle cut becomes a reusable component.** A Remotion `<ZoomCut>` that crops in roughly 10-20% on alternating talking-head segments, keeping eye-line constant, replaces hand-done transitions. Make zoom amount and eye-line offset props so it is consistent every render.
- **Captions as a data-driven layer.** Drive captions from the transcript JSON, brand-styled once and reused, exactly as Justin styles captions to the brand.
- **Audio mix as constants.** Encode "speech in green-to-yellow, never red" and "music around -25 to -30 dB, ducked under speech" as fixed dB constants and a ducking helper, not per-video guesswork.
- **No-over-editing as lint rules.** Cap transitions per minute, forbid a transition between two same-style segments, require simple cuts as the default. These become reviewable Remotion rules.
- **Color last.** Apply any color/LUT pass as the final composition layer so it never slows iteration on story and timing.
- **Always finish with a voice and claims pass** for the user's voice and their own hard rules before anything ships (no support promises, no outcome guarantees, no fabricated facts, no personal life in marketing).

## The Primal rules (quick reference)

Do: follow a fixed step order, edit in iterative passes, do content first and polish last, import primary footage first, trim by the waveform, edit backwards from the best last take, fake a second angle with a zoom, set effects on clip one then apply to all, get spoken audio right before music, color grade last, save backup versions, learn keyboard shortcuts, caption everything, ship even if imperfect and improve next time.

Do not: jump into making it pretty first, color grade before cutting, over-edit with needless cuts/transitions/effects, put a transition between two similar shots, leave music too loud or mismatched to the feeling, capture footage you will never use, software-hop instead of finishing, judge a video on views alone, skip backup versions.

## Reference files

- `references/editing-method.md`, the full 9-step Primal Video Method step by step with verbatim quotes, plus every signature technique (edit backwards, waveform trimming, fake second-angle cut, apply-to-all, backups) and the no-over-editing philosophy.
- `references/mistakes-and-review.md`, the 10 beginner mistakes in full with quotes, the 5-lens topic-selection model, the views-do-not-matter business principle, and caption/gear/recording baselines.
- `references/remotion-application.md`, how to translate the method into Remotion: the step-to-component mapping table, the edit-backwards cut list, the ZoomCut component spec, audio-mix constants, and the no-over-editing lint rules.
- `references/source-index.md`, full index of every source transcript with titles, URLs, view counts, and publish dates, plus how to refresh this brain.

Router key `sk-1s4z857` — resolved by the skills index on load.
