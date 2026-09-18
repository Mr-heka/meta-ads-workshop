# Experts Mined: Meta Troubleshooting Diagnostics

11 videos mined 2026-07-06. All under 12 months old. 9 usable after excluding one thin and one era-flagged source (detailed at the bottom). This set skews heavily toward hidden-gem operators surfaced on engagement, not view count, which is exactly what a triage brain wants: hands-on repair walkthroughs, not big-channel theory.

---

## Godbless Iboyi - Growth With Paid Ads (hidden gem)
- **Angle**: pure step-by-step delivery-repair. Walks live through Ads Manager to diagnose a non-spending ad set in a fixed order.
- **Uniquely adds**: the canonical non-delivery ladder (account status -> ad/asset status -> manual bid -> audience size -> force delivery) and the "2-3x target CPA to force auction wins" bid tactic. One of the two spine sources for the whole delivery half of this brain.

## AdAmigo AI (strong engagement for its size)
- **Angle**: media-buyer escalation ladder for non-spending ad sets, with explicit numeric thresholds and increasingly aggressive fixes.
- **Uniquely adds**: the audience-size floor line ("anything below 200,000 is playing with fire"), the AOV-relative bid framing ($5 target on a $5,000 product is too low), the "bid 1,500 when target is 250" forcing move, and the crucial safety caveat: monitor hourly, remove the forcing bid once delivery starts. Independently corroborates Iboyi's diagnostic order, which is what makes Themes 1-4 consensus rather than one-off.

## Learn with Bilal (hidden gem)
- **Angle**: reframes the whole triage as a trust/authority/system problem, not a Meta problem. Meta's only job is to deliver the message; sales and CPM are downstream symptoms.
- **Uniquely adds**: the 50-conversions-per-week learning-phase rule quoted from the Meta doc, the "editing every 24 hours breaks the algorithm" warning, the 2.5% CTR winning-ad threshold, the non-converting diagnostic order (creative -> copy -> page speed -> checkout -> trust -> retargeting), and the boost-button-is-not-optimisation callout. The broadest single source in the set.

## Kamal Bunkar (hidden gem)
- **Angle**: a fast, data-driven 24-hour creative diagnostic built on the 3-second video play rate, positioned as a replacement for the 5-7 day creative-test wait.
- **Uniquely adds**: the single cleanest diagnostic branch in the set (low 3-second count = bad hook; high count, low completion = weak offer/body; high on both = scale), the exact Customize Columns path to surface those metrics, and the mechanism linking a high 3-second rate to a falling CPM. His 40% threshold is a single-operator number; treat as directional.

## Mouss Unlimited Scaling (hidden gem)
- **Angle**: insider-brief framing of a hidden Meta customer-satisfaction score that drives CPM and auction priority, treating CPM spikes as a reputation symptom.
- **Uniquely adds**: the per-category complaint scoring model (below 70% healthy, 80-90%+ = dying), the three-layer trust hierarchy (feedback score / asset health bronze-to-platinum / BM trust), and the remediation path (request the "customer experience insight" report, fix the one or two worst categories). The most contested source: single, insider-framed, exact mechanics uncorroborated. Used as a triage prompt, not a hard rule.

## Mohanad Anan (hidden gem)
- **Angle**: ties expensive CPM/CPC/CPL directly to message-market mismatch at the awareness stage, with a concrete 6-step, ~4-day rewrite plan.
- **Uniquely adds**: the mechanism (0.5-second scroll-past = irrelevance signal = higher cost), the 6-stage awareness ladder mapped to ad copy, the 80/20 pain-to-offer landing-page split, the 4-day minimum test window, and the rule that testimonials/guarantees belong in retargeting, not cold ads. Strongly aligned with our own plain-English positioning doctrine.

## GUMY Art (hidden gem)
- **Angle**: bare-bones beginner checklist for a zero-results dashboard.
- **Uniquely adds**: the four literal causes of zero results in order (date filter, unpublished draft, no funded payment method, browser ad blockers suppressing the report itself) and the draft-to-results lag of up to 48 hours. The ad-blocker-suppresses-reporting cause is a genuinely non-obvious catch not found elsewhere in the set.

## Digital Surjeet (strong engagement for its size)
- **Angle**: screen-recorded live walkthrough clicking through actual error states one by one, showing the literal error text and the fix for each.
- **Uniquely adds**: named error-state fixes tied to exact on-screen text ("something went wrong, accepted error" -> duplicate rather than debug; "invalid message template, must have greeting text"; special ad category declaration blocks; "No ads" sync lag; "Processing" resolves in 5-7 minutes) and the core diagnostic habit: click the red error indicator to read the specific validation message.

## Jamie Stenton - Digital Marketing Expert (strong engagement for its size)
- **Angle**: agency auditor's warning that broken/duplicate/miswired pixel events are endemic (50-60% of audited accounts) and silently corrupt optimisation before any spend.
- **Uniquely adds**: the three event failure modes (don't fire / fire twice / wrong event fires), the named miswire (a contact form firing both Lead and Purchase), the Test Events walkthrough, testing every checkout path separately, and the pre-launch mandatory-gate framing. The only tracking-mismatch source, and the highest-value single-source contribution to that slice of the scope.

---

## Source quality notes

- **Usable sources: 9** (Godbless Iboyi, AdAmigo AI, Learn with Bilal, Kamal Bunkar, Mouss Unlimited Scaling, Mohanad Anan, GUMY Art, Digital Surjeet, Jamie Stenton). This is above the 8-source bar, but only just, and the distribution is uneven across the scope (see below).
- **Freshness**: all 11 mined videos passed the <=12-months rule at discovery. No freshness exceptions.
- **Excluded, thin**: **Bizliftng** ("Why Your Facebook Ads Are Not Working (Even If You Followed Tutorials)"). Strategy/mindset framing, not technical triage. Its one relevant line (2-3 days "is not testing, it's panicking") is noted as corroboration under the learning-phase theme but the video does not back any theme.
- **Excluded, era-flagged**: **Jason Gan** ("Fix Facebook Ads That Stopped Working in 2026"). Presents the fully-Advantage+ single-campaign/single-adset Andromeda restructure as settled best practice while conceding the field is still transitioning. Conflicts with our locked manual-control, no-Advantage+ doctrine. Andromeda structure questions route to `brain-meta-andromeda-advantage-mastery`.

### Honest coverage gaps within the scope
The locked scope names auction/audience overlap as a symptom, but this set is thin there. No mined source gives a real overlap-symptom-to-cause walkthrough. Overlap is only implied (narrow interest stacking as a delivery blocker). For genuine auction/audience-overlap diagnosis, route to `brain-meta-exclusion-architecture` and `brain-meta-auction-and-delivery`, which own that ground. Similarly, deep tracking mechanics rest on a single source (Stenton); this brain triages the mismatch and routes to `brain-post-click-tracking-plumbing` and `brain-meta-pixel-capi-signals` for the fix. This brain is deliberately a front door, so those gaps are handled by design, but they are real gaps in the source material and should not be papered over.
