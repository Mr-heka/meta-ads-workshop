# Synthesis: Meta lookalike audiences and seeds

Built 2026-07-06 from 9 mined transcripts (7 used for themes, 2 excluded, see bottom).
Cross-checked against the verified evidence base in
`brain-meta-ads-manual-control-no-advantage/references/synthesis.md`. Where a source
conflicts with that base, the conflict is flagged and the verified base wins.

---

## Theme 1: A lookalike is a rank-ordered similarity slice, nothing more (CONSENSUS)

Meta ranks the entire selected population by similarity to your seed audience and cuts
off the top X%. The percentage is literal maths, not a quality dial.

- **Andrew Southworth**: US pool of 278 million people, so a 1% lookalike = the top 2.78 million most similar people.
- **EfesAdLab**: same 278 million / 2.78 million worked example, independently.
- **Paul Chinedu Nnamani**: "platform analyze a seed list, example top 10% of spender to identify common traits then based on those find similar people."
- **Marketer Tawhida**: 1% lands around 100K to a couple hundred thousand people, 10% is "10 million plus", roughly a tenth of the US population.

Corollary all of them state: a lookalike is COLD traffic. New people who merely resemble
your seed, never people who have touched you. Paul Nnamani calls confusing it with a warm
audience a common advertiser mistake.

## Theme 2: Seed quality rules everything (CONSENSUS, the strongest theme in the set)

The single most repeated line across the batch, near word-for-word from multiple creators:
the lookalike can never be better than the seed.

- **Andrew Southworth**: "if the source sucks, the lookalike sucks." Also: match the seed to the campaign goal (customer-list seed for customer campaigns, follower seed for follower campaigns).
- **Blake Bauer Business**: "A look-alike audience is only as good as the source you build it from."
- **Christian Jamal**: "Feed the system garbage data, and you're going to get garbage audience."
- **Paul Chinedu Nnamani**: uploaded customer data beats pixel-only signals for seed accuracy.

Concrete number: Southworth adds a volume caveat, he would pick 100,000 people with
15-second video views over 1,000 people with 95% views as a seed, then test both.
Accuracy vs volume is a trade, not a rule.

## Theme 3: Buyers beat leads beat engagers, and filter the seed hard (MOSTLY CONSENSUS, contested at the edge)

- **Christian Jamal** (the sharpest framework in the set): never upload the full average customer list. E-commerce: seed from the top 25% of customers by revenue (repeat buyers, highest LTV). Service and lead gen: closed-deal customers only, never all form fills. "There's a massive difference between someone who fills out a form and someone who pulls out their credit card to pay you."
- **Blake Bauer Business**: default the seed to the pixel's highest-value event (purchases in the last 60 days is Meta's own default suggestion).
- **Paul Chinedu Nnamani** (lead-form version of the same logic): split form-openers from form-submitters; 100,000 may open a form while only 10,000 submit, and those are different seeds.

CONTESTED edge: **Paul Chinedu Nnamani** reports strong personal results seeding from
roughly 15,000 LEADS (3 years of CRM leads, not buyers): "100 conversion at a rate at an
amount that I have not gotten before." That cuts against Jamal's closed-deals-only rule.
Read: a big lead list can work, but the buyers-first hierarchy is the safer default and
has more backers.

## Theme 4: Fallback seeds when you have no buyer list (CONSENSUS on the hierarchy)

- **Christian Jamal**: fallback order is website visitors, video viewers, Instagram/Facebook engagers, but always the highest-intent version. Thresholds he names: engaged 10+ times in the last 365 days; video watch at 75% or 95%; and only use videos 2 minutes or longer, because on a 3-second video everybody watches 75% of it, so it cannot discriminate.
- **Paul Chinedu Nnamani**: for tiny accounts, pick the broadest custom-audience definition ("everyone who engaged with your page", 365 days) so the seed is big enough to matter.
- **Blake Bauer Business / Marketer Tawhida**: for lead events with no dollar value attached, wrap all leads in a custom audience first, then build the lookalike off that custom audience. Website windows at the max 180 days for the most data.

## Theme 5: Minimum seed sizes, the floor has dropped (ERA SHIFT, worth knowing both states)

- Old state (**Andrew Southworth**): at least 100 people per selected country, and Meta will not tell you which countries fail. Country selection still required in his account and most he knows.
- New state (**Blake Bauer Business** and **Marketer Tawhida**, both demonstrated live): Meta removed the hard minimum. A 1% lookalike was built from 9 purchase events and just 3 unique customers in 60 days. Both flag it as "probably not going to be very efficient" but technically buildable. Country selection no longer required in some accounts.

Practical read: buildable is not the same as usable. Treat a few hundred quality seed
entries as the realistic working floor even though the platform no longer enforces one.

## Theme 6: Percentage tiers, sizes, and the broad reversal (CONTESTED: 1% default vs 10% default)

Size bands (Blake Bauer Business / Marketer Tawhida): 1% runs low hundreds of thousands,
scaling through half a million to a million, 10% lands at 10 million plus.

The dispute is which tier to default to:

- **1% camp**: Christian Jamal says 1% "is the general one that everybody does" and has performed for him, alongside 3% and 10%.
- **10%/broad camp**: **EfesAdLab** states the pre/post iOS 14 rule flipped: "Smaller lookalike audiences used to perform better before iOS 14, but after that the broader you go, the better they tend to perform." **Blake Bauer Business**: "Creating broader is typically better. So, starting with that 10% is usually going to be your best audience."
- **Test-the-spread camp** (compatible with both): Blake Bauer Business and Marketer Tawhida both say if you will not test every tier, build 1%, 5% and 10% for the widest spread. Jamal's tested set is 1%, 3%, 10%.

Verified-base check: the broad-reversal claim is consistent with our verified base
(broad beats interest stacks once the pixel is trained). No conflict.

## Theme 7: Never stack tiers or sources in one ad set (CONSENSUS)

- **Paul Chinedu Nnamani**: duplicate the ad set per tier (he demos 1%, 1-2%, 2-3%, 3-4%, 5-10% as five separate duplicates). Stacking means "I can't say it's because of this particular audience." His demo sizes: 0-1% = 555,000; 1-2% = 515,000; 5-10% = 2.6 million (Nigeria-targeted source), and he stresses same-size bands are NOT the same people.
- **Christian Jamal**: one lookalike per ad set, "how are you going to know which one is actually working if you put them all together." Build a full map of custom audiences and split-test each resulting lookalike separately.
- **EfesAdLab**: two clean test structures, separate campaigns per breadth, or same campaign under CBO as an "or" test.

## Theme 8: Deployment, hard boundary vs soft suggestion (CONTESTED, conflict flagged)

- **Blake Bauer Business**: in the ad set, switch from "suggested audience" to the manual "further limit the reach" toggle so the lookalike is a hard, enforced boundary.
- **Christian Jamal** argues the opposite: post-Andromeda, "Meta treats your audience section as a suggestion, not a hard boundary," so "the best way to use lookalikes in 2026 is not as a restriction, it's as a seed" fed into an Advantage+ campaign.

CONFLICT WITH VERIFIED BASE: our verified base (brain-meta-ads-manual-control-no-advantage)
runs manual campaigns only, Advantage+ Audiences OFF, and records Piliero's gotcha that
leaving "use as a suggestion" ticked turns your list into a broad seed. Jamal's Advantage+
suggestion workflow is noted as the automation-era view, but for small manual accounts the verified
base wins: deploy lookalikes as hard boundaries in manual campaigns, or do not use them.

## Theme 9: Strip interest layering, the lookalike IS the targeting (CONSENSUS, matches verified base)

- **Andrew Southworth**: keep country and a broad age range, drop interest stacks entirely, "the lookalike is your targeting."
- **Blake Bauer Business / Marketer Tawhida** (near-identical wording): limit country, age range, gender if applicable, "don't add in any interest beyond that."

## Theme 10: Are lookalikes still worth it post-Andromeda? (THE LIVE DEBATE, no clean verdict)

- **EfesAdLab** frames it head-on: "Some people say they're dead, but I have seen some success with them." His operating rule: A/B test, never take a verdict on faith. Tell clients "we tested it and it failed", never "someone on YouTube said do not use it."
- **Andrew Southworth** is honest about variance: lookalikes have "cut my cost per conversion in half" some times, underperformed other times, made no difference at others. Test cheaply, kill losers, keep winners. Lookalikes improve as the underlying custom audience grows.
- **Christian Jamal** keeps them alive only as high-quality seeds for the algorithm, not as restrictions.
- Verified-base position: lookalikes are dead as PRIMARY levers, creative is the targeting. Nothing in this batch overturns that; the honest post-Andromeda role for lookalikes is a testable secondary lever against a broad control.

## Theme 11: Operational hygiene (CONSENSUS, brief; upload mechanics live in the list-audiences brain)

- Wait for population before spending: audiences start at 0 and grow. **Andrew Southworth** waits for a real estimated size in Audience Manager; **Paul Chinedu Nnamani** allows up to 24 hours and waits for "ready".
- Customer-list lookalikes need a Business Manager account, not a personal ad account (**Paul Chinedu Nnamani**). Process is identical at 500, 10,000 or 50,000 rows.
- Retention windows the sources use: website up to 180 days, page/social engagement up to 365 days, lead forms capped at 90 days by Meta (**EfesAdLab**, **Paul Chinedu Nnamani**, **Christian Jamal**).

---

## Exclusions

- **SMART TECH** (How To Create Lookalike Audiences on Facebook Ads in 2026): excluded from themes. Machine-translated/dubbed transcript with garbled phrasing; its 100-person minimum claim is directionally consistent with the old floor (Theme 5) but too low-precision to cite as evidence.
- **Digital Growth Tutor** (How to Create a Lookalike Audience in Meta Ads Manager): excluded from themes. Generic evergreen tutorial with zero engagement with Andromeda, Advantage+ or the current debate despite a 2026 upload date. Its 1%-default recommendation is already covered (and contested) in Theme 6 by stronger sources.
- Note: **Blake Bauer Business** and **Marketer Tawhida** present near-identical demos, numbers and phrasing (same 3-customer seed demo, same 1/5/10 spread lines). They are counted as corroborating rather than fully independent sources.
