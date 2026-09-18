# Worked session: is the online-course ROAS real, and do we scale?

**Scenario.** A business runs one Meta ad account (`<YOUR_AD_ACCOUNT_ID>`) at $50/day, selling a $500 online course to non-technical business owners, with a CRM as the record of truth. CAPI and the course Purchase event on pixel `<YOUR_PIXEL_ID>` have both been verified as firing. In the first week of real Purchase data, Ads Manager reports more course purchases than the CRM shows, and the reported ROAS looks strong enough to tempt a budget rise. Question on the table: is that ROAS real, and should the budget scale?

**Brain loaded:** `brain-meta-attribution-measurement-deep` (SKILL.md, then `references/quote-library.md` for verbatim grounding). Every expert claim below comes from the quote library or is a paraphrase with the expert named. No new sources, no new numbers.

---

## Q1. Ads Manager shows more course purchases than the CRM does. Which number is real?

The CRM. The brain's consensus is that every platform dashboard over-credits itself, and the quote library carries it directly:

> "If you look at the numbers that is being tracked in meta's dashboard, you won't see actual meta impact." — Boolean Maths, *Multi-Touch Attribution for Shopify Brands*

The gap is structural, not a bug in our CAPI setup. Per the brain's playbook (grounded in Boolean Maths), when Meta reports more conversions than the CRM, the difference is view-through credit, returning contacts, and channel overlap Meta claims but did not cause. Marketing Operators explain why Meta's own window changes push it to claim harder:

> "the attribution window going from 28 day click to 7-Day click advertisers only optimizing four click-based outcomes it just ends up you were asking meta to go further and further down funnel to attribute sales to itself" — Marketing Operators, *E051: Why Meta Purchase Conversion Isn't Enough*

**Move:** keep the Purchase event live (it feeds the algorithm signal), but reconcile every reported purchase against the CRM/Stripe actuals before any budget decision. The CRM is the scoreboard.

## Q2. Fine, but the reported ROAS still looks strong. Is it real enough to scale on?

Wrong metric. The brain's rule is that the decision metric is marginal, not blended, and the deciding question is Lorenzo Pravata's:

> "how many sales did my ads generate if I exclude the ones that would have occurred anyway and also how does the CPA change when I increase the budget" — Lorenzo Pravata, *We Scale Brands to $1M/Month Using This One Metric*

Pravata's worked example in the brain shows how a blended number hides a bleeding edge: spend rises, the blended CPA still looks fine against target, but the extra spend alone bought so few orders that the marginal CPA came out at $33, above target. His rule for the read:

> "the CPA for the incremental purchases is $33 okay so if that's still below your target CPA that's great and you can increase the budget" — Lorenzo Pravata, *We Scale Brands to $1M/Month Using This One Metric*

And his warning about what scaling does to the two numbers:

> "when you increase the budget, the blended efficiency looks very good, but then the marginal efficiency as we saw actually starts to drop much faster" — Lorenzo Pravata, *We Scale Brands to $1M/Month Using This One Metric*

**Move:** run the brain's budget-delta read (Lorenzo Pravata's method): raise the course budget roughly 20-25 per cent, hold about a week, then judge only the marginal CRM-recorded purchases bought by the extra spend against target. Scale only while the marginal read stays under target; the blended average gets no vote.

## Q3. Should we run a holdout or a conversion-lift study to settle it properly?

No. The brain is explicit that formal incrementality testing is a scale-only tactic, and the sources say so themselves. Marketing Operators describe the cadence real testing demands:

> "We ran 58 tests last year, which is like more than one a week." — Marketing Operators, *The Incrementality Playbook Every Ecommerce Marketer Needs*

That cadence needs multiple concurrent revenue lines so tests do not cross-contaminate, plus weeks-to-months per read. Full-funnel effects are slower still:

> "meta has shared some data I've even seen it like this stuff does best with like 6 months like this is like full funnel marketing that I don't think we can measure as like performance market" — Marketing Operators, *E051: Why Meta Purchase Conversion Isn't Enough*

Lorenzo Pravata draws the same floor for modelling:

> "marketing mix models. That would be only like for bigger businesses... for example, nine figure businesses, use marketing mix models to understand impact of each channel on the total sales" — Lorenzo Pravata, *We Scale Brands to $1M/Month Using This One Metric*

Lifesight's eBay case is the founding proof the question matters at all (paraphrase, Lifesight): eBay spent $50M a year on Google ads, and switching them off dropped paid traffic but spiked organic in the same markets, showing much of the spend was not incremental. But Lifesight also notes big retailers have run incrementality practices for decades; it is a big-account discipline. Scalability School tested Meta's native Incremental Attribution at $150-200K/month and still reverted to one-day-click after Meta's click-definition change broke the signal (paraphrase, Scalability School). At $50/day we have neither the spend nor the conversion volume for any of it to read as more than noise.

**Move:** decline the holdout. The runnable stand-ins at small scale are the budget-delta read (Q2) and a weekly MER: total CRM-recorded revenue across every offer over total Meta spend.

## Q4. The warm retargeting ad set has the best reported ROAS. Shift budget there?

No, and the brain treats this as the classic trap: the highest-ROAS spend is usually the least incremental, because warm audiences were converting anyway. Nitro Commerce put lift numbers on it:

> "a brand search is giving an incremental lift of only 0.6x. The retargeting is giving an incremental lift of 0.9. The prospecting actually is giving the highest incremental lift of 1.8" — Nitro Commerce, *The Incrementality Era Webinar*

**Move:** discount the retargeting ROAS and protect the prospecting budget that finds net-new owner-operators. Judge warm spend with extra suspicion in the CRM reconciliation.

## Q5. What do we watch week to week so this stays honest?

Three reads, all runnable at $50/day, all from the brain:

1. **MER, not platform ROAS.** Total CRM-recorded revenue over total Meta spend, tracked weekly. The brain's line from Marketing Operators is the standing warning:

> "If you're still making budget decisions based on platform dashboards, you're not optimizing, you're gambling." — Marketing Operators, *The Incrementality Playbook Every Ecommerce Marketer Needs*

2. **Marginal reads on every budget change.** Any rise or cut gets judged on the delta against the CRM actuals (Lorenzo Pravata's method, Q2).

3. **Creative cohorts.** Track what share of spend goes to ads launched this month. Pravata's warning:

> "not every new ad or every new creative adds revenue, right? So some ads will just replace what's already working and make it look like you're scaling" — Lorenzo Pravata, *We Scale Brands to $1M/Month Using This One Metric*

And the compounding case for keeping the pipeline fed:

> "if you can make more ads every single month that earns spend in the ad account, then that's what compounds over time and allows you to increase spend" — Scalability School, *We Tested Meta's Incremental Attribution on $200K/Month*

---

## How the brain was used

- **Pre-flight checklist applied:** dashboard vs CRM (Q1), blended vs marginal (Q2), prospecting vs warm weighting (Q4), scale-only tactic declined (Q3), volume sanity on every read (Q2, Q5).
- **Consensus led; the contested takes stayed flagged.** Meta's native Incremental Attribution was mentioned only to rule it out at our volume, matching the brain's "cross-check, never truth" stance.
- **Nothing here overrides the verified account base** (`brain-meta-ads-manual-control-no-advantage`): campaign settings and kill rules live there, this session only decided what the numbers mean.
