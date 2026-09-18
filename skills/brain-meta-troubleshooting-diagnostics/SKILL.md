---
name: brain-meta-troubleshooting-diagnostics
description: "Use when the user says \"my ad isn't spending\", \"stuck in review\", \"zero results\", \"CPM/CPL spiked\", \"Ads Manager says X but my CRM says Y\", or \"ads stopped working\". Hand performance-drop verdicts back to the user with the next test to run; route auction or fatigue to brain-meta-auction-and-delivery, and tracking faults to brain-post-click-tracking-plumbing."
metadata:
  type: expert-brain
  topic: "Meta troubleshooting diagnostics (no delivery, CPM spikes, tracking mismatch, auction overlap)"
  aliases: "meta ads troubleshooting, facebook ads not working, ad set not delivering, ads not spending, no delivery, CPM spike, high CPM, expensive ads, expensive leads, cost per lead too high, zero results, ads manager error, stuck in review, preparing draft processing, ad rejected, tracking mismatch, ads manager vs CRM, pixel not firing, duplicate events, auction overlap, audience overlap, learning phase reset, repair manual, ad diagnostics, why did my ads stop working"
  domain: "advertising"
  built: "2026-07-06"
  sources: 11
---

# Brain: Meta troubleshooting diagnostics (no delivery, CPM spikes, tracking mismatch, auction overlap)⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

> Built by topic-brain-builder from 11 YouTube sources
> (8 hidden-gem creators surfaced on engagement,
> not views). Made by Selr AI.

## How to use this brain

When the user is working on Meta troubleshooting diagnostics (no delivery, CPM spikes, tracking mismatch, auction overlap), load this brain first. Ground answers in
the synthesis below and cite experts by name from the quote library. Prefer the
consensus view; surface a contrarian take when it's well-argued.

## What the experts agree on

1. **There is a fixed diagnostic order for a non-delivering ad set: account -> ad/asset -> audience -> bid -> force delivery.** Both hands-on delivery creators (Godbless Iboyi, AdAmigo AI) walk the same ladder. Start at the top, stop at the first thing wrong. Tell for account-level vs local: if other ad sets in the account are spending, the account is fine.
2. **Audience-size floors are a real delivery blocker.** Detailed-targeting under 200k is "playing with fire" (AdAmigo AI, echoed by Iboyi and Learn with Bilal); custom/retargeting audiences need at least 1,000 people in the source before they deliver reliably (Iboyi, AdAmigo AI).
3. **An overly restrictive manual bid silently blocks auction entry; reverting to automatic bidding is the default fix** (Iboyi, AdAmigo AI). The bid must respect AOV: a $5 target on a $5,000 product never enters the auction.
4. **When delivery is truly stuck, the sources force it three ways: duplicate the ad set, inflate the bid to 2-3x target CPA, or switch to Accelerated Delivery, then monitor closely and remove the forcing bid once spend flows** (Iboyi, AdAmigo AI). **Only the duplicate is beginner-safe.** Bid inflation is an advanced, money-losing-by-design tactic (see the force-delivery toolkit below for the guardrails it requires), and Accelerated Delivery is a legacy pacing control that most 2026 accounts no longer have and that does not exist under Advantage+ campaign budget. Check whether the option is even present before recommending it.
5. **Zero-results and error states are almost always a status/config problem, not a bug. Read the literal on-screen error and match it to a known fix** (GUMY Art, Digital Surjeet). Duplicate rather than debug a catch-all "accepted error".
6. **The learning phase needs ~50 conversions per week and resets on every significant edit; rapid editing is the self-inflicted wound** (Learn with Bilal, corroborated by our verified base).
7. **CPM/CPC/CPL spikes are a relevance penalty. A fast scroll-past tells Meta the ad is irrelevant and it charges more; a high early view rate lowers CPM** (Mohanad Anan on the cause, Kamal Bunkar on the cure, Learn with Bilal on the frame).
8. **Broken/duplicate/miswired pixel events silently corrupt optimisation and must be tested before spend** (Jamie Stenton). Test events live before trusting any number.

## Named frameworks & methods

- **The non-delivery ladder (Iboyi / AdAmigo AI):** account status (ban/restriction/payment) -> ad-level active -> asset-level active (Page/IG) -> manual bid not too low -> audience size (>=200k detailed; >=1,000 source for custom) -> force delivery.
- **Force-delivery toolkit (Iboyi / AdAmigo AI):** duplicate the ad set + slightly raise the daily budget. That is the beginner-safe move, and usually the only one you need.

  > **ADVANCED, SPENDS REAL MONEY FAST. Not a beginner step.**
  > The sources also inflate the manual bid to **2-3x target CPA/AOV** ("bid 1,500 when target is 250") to force auction entry, then remove it. Understand what that actually does before you try it: a bid cap sets the **maximum Meta may pay for one auction**, it is not your reported cost per result and it is not a spend limit. Bidding 1,500 tells Meta it may pay up to 1,500 for a single conversion, and on a stuck ad set that can empty a day's budget in minutes.
  > If you use it at all: (1) set an **account spending limit** and a **campaign lifetime budget or hard daily budget** FIRST, so there is a real ceiling underneath you, (2) check spend and cost per result **hourly**, not daily, (3) remove the forcing bid the moment delivery starts. If you are not comfortable watching it hourly, do not use it. Fix the audience size, the offer, or the creative instead.
  > **Accelerated Delivery** appears in these sources as the third lever. It is a legacy pacing option, not generally available in 2026, and unavailable under Advantage+ campaign budget. Confirm the setting actually exists in your ad set before treating it as a step; if it is not there, skip it, nothing is broken.
- **The 3-second play-rate diagnostic (Bunkar):** add "3-Second Video Play Rate" + a ThruPlay metric via Customize Columns. **<40% 3-sec rate = fix the hook.** High 3-sec + low completion = fix the offer/body. High on both = scale. His live read: winning creative 55-56% vs failing 13-14%. (Use as a WHY-diagnostic, decide kills on cost-per-result.)
- **The awareness ladder (Anan):** awareness -> interest -> consideration -> intent -> evaluation -> purchase. Testimonials/guarantees only land at consideration+; using them cold inflates cost. **80/20 pain-to-offer** landing page split, **4-day** minimum test window, features/testimonials belong in retargeting.
- **The three event failure modes (Stenton):** events don't fire / fire twice (duplicate) / wrong event fires (a form firing both Lead and Purchase). Test path: Events Manager -> pixel -> Test Events -> channel Website -> perform actions live; test every checkout path separately.
- **The hidden reputation score (Mouss, contested):** per-category customer-satisfaction percentile vs same-niche advertisers. **Below 70% healthy; 80-90%+ dies.** Three-layer trust: feedback score / asset health (bronze-silver-gold-platinum) / BM trust. Fix: request the "customer experience insight" report, fix the worst 1-2 categories.
- **Named benchmarks (single-source, directional):** CTR **>2.5%** = winning ad (Bilal); scroll-past window **0.5s** (Anan); ~**50** conversions/week to exit learning (Bilal); broken events on **50-60%** of accounts (Stenton).

## Contrarian / disputed takes

- **Kill on the 3-second rate vs kill on cost-per-result.** Bunkar says a <40% 3-second play rate is enough to condemn the hook and act. Our verified base (Ben Heath) is firm the opposite way: hook rate and CTR "explain WHY, never decide WHAT to kill" (his 16% hook-rate ad lost on cost-per-purchase to a 10% one). **Resolution: use Bunkar's metric to decide what to fix, make the final kill/keep call on CPL/CPA. Side with the verified base on the decision.**
- **The hidden reputation score is a single insider claim.** Mouss presents exact percentile mechanics and bronze/platinum tiers as fact. No other source in the set corroborates them. **Treat as a triage prompt (if CPM is high and creative + message-match are clean, check account/customer-experience health), not confirmed platform mechanics.**
- **CTR >2.5% as a winning threshold (Bilal) sits in mild tension with the same "don't decide kills on CTR" caution.** Treat 2.5% as a health check, not a kill trigger.
- **Excluded as contrarian-but-wrong-for-us:** Jason Gan's fully-Advantage+ single-adset Andromeda restructure. Conflicts with our locked manual-control doctrine; era-flagged and self-admittedly "still transitioning". Not used.

## Execution playbook

### IF / THEN operating rules
- **IF an ad set is not spending THEN run the ladder in order** (Iboyi/AdAmigo AI): check account status (other ad sets spending? then it's local) -> ad + asset both Active -> audience >=200k / source >=1,000 -> manual bid not too low -> only then force delivery.
- **IF the manual bid looks low relative to product price THEN revert to automatic bidding first** (Iboyi/AdAmigo AI). Don't hand-tune a cap you set too tight.
- **IF everything checks out and there's still no spend THEN duplicate the ad set** (AdAmigo AI). If it is still dead after ~0.5-2 days, the forcing bid at 2-3x target CPA is the next lever, but only under the guardrails in the force-delivery toolkit above: spending ceiling set first, hourly checks, bid removed the moment delivery starts. Not a beginner step.
- **IF the dashboard shows zero results THEN check, in order: date filter, Draft-vs-published, funded payment method, browser ad blocker** (GUMY Art). Wait up to 48h after publish before assuming failure.
- **IF there's a red error THEN click it, read the literal text, match to fix** (Surjeet). Catch-all "accepted error" -> duplicate the ad. "Processing/No ads" on a fresh ad -> wait 5-7 min. Special ad category error -> declare the category.
- **IF CPM/CPL spiked THEN check relevance before blaming Meta** (Anan/Bunkar): is the ad getting scrolled past (low 3-sec rate)? Is the message matched to the audience's awareness stage? Only after that, consider account-health (Mouss).
- **IF ads deliver and click but don't convert THEN move downstream** (Bilal): page speed (a 15-20s load kills it), form-field count, trust signals, then retargeting.
- **IF Ads Manager disagrees with the CRM THEN test every event live before trusting any number** (Stenton), hunting duplicate/miswired fires, then route to the tracking siblings.
- **IF you're tempted to edit a live ad set THEN don't** (Bilal + verified base): every significant edit resets learning (~48h). Touch nothing more than once every 7-10 days on a small budget.

### Default numbers experts use
- Audience floor: **200k** detailed-targeting, **1,000** source people for custom/retargeting.
- Forcing bid: **2-3x** target CPA/AOV, removed once delivery starts.
- Learning phase: **~50** conversions/week; edit resets it (~48h).
- Winning-ad checks (directional): CTR **>2.5%**, 3-sec play rate **>40%**, scroll-past danger at **0.5s**.
- Test window: **4 days** minimum before judging new creative (Anan).
- Lag windows: new ad "Processing" resolves in **5-7 min**; Draft-to-results up to **48h**.
- Landing page: **80/20** pain-to-offer.

### Pre-flight checklist (before you touch anything)
1. Confirm what kind of problem it is: delivery / cost / conversion / tracking. Wrong bucket = wrong fix.
2. Confirm the account isn't banned, restricted, or payment-failed. This masks everything below it.
3. Confirm you're reading the right date range and the ad is actually published (not Draft).
4. For any cost/tracking question, confirm the pixel and events are firing correctly first (Stenton's gate).
5. Note the last significant edit timestamp. If it's inside ~48h, the ad set may just be re-learning, not broken.

### Top 5 failure modes and their fix
1. **Helicopter-editing the ad set** (budget/audience/bid every 24h) -> resets learning every time. Fix: fixed schedule, touch at most once every 7-10 days (Bilal, verified base).
2. **Blaming Meta for a status problem** -> the ad is in Draft, the card is declined, or the audience is 40k. Fix: run the status ladder before touching strategy (Iboyi/AdAmigo AI/GUMY Art).
3. **Setting a manual bid too low and wondering why nothing spends** -> revert to automatic bidding (Iboyi/AdAmigo AI).
4. **Trusting the dashboard when events are broken** -> 50-60% of accounts have broken/duplicate events; a form firing both Lead and Purchase silently mis-optimises. Fix: test every event live pre-launch (Stenton).
5. **Fixing the hook when the offer is the problem (or vice versa)** -> the 3-sec-plus-completion split tells you which. Low 3-sec = hook; high 3-sec, low completion = offer/body (Bunkar).

## Applied to your business

**Write your own facts down before triaging anything:** ad account `<YOUR_AD_ACCOUNT_ID>`, pixel `<YOUR_PIXEL_ID>`, Page `<YOUR_PAGE_ID>`, `<your CRM>`, `<your landing-page stack>`, and your offer list with real prices (`<your flagship offer + price>`, `<your secondary offer + price>`, `<offers you never advertise cold>`). Diagnosis without those written down turns into guessing.

**Before you optimise toward any event, verify it is actually live.** Confirm the pixel fires, confirm CAPI is connected if you use it, and confirm the specific event you want to optimise for shows up cleanly in Test Events. A conversion Meta cannot see is a conversion it cannot optimise toward, and this is the single most common root cause behind "my ads stopped working".

### Which funnels this feeds
- **Your live cold-traffic campaigns**: this brain is the first thing to load when an ad set stalls or cost per result jumps. Triage first, do not just add spend. A fatigued ad set can go from `<your target CPL>` to several times that inside a fortnight; more budget makes that worse, not better.
- **Any offer you are about to optimise to a purchase event**: the tracking-mismatch and event-testing themes are the pre-flight gate. Confirm the event fires cleanly in Test Events before optimising to it.
- **Offers with no cold ads** (warm-only, referral, or sales-call driven): this brain applies only when their retargeting or feeder ad sets misbehave.

### Consensus translated into moves
1. **Run the status ladder before touching a stalled ad set.** Is `<YOUR_AD_ACCOUNT_ID>` healthy? Are other ad sets spending? Are the ad and the Page asset Active? Is the audience above the size floor? Only then consider forcing delivery. If you target a tight geographic radius, watch the 200k/1,000 floors closely: a small radius plus stacked interests is the most likely non-delivery cause.
2. **When cost per lead spikes, diagnose relevance and fatigue before spend.** Check the 3-second rate to tell a dead hook from a dead offer, check message-to-awareness match (are you pitching the mechanics to a cold buyer still at the awareness stage?), then route creative fatigue to the auction sibling. The fix is usually new creative concepts, not more budget.
3. **Gate every optimisation change on a live Test Events check.** Before running `<your offer>` to a Purchase or Lead event, walk Stenton's path on `<YOUR_PIXEL_ID>`: fire a test conversion, confirm one clean event, no duplicate, no stray second event. If you run browser and server events together, verify they are deduplicating rather than double-counting.
4. **Treat Ads-Manager-vs-CRM gaps as a tracking triage, then hand off.** This brain confirms the mismatch exists and whether it is a fire/duplicate/miswire; the fix lives in the tracking siblings. Never change optimisation off numbers you have not event-tested.
5. **Force-delivery tactics are a last resort with a hard leash.** If an ad set genuinely will not spend, duplicate first. Only inflate the bid as a temporary forcing move, with a spending ceiling set beforehand, hourly monitoring against `<your target CPL>`, and the bid pulled the moment delivery starts. Never leave a 2-3x forcing bid running.

### What does NOT apply to a lead-gen or service business
- **The COD/e-commerce trust levers (Bilal): "open the parcel first, then pay", return-policy lines, product-fake complaints.** Irrelevant to lead-gen and event sales, and they brush compliance walls if your own rules ban refund language, outcome guarantees and support promises. Use the message-match principle, drop the parcel scripts.
- **The boost button (Bilal) and any Advantage+ auto-restructure (Jason Gan, excluded).** If you have chosen manual campaigns, boosting and full-auto restructures are off-doctrine. Note the manual/Advantage+ setup flow changed in early 2026; re-verify against the live UI before assuming a toggle still exists.
- **Mouss's exact reputation-score numbers as gospel.** Useful as a "check account health" prompt if CPM is high with clean creative, but the specific 70%/bronze-platinum mechanics are uncorroborated and the "customer experience insight" report generally needs a Meta rep relationship. Directional only.
- **Blanket scepticism of instant forms.** Native lead forms are a legitimate funnel, not a shortcut. Whether they beat a landing page for you depends on lead quality downstream, so judge on booked/closed rate, never on raw cost per form.

## Related brains

- `brain-meta-auction-and-delivery`: Meta ad auction and delivery (ranking mechanics, diagnostics, fatigue)
- `brain-meta-exclusion-architecture`: Meta ads exclusion architecture (exclusions, overlap control, funnel sequencing)
- `brain-meta-ad-to-page-congruence`: Meta ad to page congruence (message match, the relevance chain, per-angle variants)

## Pairs with / boundaries

This brain is the triage front door. It confirms the symptom, names the likely cause, applies the quick fix, and routes deep mechanics elsewhere. It does not duplicate the siblings.

- **Auction mechanics, delivery ranking, creative fatigue** live in `brain-meta-auction-and-delivery`. This brain spots "CPM spiked / ad set stalled"; that brain explains why the auction is pricing you out and how fatigue unfolds.
- **Audience/auction overlap and exclusions** live in `brain-meta-exclusion-architecture`. This brain flags overlap as a symptom; that brain owns the diagnosis and the exclusion fix. Overlap is explicitly OUT of scope here beyond routing (the source set is thin on it).
- **Tracking plumbing and pixel/CAPI signal quality** live in `brain-post-click-tracking-plumbing` and `brain-meta-pixel-capi-signals`. This brain confirms a mismatch and whether events fire/duplicate/miswire; those brains own the wiring fix.
- **Andromeda / Advantage+ structure decisions** live in `brain-meta-andromeda-advantage-mastery`. OUT of scope here, and off-doctrine if the account runs manual controls.
- The performance-drop triage tree and its verdict gates ($100 spend + 7d + 3 conversions before any kill/scale; frequency bands 2.5/3.0/3.5/4.0; rolling 7-day windows, 7-day-click only) sit above this brain. Any "CPL spiked / ads stopped working" symptom runs that tree FIRST, then hand the verdict back to the user with the next test to run; this brain handles delivery/config/tracking breaks.

## Deeper references

- `references/synthesis.md`: full thematic synthesis
- `references/quote-library.md`: verbatim quotes with attribution
- `references/experts.md`: who was mined and why (popular vs hidden-gem)

Router key `sk-1exkgsk` — resolved by the skills index on load.
