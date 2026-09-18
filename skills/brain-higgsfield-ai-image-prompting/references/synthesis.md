# Synthesis — Higgsfield AI image prompting

Collated from 26 YouTube transcripts (mined 2026-06-14). Every claim is attributed; disagreements marked **contested**. Higgsfield routes to several image models, so most "Higgsfield image prompting" is really prompting **Nano Banana Pro, Higgsfield Soul / Soul 2, GPT Image, Seedream, or FLUX**. Pick the model first, then prompt to its strengths.

---

## 1. The core image-prompt formula (the one structure everyone teaches)

**Subject + Action + Environment + Art style + Lighting + Details.** Six slots, each specific.

- Bad: "woman in cafe." Good: "A young woman with freckles, smiling thoughtfully and sitting on a bench, in a cozy cafe by the window, shot on a Canon 5D Mark IV, natural window light, warm and inviting." (AI Master, Taylor Bay Studios — nearly identical formula, strong corroboration.)
- AI Master's GPT-Image variant adds **"sharp focus on the eyes"** and a lens spec; without "sharp focus on the face," the model focuses on everything and the portrait look dies.
- **Consensus.** Every concrete tutorial in the set uses some version of this six-part skeleton.

## 2. Camera + lens + aperture is the "art style" lever

The "art style" slot is where camera gear lives, and it measurably changes the output.

- Name the body and glass: "shot on a Canon 5D Mark IV," "85mm portrait lens on medium format film," "macro lens for sharp detail," "35mm focal length, f1.4 aperture," "grand format 70mm film, vintage prime." (AI Master, Artturi Jalli, Taylor Bay Studios)
- It is a ballpark, not real physics, but it shifts the look reliably. Theoretically Media: "Panavision Millennium DXL2, Zeiss prime 14mm, f1.4." Source real film data from **Shotdeck.com** (camera, lens, film stock, palette).
- **Product vs portrait differ.** Drop "macro lens for sharp detail" from a product prompt and the watch face goes soft. "Product photography has different requirements than portrait photography, and your prompts need to reflect that." (AI Master)

## 3. Lighting vocabulary that actually moves the needle

Generic "nice lighting" loses to specific terms (AI Master, consensus):

- "dramatic window lighting creating a rim light effect," "natural window light," "golden hour," "soft afternoon light filtering through street trees," "dramatic side lighting from camera left," "natural sunlight streaming in from the right."
- Always **name the light direction** for interiors/architecture or you get flat, ambiguous lighting.
- Atmospheric terms ("subtle morning mist," "soft golden light") work best when subtle and additive, not overwhelming.

## 4. Model selection for images (reach for the right one)

- **Nano Banana Pro (Google)** — consensus best for photoreal quality, reference-image fidelity, **accurate in-image text** (thumbnails, infographics, posters), reliable celebrity/landmark likeness, 2K/4K. "The best one out there right now, no questions asked." (DGI Kaos, metricsmule). Default for hero shots and edits.
- **Higgsfield Soul / Soul 2** — Higgsfield's own model and the **only** one that supports Soul ID trained characters. Soul 2 called "the best model right now for production-ready images." Switching off it drops the character. Offers cinematic style presets (Super 8, VHS, anamorphic) the other models lack. (DGI Kaos, Joseph Martin, Jack Vs. AI)
- **GPT Image (1.5 / 2)** — strong for broad realistic photography and **multi-reference composites** (insert a person + multiple logos). In-Higgsfield text rendering is weaker than native ChatGPT GPT Image. (Joseph Martin, AI Master, AI Foundations)
- **Seedream / Grok Imagine / FLUX** — available (notably in Canvas) but treated as lower-priority; little model-specific prompting guidance in the corpus.

## 5. Character & identity consistency (the recurring hard problem)

- **Soul ID:** train on **20-31 photos**, solid background, varied angles and expressions, no glasses/hats/extreme angles. ~5-60 min to train. Then tag with `@` anywhere (image generator, Cinematic Cameras, Mood Board, Canvas). Must stay on the Soul model. (Artturi Jalli, DGI Kaos, Jack Vs. AI)
- **Reference-image route (no training):** drop 1-4 photos into the generator + "create a professional headshot that looks exactly like him." Nano Banana Pro is preferred for this over GPT Image. (Artturi Jalli)
- **Expression / character sheets:** generate the character from multiple angles ("change nothing about appearance") before reusing — more angles = less drift. (Matt Loui, Rourke Heath, Higgsfield AI)
- **Include identity-defining accessories in the text** (glasses, cap) even with a trained character, or it drifts. (Jack Vs. AI)
- **If drift happens, restate:** "exact same facial features, hair color, and clothing as the reference image." (AI Master)

## 6. Editing existing images (the action-word system)

- **Lead every edit with one of five action words: Add, Change, Make, Remove, Replace.** Then name the exact element. Vague edits cause face/body drift. (Taylor Bay Studios)
- **Clothing swap without face drift:** "Replace the woman's [color] [garment] with the [new garment] in the image" + upload a reference of the new garment. Naming the existing color preserves identity; works with two people in frame. (Taylor Bay Studios)
- **Background replacement needs a lighting anchor:** add "maintain natural lighting on the subject" and "preserve original subject shadows," or the composite reads as fake. (AI Master)
- **Inpainting / object removal:** paint the region AND describe the fill ("remove the telephone pole, replace with sky matching the surrounding area"). Saying *how* to fill the gap beats saying only what to remove. **Contested:** Artturi Jalli rates Higgsfield's inpaint brush unreliable and prefers re-prompting from scratch.
- **Minor in-context edits beat re-rolling.** Once an image is 90% right in Nano Banana Pro, ask for surgical changes in the same chat ("zoom out from the mug," "move text left," "make the lighting more dramatic") rather than regenerating. (Dylan Davis)

## 7. Subject-specific recipes (AI Master's most useful contribution)

- **Portrait:** age + clothing + background descriptor + light direction + depth of field + "sharp focus on the eyes" + lens.
- **Product:** "white seamless background," "no shadows" (critical for e-commerce), "soft diffused lighting from above," then keep the core prompt fixed and swap only the view ("3/4 view from front left," "top-down," "close-up of controls").
- **Architecture / interior:** name the light source + direction, name materials ("light oak flooring," "gray sofa"), state lens ("wide-angle").
- **Landscape:** write "foreground, midground, background" to force depth layers; "calm blue lake showing perfect reflections" for water; explicit time-of-day light.
- **Street / candid:** "candid," "looking to the side" (kills the stiff pose), "blurred pedestrians in the background," "slightly grainy film look," "50mm lens."
- **Text-in-image:** short text only; "bold sans-serif font," "high contrast," "sharp legible text," and "ultra-sharp text rendering" if blurry. Finish complex layouts in Canva/Figma.
- **Style transfer:** name the *technique*, not just the style — "thick visible brush strokes," "visible canvas texture," "impasto," "+ in the style of Van Gogh," and add "maintain subject recognition" to avoid over-transformation.
- **Abstract:** name the forms AND their behaviors ("swirling liquid metal flowing upward," "geometric shapes fracturing").

## 8. JSON prompting & the 5-input "creative director" system

- **JSON prompts (label/value pairs) outperform freeform prose for Nano Banana Pro** and make edits surgical — change one field, keep the rest. (Dylan Davis, WealthWise)
- **5-input creative-director framework:** you supply (1) purpose/use case, (2) audience, (3) subject, (4) brand rules/colors, (5) optional reference image. A system prompt (distilled from Google's official Nano Banana Pro tips) writes the JSON. If an input is missing, it asks first. (Dylan Davis)
- **Face/character consistency via JSON:** reuse the same reference face across different JSON prompts to keep one character across shots. (WealthWise)

## 9. Context-rich prose vs keyword stuffing (the Nano Banana Pro shift)

- **Contested but important.** Dylan Davis (citing Google's blog): "With reasoning-heavy image models like Nano Banana Pro, you don't have to use all this jargon. Give it rich context and it infers what's best." Other sources (AI Master, Taylor Bay) still teach explicit camera/lighting keywords and report them working. Reconciliation: keywords still help, but on Nano Banana Pro a clear, complete *description of intent* matters more than stacking tokens.

## 10. Realism meta-tokens & reverse-engineering a look

- **Reverse-engineer:** give a great image to ChatGPT — "what meta tokens should I use to regenerate this and keep the hyperrealism?" — and reuse the camera/lighting/film tokens. (metricsmule, Jack Vs. AI)
- **Realism anchors:** "bokeh effect," "blurriness in the background," close-up framing. (metricsmule)
- **Seed tokens (cross-platform, MidJourney/Leonardo/Freepik):** "the most realistic photograph ever in the world," "stills archive," studio-domain tokens. Note: demonstrated on other platforms, applies loosely to Higgsfield. (metricsmule)

## 11. Higgsfield-specific image features

- **Cinematic Cameras** — choose camera body, lens, focal length, aperture in the UI; it appends them to the prompt. Tag `@character` to pull a Soul ID. (Artturi Jalli)
- **Mood Board** — upload 20-30 same-style images (don't mix cartoon + photoreal + vintage — it breaks) or pick a community preset; combine with Soul ID on the "Soul preset" model. (Artturi Jalli)
- **Shots app** — 9 cinematic angles from one image (3×3 grid), ~4 credits, upscale keepers. Great for e-commerce coverage and storyboards. (DGI Kaos, Creative Suite Tutorials, Sebastien Jefferies — "Angles 2.0" 12-angle variant)
- **Skin Enhancer** — soft / realistic / imperfect, ~4 credits, fixes plastic skin. (DGI Kaos)
- **Relight** — set light direction, hardness, brightness, color post-generation. (Artturi Jalli)
- **Upscale** — Topaz model, 2x/4x/8x. (Artturi Jalli)
- **Canvas** — node graph (Prompt → Image), pick any model per node, fork one prompt into 3 models to compare side-by-side, add an LLM Assistant node. (Artturi Jalli)
- **Recreate** — homepage templates (and a browser extension) show the prompt + image; click Recreate to auto-fill, then swap in your image/character. (Joseph Martin, Jack Vs. AI)
- **Cinema Studio Cast** — guided character builder (genre/era/archetype/appearance/outfit), ~0.625 credits each, reusable named elements. (David Manning)

## 12. Workflow rules of thumb

- **Generate 4, not 1.** Batch four results (~2 credits) and cherry-pick before committing. Unlimited toggle gives only 1. (DGI Kaos, Higgsfield AI)
- **Test at low quality, then upscale.** Check composition at 720p/2K, regenerate the keeper at 4K. (Rourke Heath, AI Foundations)
- **Aspect ratio by use case:** 16:9 thumbnails/hero, 9:16 reels/stories, 1:1 feed, **21:9** for cinematic anamorphic (Nano Banana Pro frames better at 21:9 because it was trained heavily on widescreen). Set it before generating. (Higgsfield AI, Theoretically Media, Artturi Jalli)
- **Suppress AI tells:** "no text on clothing," "solid [color] hat," "no subtext" to stop fake logos/lettering on garments. (DGI Kaos, LTDesign97)
- **Prompt enhancer toggle — contested.** Turn ON for quick image creation (it expands a bare prompt); turn OFF when you have a precise prompt and want exact wording. (Higgsfield AI says on by default for Soul 2; DGI Kaos and Jack Vs. AI say off for control.)

## 13. Caveats & risk

- **Credit/plan caveats:** "unlimited" tiers have been repeatedly restricted (resolution capped to 1K/2K on unlimited; concurrent generations cut). Re-check current plan before relying on "unlimited 4K." (Yaroflasher)
- **Data/privacy:** Higgsfield's terms can let them use your generations in promotion — not suitable for NDA/confidential client work. (Yaroflasher, Jack Vs. AI)
- **Higgsfield vs MidJourney:** Higgsfield wins on photoreal; MidJourney still wins on surreal/dreamlike. Many pros use MidJourney for environment refs, then Nano Banana Pro for character consistency. (Jack Vs. AI)
- **GPT Image text gotcha:** in-Higgsfield GPT Image is less text-accurate than native ChatGPT — use Nano Banana Pro for text-heavy images. (Artturi Jalli, Joseph Martin)
- **Soul ID prompting depth not in this corpus.** These videos cover the *training/tagging mechanics* well but light on advanced Soul ID prompt craft. See the existing `higgsfield-soul-id` skill for that.
