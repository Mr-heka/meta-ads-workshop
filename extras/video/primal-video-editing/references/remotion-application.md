# Applying the Primal Video Method to Selr AI Talking-Head Video in Remotion

How to translate Justin Brown's editing method into Remotion (React-based programmatic video) so a talking-head video is built as a repeatable, codified pipeline. Pairs with the Remotion documentation.

The Primal Video Method maps onto Remotion almost one-to-one because both are **fixed, ordered, repeatable pipelines**. Justin's method is "literally step 1 do this, step 2 do this"; Remotion is a composition built layer by layer in a fixed order. The job is to encode each step as a build stage, each signature technique as a reusable component, and each "do not" as a lint rule.

---

## Step-to-Remotion mapping table

| Primal Video Method step | Remotion implementation |
|---|---|
| 1. Project setup (format, fps, resolution) | The `<Composition>` config: `width`/`height` (1920x1080 for 16:9, 1080x1920 for 9:16), `fps` (24 or 30, locked), `durationInFrames`. Decide format and fps once, up front. |
| 2. Primary footage track | A base `<OffthreadVideo>` (or `<Video>`) layer holding the talking-head footage. Built first; everything else layers above it. |
| 3. Trim down / remove bad takes | Drive trims from a **cut list** (JSON of in/out frame pairs). Use `startFrom`/`endAt` on the video, or a `<Sequence>` per kept segment. Generate the cut list from the transcript (see edit-backwards below). |
| 4. B-roll / overlay layer | B-roll `<Sequence>`s on a higher track index, positioned over chosen segments, with their audio muted (`volume={0}`). |
| 5. Text and titles | A brand-styled `<Title>` / `<LowerThird>` component, each wrapped in a `<Sequence>` with explicit `from` and `durationInFrames`. |
| 6. Transitions and effects | `@remotion/transitions` between genuinely different segments only. The fake second-angle cut becomes a `<ZoomCut>` component (see below). |
| 7. Music and sound effects | An `<Audio>` track for licensed music (Artlist/Epidemic Sound), trimmed to composition length; `<Audio>` clips for SFX. |
| 8. Volume mix | Fixed dB constants for speech vs music; a ducking helper that lowers music under speech (see audio constants below). |
| 9. Color, then export | A single final color/LUT layer (CSS filter or shader overlay) wrapping the composition. Render last. |

**Build rule:** construct the composition in this exact order. Do not write the color layer or fancy effects before the cut list and audio are correct, that is Justin's "polish last" rule, and in Remotion it also keeps the Studio preview fast.

---

## Edit-backwards as a programmatic cut list

Justin's edit-backwards technique relies on one fact: **the last take of any section is always the keeper**, because the presenter only moves on when happy with the last take.

In Remotion this becomes a deterministic rule, not a manual scrub:

- Get a timestamped transcript of the raw recording (Whisper, Descript export, or similar).
- Apply the retake-removal rule: **for any sentence or section spoken more than once, keep the last instance, discard all earlier ones.** This is the codified version of Descript's "remove retakes" and of Justin's edit-backwards.
- Also strip silences longer than a threshold (Descript shortens gaps over 0.5s down to 0.5s, use that as the default constant).
- Emit a cut list: an array of `{ startFrame, endFrame }` for the kept segments.
- Feed the cut list to Remotion as a series of `<Sequence>`s or `startFrom`/`endAt` trims on the primary video.

Result: the trimming pass (Step 3) is data-driven and repeatable, and re-rendering after a re-record is automatic.

---

## The ZoomCut component (fake second-camera angle)

Justin's default for joining two similar talking-head clips is NOT a transition, it is a zoom that fakes a second camera angle. Codify it:

- Build a `<ZoomCut>` component that crops/scales the talking-head footage in by a fixed amount (start around **1.1x to 1.2x**, i.e. 10-20%, matching "you don't want to go too far").
- Apply it to **alternating segments** so consecutive same-style cuts read as A-cam / B-cam.
- **Keep the eye-line constant**, expose an `eyeLineOffsetY` prop so the subject's eyes stay in the same screen position after the zoom. This is Justin's critical detail: "if you make sure the person's eyes are in a very similar position it's going to be way less jarring."
- Make zoom amount and eye-line offset **props**, so every cut is identical every render (Descript does this via a saved zoom-cut template, "the zoom cut goes in the same amount every time").
- Optionally animate a fast push-in with `interpolate` + `spring` for a subtle motion cut, but keep it understated.

Use real `@remotion/transitions` (fade, slide, wipe) only between genuinely different footage, Justin's rule that a transition is "for change, not sameness."

---

## Captions as a data-driven layer

Justin styles captions once to the brand, then auto-generates and corrects them per video.

- Drive captions from the **transcript JSON** (the same artifact used for the cut list), word- or phrase-timed.
- Build one brand-styled `<Captions>` component (font, color, size, position, optional outline/highlight) and reuse it across every Selr AI video.
- Render captions as a top track so they sit above b-roll and titles.
- `@remotion/captions` and Whisper-style word timings are the natural fit.

---

## Audio mix as fixed constants

Encode Justin's audio rules as constants and a helper, not per-video guesswork.

- **Speech target:** "green-to-yellow, never red." In practice, normalise speech so peaks sit roughly -6 to -3 dBFS and never clip at 0. Keep speech `volume` at 1 and normalise the source instead.
- **Music level:** Justin starts music around **-25 to -30 dB** relative to full. As a Remotion `volume` multiplier that is roughly **0.05 to 0.07** (a rough linear approximation; tune by ear). Define it as a constant, e.g. `MUSIC_VOLUME = 0.06`.
- **Ducking:** Descript auto-ducks music about 12 dB under speech. Build a ducking helper: when a speech segment is active, multiply music volume down (e.g. to `MUSIC_VOLUME * 0.25`); lift it back under b-roll-only segments. Drive it off the cut list segment metadata.
- **Music ends with the video**, trim the `<Audio>` to `durationInFrames` and apply a short fade-out.

---

## No-over-editing as lint rules

Justin's strongest review principle, turned into checkable Remotion rules:

- **Default to a hard cut.** Two adjacent talking-head segments get either a hard cut or a `<ZoomCut>`, never a decorative transition.
- **Cap transitions.** Set a max transitions-per-minute (Justin's YouTube videos are "pretty much all basic jump cuts"). Flag any composition that exceeds it.
- **Forbid same-style transitions.** A real transition is only valid between segments of different footage type (talking-head -> b-roll, or scene change). A transition between two talking-head segments is a lint failure.
- **No effect before the cut list.** Color, LUT, and decorative effects must be applied after trimming and audio, enforce build order in the composition file.
- **One feeling for the music.** Pick music that matches the intended viewer feeling; mismatched or too-loud music is a review reject.

---

## Recommended build sequence for a Selr AI talking-head Remotion video

1. **Plan the video** with the 5-lens topic model (`mistakes-and-review.md`); confirm the goal (think/feel/know/do) and the real business metric (leads/DMs, not views).
2. **Record** to the gear baselines (4K, locked fps, exposure triangle, good audio).
3. **Transcribe** the raw recording and generate the **cut list** (last-take-wins retake removal, silence trimming).
4. **Scaffold the `<Composition>`** with the right format and fps.
5. **Layer in build order:** primary video -> trimmed via cut list -> b-roll layer (audio muted) -> titles -> ZoomCut on alternating segments -> licensed music + SFX -> audio mix with ducking -> captions -> color layer last.
6. **Lint** against the no-over-editing rules and the 10-mistakes checklist in `mistakes-and-review.md`.
7. **Render**, then review on a second device (Justin's playback rule).
8. **Run the script and any on-screen copy through a voice and claims pass** for the user's voice and their own hard rules (no support promises, no outcome guarantees, no fabricated facts, no personal life in marketing).

The payoff is Justin's own result, achieved through code instead of manual labour: Primal Video cut editing time from "14 to 20 hours" to "1 to two hours" by systemising. A Remotion pipeline built on this method makes a talking-head video a deterministic, re-renderable artifact.
