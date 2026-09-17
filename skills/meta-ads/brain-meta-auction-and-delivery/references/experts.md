# Experts Mined: Meta ad auction and delivery (ranking mechanics, diagnostics, fatigue)

Popular vs hidden-gem status comes from the source index built at mining time (hidden gem = small channel, top-decile engagement).

## Usable sources (10)

**Manny Ko** (hidden gem). The most technically dense source in the set. Walks the full four-stage pipeline (retrieval, light ranking, heavy ranking, auction, roughly 200ms per impression) and states the total value equation in its full form (advertiser value = bid x estimated action rate). Uniquely adds: Andromeda's cause (AI creative volume broke the old sorting), the learning phase as a permanent state, EMQ and CAPI kept in proportion, and scepticism about Meta's in-platform recommendations.

**Jon Loomer** (popular, the best-known name in the set). Precision explainer who draws the clean architectural line: Andromeda and optimisation decide auction eligibility, the auction decides the winner. Uniquely adds: named low-quality signals (engagement bait, clickbait, withholding information, post-click bounce), the higher-spend penalty for chronic low quality, and the thesis that quality, not bid manipulation, is the advertiser's real lever.

**Aptly Learning** (popular bucket). Textbook-clean walkthrough of the total value formula with the worked flower-advertiser example where quality alone flips a tied auction. Uniquely adds: the billing layer (CPM maths, budget as cap not spend, automatic vs manual payment models), which no other source covers.

**Jason Cavallaro, Elite Ads** (popular bucket). Ties the value formula directly to daily budget. Uniquely adds: the low-budget dead zone mechanism with numbers ($30-50/day at $20-30 CPM = 1,000-1,500 impressions/day) and the data-starvation spiral ("the scraps of the auction").

**AdAmigo AI** (popular bucket). The only procedural non-delivery troubleshooter in the set. Uniquely adds: the ordered diagnostic ladder for ad sets at zero spend (account health, audience floor of 200,000, 1,000-person pixel minimum for custom audiences, bid-cap check, duplicate, temporary 2-3x overbid, accelerated delivery as last resort), with exact UI paths.

**Nick Boddington** (popular bucket). Agency operator supporting 200+ SMB accounts, explicitly framed around post-Andromeda reality. Uniquely adds: structural simplification as the first fix for a performance drop, mandatory creative diversification across formats and placements, and tracking health (pixel, CAPI, deduplication) as a delivery prerequisite.

**Mukuba Consulting Services** (hidden gem). Diagnostic checklist separating uncontrollable underdelivery causes (macro, seasonality, regulation) from controllable ones. Uniquely adds: the adoption-curve rollout explanation for early-strong-then-soft performance (2.5% innovators, 13.5% early adopters, 34% early majority), the 7-14 day settle window, and the never-stop-the-winner fatigue rule with a 20-50 creative bench.

**Digital Prostuti** (hidden gem). Practical fatigue playbook. Uniquely adds: frequency bands by audience temperature (cold 1.5-2, warm 2-3, act immediately above 5), the surface-rotation model (thumbnail, hook, first 3 seconds read as a new creative), and four offer angles from one offer (problem, result, urgency, before/after). One take contested: the 30-45 day campaign duplicate-and-reset, which loses to the verified never-touch-a-winner rule.

**Keystone Digital Hub** (hidden gem). Marketing-101 framing whose distinctive contribution is breaking ad quality into the three named sub-rankings (quality, engagement rate, conversion rate) each paired with concrete cause-and-effect examples, plus a practical winning-ad checklist.

**Belad Tech Weekly** (hidden gem). Straightforward auction explainer; corroborates the total value formula and the not-highest-bid-wins principle. Least depth of the usable ten but clean on the core mechanic.

## Excluded sources (8)

- **Laurel Portié** (hidden gem): fixture-vs-injection content cadence framework; organic and no-ads campaigns, off-scope for auction and delivery. Thin.
- **Jason Chappel** (hidden gem): "cash flow and margin problem disguised as a marketing problem"; valuable framing but zero auction content. Thin.
- **Ahro Ali** (hidden gem): CRM follow-up workflow mislabelled as a creative system. Thin.
- **Param Digital Marketer** (popular bucket): era-flagged, presents manual interest targeting as the primary auction lever with no Andromeda framing.
- **Paul Chinedu Nnamani** (popular bucket): era-flagged, 50-conversions-per-week rule and manual audience-size doctrine; conflicts with the verified base, which wins.
- **Deneth Liyanagamage** (popular bucket): transcript too garbled (auto-translated) to cite, though his CTR-first fatigue signal sequence corroborates Theme 7.
- **Attract. Enroll.** (popular bucket): vertical-specific (dance studios), vague on the algorithm era, uncorroborated creative-ratio numbers.
- **Usman Saeed** (popular bucket): 2026 tactics listicle, sidesteps auction and delivery mechanics; number claims asserted without evidence.

## Source quality notes

- 18 sources mined, **10 fully usable** for the themes, 3 thin (off-scope), 5 era- or quality-flagged. Ten usable clears the 8-source floor, but the margin is real, not comfortable.
- Freshness: all 18 videos are within 12 months of the 2026-07-05 build. Two (Param Digital Marketer, Paul Chinedu Nnamani) present pre-Andromeda manual-targeting mechanics as current despite recent publish dates; both excluded from the themes.
- Thin sub-areas of the locked scope: **auction overlap** has no dedicated source in this set (nearest coverage is Cavallaro's you-compete-with-same-audience-advertisers point and the sibling exclusion-architecture brain); the fatigue **signal sequence** (CTR falls, CPM rises, CVR falls) rests only on the garbled Deneth transcript, so it is noted as corroboration rather than evidence. The AdAmigo non-delivery ladder and the Cavallaro dead-zone maths are each single-source; treat their specific numbers as one practitioner's defaults.
- Verified-base conflicts found and resolved (base wins in all four): frequency kill thresholds, calendar-based campaign resets, forced overbids as routine practice, and the 50-conversions-per-week learning rule. Detail in `synthesis.md`.
