---
name: brain-meta-automated-rules-and-experiments
description: Use when the user is building Meta rules or experiments, or asks "set up a kill rule", "automate scaling", "auto-pause ads", "how long should an A/B test run", "split test or launch fresh", or "duplicate the winner". Route bid and learning questions to brain-meta-budgets-bidding-learning, attribution reads to brain-meta-attribution-truth.
metadata:
  type: expert-brain
  topic: "Meta automated rules and experiments (rules engine, A/B tests, holdouts, bulk ops)"
  aliases: "automated rules, Meta rules engine, Facebook automated rules, scale rule, kill rule, auto-pause, budget rule, A/B test, split test, Experiments tool, Intelligence, holdout test, lift test, incrementality, bulk duplication, post-ID duplicate, cost-per-result rule, CPL kill rule, +20% scale"
  domain: advertising
  built: "2026-07-06"
  sources: 12
---

# Brain: Meta automated rules and experiments (rules engine, A/B tests, holdouts, bulk ops)⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

> Built by topic-brain-builder from 12 YouTube sources
> (2 hidden-gem creators surfaced on engagement,
> not views; 9 usable after excluding 3 thin/off-scope). Made by Selr AI.

## How to use this brain

When the user is working on Meta automated rules or experiments, load this brain first. Ground answers in the synthesis below and cite experts by name from the quote library. Prefer the consensus view; surface a contrarian take when it's well-argued. Single-source claims are marked, treat them as high-value-but-verify.## What the experts agree on

1. **The Rules engine runs unattended at any level.** Automated Rules is native to Ads Manager, reached via the Rules option at each level or All Tools > Automated Rules, and can be built at campaign, ad set, or ad level (Belad Tech Weekly, Damini Tripathi, Chris Marrano, Leadstio). It "is doing" optimisation "even when you are not working on the Facebook ads account" (Belad).
2. **A scale rule is IF cost-per-result beats target THEN raise budget by a fixed % behind a max-budget cap.** Every rules source builds this same shape (Tripathi, Marrano, Belad). The cap is the non-negotiable part; the percentage varies.
3. **A kill rule is IF cost/spend/underperformance crosses a ceiling THEN turn off the entity.** Same across the set (Leadstio's CPL ceiling, Belad's spend cap and CTR floor, Tripathi's ROAS floor, Theriot's 7-day CPA cut).
4. **Change one variable at a time or the test is worthless.** Unanimous (Michael Diaz, William Kast, Tej). This is the reason a systematic rule beats eyeballing.
5. **Don't panic-kill; give a test days, not hours.** Everyone sets a floor (Diaz 2-3 days, Theriot 7-day window, Tej 1-2 weeks). They disagree on the number, not the principle.
6. **After a test, pause the loser and scale the winner.** Nobody keeps a losing variant running for fairness (Tej, Diaz, Kast, Marketing Operators).
7. **Meta will misallocate spend inside an ad set.** The behaviour is real and agreed (Diaz's $200-at-0.49-ROAS spender vs the underspent 2.68-ROAS ad; Theriot's "it doesn't ensure that every adset gets spin"). They split on whether to cut manually or let a kill rule handle it.

## Named frameworks & methods

- **The 3-classic-rule stack (Belad Tech Weekly):** (1) kill-on-spend, turn off campaign when spend > $1,000; (2) scale-on-performance, raise ad-set budget when results > threshold, behind a max cap; (3) kill-on-underperformance, turn off ads when results < 1 AND CTR < 1%.
- **The scale rule, two named numbers:** Marrano runs +10%/day, cost per result < CPA target (example $40) over 14 days, max cap $1,000/day, once daily. Tripathi runs +20% every 12 hours, cost per purchase < ₹300 over 3 days, capped at ₹400.
- **The two-layer safety system (Marrano):** an automated budget-scaling rule (controls budget growth) paired with a manual bid cap (controls auction efficiency). Example: a $50.40 bid cap produced 320 purchases at $28 cost per result on ~$10,000 spend.
- **Human 3-day cadence vs automated daily cadence (Marrano):** "my team works on three-day rules... increasing budgets turning off turning on scaling scaling down", distinct from the daily automated rule taught to DIY advertisers.
- **The CPL-multiple kill rule (Leadstio):** define a normal cost-per-lead (~$50), auto-stop the campaign at a multiple/ceiling ($100-$150). Channel-specific ceilings via campaign-name filtering.
- **The native A/B Test flow (Tej):** A/B Test > Get Started > Make a copy of an ad > choose variable (creative/audience/placement/other) > name, key metric, start/end dates, constant budget across A and B > "end the test early if a winner is found".
- **7-day-window kill (Nick Theriot):** in a single-CBO structure, only turn off an ad set if on a rolling 7-day window it has a very high CPA hurting the campaign.
- **Iterative-test vs launch-fresh (Marketing Operators):** native A/B tool for true single-variable iterative tests on an existing page; a new offer/template/funnel launches as fresh ads/ad sets, treated as incremental volume, not a split.

## Contrarian / disputed takes

- **Scale percentage:** Marrano's +10%/day vs Tripathi's +20%/12h vs HubSpot's (excluded) manual +20-30%/3-5 days. Only the max-budget cap is universal.
- **Test duration:** Diaz (2-3 days) vs Tej (1-2 weeks) vs Theriot (7-day window) vs Marketing Operators (deliberate 1-3 day "canary" tests, shipped without stat-sig on purpose, "high velocity of low precision"). Genuine disagreement on rigour vs speed.
- **Intervene vs let it ride when Meta starves an ad:** Diaz kills the bad spenders manually to force budget onto the winner; Theriot accepts uneven CBO allocation and only acts on the 7-day CPA rule.
- **Where a cost-per-result rule can live (single source, disputed against the "any level" consensus):** Leadstio says cost-per-result conditions are not available at ad-set level and must run at campaign level, which triggers Meta's campaign-level minimums. No other source confirms this. Verify in-account before relying on it.
- **50 conversions in 7 days as a scale gate:** Tripathi treats it as the learning-phase exit before scaling. Our verified base rejects it for small accounts (back-propagates to ~$714/day per test). Side with the verified base.

## Execution playbook

**IF/THEN operating rules (attributed):**

- IF building a scale rule THEN condition = cost-per-result < target over a lookback window, action = raise daily budget by a fixed %, ALWAYS set a max daily budget cap (Marrano, Tripathi, Belad).
- IF building a kill rule for lead gen THEN condition = cost per result > (multiple × your normal CPL), action = turn off, at campaign level (Leadstio).
- IF a cost-per-result rule won't accept ad-set scope THEN move it to campaign level (Leadstio, verify in-account).
- IF you need channel-specific CPL ceilings THEN filter one rule by campaign-name string match rather than building per-campaign rules (Leadstio).
- IF you need exact non-standard scheduling THEN pair a turn-on rule with a turn-off rule (Leadstio).
- IF running a controlled test THEN change exactly one variable and use the native A/B Test tool with constant budget across A and B (Diaz, Tej).
- IF testing a fundamentally new offer/funnel THEN launch it as fresh ads/ad sets, do NOT split existing learned traffic (Marketing Operators).
- IF a test has a clear winner THEN pause the loser, scale the winner, then iterate the winning angle into new formats (Tej, Kast).
- IF Meta is starving a genuine winner inside an ad set THEN either kill the bad spenders manually (Diaz) or let the 7-day CPA kill rule handle it (Theriot); pick one and be consistent.
- IF you have a live winner THEN never edit it directly, duplicate via post ID (our verified base; preserves social proof, avoids a learning reset).

**Default numbers experts actually use:**

- Scale: +10%/day (Marrano) to +20%/12h (Tripathi). Our house number: +20% every 3 days on a 3-day average, never same-day.
- Scale lookback: 3 days (Tripathi) to 14 days (Marrano).
- Kill ceiling: 2-3x normal cost (Leadstio's $50 → $100-$150). Our house number: 3x target CPL after 7 days, lifetime view.
- Kill window: 7-day rolling (Theriot), matches our house rule.
- Test duration floor: 2-3 days (Diaz) to 1-2 weeks (Tej).
- Rule check frequency: system checks every 30-60 min, aggregates to the action frequency you set (Marrano). Set action frequency to match your decision cadence, not faster.

**Pre-flight checklist before building a rule:**

1. Confirm the entity level the condition supports (cost-per-result may need campaign level, per Leadstio).
2. Set the lookback window to match how you judge (3-7 days for scaling, 7 days for killing).
3. Always add the max daily budget cap on any scale rule.
4. Set action frequency to your cadence (once daily or once/3-day), not the 30-60 min check interval.
5. Name the rule clearly and, if channel-specific, add the campaign-name filter.
6. Decide the trigger metric by objective: CPL for lead gen, CPA/ROAS for sales, raw spend only as a blunt backstop.
7. Confirm you are not relying on a signal that isn't live (see "Applied to your business").

**Top 5 failure modes and fixes:**

1. **No max-budget cap → runaway scaling.** Fix: cap every scale rule (Marrano's $1,000, Tripathi's ₹400).
2. **Multi-variable relaunch → unattributable result.** Fix: change one variable; use the native A/B tool to enforce it (Diaz, Tej).
3. **Panic-kill within hours.** Fix: hold to a duration floor; campaigns take 2-3 days to ramp (Diaz).
4. **Splitting existing learned traffic to test a new offer → doubled CAC.** Fix: launch new offers as fresh funnels (Marketing Operators, documented failure case).
5. **Letting Meta's allocation silently starve a winner.** Fix: a kill rule or a manual cut, not "let Meta sort it" (Diaz, Theriot).

## Applied to your business

Write your own facts down before you arm a single rule: ad account `<YOUR_AD_ACCOUNT_ID>`, pixel `<YOUR_PIXEL_ID>`, Page `<YOUR_PAGE_ID>`, `<your CRM>`, `<your landing-page stack>`, and your offer ladder with real prices.

**Before any automated rule goes live, confirm the signal it fires on is real.** A rule that reads a broken or duplicated conversion event will happily pause your best ad set. Check the pixel fires, CAPI is connected if you use it, and the event you are triggering on shows clean in Test Events. No live signal, no rule.

**Which offers this feeds:**

- **`<your flagship offer + price>`.** One campaign per launch or location, `<your starting daily budget>` scaling to `<your ceiling daily budget>` in the final stretch. This is the prime home for the house rules: the kill rule (3x `<your target CPL>`, so a $12 target gives a ~$36 ceiling; read after 7 days, lifetime view) and the scale rule (+20% no more often than every 3 days on a 3-day average).
- **`<your secondary offer + price>`.** Once its conversion event is running clean, the same kill/scale rules apply against `<its own target CPL>`.
- **Offers you never advertise cold** (memberships, high-ticket engagements, strategy calls): no automated rules here; warm retargeting only.

**Consensus translated into execution moves:**

1. **Build the kill rule as a campaign-level cost-per-result rule** (Leadstio's shape): condition = cost per result > 3x `<your target CPL>`, over a 7-day lifetime-view window, action = turn off, filtered by campaign name so each launch or offer gets its own ceiling. Verify the ad-set-level block in-account first. Add an evidence floor to the conditions: never fire below a minimum spend, 7 days, and 3 conversions in the window, because a cost-only trigger will kill an under-evidenced ad set. Point the trigger at the specific lead action type; a summed actions total double-counts and fires rules early.
2. **Build the scale rule with a hard max-budget cap** (Marrano/Tripathi): +20% budget when cost per result beats target over 3 days, capped at `<your ceiling daily budget>`, action frequency once per 3 days, never same-day. Never let it edit a live winner directly, scale by budget only.
3. **Every controlled test goes through the native A/B Test tool, one variable** (Tej, Diaz), or through a 3-2-2 DCT ad set where budget allocation is the read. Hold copy, headline, CTA and URL constant.
4. **New offers and new landing pages launch as fresh ads/ad sets, not splits of existing traffic** (Marketing Operators). Launch a reopening or a rebuilt VSL clean rather than splitting a working campaign's traffic.
5. **Rule check frequency set to your cadence, not faster.** Once-daily or once-per-3-days action frequency, mirroring the never-same-day scaling rule.

**What the experts say that does NOT apply at small spend, and why:**

- **Advantage+ Audiences, Advantage+ Creative enhancements, and the "Enable Advantage+ Creative" rule template** (Tripathi, Belad): off if you have chosen manual control. Take their rule mechanics, drop the Advantage+ audience/creative advice.
- **"50 conversions in 7 days" as a scale GATE** (Tripathi): 50 events per ad set per 7 days is Meta's learning-phase exit threshold, and a small lead-gen account will rarely reach it. Do not use it as a permission-to-scale bar; scale on conversion volume relative to `<your target CPL>` instead.
- **ROAS-trigger kill rules** (Tripathi, Belad): if your front end is lead gen rather than e-commerce, the trigger is cost per lead, not ROAS. ROAS logic only becomes relevant when a real purchase value flows back to Meta.
- **Raw spend-cap kill of $1,000** (Belad): far above a small per-launch budget. At `<your total budget per launch>` the backstop is the cost-per-lead ceiling, not a spend cap.
- **n8n / external orchestration:** not our infra. Rules run natively in Meta or via server cron.

## Related brains

- `brain-meta-budgets-bidding-learning`: what to scale and the learning-phase mechanics behind the scale rule.
- `brain-meta-attribution-truth`: how to read a holdout/lift result and trust the signal a rule fires on.
- `brain-meta-ads-manual-control-no-advantage`: our verified evidence base for manual control and the settings kill-list.
- `brain-meta-media-buyer-manual`: campaign build, settings, budget structure the rules sit on top of.

## Pairs with / boundaries

- **Budgets/bidding/learning lives in `brain-meta-budgets-bidding-learning`.** This brain does not re-derive learning-phase theory or bid-strategy selection; it consumes them and encodes the trigger into a rule.
- **Attribution and holdout *reads* live in `brain-meta-attribution-truth`.** This brain covers how to *set up* an A/B or holdout-adjacent test; interpreting lift and trusting the number is that brain's job.
- **Manual-control doctrine and the Advantage+ kill-list live in `brain-meta-ads-manual-control-no-advantage`.** This brain defers to it on every Advantage+ on/off call.
- **Explicitly OUT of scope here:** creative angle strategy, audience building, campaign objective selection, pixel/CAPI plumbing. Route those to their own brains. Check it when a question spans topics.

## Deeper references

- `references/synthesis.md`: full thematic synthesis (10 themes, consensus vs contested)
- `references/quote-library.md`: verbatim quotes with attribution
- `references/experts.md`: who was mined and why (popular vs hidden-gem), plus source quality notes

Router key `sk-klfgc0` — resolved by the skills index on load.
