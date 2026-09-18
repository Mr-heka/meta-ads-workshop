---
name: brain-meta-media-buyer-manual
description: "Use when the user asks how to structure, budget, test, kill, or scale manual Meta campaigns, or about CBO vs ABO, the learning phase, campaign consolidation, or manual-control and Advantage+ settings. Route hooks and concepts to brain-meta-creative-strategist-manual and total spend sizing to brain-paid-media-planning-and-forecasting."
metadata:
  type: expert-brain
  topic: "Meta ads — manual media buying (structure, testing, scaling, math)"
  domain: ads
  aliases: "media buying, media buyer, Meta ads, Facebook ads, FB ads, IG ads, Instagram ads, campaign structure, CBO, ABO, ad set, learning phase, kill rules, scaling ads, ad budget, DCT, 3-2-2"
  angle: "media-buyer / operator"
  built: "2026-07-01"
  lens: "AU small-business lead-gen, 2-8k AUD/month"
  companion: brain-meta-creative-strategist-manual
  evidence_base: brain-meta-ads-manual-control-no-advantage
---

# Brain: Meta Ads — the Manual Media Buyer⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

> One of two companion brains. This is the **operator / media-buyer** angle: how the
> account is built, tested, budgeted, and scaled BY HAND. The sister brain
> [[brain-meta-creative-strategist-manual]] covers the creative that does the
> targeting. Shared evidence lives in
> [[brain-meta-ads-manual-control-no-advantage]]. Made by Selr AI.

> **STALE-SETTINGS WARNING — re-verify against the live UI before you click anything (flagged 2026-07-28).**
> The settings walkthrough in this brain (the kill-list below, "Advantage+ Audiences off, switch to original audience", and the interest-targeting strategy) was written against the pre-2026 Ads Manager. Two things changed underneath it: Meta **merged the manual and Advantage+ campaign creation flows in early 2026**, so the two are no longer separate paths with separate toggles; and **deprecated detailed-targeting interests stopped delivering on 15 January 2026**.
> Some options named here have moved, been renamed, or no longer exist. The *strategy* still holds: consolidate, judge on cost per result, creative is the targeting, never disturb a winner. The *click-by-click settings do not*. Open Ads Manager, confirm each setting actually exists where this brain says it does, and where a toggle is gone, follow the intent rather than hunting for a checkbox.

## How to use this brain

Load this when the task is media buying: structure, budgets, testing plans, learning
phase, kill/scale decisions, the math. Ground answers in the synthesis below and cite
experts by name. Prefer the consensus; surface a contrarian take when it's well
argued. The lens is **small-business lead-gen at a modest monthly budget (roughly 2-8k AUD/month)** — the sources are mostly
e-commerce/ROAS-framed, so **swap ROAS for cost-per-lead against a target CPA**.
Deeper material: `references/playbook.md` and `references/quote-library.md`.

## The doctrine: manual control, Andromeda OFF

We run **manual campaigns**. We do NOT hand the account to Advantage+ Shopping/Sales/App
(ASC/AAC), Advantage+ Audiences, or the advertiser-level Advantage+ defaults. Automation
is allowed only where the corpus agrees it wins: delivery on a broad audience, permutation
matching inside a controlled dynamic-creative ad, and budget routing across proven winners
(CBO). Everything else — structure, test design, exclusions, analysis — is the operator's.

Why, in the practitioners' words:
- **Nick Theriot** ran the set's only controlled same-ads test: **manual prospecting 2.91 ROAS vs identical-ads ASC 2.14**. "Facebook is basically trying to get us to be their guinea pigs with no ad credits to test their specific thing."
- **Charley Tichenor**: ASC "will make a D-minus account a C-plus; if you're great at Facebook it'll make your A-minus account a C-plus." It equalises you DOWN.
- Contrarian pole to respect: **Davie Fogarty** (100M+ spent) says "this Advantage Plus setting is basically all you need" — but that's a 5-20k/DAY e-com whale who wants hands-off. At our scale, manual is the edge.

**Settings kill-list — disarm before every launch** (Blue Sense, Hunyor, Pawliw, Piliero):
ASC/AAC off (run manual sales) · Advantage+ Audiences off → "switch to original audience" · Advantage+ creative enhancements off · Flexible Ads off *for testing* · Audience Network off (Hunyor's 14%-CTR junk-click trap) · untick "use as a suggestion" on retargeting lists · never edit a live ad (duplicate it) · schedule launches for midnight. The one auto-toggle Theriot KEEPS on: **Advantage+ Placements**.

> **Placement note: "Advantage+ Placements on, Audience Network off" is not possible at ad-set level.** Unticking any surface (Audience Network included) switches that ad set to **manual placements**, which turns Advantage+ Placements off. If you want Advantage+ Placements on AND Audience Network out, set an **account-level placement exclusion** (Business settings > Brand safety and suitability), once, for the whole account. Otherwise pick one: Advantage+ Placements as-is, or manual placements with the surfaces you want. Do not go looking for an ad-set checkbox that does both.

## What the experts agree on

1. **Consolidate, don't fragment.** Conversion data silos per ad set. Meta's stated learning-phase exit is **~50 optimisation events per ad set per 7 days**: 50 conversions through ONE ad set exits learning; the same 50 split across five ad sets (10 each) never does. Small account = one offer, one campaign, one (or very few) ad sets. (Heath, Charley T, Theriot, Pawliw, Blue Sense.)
2. **The learning phase is conversion VOLUME, not time** — and every significant edit resets it (~48h). Set a fixed optimisation schedule; on a small budget touch nothing more than once every 7-10 days. Heath: "Don't helicopter parent your ad campaigns."
3. **Kill/scale on CPA/ROAS (for us, cost-per-lead) ONLY.** CTR, CPM, hook rate, frequency *diagnose why* — they never decide what dies. (Heath, Charley T, Blue Sense.)
4. **Never touch what's working.** "Do something next to it. Don't ruin the thing that's working." (Blue Sense.) Duplicate a winner **via post ID** — keeps social proof, no learning reset (Hunyor, Scalability School, Charley T).
5. **Broad is the audience; the creative is the targeting.** Age/gender/location as hard controls, interests as soft suggestions Meta may ignore. Lookalikes/interest stacks are dead as primary levers post-Andromeda. (Fedotoff, Hunyor, Theriot, Charley T, Heath.)
6. **Scale by improving efficiency first, then nudge budget** (+3%/day Heath, or +20% per 3-day Theriot/Chappell) — never shock the machine, never duplicate campaigns to scale (auction overlap).
7. **You're not smarter than the machine on delivery — you're smarter on structure and creative.** Charley T: "Andromeda is really smart. And it only stays smart if we don't spend all of our time and energy keeping it stupid."

## Named frameworks & methods

- **1 Campaign Ad Account** (Charley T): one campaign per business objective, CBO, broad only, one Control ad set of the 4-6 top post IDs + test ad sets. Complexity math: 1×1×5 = order 5 vs 10×10×10 = 1000. "It's far easier to win in 1 place."
- **Two-campaign spine** (Ben Heath): Scaling campaign (winners, ~80% budget) + Testing campaign (new, ~20%); each one cold + one warm, **one ad set each**. The ad-count figure attached to this framework is **≤6 ads (2-3 or even 1 on small budgets) — that is the PRE-ANDROMEDA number and Heath himself now calls it obsolete.** Current post-Andromeda guidance is many more genuinely distinct ads per ad set (Heath now says 20+); see `brain-meta-andromeda-advantage-mastery`. Use ≤6 only as a floor set by your real production capacity, not as a ceiling.
- **3-2-2 Method** (Charley T): one Flexible/DCT ad = 3 creatives × 2 primary texts × 2 headlines. "Nothing more than that." A *concept* gets 3-4 iterations across 3-4 DCTs = 10-12 tests of one angle.
- **Packs** (Sam Piliero): each creative round = a new ad set in one prospecting CBO (4-8 creatives), ad-set minimum = 1x target CPA, hard removal after 7 days. Plus a separate existing-customer exclusion campaign. "Rule of 10,000": 10 new ads/week per 10k/month.
- **3222** (Spencer Pawliw): 3-2-2 plus a **2 landing-pages** variable in one CBO; Meta crawls and ranks your LPs for free.
- **One main ad set + rolling DCTs** (Nick Theriot): 1 winners ad set + up to 4 DCTs, 2-3 new DCTs/week, 3 photos OR 3 videos per DCT, one new idea each. "About one out of 10 DCTs takes majority of spend and performs."
- **Hit-rate rule** (Scalability School): ABO if your test hit rate is high (you beat Meta more often than not); CBO if hit rate is low or the budget is small.
- **Gladiators arena** (Scalability School): one scaling ad set, all proven winners, 7-day click, cost cap — breathes up on weekend demand, throttles midweek.
- **Test-capacity formula** (Pawliw): daily budget ÷ target CPA = simultaneous tests you can afford. $100/day at $20 CPA = 5. (At a modest monthly budget with lead-gen CPL targets in the $10-20 range: 2-9 tests.)
- **Spend-tier ladder** (Piliero/Chappell): under ~$3k/mo = one CBO, broad + 2 niche interests; under $30k = manual interests + structured testing still work; caps/day-parting only earn their place at $100k+.

## Kill / scale rules (pick one ladder, stick to it)

- **Kill:** Hunyor 1x avg CPA spent with zero conv (cheapest) · Denney ~2x account-avg CPA / ad set dead if no winner in 5-7 days · Fogarty 2x AOV · Blue Sense 3x target CPA min (0-1 conv cut, 2 = +$50, 3+ keep) · Theriot cut a new ad that gets ~0 spend in 3 days ("great ads take off within 48 hours"). A sensible default: **3x kill rule** — pause any ad set >3x target CPL after 7 days.
- **Scale:** efficiency first, then budget. Heath +3%/day (automated rule, once/day, only when under threshold, ~a week between manual jumps). Theriot +20% per day if 24h CPA on target / -20% per 3 days if 3-day avg over — "slow is fast." House override (Neiman, canonical): +20% max every 3-4 days, verdicts on rolling 7-day windows only, never a 24h read; no verdict under $100 spend + 7d + 3 conversions. NEVER duplicate campaigns to scale.
- **Winner care:** never edit a live winner; duplicate via post ID. Post-ID archaeology (Scalability School): a 1-2 year-old winner still wins 7-8/10 times.

## Contrarian / disputed takes

- **Cost caps:** anti at small scale (Charley T, Blue Sense, Pawliw, Piliero, Theriot — under $200k/mo skip them) vs pro-for-scaling-only (Scalability School's gladiators arena, Hunyor as a brake) vs pro-as-launch-net (Bottom Line: caps 30-50% below actual CPA, inch up every 24-48h). A sensible default: skip caps; if you want a brake, cap only a proven-winners ad set.
- **Small-account targeting:** all-broad now (Fedotoff, Hunyor, Theriot, Charley T) vs still-train-with-interests under $30k (Chappell) / 1 broad + 2 niche day one (Piliero). Most relevant disagreement for us.
- **ABO vs CBO:** no doctrine — a hit-rate/risk bet (Scalability School, Blue Sense) vs CBO-default (Charley T, Theriot).
- **Duplication:** duplicating **ad sets to scale** = bad (Heath, Theriot, Charley T) vs duplicating a **winning ad via post ID** = good (Hunyor, Scalability School).
- **Attribution:** move to 7-day-click-only once view-through > ~25% (Scalability School); Pawliw saw reported 7-10x ROAS collapse to a real 2-3x. Judge on profit volume / true CPL, not per-ad in-platform numbers (Charley T: "ROAS is a lie to begin with").

## Execution playbook

Operating rules:
- IF launching a new account or offer THEN one campaign, one or very few ad sets, broad audience with age/gender/location controls only (per Ben Heath, Charley Tichenor, Nick Theriot)
- IF an ad set runs over 3x target CPL after 7 days THEN pause it (per Blue Sense Digital, a sensible default)
- IF an ad is working THEN never edit it live; duplicate via post ID next to it (per Máté Hunyor, Blue Sense Digital, Scalability School)
- IF a winner earns more budget THEN raise +3%/day (per Ben Heath) or +20% steps (per Nick Theriot); never duplicate campaigns to scale (per Heath, Theriot, Charley Tichenor)
- IF a new ad gets near-zero spend in 3 days THEN cut it, "great ads take off within 48 hours" (per Nick Theriot)
- IF CTR, CPM or hook rate look ugly but CPL is on target THEN keep running; those metrics diagnose, only CPA/CPL decides (per Ben Heath, Charley Tichenor)
- IF sizing a test plan THEN daily budget ÷ target CPA = simultaneous tests you can afford (per Spencer Pawliw)
- IF your test hit rate is high THEN ABO; low hit rate or small budget THEN CBO (per Scalability School)
- IF view-through share passes ~25% THEN switch to 7-day-click-only attribution (per Scalability School)

Defaults: 3x target CPL kill after 7 days (Blue Sense, a sensible default); scale +3%/day (Heath) or +20% per 3 days (Theriot/Chappell); ~5,000 impressions before judging an ad, 3-7 days per ad, testing ~20% of budget (Heath); learning-phase exit ~50 optimisation events per ad set per 7 days (Meta); ads per ad set: ≤6 is the pre-Andromeda number, current guidance is 20+ genuinely distinct ads, capped by what you can actually produce (Heath, post-Andromeda); 2-3 new DCTs/week, 3 photos OR 3 videos each (Theriot); touch the account no more than once per 7-10 days on small budgets; launch at midnight (Pawliw); frequency ceiling ~2.5 cold (Heath).

Pre-flight:
1. Kill-list disarmed: ASC/AAC off, Advantage+ Audiences off, creative enhancements off, Audience Network out; keep Advantage+ Placements on (Theriot). Remember the two cannot both be done in the ad set: exclude Audience Network at **account level** or accept manual placements (see the placement note above).
2. One campaign per objective; existing customers excluded manually (Charley Tichenor, Piliero).
3. Target CPL and the kill rule written down before a dollar is spent.
4. Test capacity sized: daily budget ÷ target CPL (Pawliw).
5. Naming convention applied; launch scheduled for midnight (Pawliw).

Failure modes:
- Fragmenting conversion data across many ad sets so learning never exits: consolidate to one (Heath).
- Editing a live winner and resetting learning: pause it, duplicate via post ID instead (Hunyor).
- Killing ads on CTR/CPM/hook rate: decide on CPA/CPL only, use the rest to diagnose (Heath, Charley Tichenor).
- Shock-scaling or duplicating campaigns for budget: small daily steps, "slow is fast" (Heath, Theriot).
- Helicopter-parenting: every significant edit resets learning ~48h, so hold a fixed optimisation schedule (Heath).

## Applied to your business

Feeds: whichever offers you actually put cold paid traffic behind. Write the ladder down with real numbers before applying anything below: front-end offer `<your offer price>`, any lower-priced entry offer, the recurring or membership offer every front-end feeds, and the high-ticket engagement bigger buyers route into. Note your real monthly ad spend (`<your monthly ad spend>`), because most thresholds in this brain are spend-gated. This brain governs how those lead-gen campaigns are structured, tested and scaled at the small-budget tier (roughly 2-8k/month).

Moves:
- Run lead-gen as ONE manual sales campaign, one ad set, broad with location and age controls (Heath/Tichenor/Theriot consolidation). No campaign-per-location fragmentation while conversion volume is thin.
- Set `<your target CPL>` backwards from `<your offer price>` and your real close rate, then write the 3x-CPL 7-day kill rule into the campaign doc before launch (Blue Sense default).
- Size this month's testing with Pawliw's formula: daily budget ÷ target CPL. At 2-8k/month that is roughly 2-9 simultaneous tests; feed them as 2-3 new DCTs per week (Theriot), one variable each.
- Duplicate proven ads via post ID so comments and social proof compound across cycles (Hunyor, Scalability School); never edit the live winner mid-flight.
- Optimise on a lead/registration event, not the purchase, when the purchase is expensive. Tichenor's bottleneck math: a `<your offer price>` purchase event on `<your daily budget>` will not produce ~50 events a week, so buy volume on a cheaper conversion further up the funnel.

Does not apply at small spend:
- Davie Fogarty's "Advantage+ is basically all you need": that is a 5-20k/DAY e-commerce posture. At small spend with a considered offer, manual control is the edge this brain argues for.
- ROAS and AOV kill ladders (Fogarty 2x AOV, e-commerce ROAS targets): if you sell services, events or memberships, judge on cost-per-lead against `<your target CPL>` instead.
- Cost caps and day-parting (Bottom Line's launch nets, Piliero's $100k+ tier): the corpus itself says they only earn their place far above 2-8k/month.

## Deeper references

- `references/playbook.md` — the full operator playbook (all nine areas, every threshold).
- `references/quote-library.md` — verbatim quotes with attribution.
- Shared evidence: see `brain-meta-ads-manual-control-no-advantage`.

Router key `sk-1eyr0pg` — resolved by the skills index on load.
