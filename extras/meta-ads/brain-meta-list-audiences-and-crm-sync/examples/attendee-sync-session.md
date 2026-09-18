# Worked example: workshop attendees into the community retargeting audience

**Scenario.** A business runs a $2,000 in-person AI workshop for non-technical business owners. Past attendees sit in the CRM. A monthly community membership runs warm-only retargeting on Meta, ad account `<YOUR_AD_ACCOUNT_ID>`. The job: build a Meta customer list audience of workshop attendees, keep it synced from the CRM with no CSV ritual, and pull people out the moment they join the community.

**Brain loaded:** `SKILL.md` plus `references/quote-library.md`. Every quote below is verbatim from the quote library; every paraphrase names its expert. Transcription quirks in quotes are kept exactly as captured.

---

## Q1: Why upload a list at all? The pixel and CAPI are live.

The pixel (`<YOUR_PIXEL_ID>`, with CAPI and the Purchase event verified as firing) covers site behaviour. The attendee list is different raw material: people who already paid and showed up.

> "This option allows you to upload a list of your customers directly into Meta Ads Manager, making it easier to target people who have already shown interest in your business." - Click by Click Tutorials, *How to Upload Customer List to Meta Ads [2025 Guide]*

And a clean list compounds later:

> "we can even create lookike audiences to find similarities between our list and people out in the world that we may want to start marketing to" - The Livingoods, *Upload Customer Lists Into Meta Ads (Facebook Ads Manager)*

(Lookalike seeding itself belongs to `brain-meta-lookalikes-and-seeds`; this brain only hands it the clean list.)

## Q2: How do I get the historical attendee export into Meta? (one-off backfill)

Path, quadruple-confirmed across Saenz Digital, Nishant Kumar, My Online Master and Easy Click Fix: Ads Manager > Audiences > Create Audience > Custom Audience > Customer List. No pixel needed for this source.

File prep before Meta sees it:

> "Put one person per row. Include clear column headers and use common identifiers like email, phone number with country code, first and last name, city, state, postal code, and country." - Easy Click Fix, *How to Create Custom Audiences in Facebook Ads Manager [Full Guide 2026]*

Rename the GHL export headers to Meta's template codes (email, phone, FN, LN, zip, CT, ST, country) so every column auto-maps. Saenz Digital hand-mapped first and last name live because his columns were not labelled FN/LN; renaming first avoids that trap. My Online Master notes the template takes up to three email columns and multiple phone columns per person, so keep any second email or number in its own column.

Phones go in full international format for AU contacts. If Excel has pushed the numbers into exponential notation, Digital Bikana's rescue applies: select the column, format General, remove decimals, save, then upload.

Customer value column: yes for this list. Saenz Digital's example is a $6,000+ average sale making the value column worth carrying; the same logic holds for real order values here (a $2,000 workshop, with course and program buyers kept as their own lists). My Online Master notes Meta asks post-upload whether the file includes a value column and prompts for an audience-level descriptor.

After upload, confirm the row count Meta reports matches the export. Saenz Digital's upload read back:

> "Going to tell me that I imported 1,444 rows" - Saenz Digital, *Facebook Ads Custom Audiences 2026| Dynamic Update Customer List with GoHighlevel*

## Q3: Some attendees only gave an email. Drop those rows?

No. The minimum identifier floor is contested in the sources, so hold both truths:

> "either email ID or mobile number is required" - Digital Bikana, *How to create Custom Audience in Facebook Ads Manager?*

> "I believe we do need to have at least an email and a phone number" - The Livingoods, *Upload Customer Lists Into Meta Ads (Facebook Ads Manager)*

> "If you have only emails or only phone numbers, that's fine, but combining multiple identifiers often improves results." - Easy Click Fix, *How to Create Custom Audiences in Facebook Ads Manager [Full Guide 2026]*

Operating call: upload email-only rows rather than binning them, and stack every identifier GHL already holds on everyone else.

> "the more data you have on somebody, the better it's going to be" - Saenz Digital, *Facebook Ads Custom Audiences 2026| Dynamic Update Customer List with GoHighlevel*

## Q4: Uploaded. Status says Populating. Attach it to the community ad set now?

Wait for Ready.

> "it may take us a few minutes to finish matching your customers to people on Facebook" - My Online Master, *How To Upload A Customer List To Meta Ads (Step-by-Step Tutorial)*

> "the list of customers will be mapped with the actual user and only then the list will be ready" - My Online Master, *How To Upload A Customer List To Meta Ads (Step-by-Step Tutorial)*

Nishant Kumar saw the same state live straight after upload:

> "it's uh named as a populating because we have this uploaded and it is calculating the members like we had just uploaded the details" - Nishant Kumar, *How to Upload a Customer List in Facebook Ads (Step by Step 2026 Guide)*

My Online Master's cadence: refresh after an hour or two depending on list size, then attach.

## Q5: I do not want to re-export a CSV after every workshop.

Correct instinct, and the core of this brain.

> "this becomes a real pain in the behind because you don't want to constantly be doing this, and this is where HighLevel comes in" - Saenz Digital, *Facebook Ads Custom Audiences 2026| Dynamic Update Customer List with GoHighlevel*

Build Saenz Digital's tag-triggered sync (single-source mechanics, so verify the menu labels in the live GHL UI first): Automations > new workflow > Trigger: Tag applied (attended-<segment>) > Action: search "Facebook" > "add to a custom audience" > pick `<YOUR_AD_ACCOUNT_ID>` > pick the attendee audience > Save.

> "I'm going to show you how to set up a dynamic way to update that customer audience list with new data once you get it using high level" - Saenz Digital, *Facebook Ads Custom Audiences 2026| Dynamic Update Customer List with GoHighlevel*

The no-CRM fallback is Easy Click Fix's cadence, not needed here because GHL is the CRM:

> "Keep your list fresh by re-uploading periodically so your targeting stays accurate." - Easy Click Fix, *How to Create Custom Audiences in Facebook Ads Manager [Full Guide 2026]*

## Q6: What happens when an attendee joins the community platform? They should stop seeing the join ads.

Saenz Digital's two-way hygiene branch: if/then on the community-member tag. Tag present, the Facebook action removes them from the attendee retarget audience and adds them to a members list in the same pass. His framing:

> "I want people to either come on the list or come off the list based on certain data points or based off of certain, you know, steps that there are within the sales process" - Saenz Digital, *Facebook Ads Custom Audiences 2026| Dynamic Update Customer List with GoHighlevel*

> "now I'm dynamically managing that custom audience list and keeping it clean" - Saenz Digital, *Facebook Ads Custom Audiences 2026| Dynamic Update Customer List with GoHighlevel*

Same branch pattern covers course-buyer and program-buyer tags so buyers leave the matching prospect audiences.

## Q7: Ad set settings once the audience reads Ready?

The list is the targeting; strip everything else.

> "if you are creating an ad campaign based on custom audiences, you do not need to do any detailed targeting" - Digital Bikana, *How to create Custom Audience in Facebook Ads Manager?*

> "I would recommend building out your audience and not letting Facebook decide" - The Livingoods, *Upload Customer Lists Into Meta Ads (Facebook Ads Manager)*

Plus the verified manual-control base (Piliero, via this brain's synthesis): untick "use as a suggestion" so Meta cannot broaden the attendee list into a seed. On what the finished audience is for:

> "Once it's ready, you can use this audience at the adset level to retarget engaged customers, exclude existing buyers, or later create a lookalike to find more people like them." - Easy Click Fix, *How to Create Custom Audiences in Facebook Ads Manager [Full Guide 2026]*

Exclusion usage lives in `brain-meta-exclusion-architecture`; this session only builds and maintains the lists it consumes.

## Q8: Can we top the audience up with a bought list of local business owners?

No.

> "A quick heads up, always make sure you have permission to use the customer data you're uploading and that it complies with Meta's advertising policies and local privacy laws." - Easy Click Fix, *How to Create Custom Audiences in Facebook Ads Manager [Full Guide 2026]*

Saenz Digital and The Livingoods both feed purchased lists mechanically; the brain sides with Easy Click Fix's consent rule, and so do the compliance walls under AU privacy law. Opted-in CRM contacts only: buyers, attendees, registrants, waitlist.

---

## What this session built

- Historical attendee CSV uploaded with template headers, value column carrying real order values, row count verified against the export.
- Audience attached to the community ad set only after it flipped from Populating to Ready, with Detailed Targeting removed and suggestions declined.
- GHL workflows live: workshop-attended-<city> adds contacts to the attendee audience; community-member removes them and moves them to the members list.
- Consent wall held: no purchased data, opted-in contacts only.

Grounding: all quotes verbatim from `references/quote-library.md`; paraphrased mechanics attributed by expert per `references/synthesis.md`. No numbers introduced beyond the quote library and the scenario's illustrative price points.
