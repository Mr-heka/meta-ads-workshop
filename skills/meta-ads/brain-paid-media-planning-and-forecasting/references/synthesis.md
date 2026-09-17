# Synthesis - Paid media planning and forecasting (the CFO layer)

Built 2026-07-06 from 11 usable mined transcripts. Topic: how much to spend per event/launch, working backward from a CAC target and offer price, the CAC/show-rate/close-rate chain to a booked cost, budget pacing across a campaign window, small-budget planning, forecasting leads and sales from spend, and when to scale.

Context lens: AU small-business advertiser running manual Meta campaigns at roughly $50-90/day per event, offer prices from a few hundred dollars to low thousands, with a CAC target per seat. Nearly every source is e-commerce or local-service framed. Transferable unit for an event model: swap "purchase" for "booked seat" and "AOV" for "seat price plus the lifetime path behind it".

One source (ElenIQ, lead-gen forecasting demo) had no transcript and is excluded. All 11 remaining sources are usable, none are era-flagged, none flagged thin.

---

## Theme 1 - Budget is derived backward from a goal, never picked as a number (CONSENSUS, strongest in the set)

Every practitioner rejects "how much should I spend" as the wrong opening question. The right one is "how many sales/jobs/seats do I want, and what does the math say that costs".

- **Michael Tracey**: "the first question should be really how many jobs do you want this month", then work backward through close rate and cost per lead.
- **Nick Boddington**: three-step process, goal and conversion event first, then a conservative expected cost per result, then how many ad sets you actually run.
- **Rich From Anywhere**: reframes from "how much should I spend" to "how much can I afford to spend" based on profit-per-sale economics.
- **Ads Daddy**: start from sale price and margin to get break-even CAC before any spend number.
- **DoneMaker**: "If you don't know the numbers, you can't do the math." Revenue goals are fiction without the at-bat funnel numbers.

Concrete: Tracey's worked example, 10 roof jobs wanted, 10% close rate = 100 leads needed, at £10 CPL = £1,000 ad spend. Consensus, no dissent.

## Theme 2 - The working-backward chain: offer price to break-even CAC to minimum spend

Two named, reusable formula families sit under Theme 1.

- **Ads Daddy's break-even CAC**: sale price minus cost of goods = gross margin = break-even CAC, and break-even ROAS = price / margin. Worked: $50 price, $10 COGS = $40 margin = $40 break-even CAC and 1.25 break-even ROAS.
- **Ads Daddy's 1%/1% rule** for minimum test spend: assume 1% CTR and 1% conversion, need to reach ~10,000 people for a valid read. At $10 CPM that is $100 minimum spend, at $3 CPM it is $30, at $15 CPM it is $150. Improving CTR or CVR cuts the required spend proportionally (double CTR to 2%, halve the minimum).
- **Rich From Anywhere's PPS (profit per sale)**: net profit last year / number of orders = the CAC ceiling. $500,000 / 1,000 orders = $500 PPS, so up to $500 to acquire a customer and stay profitable. Rule: "cost of acquiring your customer should always be less than your profit per sale."
- **Michael Tracey's local-service chain**: jobs wanted / close rate = leads needed, leads x CPL = ad spend. Improving close rate from 10% to 20% halves the leads and halves the spend for the same jobs.

Consensus that the chain exists and runs price to CAC to spend. The formulas differ in surface (margin-based vs profit-per-sale vs close-rate-based) but agree in structure.

## Theme 3 - CAC is a range with a sweet spot, not a single lowest number (CONTESTED nuance)

Most sources treat CAC as a ceiling. Brotherdale pushes further: model CAC as a range and drive *toward* the sweet spot, not minimise it.

- **Brotherdale**: bottom $28, sweet spot $40, high $52 on one client. Below the sweet spot means "leaving meat on the bone" (underspending, missing available customers), above the high means overspending for the same result. CAC is expected to rise as you scale into worse-qualified tiers, and that should not scare you.
- **Ben Heath** aligns on the ratio being the wrong obsession: "Much better to generate a 4x return on ad spend spending a million dollars a month than a 10x return on ad spend spending $10,000 a month." Absolute profit dollars beat the ratio.
- **Rich From Anywhere** cites "the business that can spend the most to acquire a customer wins".

Contested against the tighter instinct in **Nikhil** and **Joly Tematio** to protect a hard CAC ceiling. Nikhil wants purchases below Rs 450 to protect an 8-12% net margin. Resolution: the ceiling protects margin on the front end, the range/LTV view widens the ceiling when backend economics justify it (Theme 4).

## Theme 4 - AOV and LTV are the highest-leverage levers on the budget ceiling (CONSENSUS among the CFO-minded)

Raising what a customer is worth expands allowable spend non-linearly.

- **Brotherdale**: AOV $60 to $90 (1.5x, no second product) shifts the sweet-spot range from $28/$40/$52 to $42/$61/$79, roughly a 33% increase in allowable spend. Levers: in-cart upsells, cross-sell education, community (Discord voting, affiliate programs, events), unboxing activations.
- **Ben Heath**: willingness to pay per conversion is a function of lifetime value and margin, not an arbitrary ROAS target. A $2,000 customer value justifies $500 to acquire (a 4x machine, still profitable); finance/mortgage/insurance run at a loss 6+ months before payback.
- **DoneMaker**: declining ROAS, AOV, or LTV are the trigger metrics that flag a funnel problem.
- **Rich From Anywhere**: backend/LTV upsell is what justifies a breakeven or loss-making front end (his $297 product example nets ~$10K profit plus 192 acquired customers for the backend).

Consensus among the CFO-minded sources. Event translation for us: the seat is a front end for the community and team-training path, so price the ads against the lifetime path, not seat margin.

## Theme 5 - The CAC / show-rate / close-rate chain to a booked cost (CONSENSUS on structure)

The full at-bat funnel is the accountability layer that makes a revenue goal real.

- **DoneMaker** walks it step by step: leads into funnel, how many warm, how many book per week, from bookings how many show, from shows how many get a quote, from quotes the close ratio. Diagnostic questions: current ARR, target date, investors, go-to-market, number of prospects, closing ratio.
- **DoneMaker's 30% close-rate heuristic**: ~30% is healthy; materially higher signals underpricing, "then perhaps you're underpriced, which means you have to go back to the drawing board".
- **Michael Tracey** operationalises the chain for local lead-gen (close rate as the multiplier on leads needed) and stresses improving the sales process can beat raising budget.
- **Joly Tematio** names the bottom-of-funnel checklist that gates scale decisions: opt-in rate, VSL watch rate, scheduling rate, show rate, email open/click rate.

Consensus on the sequence. The specific benchmark numbers (30% close, show rates) are context-dependent and given as heuristics, not laws.

## Theme 6 - Small-budget floors: $5/day buys data, $30-50/day runs a campaign (CONSENSUS)

Strong agreement that there is a floor below which the algorithm cannot generate reliable signal.

- **Jason Hunt**: "$5 to $10 a day... you're not running a campaign. You're buying data." Real consistent lead gen needs "$30 to $50 a day per platform". Facebook needs "at least about 100 actions" before the algorithm knows who to target.
- **Ben Heath**: small budget = under $3,000/month (~$100/day); tiny = $600/month or less (~$20/day). Adjust no more than once every 7-10 days on a small budget.
- **Michael Tracey**: "I wouldn't spend under £25 a day to begin with." Under that, not enough people reached for signal data.
- **Joly Tematio**: $5/day tests are functionally useless. A $50/day advertiser tests 3-4 creatives, ~5 copies, multiple audiences, spending $250/week and reaching confidence far faster than a $5/day advertiser spending $35/week.
- **Nick Boddington**: aim for ~50 optimised actions per week for the algorithm to learn.

Consensus floor is roughly $25-50/day. Our $50/day start sits exactly at the top of that floor, which the sources treat as the real entry point, not the ceiling.

## Theme 7 - Consolidate budget; complexity, not insufficient budget, is the usual failure (CONSENSUS)

Fragmenting a modest budget across too many ad sets/ads starves each of signal.

- **Nick Boddington**: "Increasing budget does not guarantee better results. But consolidating budget always improves performance." His £350/day estimate is *per ad set*; three ad sets means £1,000+/day, so a split £50/day budget can never hit the 50-actions threshold. Fix is fewer ad sets, not more budget.
- **Ben Heath**: 5 ad sets at 20 conversions/week = 4 each (never learns) vs 1 ad set getting all 20 (clears learning faster). One offer, one campaign, one ad set for small budgets.
- **Christian Jamal**: $50 across 50 ads = $1/ad, not enough exposure to judge; conversely $10,000 on one unproven video causes high-frequency fatigue. Balance total vs per-ad budget.
- **Nikhil**: over-segmenting a catalogue into best-seller/new-arrival/t-shirt causes audience overlap and hurts delivery.

Consensus, and it aligns exactly with our verified manual-control base (the Ben Heath consolidation math is cited there too).

## Theme 8 - Per-ad kill thresholds are a multiple of sale price (CONSENSUS on method, numbers vary)

Every source that gives a kill rule ties it to the offer price, so the decision scales with the offer.

- **Ads Daddy**: hard kill at 5x sale price with zero conversions. $250 spent on a $50 product with zero sales = kill.
- **Christian Jamal**: medium risk tolerance = 2.5x sale price per ad as the spend ceiling before shutoff. $250 on a $100 widget with no sale = off. Whole-account formula: ads x ad sets = ad spend / half the sale price.
- **Nikhil**: don't kill on emotion or day one; check learning phase, whether full budget was actually spent, and multi-day CTR trend. Wait 2-4 consecutive bad days.
- **Michael Tracey**: 1-3 days is not enough, especially on a new ad account; let it run and judge on ROI over the month.
- **Christian Jamal**: let it ride 2-3 days before changes, not 2-4 weeks.

Contested only on the multiple (2.5x vs 5x) and the patience window (2-3 days vs weeks). Method is consensus: kill threshold = a multiple of the price, judged on data over multiple days. Our verified base uses 3x target CPL after 7 days on a lifetime view, which sits inside this range.

## Theme 9 - Scale only after proof, gradually, gated on backend economics (CONSENSUS)

Do not start at maximum budget; scale confirmed winners in small steps.

- **Joly Tematio**: be conservative to start, gather data, then scale. Real client moved $1,000/day to $10,000/day once winners were confirmed. The 75/25 rule governs ongoing allocation (75% to proven, 25% to testing); flip to ~80/20 favouring testing from a cold start.
- **Nikhil's pre-scale checklist**: 3+ winning creatives, 5-7 consecutive days of consistent orders, purchases under the CAC ceiling, don't cut after one bad day, only scale if already spending full budget. Scale a winner by 10-20% at a time, never a full re-scale.
- **Ben Heath**: get a campaign profitable (e.g. 4x ROAS) as fast as possible then reinvest.
- **Joly Tematio's scale gate**: bottom-of-funnel economics decide. A $50-70 CPA on a $200 AOV justifies reinvestment; a $500 CPA on a $250 AOV is a red flag (negative ROI).

Consensus. Our verified base already uses +20%/3 days on a 3-day average, never same-day, which matches the "gradual, on averaged data" doctrine.

## Theme 10 - Signal accuracy is a prerequisite for every budget decision (CONSENSUS)

Broken or wrong-event tracking distorts the CAC math before any budgeting is possible.

- **Nikhil**: under-reporting inflates the effective cost the algorithm thinks it needs. 10 real purchases showing as 7 or 5 pushes a Rs 10,000 learning budget to Rs 15,000-20,000. Fix event distribution in Events Manager; split browser-side and server-side (CAPI). Always optimise against the sale event, not proxy events (Add-to-Cart optimisation gave 5,000 ATCs but 2-3 purchases).
- **Joly Tematio**: a missing pixel on non-opt-in funnel pages starves Meta's algorithm and degrades lead quality over time. Track opt-in, VSL watch, scheduling, show, email metrics.
- **DoneMaker**: you can't set a real goal or diagnose scale-readiness without knowing your own conversion numbers.

Consensus. This is the hinge to the verified base: signal quality gates spend. Once CAPI and a real sale event are verified firing, CAC becomes measurable and you can plan against it — but the doctrine (fix signal before trusting CAC) still holds, and until that verification exists nothing downstream of it is trustworthy.

## Theme 11 - Don't fund awareness/proxy campaigns on a small budget (CONSENSUS)

At small spend, put budget behind the direct conversion objective, not warm-up or vanity campaigns.

- **Nikhil**: no standalone traffic/awareness campaigns to "warm up the pixel". Direct sales campaigns get the budget. Exception: a tiny Rs 200-500 traffic campaign only if landing cost is very high. Optimise against the sale event, not proxy events.
- **Ben Heath**: leads or sales objective only for small budgets; awareness is for big companies without a direct conversion path (the Coca-Cola example).
- **Jason Hunt**: one carve-out, a separate tiny $1-2/day evergreen video-views campaign to build a warm retargeting audience, kept distinct from the lead-gen budget.

Consensus that the main budget goes to conversion objectives. Only Jason Hunt sets aside a deliberate micro-budget for audience-building, and he treats it as separate accounting.

## Theme 12 - Judge budget on ROI/profit volume, not cost-per-result in isolation (CONSENSUS)

- **Michael Tracey**: if £1,000 spend returns £5-20K+, the CPL (£5 or £20) is irrelevant; only worry if total spend fails to return more than itself.
- **Ben Heath**: absolute profit dollars beat the ROAS ratio at scale.
- **Joly Tematio**: real client numbers ($700-750K/month at ~3x ROAS on a $50-70 CPA) justify reinvestment on profit volume, not the per-lead number.
- **DoneMaker**: know your margins and cost of goods before any scale conversation.

Consensus, and it echoes the verified base's "judge on profit volume, not per-ad attribution" (Charley T).

---

## Exclusions

- **ElenIQ - "Lead Gen Forecasting Demo / Build Smarter Paid M"**: no transcript available, not mined, excluded from all synthesis.
- No sources were era-flagged; all videos passed the <=18-month freshness rule.
- No sources were flagged thin in the input notes.
