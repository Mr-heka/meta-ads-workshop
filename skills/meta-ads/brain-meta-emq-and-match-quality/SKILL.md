---
name: brain-meta-emq-and-match-quality
description: Use when the user says "fix our EMQ", "Lead EMQ is 5.2", "why is there no EMQ score", "events are double firing", or asks about advanced matching, match keys, hashing, fbc or fbp, event_id deduplication, Event Quality coverage, or a CAPI 400 from user_data. Route server transport and GHL wiring to brain-meta-capi-server-side-deep.
metadata:
  type: expert-brain
  topic: "Meta event match quality and advanced matching (EMQ)"
  aliases: "EMQ, event match quality, match quality, match score, EMQ dropped, no EMQ score, advanced matching, automatic advanced matching, manual advanced matching, match keys, customer information parameters, user_data parameters, what parameters should the pixel send, hashed email, SHA-256 hashing, PII hashing, lowercase and trim, E.164, Unix timestamp, fbc, fbp, fbclid, click ID, browser ID, external ID, IP address, user agent, event deduplication, dedup, double counting, same event twice, event ID, event_id, Event Quality tab, parameter coverage, Lead EMQ, Purchase EMQ, push events to 7+"
  domain: tracking
  built: "2026-07-05"
  sources: 17
---

# Brain: Meta event match quality and advanced matching (EMQ)⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

> Built by topic-brain-builder from 17 YouTube sources
> (3 hidden-gem creators surfaced on engagement,
> not views). Made by Selr AI.

## Jump to

- [What the experts agree on](#what-the-experts-agree-on): the 7-point consensus
- [Named frameworks & methods](#named-frameworks--methods): stacking ladder, bands, dedup procedure
- [Contrarian / disputed takes](#contrarian--disputed-takes): plugins vs GTM, phone's rank, vendor stats
- [Execution playbook](#execution-playbook): IF/THEN rules, default numbers, pre-flight, failure modes
- [Applied to your business](#applied-to-your-business): fill-in-your-own-numbers moves and exclusions
- [Related brains](#related-brains) and [boundaries](#pairs-with--boundaries)
- [Deeper references](#deeper-references): synthesis, quotes, experts, transcripts, worked example

## How to use this brain

When the user is working on Meta event match quality and advanced matching (EMQ), load this brain first. Ground answers in
the synthesis below and cite experts by name from the quote library. Prefer the
consensus view; surface a contrarian take when it's well-argued.

## What the experts agree on

1. **EMQ is a 0-10 score per event type, not per pixel.** Purchase, Lead and PageView on the same pixel each carry their own score, and low-signal events (PageView) naturally score lower because no personal data exists at that moment. Backed by SignalBridge, Jack Newman, CreatorOpsMatrix, Germinate IT.
2. **Hashed email is the single highest-impact match key, click ID close behind.** SignalBridge puts email alone at +1.5 to 2 points; Habibur Rahman shows Meta's own doc ranking email and Click ID as the only HIGH-priority keys; Meta for Business confirms the high-priority set officially.
3. **Normalise before you hash, or the key is worthless.** Lowercase and trim email, E.164 the phone, then SHA-256; event_time as a Unix timestamp. Backed by SignalBridge, CreatorOpsMatrix, Habibur Rahman, Germinate IT (who also lists the fields that stay plain, like IP).
4. **No CAPI, no EMQ score at all.** EMQ is a Conversions API metric: an event with no server-side data will not display a score regardless of volume (Jack Newman). If you are pixel-only, the job is not "raise your EMQ", it is "start sending server events" — the score only exists once CAPI does. CAPI is also the layer ad blockers and Safari cannot touch (PixelYourSite, TrackingFixes).
5. **Deduplication lives or dies on one identical event ID on both sides.** Browser and server event must share a genuinely unique ID; if the platform cannot match them, run CAPI-only rather than double count. Backed by Pro Data Track, PixelYourSite, Jack Newman, TrackingFixes.
6. **Real data only; an empty field beats a fake one.** A 10/10 built on fabricated data is noise that misleads optimisation (Pro Data Track, uncontested across the set).
7. **Diagnose in the Event Quality tab, and give fixes time.** Per-parameter coverage percentages show exactly which key is missing (Jack Newman); EMQ moves on a rolling window that includes pre-fix history, so scores lag fixes (TrackingFixes). Breaks are silent, so monitor weekly (SignalBridge, CreatorOpsMatrix).

## Named frameworks & methods

- **SignalBridge's parameter stacking ladder** (server events only, thin payload to rich): IP-only event scores 2-3; add hashed email, 6-7; add phone plus click IDs, 8-9; all six parameters, 9.5-10.
- **SignalBridge's EMQ bands:** 1-3 critical, 4-6 partial, 7-8 strong, 9-10 excellent. Vendor framing, and it describes accounts that ALREADY send server events. A pixel-only event has no score at all, so it cannot "land" in a band; the bands start applying the day CAPI starts. Their 7-step playbook claims the payload steps (email, phone, richer user_data) alone move an account from the 4-6 band to 8-9.
- **SignalBridge's weekly 4-step check:** open Events Manager; open the conversion event and read its EMQ; scan customer information parameters for green-to-yellow/red changes; investigate any drop immediately.
- **Habibur Rahman's Meta priority tiers:** HIGH = email, Click ID. MEDIUM = phone, date of birth, country, External ID, FBP, name fields, Facebook Login ID. LOW = state/city. One missing HIGH key can collapse the score.
- **CreatorOpsMatrix's 6.0 threshold and three traps:** below 6.0 is a critical tracking gap; the traps are FBP without FBC, hashing without normalising, and the "batching penalty" (hourly batched sends instead of near real-time).
- **CreatorOpsMatrix's FBC chain:** ad click appends FBCLID; landing page captures and stores it; automation parses the payload; CAPI maps it to FBC. Any broken link loses the key.
- **Pro Data Track's GTM dedup procedure:** install the unique-event-ID community template as a variable, attach it to the Event ID field of every browser AND server tag, verify the same ID digits appear on both sides in preview, confirm Events Manager counts one event.
- **Jack Newman's two capture methods:** read localStorage variables the platform already writes (GoHighLevel writes '_UD' with phone and name after form submit), or build a GTM tag that watches form field IDs and writes localStorage yourself.
- **TrackingFixes' rolling window rule:** EMQ averages over roughly 48 hours plus history, and low volume slows movement; his coverage bar is 95%+ on technical parameters.

## Contrarian / disputed takes

- **Plugins vs GTM (the live fight).** PixelYourSite (vendor) says plugins handle paired events, dedup and advanced matching natively. Pro Data Track says plugin/app setups block the backend control needed for proper event IDs, and migrated a client OFF PixelYourSite to fix corrupted fbc/fbp values; TrackingFixes says the same about Shopify's default apps. The GTM camp has the before/after receipts.
- **Phone's rank.** SignalBridge puts phone in Tier 1 beside email; Rahman's reading of Meta's doc has it at medium priority. Practical order: email, click ID, phone.
- **The score scale.** Rahman describes 0-100 with 10.8-style examples; everyone else, including Meta's flow, works on 0-10. Side with 0-10.
- **Vendor statistics.** The 22% CPA penalty and 8-15% CPA improvement figures come from a tracking vendor (SignalBridge) citing uncheckable case studies, and their own threshold shifts between videos. Directional only.
- **Both-sides vs CAPI-only.** Consensus says send browser and server together, deduplicated. Jack Newman's dissent: when event IDs cannot be matched across sides, kill the browser event and run CAPI-only, a cleaner signal beats a duplicated one.
- **Flagged from an excluded source:** Meta's account scorecard (via Professor Charley T, thin) bundles EMQ targets with Advantage+ adoption nudges. Our verified base (brain-meta-ads-manual-control-no-advantage) overrides the Advantage+ nudge; take the EMQ target, ignore the automation push.

## Execution playbook

**IF/THEN operating rules**

- IF an event shows no EMQ score at all THEN CAPI is not sending for that event; fix server-side delivery before touching parameters (Jack Newman).
- IF Lead or Purchase EMQ is below the 6.0 floor THEN add hashed email first (+1.5 to 2 points), then phone; email plus phone typically lands 7-8, which clears the 7+ target (SignalBridge).
- IF a parameter's coverage percentage drops in the Event Quality tab THEN trace it to that week's site, form or plugin change; breaks are silent (SignalBridge, CreatorOpsMatrix).
- IF browser and server events cannot share one unique event ID THEN turn off the browser event and run CAPI-only (Jack Newman).
- IF you test a page from a direct URL and FBC is missing THEN that is expected, FBC only exists on ad clicks; do not "fix" it (CreatorOpsMatrix).
- IF Events Manager diagnostics warn of a modified fbc/fbp value THEN read the cookies directly as variables and send them unaltered in Meta's exact format (Pro Data Track).
- IF a customer data field has no value THEN send it empty, never a fabricated fallback (Pro Data Track).
- IF a fix shipped and the score has not moved THEN wait it out; EMQ rolls over roughly 48 hours plus history and low volume slows it (TrackingFixes).
- IF PageView or other low-signal events score 5-6 THEN leave them; only Lead and Purchase need the 7+ push (Jack Newman).

**Default numbers the experts use**

- **Library-wide EMQ standard: 6.0 is the floor, 7+ is the target** on Lead and Purchase. Below 6.0, fix the payload before scaling spend (CreatorOpsMatrix's threshold); 8+ is the strong band (SignalBridge).
- Hashed email alone: +1.5 to 2 points. Full six-parameter stack: 9.5-10 (SignalBridge).
- Adding CAPI to a pixel-only setup does not "add 2-3 points" — it creates the score that did not exist. SignalBridge's "+2-3" is a vendor comparison of thin vs rich server payloads on accounts already sending them; treat it as direction, not arithmetic.
- Learning phase needs roughly **50 optimisation events per ad set per 7 days** (library-wide standard); higher EMQ means more of your events match and count toward it (SignalBridge, consistent with the verified manual-control base).
- Formats: email lowercase + trimmed, phone E.164, both SHA-256; event_time Unix seconds (SignalBridge, CreatorOpsMatrix).
- Coverage: 95%+ on technical parameters (IP, user agent, FBP); user-entered fields will trail (TrackingFixes, Jack Newman).
- Send events near real-time, never hourly batches (CreatorOpsMatrix). Check EMQ weekly (SignalBridge).

**Pre-flight checklist before any EMQ work or campaign launch**

1. Server events arriving: Events Manager shows CAPI receiving for the target event.
2. Dedup verified: identical event ID on browser and server sides in Test Events / GTM preview.
3. Email and phone normalised then SHA-256 hashed; no raw PII in any payload.
4. FBC and FBP captured and passed through unmodified; landing pages keep the fbclid.
5. Event Quality tab baseline recorded: EMQ score plus per-parameter coverage percentages.
6. Every empty field sends empty, no fake fallbacks anywhere.
7. Events send in near real-time, not batched.

**Top 5 failure modes and fixes**

1. **Silent CAPI death.** Server-side failures throw no warnings; you notice via CPA weeks later. Fix: the weekly Event Quality check, treat any parameter colour change as an incident (CreatorOpsMatrix, SignalBridge).
2. **Broken dedup double counting conversions.** Random per-side IDs or stacked plugin tags. Fix: one dynamic unique-event-ID variable on every tag's Event ID field; if IDs cannot match, CAPI-only (Pro Data Track, Jack Newman, TrackingFixes).
3. **Hashing unnormalised PII.** "User@Gmail.com " hashed as-is never matches. Fix: lowercase, trim, E.164 before SHA-256; malformed payloads can 400 (CreatorOpsMatrix, Rahman).
4. **Gaming the score with fake data.** 10/10 on noise misleads optimisation and wastes budget. Fix: empty fallbacks, real data only (Pro Data Track).
5. **The batching penalty.** Hourly batched server sends degrade match quality. Fix: fire events synchronously or near real-time on the conversion (CreatorOpsMatrix).

## Applied to your business

Work through this with your own account open. Fill in the bracketed values before you act on anything.

**Write these down first**

- Your dataset/pixel: `<YOUR_PIXEL_ID>`. Your ad account: `<YOUR_AD_ACCOUNT_ID>`.
- Your money event: `<your main conversion event>` (Lead for service and info businesses, Purchase for a checkout).
- Your current EMQ on that event: `<score today>`. Your gap to the 7+ target: `<7 minus your score>`.
- Your CRM or form tool: `<your CRM>`. Your page stack: `<your site builder>`.

**Which of your offers this feeds**

- **Any offer whose ads optimise for Lead**: your Lead EMQ decides how much of that form-fill signal Meta can actually match to a person. Instant-form leads are a separate path, they match on Meta's own lead ID.
- **Any offer with a checkout**: the Purchase event needs value, currency and the full hashed customer payload from the day it goes live, not bolted on later.
- **Warm retargeting and pipeline routing**: both depend on matched site events, so they inherit whatever match quality your server events carry.

**Consensus translated into execution moves**

1. **Confirm server events exist before chasing a score.** Open Events Manager on `<YOUR_PIXEL_ID>` and check the event is arriving via the Conversions API. Per Jack Newman, no server events means there is no EMQ score to improve — a blank score is a CAPI problem, not a parameter problem.
2. **Wire Lead events with hashed email and phone.** If your pages are on a CRM funnel builder, Newman's method applies directly: many builders write the submitted phone and name into a localStorage variable you can read browser-side, while the CRM's webhook or workflow feeds the server event. Normalise first (lowercase and trim the email, E.164 the phone for `<your country code>`), then SHA-256.
3. **Dedup the Lead event.** One shared unique event ID on the browser event and the server event. If your builder cannot carry a matching ID on both sides, run that event CAPI-only per Newman rather than double count into learning.
4. **Build any Purchase event complete on day one**: value, currency (`<your currency>`), hashed email, phone and name, plus fbc/fbp passed through from the click. Partial events score lower (SignalBridge), so do not ship a value-only Purchase.
5. **Add a weekly EMQ check to your ads ritual:** Events Manager > event > View Details > Event Quality. Floor 6.0, target 7+ on your money events, log per-parameter coverage, investigate any drop the same week. On custom-coded pages, capture and persist `fbclid` on landing so FBC survives to the conversion.

**What may NOT apply to you, and why**

- **Catalog match rate and content ID work** (Pro Data Track, TrackingFixes): only relevant with a product catalog or Commerce Manager feed. Skip it if you sell services, events or a single course.
- **Shopify and WooCommerce plugin fixes** (PixelYourSite, TrackingFixes): shop-CMS specific. On a CRM funnel builder plus a custom site, the plugin-vs-GTM debate resolves toward a direct server integration from the CRM plus code-level capture on your own pages.
- **The full ecommerce event chain** (ViewContent, AddToCart, InitiateCheckout with content IDs): if your funnel is simply Lead then Purchase, InitiateCheckout is at most an interim proxy while Purchase volume builds.
- **Meta scorecard's Advantage+ adoption nudges** (surfaced via an excluded thin source): if you run manual campaigns, take the EMQ and CAPI-coverage targets from that scorecard and discard the automation push.

## Related brains

- `brain-meta-capi-server-side-deep`: the server-side plumbing this brain's scores depend on
- `brain-meta-ads-manual-control-no-advantage`: the verified evidence base; wins any conflict
- `brain-meta-media-buyer-manual`: campaign structure, budgets, kill rules
- `brain-meta-creative-strategist-manual`: hooks, angles, creative briefs
- `brain-meta-optimisation-event-strategy`: which event to optimise for

## Pairs with / boundaries

- **brain-meta-capi-server-side-deep** owns the transport layer: GTM server containers, Stape, direct API calls, GHL-to-Meta wiring, Graph API errors, test event codes. This brain owns what travels IN those events (match keys, hashing, dedup IDs) and how Meta scores it.
- **brain-meta-media-buyer-manual** and **brain-meta-ads-manual-control-no-advantage** own campaign structure, budgets, bidding and the automation stance; where any EMQ source or Meta tool nudges Advantage+, the manual-control base wins.
- **brain-meta-optimisation-event-strategy** owns WHICH event to optimise toward; this brain owns making whichever event you chose match well.
- Out of scope here: creative and copy, catalog/feed management, GA4 or non-Meta analytics, and campaign-level performance analysis.

## Deeper references

- `references/synthesis.md`: full thematic synthesis
- `references/quote-library.md`: verbatim quotes with attribution
- `references/experts.md`: who was mined and why (popular vs hidden-gem)
- `examples/emq-diagnosis-session.md`: worked session, diagnosing a Lead EMQ of 5.2 end-to-end

Router key `sk-1nw6q92` — resolved by the skills index on load.
