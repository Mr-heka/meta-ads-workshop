# Playbook — Meta Ads Manual Media Buying

Lens: AU small-business lead-gen at a modest monthly budget (roughly 2-8k AUD/month). Sources are mostly e-com/ROAS-framed — swap **ROAS → cost-per-lead (CPL) vs a target CPA**. Doctrine: manual control, no ASC/AAC, no Advantage+ Audiences, no auto-targeting reliance. Automation endorsements are flagged as exceptions.

---

## 1. Account structure (manual)

Consolidation is the consensus; fragmentation starves the algorithm.

- **Ben Heath — two-campaign spine + one ad set.** Scaling campaign (proven winners, ~80% budget) + Testing campaign (new creative/offers, ~20%). One cold campaign + one warm campaign, **one ad set each**. "One campaign per product range" so products don't compete in auction. Ads per ad set: "six or fewer... on a small budget, two, three, even one." He long resisted Meta's push to one ad set, now runs it.
- **Charley Tichenor — 1 Campaign Ad Account.** One campaign per business objective, CBO, broad (age/gender/location only — "Broad is a noun, not an adjective"). One Control ad set holding the 4-6 top post IDs; each test ad set = one 3-2-2 DCT organised by concept. Complexity order = campaigns × ad sets × ads (5 vs 1000). "The Ad is a Sales Pitch, the Ad Set is a Salesman, the Campaign is the Manager." Meta "can realistically be managed in under 3-4 hours a week."
- **Nick Theriot — "Advantage+ minus the packaging."** One CBO campaign, one main ad set for winners + rolling DCT ad sets. One campaign per objective/country/collection. Manual sales campaign, age/gender/location only, no interests/LAL/custom since Dec 2022. Run 3-5 ad sets live, test 2-3 new/week. "10-15 minutes a day in the account... the other 7h45 building better ads."
- **Sam Piliero — packs in one prospecting CBO.** Each creative round = new ad set (4-8 creatives) + a separate existing-customer exclusion campaign. Rule of 10,000: 10 new ads/week per $10k/mo.
- **Spencer Pawliw.** Under $1,000/day never more than one campaign. Champions + test batches + offer tests as three ad-set types in one CBO. "There is no ad account structure that will save your bad ads."
- **Blue Sense Digital.** Structure from business economics, not templates. Under $50k/mo: one testing campaign, ad sets = concepts (persona × angle × offer), 3-5 creatives each, exclude existing customers.
- **Naming convention:** `<Platform>_<Concept>_<Audience>_<Format>_<City>_<Month>` e.g. `META_Wedge_Founders_SI_<City>_<Month>`.

## 2. ABO vs CBO

- **Scalability School (cleanest rule):** "If your hit rate of the tests is high enough you can squeeze more with [ABO]. If your hit rate is bad, stick with CBO." The bet: you're right more often than Meta, or at bigger scale. Low budget / low hit rate → CBO.
- **Charley T:** CBO "often the better choice" — the manager moves money to the best salesman automatically. Testing in dedicated ABO wastes ~90% of spend on losers; test inside CBO where ads "earn spend." "Spend is a meritocracy."
- **Nick Theriot:** CBO on, single campaign per objective.
- **Blue Sense:** at scale, CBO with min/max spend limits (~60% controlled / 40% free). Rotate: CBO in Q4 (efficiency), ABO in Q1 (testing).
- **Dara Denney (pre-Andromeda ~2021):** isolated ABO testing, one variable/test — but concedes it suits $20k+/mo; below that, drip creatives into core campaigns.
- **Fedotoff:** "Don't do CBOs just because everyone does... do what works for your account." "Don't abandon a working ABO for the new shiny thing."

## 3. Testing systems

| Framework | Owner | Shape |
|---|---|---|
| 3-2-2 | Charley T | 3 creatives × 2 primary texts × 2 headlines in one Flexible/DCT ad. "Nothing more." |
| Testing by concept | Charley T | concept = one angle; 3-4 iterations × 3-4 DCTs = 10-12 tests of one angle; winners become controls |
| Andromeda 1 / One Campaign 2.0 | Charley T | control ad set + 1-2 test ad sets (each one 3-2-2 flex ad); judge on profit volume; $10k+/mo, collapse below |
| 3222 | Pawliw | 3-2-2 + 2 landing pages; Champions + tests in one CBO |
| Packs | Piliero | new ad set per round in prospecting CBO, 4-8 creatives, min = 1x CPA, remove after 7 days; $3-10k+ |
| Main ad set + rolling DCTs | Theriot | 1 winners ad set + ≤4 DCTs; 2-3 new/week; 3 photos OR 3 videos each; ~1 in 10 DCTs wins |
| Single-variable ad sets | Denney | dedicated testing campaign, 1 variable, 3-6 ads, broad; $20k+/mo |
| 5×$10 single-variable | Ac Hampton | manual sales campaign, 5 ad sets @ $10/day identical except the video |
| DCT + cost caps | Bottom Line | 4 creatives/DCT, caps as filter, launch everything; mass UGC |

- **Test-capacity (Pawliw):** daily budget ÷ target CPA = simultaneous tests. $100 ÷ $20 = 5.
- **Test-budget (Blue Sense):** target conversions × expected CPA ÷ test days. Ignore Meta's "50 conv in 7 days" (= $714/day/test) on small accounts.
- **Theriot testing rules:** one variable per test ("same hook, different visual" / "same video 3× with a 3-second difference"); never mix photos and videos in one DCT; copy = 2 primary texts + 2 headlines, "one new and one winner."
- **Heath judging thresholds:** ~5,000 impressions before any ad decision; 50-100 conv/variation for ecom conclusiveness; 3-7 days to judge an ad, 3-6 months a strategy; run a stat-sig calculator before declaring A beats B.
- **Charley T philosophy:** "We are not testing to find winners to scale and abuse. We are testing to answer one simple question: did this change make the campaign better or worse?" "No matter how good you are, your guesswork will never beat the scientific method."

## 4. Kill / scale

**Kill ladder (pick one):** Hunyor 1x avg CPA @ 0 conv · Denney ~2x account-avg CPA, ad set dead if no winner 5-7 days ("we never turn off an ad set getting good results") · Fogarty 2x AOV · Blue Sense 3x target CPA min (prefers 5x; 0-1 cut, 2 = +$50, 3+ keep) · Theriot cut a new ad at ~0 spend after 3 days · Charley T stop-loss on *lifetime* not a 24h snapshot · ads-master default **3x kill rule** (pause ad set >3x target CPL after 7 days; CTR floor <0.50%; frequency ceiling >5 cold).

**Scale:** Heath +3%/day automated rule, once/day, only under threshold, ~a week between manual jumps; if cost-per-result too high, reduce budget don't pause; expect ROAS to fall as you scale. Theriot +20%/day if 24h on target, -20%/3 days if 3-day avg over; "never decide on current-day performance." Chappell +20% per 3 days. Charley T: improve efficiency first, then raise budget; relaunch top-5 spenders to broad via post IDs. NEVER duplicate campaigns to scale (Heath, Theriot, Charley T — auction overlap, no guarantee $100/day works at $1,000/day).

**Never touch the winner (universal):** Blue Sense — "never touch something that's working... do something next to it." Duplicate via post ID to keep social proof + avoid learning reset (Hunyor "never edit an existing ad... pause and duplicate", Scalability School, Charley T). Post-ID archaeology: old winners still win 7-8/10.

## 5. Budget & bidding — cost caps (the dispute)

- **Anti (our scale):** Charley T (caps + ASC harvest existing demand — "your Facebook ROAS looks good but your bank account doesn't go up"; if used, 10-15%, max 20% of budget) · Blue Sense (no caps under $200k/mo) · Piliero (caps/day-parting only at $100k+) · Pawliw (no caps, no forced minimums — "forcing spend Meta won't fund is ego") · Theriot (caps break — "Facebook blew the whole budget without hitting the cost-per-result goal").
- **Pro for scaling only:** Scalability School gladiators arena (one proven-winner ad set, 7-day click, cost cap; breathes on weekends) · Hunyor (cap at historical avg CPA as a brake).
- **Pro as launch net:** Bottom Line — launch everything, caps 30-50% below actual CPA so day 1 spends zero, inch up every 24-48h. "The only way you lose is out on opportunity."
- **Scaling cadence:** Heath +3%/day; Theriot/Chappell +20% (daily / per-3-days); generic +20-30% per 3-5 days.
- **Scheduling:** launch at **midnight** (Pawliw) or Meta crams the day's budget into remaining hours. Theriot for known peaks: pump budget 2-10x at 12am, "easier to scale back than spend more."
- **Daily budget floor:** Heath ~$10/day/campaign, "afford to lose but care enough to manage." Theriot: "a budget you can spend for 30 days and not be attached to."

## 6. Manual disarming of Meta defaults (the OFF list)

ASC/AAC off — run manual sales (Theriot: Advantage+ "prioritises middle/bottom-funnel, frequency shoots to the roof"; kills ad-set testing) · Advantage+ Audiences off → "switch to original audience" (Theriot: frequency skyrockets, faster burnout) · Advantage+ creative enhancements off (Blue Sense/Hunyor: "Meta ads are not at the level where they can make good ads") · Flexible Ads off for testing (Pawliw/Blue Sense: no per-creative data — but Charley T uses the flexible-ad shell as the 3-2-2 container, different use) · Audience Network off (Hunyor 14%-CTR accidental-click trap) · untick "use as a suggestion" on retargeting lists (Piliero: else Meta broadens your seed) · never edit live ads, duplicate them · schedule launches midnight · keep exclusions manual (exclude existing customers — Meta overspends on them). **KEEP ON:** Advantage+ Placements (Theriot's one kept auto-toggle). **Note: you cannot do both in the ad set.** Unticking Audience Network switches the ad set to manual placements, which turns Advantage+ Placements off. Exclude Audience Network at ACCOUNT level (Business settings > Brand safety and suitability) if you want to keep Advantage+ Placements on.

## 7. Audience / targeting (manual era)

Broad wins once the pixel is trained — "creative is the targeting" (Fedotoff, Hunyor, Denney, Theriot "my creative creates the audience," Charley T). Heath: location/age/language = hard controls, interests = soft suggestions Meta may ignore; test broad vs interests and let the account decide.

Small-account carve-out (contested): Chappell — under $30k/mo you're still training the model, single-interest ad sets still work, all-broad too early is premature. Piliero — day 1 one CBO with 1 broad + 2 niche interest ad sets to steer the pixel toward broad ("find the most niche brand you could target").

Retargeting/exclusions stay manual: Piliero "broad audiences are not for retargeting," untick "use as a suggestion," exclude existing customers. Charley T: exclusions so no one is eligible for >1 retargeting audience. Heath (warm): same ads as cold, no creepy "still thinking about us?" copy; don't exclude best customers, don't target a tiny audience. Lookalikes broadly dead as a primary lever; ~30% of an interest group is mis-assigned (Blue Sense).

## 8. The math

- Consolidation (Heath): learning exit is ~50 optimisation events per ad set per 7 days, so 50 conv/week ÷ 5 ad sets = never learns; ÷ 1 = exits learning.
- Test-capacity (Pawliw): budget ÷ target CPA. Test-budget (Blue Sense): target conv × expected CPA ÷ test days.
- Learning phase = conversion volume not time (Heath). Bottleneck math (Charley T): CPA $500 on $200/day can never leave learning → optimise a cheaper bottleneck event.
- Break-even reframe (Heath): early campaigns are proof-of-concept that fund scale. "Much better to generate a 4x spending a million a month than a 10x spending 10,000 a month." Accept 2-3x / break-even to buy learning volume.
- Attribution: 7-day-click-only once view-through > ~25% (Scalability School); Pawliw's reported 7-10x collapsed to real 2-3x; Heath — in-platform understates LTV, overstates retargeting. Charley T PSM (profitable scaling margin) over raw ROAS — "ROAS is a lie to begin with," but attribution is consistent enough for trend direction.
- Diagnostics (Heath, decisions on CPA/CPL only): hook rate = 3-sec plays ÷ impressions (>10% good, <5% poor; Hunyor benchmarks ≥25% ecom); frequency cold ≤2.5, warm 6-8, hot 10+ ok; good hook + low CTR = weak offer/proof; good CTR + poor conversion = landing page; LP-view vs link-click gap >50% = slow page/junk placement. CPM inflates 20-30%/year — efficiency comes from creative, not knob-turning.

## 9. Contrarian / disputed (both sides)

A. Cost caps — §5. B. Small-account targeting — all-broad vs train-with-interests (§7), the most relevant dispute for a small account. C. ASC/Advantage+ — Theriot against (controlled test), Charley T equaliser, Heath/Fogarty pro for simple accounts, Chappell staged. D. ABO vs CBO — hit-rate/risk vs CBO-default. E. Duplication — ad sets bad / post-ID good. F. Flexible ads — off for testing vs 3-2-2 container vs validated-variations. G. Incrementality (Charley T): automation over-indexes bottom-funnel; "bad ads getting spend is often very good for your business"; judge on profit volume. H. 7-day click — Scalability School uses it on scaling vs Piliero "gone are the days of 7-day click." I. "Good ads work day one" (Fedotoff) vs "expect to lose before you make" (Heath).
