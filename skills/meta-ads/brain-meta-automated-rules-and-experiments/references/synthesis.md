# Synthesis: Meta automated rules and experiments (rules engine, A/B tests, holdouts, bulk ops)

Built 2026-07-06 from 12 mined transcripts. 9 usable after exclusions (3 dropped for thin/era-flag; see bottom).

Context lens applied throughout: AU small-business lead-gen advertiser running manual campaigns on one ad account. Nearly every source is e-commerce/ROAS-framed. Transferable unit for lead-gen: swap ROAS/CPA for cost-per-lead against a target CPL.

Scope note stated honestly: the sources are strong on the native Rules engine UI, the native A/B Test tool UI, and the manual testing discipline that justifies a systematic kill/scale rule. They are light on holdout/lift tests (one operator source only) and near-silent on API automation. Marked where thin.

---

## Theme 1: The native Rules engine: what it is and where it lives (CONSENSUS)

Automated Rules is a native Meta Ads Manager feature. You set conditions; when they are met, Meta takes an action (pause, raise budget, notify) on a campaign, ad set, or ad, running in the background whether or not you are logged in.

- **Belad Tech Weekly**: rules are reached via the Rules option at every level or via All Tools > Automated Rules, and can be built at campaign, ad set, or ad level. Described as "an automated optimization which Facebook is doing even when you are not working on the Facebook ads account uh yourself."
- **Damini Tripathi**: same path, Ads Manager > All Tools > Automated Rules > Create Rule; frames rules as "the safest scaling method" for accounts with many campaigns.
- **Chris Marrano**: builds one live in the UI (menu > Automated Rules), naming it "scale baby scale"; notes the system checks every 30-60 min but aggregates to the action frequency you set.
- **Leadstio**: confirms rules can be scoped at ad, ad set, or campaign level, but flags a hard limitation (see Theme 5).

**Consensus.** All four rules-focused creators describe the same tool and the same access paths. No dissent on what it is or that it runs unattended.

## Theme 2: The scale rule: raise budget on a winner by a fixed percentage (CONSENSUS on shape, CONTESTED on the number)

Every rules source builds essentially the same scale rule: IF cost-per-result beats a target THEN increase daily budget by a fixed percentage, capped by a maximum daily budget.

- **Damini Tripathi**: increase daily budget by 20% when cost per purchase is under ₹300 over the last 3 days, max daily budget cap ₹400, action frequency once every 12 hours.
- **Chris Marrano**: increase daily budget by 10% when cost per result is smaller than the CPA target (example $40) over 14 days, max cap $1,000/day, action frequency once daily.
- **Belad Tech Weekly**: increase an ad set's daily budget by a percentage or exact amount when it is performing (example condition: results greater than 5), with a maximum daily budget cap as the upper limit.
- **HubSpot** (excluded as a backer, manual mirror only): "Increase your budget by 20 to 30% every three to five days."

The percentage is contested: **Marrano runs 10%/day**, **Tripathi runs 20% every 12 hours**. The one point they agree on is the **maximum daily budget cap** so scaling never runs away. Marrano additionally separates the *automated* daily cadence he teaches DIY advertisers from his agency's tighter human cadence: "my team works on three-day rules here in terms of increasing budgets turning off turning on scaling scaling down."

**Net:** the +20%/3-day pattern our house rule uses sits inside the consensus band. Marrano's 3-day human cadence is the closest named match to it; the automated versions tend to run faster (daily or twice-daily) but always behind a max-budget cap.

## Theme 3: The kill rule: auto-pause on a cost/spend/performance ceiling (CONSENSUS)

The mirror of the scale rule. IF cost per result exceeds a ceiling (or spend exceeds a cap, or results fall below a floor) THEN turn off the entity.

- **Leadstio**: the cleanest CPL-kill match in the set. Define a normal cost-per-lead (example ~$50), then auto-stop the campaign at a defined multiple/ceiling above it (example $100-$150): "cost per result greater than 150 and you can turn off this campaign." Different channels (Messenger vs lead forms) get separate ceilings via campaign-name filtering.
- **Belad Tech Weekly**: two kill variants. Spend-cap kill (turn off a campaign when spend is greater than $1,000) and underperformance kill (turn off ads when results are smaller than 1 AND CTR is less than 1%).
- **Damini Tripathi**: ROAS-trigger kill, auto-stop a campaign "if my purchase rate goes below two," while targeting a 4-5 ROAS.
- **Nick Theriot** (manual, not the rules engine): "the only time we're turning things off is if on a 7-day window that particular adset has a very high CPA hurting the performance for that particular campaign." The human-cadence version of the same logic our house 7-day kill window uses.

**Consensus** on the mechanic. The trigger metric varies by objective (CPL for lead gen, ROAS/CPA for ecom, raw spend as a blunt cap). Leadstio's "define normal CPL, kill at a multiple of it" is the exact shape of our 3x-target-CPL-after-7-days rule.

## Theme 4: Change one variable at a time (STRONG CONSENSUS, the single most repeated rule)

The core testing law. Change one thing between variants or you cannot attribute the result.

- **Michael Diaz**: "Principle number one, only change one variable at a time." Changing creative + copy + audience at once makes the win unattributable; change only the image, hold primary text/headline/description/URL/CTA, and the creative is isolated as the cause.
- **William Kast**: post-Andromeda, test "just one high-level variable" (three variations of one idea), because minor tweaks no longer register as distinct ads.
- **Tej**: the native A/B Test tool enforces it; "which variable would you like to test? So you can test a creative, an audience, a placement or anything else." Keep copy/headline/CTA/URL identical across A and B.
- **HubSpot** (excluded as a backer, manual mirror): five sequential phases, each isolating one variable.

**Consensus, unanimous.** This is the justification for a *systematic* rule set: a human eyeballing a multi-variable relaunch learns nothing, so the discipline has to be built into the test or the rule.

## Theme 5: Rule scope limits and filtering (the sharpest practical gotcha)

Rule capability differs by level, and this changes where you can even build a CPL kill rule.

- **Leadstio** (unique, load-bearing): "in ad set level you are not able to use any cost per result campaign." Cost-per-result conditions must run at **campaign level**, which triggers Meta's minimum campaign-level requirements (more campaigns, bigger budget). The single most important constraint in the set for anyone building a CPL kill rule, and it is stated by only one source, so treat as a to-verify in-account rather than settled consensus.
- **Leadstio**: rules can be filtered by campaign-name string match, so one rule applies only to campaigns whose name contains a phrase. This is how you run channel-specific CPL ceilings.
- **Leadstio**: pair a turn-on rule with a turn-off rule for exact non-standard scheduling: "you can create one rule for turning on campaign another rule for turning off campaign and here you have more possibilities than in regular scheduling settings."
- **Belad Tech Weekly**: rules can run continuously, daily at a set time, or on a custom schedule.

**Single-source on the cost-per-result-at-ad-set-level block.** High-value but verify in the account before relying on it.

## Theme 6: The native A/B Test tool: step-by-step (CONSENSUS on the flow)

The native A/B Test tool is UI-driven, distinct from manual campaign duplication.

- **Tej**: Ads Manager > A/B Test > Get Started > "Make a copy of an ad" > select an existing ad > choose the test variable (creative, audience, placement, or other). Name the test, pick a key metric, set start/end dates, hold budget constant across A and B. Meta auto-duplicates the ad set into A and B; you change only the one variable. Advanced settings include "end the test early if a winner is found and include the upper funnel matrix in the test report."
- **Marketing Operators**: same tool, referred to as "Intelligence"/"Intelligj" (a likely rebrand or transcription artifact of the same underlying A/B/Experiments feature). Used for URL split tests targeting Meta traffic via UTMs.

**Consensus** on the mechanic. The naming drift ("Experiments" vs "A/B Test" vs "Intelligence") is noted; treat as the same tool family, verify the current label in-account.

## Theme 7: Test duration: how long before you act (CONTESTED range, consensus on "don't panic-kill")

Everyone agrees you must not judge within hours. The floor varies.

- **Michael Diaz**: "These ad campaigns can take 2 to 3 days to really ramp up sometimes"; give a test 2-3 days minimum.
- **Tej**: "make sure you let it run at least for a week or two so you can gather some meaningful data before making any sort of changes."
- **Nick Theriot**: judges on a rolling **7-day window** for the kill decision.
- **Marketing Operators** (contrarian on rigour): deliberately trade precision for velocity, running "canary in the coal mine" tests for just 1-3 days to check nothing is catastrophically broken, then shipping without waiting for statistical significance. "What can you do a test on and end it early just to get directional learnings?"

**Contested.** Range runs from 2-3 days (Diaz) to 1-2 weeks (Tej), with a 7-day window as the common middle (Theriot) and a velocity-over-rigour school (Marketing Operators) that accepts low precision on purpose. Our house 7-day kill window sits with Theriot in the middle.

## Theme 8: Post-test action: pause the loser, scale the winner (CONSENSUS)

- **Tej**: "once you have a winner, you can pause the one that's not performing well and scale the winner and work on the next steps."
- **Michael Diaz**: manual version, turn off the two bad spenders to force budget onto the underspent winner, then reassess in another 2-3 days.
- **William Kast**: once a winning message/angle is found, iterate it into new formats (change format only, since format is "less impactful than the message").
- **Marketing Operators**: when a winner is clear, roll it out globally (ended one split 100/0, switched every new ad to the winning listicle page after a 15% lift in revenue per session).

**Consensus.** Nobody keeps a losing variant running "to be fair." The winner gets the budget, the loser dies.

## Theme 9: Meta misallocates spend inside an ad set; a rule or a manual cut fixes it (CONSENSUS)

A recurring warning: leaving budget allocation entirely to Meta inside a shared ad set can starve a genuine winner.

- **Michael Diaz** (concrete): 3 videos, same audience. The top *spender* got $200 for 0.49 ROAS (1 purchase); the ad that barely got spend got $36 for 2.68 ROAS (2 purchases). Fix: turn off the two bad spenders to force budget onto the underspent winner.
- **Damini Tripathi**: CBO auto-shifts spend to the best-performing ad set after 3-4 days, the *intended* version of the same behaviour when it works.
- **Nick Theriot**: accepts the downside honestly, "it doesn't ensure that every adset gets spin"; some ad sets get little or no spend under CBO allocation.

**Consensus that the behaviour exists.** Split on whether to intervene: Diaz cuts manually, Theriot lets CBO ride and only kills on the 7-day CPA rule. This is exactly why a kill rule (not just "let Meta sort it") earns its place.

## Theme 10: When to A/B test vs when to launch a separate funnel (the holdout-adjacent lesson, single strong source)

The most sophisticated methodology point comes from the one operator source, and it is the closest thing in the set to a holdout/lift discipline.

- **Marketing Operators** (unique, documented failure case): splitting *existing learned traffic* to test a fundamentally new offer invalidated the test. The Gut Culture fibre brand tested an $88 quarterly bundle against a $39/month subscription via Meta's native split test; conversion on the $88 offer was "essentially zero" and CAC doubled, "the worst test we've ever launched." Re-launching the same $88 offer as a **brand new separate funnel** (new ads/ad sets) made it "a very solid performing part of the ad account."
- **Rule of thumb** (Marketing Operators): use the native A/B tool only for true iterative single-variable tests on an existing page (example: same landing page, PDP vs checkout destination). Launch a **new offer, new template, or new funnel stage as new ads/ad sets**, treated as incremental volume, not a controlled split.
- **Revenue-per-session over conversion rate** (Marketing Operators): a clean URL split (Atomic Purple power bank PDP vs a "six reasons why" listicle) ran to hundreds of orders per cell and tens of thousands of visitors, and was decided on a **15% lift in revenue per session**, not landing-page conversion alone. Then rolled out 100/0.

**Single-source but high-signal.** No other creator in the set covers holdout/lift methodology or the "split existing traffic vs launch fresh" distinction. Flag as under-covered in the source pool.

---

## Cross-check against our verified base (brain-meta-ads-manual-control-no-advantage)

- The verified base's kill-rule ladder (Hunyor 1x CPA, Denney 2x, Blue Sense 3x-5x) and the +20% scale cadence are consistent with this brain's Theme 2/3. No conflict.
- The verified base's "learning phase is conversion-volume not time" and "never edit a live winner, duplicate via post ID" hold here too and should override any source that implies you can freely edit a running rule target mid-flight.
- Damini Tripathi cites Meta's "50 conversions in 7 days" learning-phase exit as a scaling gate. The verified base flags that this back-propagates to ~$714/day per test and is absurd for small accounts. **Side with the verified base:** do not treat 50-in-7 as a hard gate on a small lead-gen account; use conversion volume relative to your own CPL instead.
- Damini Tripathi and Belad Tech Weekly lean on Advantage+ Placements/Creative and Advantage+ audiences as scaling aids. **Side with our doctrine:** Advantage+ Placements is ON for us, but Advantage+ Audiences, creative enhancements, and ASC stay OFF (03-campaign-playbook and the verified base). Take their rule mechanics, drop the Advantage+ audience/creative advice.

---

## Exclusions

- **Chase Chappell, "The NEW Way To Test Facebook Ad Creatives"**: flagged `thin: true`. Funnel-stage creative strategy, no rules/experiments/holdout content. Excluded from backing.
- **HubSpot Marketing, "The Best Facebook Ads Testing Strategy"**: era-flagged. Its sequential creative-then-audience-then-text-then-placement phasing is the exact approach Kast and others describe as obsolete post-Andromeda. Excluded as a current-practice backer; its budget numbers ("$5-$20 per day", "20 to 30% every three to five days") are quoted once as a manual mirror only.
- **Mark Builds Brands, "how to test facebook ads post andromeda update"**: era-flagged for scope, not freshness. Passes the 18-month window but covers CBO creative-testing structure and a budget-sizing formula, nothing on the Rules engine, A/B/Experiments tool, or holdouts. Excluded as off-scope.
- **Marketing Operators, retained** despite an era note: the note is a naming caveat ("Intelligence" vs "Experiments"), and the source explicitly sits inside the freshness window and current holdout practice. Kept, with the naming drift flagged in Theme 6.
