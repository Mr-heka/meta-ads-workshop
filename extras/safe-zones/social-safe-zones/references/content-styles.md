# Content and subject placement

These are Selr layout choices. Use the actual source and requested creative direction; do not invent an approval requirement for a different layout. Read the matching renderer's current skill before building.

| Route | Use when | Placement check |
|---|---|---|
| `straight_talking_head` | Delivery carries the idea | Measure the face/body and keep overlays outside the padded face area |
| `above_head_graphic` | One explanation benefits from a small graphic | Graphic bottom stays at least 56px above the measured face; otherwise reframe or choose another layout |
| `split_person_bottom_broll_top` | Proof and presenter both need visibility | Put proof in the selected safe panel, presenter below; inspect small text and every transition |
| `full_cutaway_broll` | Proof needs the whole frame | Replace the presenter for the beat; keep important product/UI details in the selected safe rectangle |
| `motion_graphic_reel` | Voiceover or motion explains the concept | Declare every important overlay and timing; no fictional face measurement needed |
| `carousel_static` | Stills communicate the story | Pick the actual static canvas/crop; check each slide rather than forcing video fields |

The framing checker validates supplied boxes against canvas bounds, face size/ranges and the chosen framing preset. It does not locate a person in an image. The face-width/height bounds are Selr composition targets, not anatomical detection. Body boxes may extend below the overlay-safe area but must remain on canvas. Product cutaway boxes require 32px inset from the selected framing preset.

Measure multiple representative frames for movement and camera changes. A single example rectangle is not proof that a moving face stays there. The plan checker conservatively compares each overlay with every supplied face box and 56px padding; it does not track faces or validate a segmentation mask. For moving subjects, record their envelope or enough measured boxes, then inspect the actual frames. A claimed behind-subject mask does not bypass this check; review that rendering separately.

The old fixed split panel of width 768 no longer fits the corrected standard-template intersection; the matching local panel is width 660. Do not squeeze a dense UI capture into it simply to obtain a pass. Use a full cutaway or a platform variant when the story needs more space.

Keep captions, logos, products and important text inside the selected scenario's safe rectangle. On vertical placements, inspect the action rail and bottom UI especially. Reframe before burning captions. If a face or important text conflicts with UI, change the crop, layout or platform variant rather than hiding the conflict behind a passing checklist.
