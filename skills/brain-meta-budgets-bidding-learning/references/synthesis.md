# Synthesis: Meta ads budgets, bidding and learning phase

Built 2026-07-05 from 22 mined transcripts (20 usable in this synthesis, 2 era-flagged and excluded, none thin).
All sources under 12 months old. Most are e-commerce/ROAS-framed; for lead gen swap ROAS for cost per lead against a target CPA.
Cross-checked against the wider verified evidence in `brain-meta-ads-manual-control-no-advantage/references/synthesis.md`; conflicts flagged inline.

---

## Theme 1: The bidding ladder: what each strategy actually does (CONSENSUS on mechanics)

Highest volume is fully automatic (Meta sets and can inflate the bid to spend the whole budget). Cost cap is semi-automatic (bid floats above or below the cap, cost averages toward target over the attribution window). Bid cap is a frozen per-auction ceiling. Target ROAS is the cost-controlled version of highest value.

- **Andrei Lunev**: "the bid is frozen. It's fixed" on bid caps; cost cap is "closer to highest volume campaign to the automatic bidding" and can overspend on day one and two before suppressing.
- **David Parrottino**: bid cap "will not bid for conversions that it thinks it can get for $51" if the cap is $50; target ROAS works on 7-day click only; platform average ROAS is around 2x, so a 4x target asks Meta for a 99th-percentile outcome and delivery throttles.
- **Konstantinos Doulgeridis**: "If you put 52 it's like you're saying give me 52 or nothing" (bid cap) versus cost cap which averages out.
- **William Kast**: highest volume spends the full daily budget regardless of that day's profitability; a bid cap campaign can carry a "ridiculously high" budget because Meta self-limits to auctions it believes hit the target.

Concrete number: Kast runs a $420 bid cap example where observed cost per purchase was $85 yet spend still stalled once the warm pool was exhausted, needing the cap raised toward $500.

## Theme 2: Caps are scaling tools, not testing tools (CONSENSUS, with a spend gate)

Nobody in the set recommends cost or bid caps as the way to test creative. The pro-cap voices use them only on proven winners, and the gatekeepers put a spend floor under them.

- **Marin Istvanic**: uses cost caps "only for scaling. I'm not using it for testing"; five reasons against cap-based testing, including that spend-based winner judgement kills learning from imperfect ads.
- **Konstantinos Doulgeridis** (5-10M/month): cost caps are a supplementary scaling tool kept evergreen for demand spikes. BFCM week: $388K spent versus ~$300K expected without the cost-cap ad sets.
- **Build Your Ecomm**: hard gate, only touch cost caps at $30,000+/month spend OR 90+ days of stable data.
- **David Parrottino**: start on highest volume, "keep scaling your budget up until it breaks", only then introduce cost cap, and bid cap only if you need still more efficiency.
- **William Kast**: bid caps suit accounts spending multiple hundred thousand per month launching 500+ ads monthly; everyone else should run auto-bid.

**Cross-check:** Piliero and Blue Sense are stricter again (Piliero: caps earn a place at $100K+/month; Blue Sense: not under $200K/month). Where they differ, take the stricter rule: at small spend, no caps at all. Both bodies of evidence agree caps never belong in testing.

## Theme 3: Setting and tuning a cap (CONSENSUS on direction, varied formulas)

Start from your real average CPA, not your wish. Move in small increments with waiting periods.

- **Marin Istvanic**: set the initial cap at account average CPA or slightly below; "if you're currently getting cost per purchase of 70 in the ad account, you cannot expect cost cap to get 50".
- **Konstantinos Doulgeridis**: average cost per purchase $50, set the cap around $45; sometimes you set 58 to be delivered 51-52. Treat the cap as a soft target Meta averages toward.
- **Cody Wittick**: ratio formula. Actual CPA $150 on a $100 target means performance is 1.5x off, so set the cap at 2/3 of the desired target ($67). Then bias it: $80 if volume matters (high LTV), $50 if efficiency matters. Max one adjustment per campaign every 3 days.
- **Alex Djordjevic**: live tuning loop. Start the bid low, raise in sub-dollar increments until spend flows ($54.72 to $57), then walk it back down ($57.02) to settle around a $38-40 CPA. Rising cost per purchase over consecutive days while still maxing the budget = overbidding.
- **Build Your Ecomm**: cost cap = (AOV x target margin %) minus break-even cost per purchase; increments of 20-30% only, at least 24 hours apart.
- **David Parrottino**: launch slightly above break-even CPA, reduce over following days.

Contested detail: Lunev prefers bid caps over cost caps because of the day-1/day-2 cost-cap overspend risk; Doulgeridis prefers cost caps because bid caps are too strict for fluctuating accounts. Both agree on the mechanics, they just weight the risk differently.

## Theme 4: Judge over the attribution window, never day three (CONSENSUS)

A 7-day-click campaign cannot be judged on 3 days of data; conversions are still landing.

- **Manny Barbas**: the common mistake is launching a cost-controlled campaign and killing it on a day-3 CPA spike; "if you let it run for seven days instead of killing it after three, it would have most likely evened out."
- **Cody Wittick**: "Meta's algorithm is factoring in conversions that can happen up to 7 days after someone clicks"; every day of spend needs its full 7-day cycle before assessment.
- **Marin Istvanic**: a $50 cap over 7-day click shows daily results of 52, 47, 42, 57 and should average to 50 across the week.
- **David Parrottino**: the window resets daily, so you need at least 7 days of data to read true cost-cap performance.
- **William Kast**: an 0.8 ROAS day between 6.5 and 7.5 days is funnel nurture, judge "over a bigger time frame."

## Theme 5: The learning phase 50-a-week number (CONTESTED, the sharpest split in the set)

Two camps on whether 50 conversions per ad set per week is a real performance gate.

- **Threshold camp**: **Rafael Hernandez** ("You're aiming for 50 optimization events per adset within 7 days"), with the up-funnel workaround (optimise for add-to-cart or LP views temporarily to hit volume). **Cody Wittick** turns it structural: cost cap x 7 x number of ad sets = minimum daily budget; a $50 cap and 5 ad sets needs $1,785/day, else consolidate.
- **Myth camp**: **William Kast** cites Meta's own article admitting the "delivery system never stops learning"; real accounts stuck in learning at ROAS 5 across $20K/30-day spend; at most a 5-10% measured difference between active and learning ads. **Derek Videll**: treat learning, learning limited and active as "the exact same thing"; learning limited is not actually limiting.

**Cross-check:** the 50-in-7 rule is a large-account guideline (it back-propagates to ~$714/day per test, absurd at small spend); under roughly $100 a day ignore it and judge on cost per result and booked or purchased outcomes (the ground rules in `meta-ads-guidelines`). Side with the myth camp at small budgets; keep Wittick's formula as a structural feasibility check before ever attempting manual bidding at scale.

## Theme 6: Change discipline: every significant edit resets learning (CONSENSUS)

- **Cody Wittick**: any adjustment over 15% resets learning. "Budget increase by 20%, back to learning. Add three new ads when you have five running, back to learning." Limit changes to under 15%, no more than 1-2 times a week.
- **Ben Heath**: don't "helicopter parent"; set an optimisation schedule of no more than one adjustment round every 7-10 days on small budgets. A campaign doing six conversions a week might need a month to judge a new ad, versus 3 hours for one doing thousands a day.
- **Rafael Hernandez**: "Every time you tweak something... it resets the learning phase." Batch edits, one edit per day max, off-peak hours (12am-1am); adding a new ad set to a live CBO can re-enter the whole campaign into learning.
- **Nick Theriot**: never react to a missed KPI until the current budget level has had at least 4 days.

Small conflict inside the camp: Wittick says a +20% budget change resets learning, Chappell and Rafael prescribe +20% precisely because it avoids a reset. Treat 20% as the ceiling, not a free pass, and keep the 3-day spacing both sides agree on.

## Theme 7: Scaling cadence: +20% every 3 days, hard decks, micro-shifts (CONSENSUS on cadence)

- **Chase Chappell**: +20% at the ad-set level every 3 days; past ~$200/day migrate to CBO; past $500/day scale in $100/$250/$500 steps every 3 days. Spiking spend 100-500% in a day is the named killer.
- **Nick Theriot**: daily SOP on one CBO per business goal. KPI hit yesterday: +20%. KPI missed for 4+ days: -20% until the "hard deck", a never-breached spend floor (e.g. hold $2,000-3,000/day of a $10,000/day budget) so there is always volume left to test new creative.
- **Rafael Hernandez**: "Go up 20% every 3 to 5 days because if you scale too fast, you'll re-enter the learning phase."
- **William Kast**: 3-day lookback decides scale up/down by 20%; 7-day lookback decides kills.
- **Build Your Ecomm**: 20-30% per increment, minimum 24 hours between moves; +50% does not produce 50% more results.
- **Chase Chappell** (unique add): microbudget shifting, move $25/day from a $65/day 6x ROAS ad set into a $120/day near-12x ad set instead of switching the weaker one off. Blended ROAS rises at flat spend.

Contested: **Manny Barbas** doubles budget every 2 days once an offer is validated under a cost cap ($900 spend, 97 purchases, $8 CPA case). That aggression only holds with a cap in place as the brake; it contradicts the 20% doctrine for uncapped campaigns.

## Theme 8: Ads not spending: the diagnostic ladder (CONSENSUS, one clear owner)

- **AdAmigo AI** owns the step-by-step: (1) account not banned, payment not failing, no red banner; (2) audience size, below 200,000 "is playing with fire", remove interest stacking; (3) retargeting audiences built on under 1,000 pixel visitors need more data first; (4) check for a forgotten low manual bid (a $5 cost-per-result goal on a $5,000 product kills delivery), remove it and return to automatic; (5) duplicate the ad set to re-enter the auction; (6) if still dead after half a day to a day, force-bid 2-3x AOV temporarily ($500 product, $250 target, bid $1,500), then pull the manual bid out once spend flows; (7) last resort, raise budget and switch to accelerated delivery, monitoring hourly.
- **Andrei Lunev** explains the mechanism: under a bid cap, if Meta can't connect CPM, expected CTR and expected conversion rate to the frozen bid, it suppresses that creative's spend entirely.
- **Cody Wittick** reframes: under cost controls, zero spend on new creative is a feature, not a bug. Test new ads at a cost control 10-20% above the account's, for up to 7 days; "if an ad is spending $3 to $5 and Meta keeps suppressing it, that's telling you something important."
- **William Kast**: Meta pre-evaluates every new ad against its database of running ads before committing budget; zero spend means it already judged the ad uncompetitive.

## Theme 9: Don't kill the top spender: read at campaign level (CONSENSUS among those who cover it)

- **William Kast**: live example, top spender at £2,000/30 days and 2.09 ROAS versus a barely-spent 3.0 ROAS ad. The high-frequency small ad harvests warm traffic the low-frequency (1.8x) top spender created; last-click credit lands on the retargeting-style ad. Rule: never turn off top spenders at or slightly below break-even. The one exception: a big spender clearly losing money (1.37 ROAS against a 2.0 break-even) where other ads can absorb the budget.
- **Manny Barbas**: individual ad CPAs of $44, $58 and $38 blended to a $33 campaign CPA; killing everything over $35 would have cut off the top-of-funnel supply. Judge at campaign/funnel level, using frequency (1.7 versus 3.15) to spot funnel stage.
- **Marin Istvanic**: "I would rather have one winning ad and four supporting ads" spending 10K at 1.8 ROAS than one ad spending 5K at 2.0.

This matches the wider verified evidence's incrementality warning (judge on profit volume, not per-ad attribution).

## Theme 10: Small-budget doctrine (CONSENSUS)

- **Ben Heath**: small = under $3,000/month (~$100/day), tiny = under $600/month (~$20/day). One offer, one campaign, one ad set (5 ad sets sharing 50 weekly conversions = 10 each, well under the ~50-per-ad-set-per-7-days exit threshold, and Meta never learns). Leads or Sales objectives only, direct offer, no traffic/awareness campaigns. Model competitors via the Ads Library (ads running 6+ months are the signal) instead of burning scarce test budget. Accept a higher CPA against real LTV; 4x ROAS at $1M/month beats 10x at $10K/month.
- **Nick Boddington** (post-Andromeda): $20/day minimum daily spend, one campaign, one broad ad set, at least 4 genuinely different creatives. Meta's similarity metric treats same-video/different-overlay as one ad. Don't switch off every ad but the winner inside a testing set; scale the winner into its own campaign instead. Test concepts as cheap statics before UGC video.
- **Rafael Hernandez**: 1-2 ad sets at $30-50/day beats five at $10/day; 2-5 creatives per ad set; audience of at least a million for lead gen.
- **Derek Videll** (contrarian pressure valve): "If you cannot be profitable at a low budget, a high budget will never ever ever be the differencemaker of you running a profitable campaign." Lowering budget is often the fastest ROAS raise; more budget makes Meta less picky about who it shows ads to.

## Theme 11: Creative volume is the real lever; budget mechanics cannot fix weak ads (CONSENSUS)

- **Chase Chappell**: brands running 5,500+ unique active ads (Rise) and a 740-ad client account; not cycling new creative in weekly makes costs rise and ROAS decay, blocking long-term scale.
- **Build Your Ecomm**: 6-10 new creatives tested every week across stores; caps can't fix bad creative (his fifth, most overlooked cost-cap mistake).
- **Manny Barbas**: "in 2025 and beyond, the content is what does the targeting"; cost controls exist to free the team to focus on creative instead of toggling ads on and off.
- **Nick Boddington**: genuinely different concepts (UGC vs demonstration vs testimonial vs offer), not text-overlay swaps.

Fully aligned with the wider verified evidence's Theme 1 (*creative IS the targeting*).

## Theme 12: CBO vs ABO in the current UI (CONTESTED placement, consistent principle)

- **Sam Piliero**: always CBO, budget adjusted at campaign level, highest volume or value bidding, Purchase event "no exceptions", ad-set spending minimum = 1x average CPA for the first 7 days of any new creative pack, then remove it.
- **Nick Theriot**: one CBO per business goal, no separate scaling or testing campaigns, all budget moves made on that single campaign ($42,000 over 7 days through one CBO).
- **Konstantinos Doulgeridis**: runs cost caps "mostly with ABOS", has seen CBO work with them too; ABO plus a cap avoids the cannibalisation he sees under daily-budget CBO logic.
- **Manny Barbas**: CBO testing campaigns split by country, cost caps set at ad-set level, inflated $5,000/day campaign budget as deliberate breathing room.
- **Rafael Hernandez** (caveat that decides ties): adding a new ad set to a live CBO can re-enter the whole campaign into learning.

Net: consolidated CBO is the default (matches the wider verified evidence); ABO appears mainly as the container some heavy spenders prefer for cap work. The principle both camps share is few learning units, concentrated conversions.

---

## Exclusions

- **Manny Barbas, *HOW TO SCALE TO 7 FIGURES A MONTH WITH BID-CAPS***: era-flagged: bid-cap doctrine presented as current with no Andromeda-era framing. His two other videos (ASC cost-caps case study, 50k-days cost caps) are clean and included.
- **Christian Jamal, *Why Your Facebook Ads Aren't Scaling (ABO vs CBO Explained)***: era-flagged: the one-ad-per-ad-set ABO-to-CBO ritual reads as pre-Andromeda doctrine presented without caveats, and directly contradicts the consolidation consensus and Andromeda same-ad-set testing.
- **Nick Boddington** carries an era note but is INCLUDED: his video explicitly corrects pre-Andromeda habits rather than teaching them.
- No sources were flagged thin.

## Conflicts with the wider verified evidence (`brain-meta-ads-manual-control-no-advantage`, in the optional extras pack of this kit)

1. **Cap spend gates**: Build Your Ecomm's $30K/month gate is looser than the wider verified evidence's $100-200K/month. Take the stricter rule at small spend: no caps.
2. **Manny Barbas runs ASC (Advantage+ Shopping) containers** for his cost-cap campaigns. Our doctrine bans ASC; take his window-patience and campaign-level-reading lessons, discard the container.
3. **Wittick's 50-conversions structural formula** assumes manual bidding is the goal; the wider verified evidence says ignore the 50-rule at small spend. Both hold in their own bands: the formula is a feasibility gate for cap-based buying at scale, not a small-account rule.
