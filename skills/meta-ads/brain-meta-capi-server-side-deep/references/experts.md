# Experts Mined: Meta Conversions API server-side tracking deep-dive

Gem status comes from the source index built at mining time (small channel + top-decile engagement = hidden gem).

## Hasib Ashad: HIDDEN GEM (3 videos; the A-to-Z video carries the gem flag)
GHL automation instructor. The sharpest taxonomy in the set: pixel website events vs CAPI funnel events vs CAPI lead events, and why they must never be confused. Uniquely adds: lead events never appear in Events Manager (normal, not broken), the feedback loop only works on Instant Form leads because of the Meta lead ID, free-form pipeline stage names as event names, and the silent attribution killer (Zapier/webhook intake = "third party lead" = CAPI skips the lead).

## Scott Henry: HIDDEN GEM
GHL practitioner focused on lead-quality gating. Uniquely adds: the if/else conditional pattern that lets unqualified prospects book while withholding the CAPI send, so the pixel is only reinforced with qualified data. Also the clearest statement that ad-set conversion location locks at publish.

## Elyes Hannachi: HIDDEN GEM
The most technically advanced source. Custom two-layer architecture ("TLDC CAPI protocol"): inline scripts + n8n middleware for user events, GHL pipeline triggers for backend events. Uniquely adds: forced manual event_id sync, persistent visitor IDs, a shared-secret bot filter, and the 25-50 conversions/week threshold before optimising deep-funnel. His "Layer 1 gives 80% of results" keeps the fancy build in proportion.

## Analytics Mania (Julius-run GTM channel): popular
The only source that rigorously evaluates the CAPI Gateway category. Uniquely adds: the live Ghostery demo proving the Gateway dies when the pixel is blocked, the "1 or 2% at best" realistic-lift estimate against Meta's 13% claim, and the cookie-lifetime limitation vs proper GTM server-side tagging.

## Danyyil Giba: popular
GHL agency onboarding. Uniquely adds: real before/after numbers (pixel-only +1.3% over-report on $7,745; pixel+CAPI -2.5% under-report on ~$16,000) and the argument that under-reporting is the healthy direction. Also documents the 10-25 minute propagation lag so nobody "fixes" a working setup.

## Ken Greeff Codes: popular (developer voice)
Rails SaaS founder. Uniquely adds: the $29,000 lesson on firing CompleteRegistration before email verification, the verified-milestone event sequence (PageView > CompleteRegistration > StartTrial > InitiateCheckout > Subscribe), and actual server-to-server code detail (SHA-256 hashing, background job posting to the API).

## Jack Newman: popular
Agency consultant on Event Match Quality specifically. Uniquely adds: per-event EMQ benchmarks (Lead 9.3, Schedule 8.8, PageView 6.1), the field-by-field send-rate drilldown (hashed email at 81% vs IP at 100%), three concrete enrichment methods (local storage `_UD` key in GHL, self-built GTM capture, Zapier/Make mapping), and the rule to kill the browser event when IDs cannot match.

## Make (webinar with Meta product marketing): popular / platform-official
The platform-side authority in the set. Uniquely adds: CAPI-for-CRM now REQUIRED for the conversion-leads goal on instant forms, the match-key hierarchy (lead ID > click ID/email > phone > supplementary), the 5-minute smart-dedup window, the 28-day CRM attribution window, the 1-40% stage-selection rule, and Events Manager CRM diagnostics (lead coverage below 60% flag).

## Localnichemarketing: popular (small)
GHL setup with an auditor's eye. Uniquely adds: the mismatched-event-name failure (Submit Application firing instead of Lead because of the GHL form's own setting) and the honesty that pipeline-stage events are worthless if the CRM is not updated at least a few times weekly.

## Ronan Nuttgens: popular (small)
High-ticket lead-gen. Uniquely adds: the store-owner analogy (pixel guesses right 60-70%), the three causes of double counting, the test-code workflow inside GHL, and the flag that circulating conversion-volume thresholds (3 to 200) are folklore, not Meta doctrine.

## MIJAN - Web Analyst GTM & GA4: popular (small)
GTM server-side specialist. Uniquely adds: the full verification drill: Test Events showing browser + server pairs, the ad-blocker isolation test proving server independence, and HTTP 200 as the per-event confirmation signal.

## Rasmus TrueROAS: popular (small, vendor)
Attribution vendor founder. Uniquely adds: the algorithm-side framing (CAPI feeds Meta's "find the next purchaser" matching), the fbclid as the single most valuable parameter to send back, and the 15-17% lift figure from his platform's aggregate data. Vendor lens; treat his lift number as directional.

## Creative Testing Lab: popular (small)
News-style coverage of Meta's April 15 Events Manager updates. Uniquely adds: the one-click native CAPI setup, the 17.8% CPA claim, guidance on when to keep an existing partner/GTM setup, and the AI pixel-enrichment rollout (30-day notice, on by default, special ad categories excluded).

## Pixel Flow: popular (small, vendor)
Vendor demo of a visual CAPI tagger for Framer sites. Uniquely adds: proof that no-code point-and-click CAPI tooling exists for platforms with no native support, plus a live payload monitor pattern. Vendor claims (40% conversion loss on Framer) are marketing figures.

## CreatorOpsMatrix: popular (small)
The payload-level debugging source. Uniquely adds: the complete Graph API 400-error checklist (data array wrapper, normalise+SHA-256, 10-digit Unix event_time, Content-Type header, capitalised event names, no trailing commas, omit empty fields) and the safe test protocol via test_event_code.

## Garazd Creation: popular (small, vendor)
Odoo module demo. Uniquely adds: the only retry/batch architecture in the set (30-minute scheduled send, per-event status and raw API response inspection, manual re-send) and the internal-user testing trap.

## Meta for Business (2 videos): popular / official
Meta's own onboarding and CAPI-for-CRM positioning. Adds the canonical three setup paths, the current Events Manager click path, and the official lift claims (13% cost per conversion, 19% cost per quality lead). Marketing figures; pair with Analytics Mania's scepticism.

## Launch Stack Labs: popular (small)
Developer-style WooCommerce build. Uniquely adds: transaction ID as event_id, the exact-ID-equality verification standard, hard-coded credentials in wp-config as a security choice, and the strongest statement of the test-code cleanup rule.

## Hridoy Banik: popular (small)
Troubleshooting checklist for CRM-connected setups. Uniquely adds: the triple-connection failure inside GHL (Settings + funnel + Forms), the Shopify redundancy warning, Meta's pixel-first dedup priority, and the one-tool-for-both-channels rule.

---

## Source quality notes

- **Usable sources: 22 of 25.** Above the 8-source floor comfortably.
- **Excluded (3):** Amit Ghodke Videos (flagged thin; token-generation click path only), Masum Jia (era-flagged as a near-content-free build-along despite the gem flag; GTM server ground covered by MIJAN), Big Short Ads (era-flagged; garbled tool names, unverifiable).
- **Freshness:** all sources passed the <=12-month rule at discovery; no pre-Andromeda-era mechanics presented as current in the usable set.
- **Thin sub-areas of the locked scope:** retries/backfill is the weak spot. Only Garazd Creation shows a real retry/batch pattern, and it is Odoo-specific; nobody covers bulk historical backfill or access-token rotation. Gateway evaluation rests heavily on one source (Analytics Mania), though it is the strongest-evidenced source in the set.
- **Vendor lenses to discount:** Rasmus TrueROAS, Pixel Flow, Garazd Creation and both Meta for Business videos are selling something; their lift/loss percentages are directional, not verified.
- **Hidden gems per index:** 4 flagged (Hasib Ashad A-to-Z, Scott Henry, Elyes Hannachi, Masum Jia). Masum Jia excluded, so 3 gems are load-bearing in this brain.
