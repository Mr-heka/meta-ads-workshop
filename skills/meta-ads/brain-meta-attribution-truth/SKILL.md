---
name: brain-meta-attribution-truth
description: Use when the user asks "why does Meta show more purchases than my dashboard", "is my ROAS real", "7-day click or 1-day view", "what is incremental attribution", or needs Meta vs CRM reconciliation, view-through, over-reporting, or holdout guidance. Route lift-test and GHL crosswalk execution to brain-meta-attribution-measurement-deep.
metadata:
  type: expert-brain
  topic: "Meta attribution truth (windows, view-through, incrementality, when ROAS lies)"
  aliases: "attribution window, attribution settings, 7-day click, 1-day view, 7-day click 1-day view, click-through window, view-through, view-through attribution, VTA, click vs view, standard attribution, incremental attribution, incrementality, incremental conversions, conversion lift, geo holdout, holdout test, ROAS lies, reported ROAS vs real, over-attribution, over-reporting, why does Meta show more purchases than my dashboard, Meta vs CRM mismatch, Ads Manager honest reading, compare attribution settings, MER, blended ROAS, IROAS, cost per lead vs cost per client, causation vs contribution"
  domain: attribution
  built: "2026-07-06"
  sources: 15
---

# Brain: Meta attribution truth (windows, view-through, incrementality, when ROAS lies)⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

> Built by topic-brain-builder from 15 YouTube sources
> (7 hidden-gem creators surfaced on engagement,
> not views). Made by Selr AI.

## How to use this brain

**Load this file's full text before answering.** When the user is working on Meta attribution truth (windows, view-through, incrementality, when ROAS lies), load this brain first. Ground answers in
the synthesis below and cite experts by name from the quote library. Prefer the
consensus view; surface a contrarian take when it's well-argued.

## What the experts agree on

1. **The default is 7-day click / 1-day view, and beginners should leave it.** Tazkeer, Denney, Gan, Stenton, Parrottino. Only change it once the Compare Attribution Settings column shows a real gap. (The full menu of settings is below; it is wider than these two.)
2. **Platform attribution can over- or under-state your real business impact; reconcile against CRM revenue.** Reported ROAS is directional, never truth. The usual direction is over-reporting, and it is what all 13 usable sources warn about: Denney and Shiver both, "Facebook will credit more of the results that it had a hand in than the actual sales it made"; Parrottino, it "assumes causation, not contribution." But the arrow reverses whenever revenue is invisible to the pixel — recurring subscriptions, LTV beyond the window, phone and DM closes, a second storefront (Heath's £58k unreported; CTC's YouTube studies reading above platform-reported). Never assume a direction. Put the platform number next to the CRM number and let the gap tell you which way it points this month.
3. **Shortening the click window loses real sales AND starves learning.** Gan: 10 conversions, only 3 in day one, you lose 7 the business still made and the campaign goes blind to them. Carve-out (Shiver): 1-day click is fine only for sub-$20 impulse ecommerce.
4. **Incrementality is the real question: would this conversion have happened anyway?** Stenton (lemonade stand: 14 sales, only 4 incremental), Parrottino, CTC, Rosewater. Meta's Incremental Attribution setting is a real model that predicts ad-caused conversions.
5. **Every platform over-attributes, so the honest scoreboard sits outside the platform.** Parrottino names Google, TikTok, Snapchat, Pinterest, Klaviyo. For lead-gen the CRM is truth (Stewart, Shiver); for ecommerce it is blended MER (Parrottino).
6. **Read the account on primary metrics only; the rest is "why".** Denney: decide on spend, purchases/CPL, cost per purchase, ROAS; CTR and hook rate explain, never decide. Analyse first, tweak second.
7. **View-through is where the number inflates hardest.** Tazkeer calls 1-day view "more dangerous" than click because there was zero interaction with the ad. (Whether to run it is contested, see below.)

## Named frameworks & methods

- **Compare Attribution Settings (the free read)** - Tazkeer, Piliero, Shiver, Stenton, CTC. Ads Manager > Columns > Compare Attribution Settings > tick 7-day click + 1-day view + Incremental Attribution > Apply. Surfaces all three side by side without changing your optimisation setting. This is the single most-endorsed move in the brain.
- **The full attribution setting menu.** Ads Manager exposes more than the famous two. At ad-set level you choose a **click window of 1 or 7 days**, optionally **1-day view**, and optionally **1-day engaged-view**; **Incremental Attribution** sits alongside them as a separate selectable setting. So the realistic options are: 1-day click; 1-day click + 1-day view; 7-day click; 7-day click + 1-day view (the default); any of those plus engaged-view; or Incremental Attribution. The reporting-only **Compare Attribution Settings** column shows several side by side without changing what the ad set optimises for — always read before you change.
- **1-day engaged-view, explained properly.** This is the video-specific window, and it is the setting people tick without knowing what it does. It credits a conversion within 1 day when the person **watched at least 10 continuous seconds of your video ad, or watched 97% of it if the video is shorter than 10 seconds, and did not click.** It sits between a click and a plain 1-day view: stronger evidence than a thumb-stop impression, weaker than a click. Two practical consequences. First, it only ever applies to video ads, so turning it on changes the reported numbers of your video ad sets and leaves image ads untouched — which quietly makes video look better than image in the same comparison. Second, because it needs no click, it inflates lead counts in exactly the businesses where 1-day view already does (booked calls, DMs). Rule of thumb: if you have turned 1-day view off for honesty, leave engaged-view off too, then turn it on only as a deliberate experiment when video is genuinely your main format and you have decided you want that signal in the optimisation. Sources here are thin on it (only Shiver and Thompson mention it, both deferring to "case-by-case on volume"), so treat any confident claim about it, including this one, as reasoning rather than tested consensus.
- **Incremental Attribution (IA)** - an ad-set-level **model**, rolled out ~April 2025. Meta describes it as a modelled estimate of which conversions were actually caused by the ad, informed by the results of its own lift studies and experiments. It is **not** a continuous holdout running invisibly on your account: your ad set is not being split into control and treatment groups in the background. Read IA as "Meta's best model of causation", which is a genuinely useful second number and still Meta marking its own homework. Real gaps: Piliero 15.77 ROAS vs 2.85 incremental; Stenton 4.8x vs 2.4x (half); Shiver "a fourth to maybe a third" of standard volume; Tazkeer 426 vs 423 leads (tiny for lead-gen). Meta's own claimed lift: 24% (Piliero) / 46% across 37 studies (Rosewater). Currently supports highest-volume bidding only.
- **Geo-holdout + discount factor (CTC)** - run media in one geo, withhold in another, measure the delta. Convert reported to incremental: 7-day-click-1-day-view 2:1 × 0.8 = 1.6 IROAS; a 7-day-click number may need a 1.2x factor because it under-reports. "100% incremental" = holdout matches reported.
- **Turn-down test (Parrottino)** - cut Meta spend 50%. Revenue drops 40% = incremental. Drops 5% = Meta was capturing existing demand, not creating it. Poor-account's holdout.
- **Lemonade-stand incrementality (Stenton)** - 10 sales/day baseline, 14 with a sign; true uplift is 4, not 14. The one-line mental model.
- **CRM crosswalk to cost-per-signed-client (Stewart)** - stitch Facebook + Calendly + GHL + email into one report. Real number = ~$4,700/client vs $4-8k/mo retainer; cost per lead was decoupled from it.
- **Primary vs storytelling metrics (Denney)** - four decision metrics; everything else is context. Plus the breakdown effect: Meta caps profitable-looking ads on purpose because force-feeding them budget lowers total profit.
- **Value-based lead-gen feedback (Heath)** - feed different lead values via different thank-you pages (roofing: $4,000 high-value lead vs $1,000 low-value) so Meta chases quality, not count.

## Contrarian / disputed takes

- **View-through: on or off for lead-gen?** OFF camp: **Shiver** (turn off 1-day view for booked-call/DM businesses; it falsely credits DM-booked calls to scrolled-past ads, >10% inflation on a real account) and **Tazkeer** (it is the more dangerous setting). ON camp: **Caden Thompson** reversed his own year-long 7-day-click-only stance to add 1-day view, because the Andromeda update collapsed full-funnel creative into one ad set and the algorithm needs view signal. He concedes the risk: if returning revenue is ~30%+ of AOV it over-prioritises warm buyers. **For our lead-gen model the OFF weight wins**, consistent with our verified base (strip to 7-day-click-only once view-through > ~25% of conversions).
- **Trust Meta's IA setting for optimisation now, or read-only?** Adopt-with-a-test camp: **Piliero, CTC, Rosewater** (dip in via the compare column, validate with a lift test, switch once it beats business-as-usual). Read-only-for-now camp: **Shiver** ("for 99% of people, I'm still encouraging the standard attribution") and **Stenton** (April 2025: "it is just a data point"), because IA cuts your optimisation events and can starve learning at low volume.
- **Does the click-vs-view debate even matter?** **CTC's strongest contrarian line:** "7-day click one day view over reports the impact and 7-day click under reports the impact. But it doesn't really matter" - what matters is knowing your discount factor and holding the setting constant, not which window you pick.
- **Does reported ROAS always over-state?** Mostly yes, but **Heath** shows the opposite for recurring revenue: Hyros tracked £96k, £58k unreported by Meta, because Meta only saw the first transaction. CTC's YouTube studies also read 3.76x *above* platform-reported. Under-reporting is real when LTV/recurring/cross-storefront revenue is invisible to the pixel.

## Execution playbook

### IF / THEN operating rules
- **IF setting up a new lead-gen ad set** THEN keep 7-day click, and for a booked-call or DM-led model turn 1-day view OFF (Shiver) and leave 1-day engaged-view off with it. Leave the click window at 7 days, never shorten it (Gan).
- **IF someone asks "why does Meta show more leads than GHL?"** THEN it is standard attribution pulling in view-through and cross-channel conversions. Open Compare Attribution Settings, add Incremental Attribution, and read the gap before touching anything (Tazkeer). Also check the lead-math trap: Meta insights "actions" double-counts leads (lead + lead_grouped + fb_pixel_lead + custom). Compute CPL from action_type=='lead' ONLY.
- **IF reported ROAS or CPL looks too good to be true** THEN read the incremental column. If incremental is a small fraction of standard, the ad is harvesting existing demand, not creating it (Piliero: 15.77 vs 2.85).
- **IF tempted to shorten the click window to "clean up" reporting** THEN don't. You lose real sales from the count and starve the algorithm's learning (Gan). Only exception is sub-$20 impulse ecommerce, which is not us (Shiver).
- **IF you want to know the true number and have the spend** THEN run a geo-holdout or a turn-down test (cut 50%, watch the drop) and derive a discount factor; apply it to reported ROAS from then on (CTC, Parrottino). At our spend, prefer the compare-column read and CRM reconciliation over a formal holdout (defer deep holdout mechanics to the sibling deep brain).
- **IF you switch to Incremental Attribution for optimisation** THEN expect in-platform ROAS to drop, that is correct not broken (CTC), and validate against a lift test or CRM before trusting it. For now, most voices say read IA, keep optimising on standard (Shiver, Stenton).
- **IF you change any attribution setting** THEN change it once and hold it. You cannot build a measurement system while moving the setting (CTC). Changing it live also resets learning; duplicate the ad set instead.
- **IF making a kill/scale decision** THEN decide on primary metrics only (spend, CPL/purchases, cost per result, ROAS). CTR and hook rate explain why, they never decide what (Denney, and our verified base via Heath).

### Default numbers experts use
- Windows: the click window is **1 or 7 days**; **1-day view** and **1-day engaged-view** are separate optional adds; **Incremental Attribution** is its own setting. **7-day click / 1-day view** is the default; **7-day click only** is the honesty setting for lead-gen once view-through gets large.
- Engaged-view qualifies at **10 continuous seconds of video**, or **97% of a video shorter than 10 seconds**, with no click, credited within 1 day. Video ad sets only.
- View-through as a red flag: **>25% of conversions from view-through** = strip to 7-day-click-only (verified base). Shiver saw **>10%** of booked calls from 1-day view on a DM campaign.
- IA vs standard volume: incremental is typically **a quarter to a third** of standard conversions (Shiver); expect roughly **half the ROAS** (Stenton).
- Discount factors (CTC): 7-day-click-1-day-view ≈ **×0.8**; 7-day-click ≈ **×1.2** (it under-reports).
- Turn-down test (Parrottino): 50% spend cut. **~40% revenue drop = real**, **~5% = capturing demand**.

### Pre-flight checklist (before answering any attribution question)
1. Is the pixel/CAPI actually firing correctly and not double-firing? A pixel bug fakes the whole picture (Shiver: 8 reported calls, 2 real).
2. Which attribution setting is the account on right now, and is view-through on?
3. Read the Compare Attribution Settings column: standard vs incremental gap.
4. What does the CRM (GHL for us) say for the same window? Reconcile, do not conflate.
5. Are we deciding on primary metrics, or getting distracted by storytelling metrics?

### Top 5 failure modes and the fix
1. **Trusting reported ROAS/CPL as truth.** Fix: treat it as directional; read the incremental column and the CRM (all sources).
2. **Optimising to the wrong event (lead, not client).** Fix: crosswalk to cost-per-signed-client / cost-per-community-member; Meta can only optimise for what you feed it (Stewart).
3. **Shortening the click window to make numbers "cleaner".** Fix: keep 7-day click; you are throwing away real, ad-caused sales and learning signal (Gan).
4. **Letting view-through inflate lead counts.** Fix: turn 1-day view off for our model; audit the view-through share (Shiver, Tazkeer).
5. **Changing the attribution setting mid-campaign to chase a better-looking number.** Fix: pick one, hold it constant, layer a periodic incremental read on top (CTC).

## Applied to your business

Fill these in first: ad account `<YOUR_AD_ACCOUNT_ID>`, pixel `<YOUR_PIXEL_ID>`, source of truth `<your CRM or payment processor>`, monthly ad spend `<your monthly spend>`, target cost per lead `<your target CPL>`, target cost per sale `<your target CAC>`.

**Which of your offers this feeds.** Whichever offers you actually run paid traffic to. For a lead-gen or booked-call business the job is reading CPL honestly; for a checkout offer it is reading ROAS honestly. If your scoreboard is a CRM rather than a storefront, you are the case Stewart and Shiver describe, not the ecommerce case most of the other sources describe — weight their advice accordingly.

**Consensus translated into execution moves:**
1. **Keep 7-day click; turn 1-day view OFF on lead-gen ad sets**, and leave 1-day engaged-view off with it. If your conversions are form-fills, calls or DMs rather than impulse buys, Shiver's rule fits: view-through credit inflates your lead count and makes CPL look better than it is.
2. **Read the account with Compare Attribution Settings on every campaign review.** Add the Incremental Attribution column so the modelled ad-caused number sits beside the reported one. For lead-gen the gap is often small (Tazkeer's 426 vs 423), but verify it in your own account rather than assuming.
3. **Reconcile Ads Manager against your CRM; never conflate them.** The reported CPL is the optimisation dial. The real number is the sales, seats or members that appear in `<your CRM>` against spend. Build the cost-per-real-outcome view the way Stewart wired cost-per-signed-client. Confirm your conversion events are actually firing before you trust either side of that comparison.
4. **Hold the attribution setting constant.** Pick it once, then leave it. Do not flip it to make a soft month look better (CTC). Changing it also resets learning and destroys month-to-month comparability; duplicate the ad set instead.
5. **Decide on primary metrics only.** Spend, CPL, cost per sale and ROAS decide. CTR, hook rate and frequency explain why. That is what keeps kill/scale calls disciplined (Denney).

**What may NOT apply to you:**
- **Formal geo-holdouts and the discount-factor maths (CTC).** Powerful, but they need volume and multi-region spend. Below roughly `<the spend level where you run several regions at once>`, use the turn-down test as a cheaper proxy; deep small-spend incrementality belongs to the sibling deep brain.
- **Multi-storefront / identity-resolution measurement (CTC "Starving Giants," Amazon + .com).** Irrelevant on a single channel into one CRM; there is no second storefront to under-count.
- **Third-party attribution tools (Triple Whale, Northbeam, Hyros).** Denney's ruling: unnecessary unless you run several paid channels at once. On one channel, your CRM is the source of truth. Do not buy the tool.
- **Ecommerce ROAS bid strategies and recurring-revenue under-reporting (Heath's Hyros case).** If your recurring offer is sold warm rather than by cold paid ads, Meta never reports on it anyway. The under-reporting concern bites when you run cold paid traffic straight at a subscription.
- **Advantage+ / IA-driven automation as a default.** If your campaigns are manual by policy, IA is a reading tool, not a switch to flip.

## Related brains

- `brain-meta-ad-to-page-congruence` - Meta ad to page congruence (message match, the relevance chain, per-angle variants)
- `brain-meta-website-and-engagement-audiences` - Meta website and engagement audiences (pixel segments, video views, engagers, recency)
- `brain-post-click-tracking-plumbing` - Post-click tracking plumbing (UTMs, fbclid, cross-domain, thank-you events, lead source to CRM)

## Pairs with / boundaries

- **`brain-meta-attribution-measurement-deep`** (P5) owns the hands-on layer: running practical incrementality tests at small spend and reconciling Meta against the CRM step by step. This brain surveys the concepts and points there; do the actual holdout/geo-lift or GHL crosswalk build in the deep sibling.
- **`brain-post-click-tracking-plumbing`** owns UTMs, fbclid, cross-domain, thank-you events and lead-source-to-CRM wiring. If the question is "is the data even arriving correctly" (pixel/CAPI firing, double-fires, event mapping), that is plumbing, not attribution truth.
- **`brain-meta-ads-manual-control-no-advantage`** owns the campaign structure, settings kill-list, and kill/scale rules. This brain only covers how to *read* the resulting numbers honestly, not how to build or bid the campaign.
- **Out of scope here:** setting up the pixel/CAPI, choosing bid strategy, building audiences, and formal geo-holdout execution. This brain is the "is this number real and which window do I use" survey only.

## Deeper references

- `references/synthesis.md` - full thematic synthesis
- `references/quote-library.md` - verbatim quotes with attribution
- `references/experts.md` - who was mined and why (popular vs hidden-gem)

Router key `sk-8e92a3` — resolved by the skills index on load.
