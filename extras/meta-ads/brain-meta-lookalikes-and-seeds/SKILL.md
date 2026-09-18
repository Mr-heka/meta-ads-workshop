---
name: brain-meta-lookalikes-and-seeds
description: "Use when the user asks \"are lookalikes still worth it\", \"lookalike or broad\", \"what percentage lookalike\", \"what should I seed it from\", \"how small can the seed be\", or is building or auditing a Meta lookalike ad set. Route list uploads to brain-meta-list-audiences-and-crm-sync."
metadata:
  type: expert-brain
  topic: "Meta lookalike audiences and seeds (seed quality, percentage tiers, lookalikes vs broad)"
  aliases: "lookalikes, lookalike audience, look-alike, LAL, LLA, seed audience, seed list, source audience, 1% lookalike, 10% lookalike, percentage tiers, lookalike stacking, tier stacking, value-based lookalike, customer list lookalike, lookalikes vs broad, similar audiences"
  domain: "meta-ads"
  built: "2026-07-06"
  sources: 9
---

# Brain: Meta lookalike audiences and seeds (seed quality, percentage tiers, lookalikes vs broad)⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

> Built by topic-brain-builder from 9 YouTube sources
> (3 hidden-gem creators surfaced on engagement,
> not views). Made by Selr AI.

## How to use this brain

When the user is working on Meta lookalike audiences and seeds (seed quality, percentage tiers, lookalikes vs broad), load this brain first. Ground answers in
the synthesis below and cite experts by name from the quote library. Prefer the
consensus view; surface a contrarian take when it's well-argued.
Load order: this SKILL.md first; open `references/synthesis.md` only if deeper
detail is needed; open `references/quote-library.md` only when citing verbatim.

## What the experts agree on

1. **A lookalike is a rank-ordered similarity slice of one country's Meta users, and it is cold traffic.** Meta ranks the people it can reach in the country you selected by similarity to your seed, then cuts the top X% (Andrew Southworth, EfesAdLab, both independently). The base it slices is Meta's addressable adult audience in that country, not the country's total population, so do not compute the size yourself from a census figure — read the estimated audience size the builder shows you and use that. It is never a warm audience; that confusion is a named advertiser mistake (Paul Chinedu Nnamani).
2. **Seed quality is the whole game.** "If the source sucks, the lookalike sucks" (Southworth); "only as good as the source you build it from" (Blake Bauer Business, Christian Jamal near word-for-word). Match the seed to the campaign goal too: customer seed for customer campaigns, follower seed for follower campaigns (Southworth).
3. **Buyers beat leads beat engagers, and the seed should be filtered hard.** Top 25% of customers by revenue, or closed deals only for lead gen (Jamal); the pixel's highest-value event as default (Bauer); form-submitters split from form-openers because only ~1 in 10 openers submits (Nnamani).
4. **One lookalike per ad set, never stacked.** Stacking tiers or sources makes attribution impossible: "how are you going to know which one is actually working if you put them all together" (Jamal; Nnamani demos five separate duplicates; EfesAdLab offers separate-campaign or CBO or-test structures).
5. **When a lookalike is the audience, strip everything else.** Country, broad age range, gender if relevant, zero interest layering: "the lookalike is your targeting" (Southworth, Bauer, Marketer Tawhida). Matches our verified manual-control base.
6. **Test, never take a verdict on faith.** Results are genuinely inconsistent post-Andromeda: sometimes half the cost per conversion, sometimes nothing (Southworth). The only defensible client answer is "we tested it and it failed" (EfesAdLab).
7. **Wait for the audience to populate before spending.** New lookalikes start at 0 and grow; wait for a real estimated size, up to 24 hours for "ready" (Southworth, Nnamani).

## Named frameworks & methods

- **The Top-25% seed filter (Christian Jamal).** E-commerce: seed only the top 25% of customers by revenue (repeat buyers, highest LTV). Lead gen and services: closed-deal customers only, never all form fills. No customer list yet: fall back to website visitors, then video viewers at 75/95% completion (videos 2 minutes or longer only, since everyone watches 75% of a 3-second clip), then people who engaged 10+ times in the last 365 days.
- **The 1/5/10 spread test (Blake Bauer Business, corroborated by Marketer Tawhida).** If you will not test every tier, build 1%, 5% and 10% for the widest read. Jamal's own tested set is 1%, 3% and 10%. Size bands: 1% runs low hundreds of thousands, 10% lands 10 million plus (US).
- **One-tier-per-ad-set duplication ladder (Paul Chinedu Nnamani).** Duplicate the ad set once per band (1%, 1-2%, 2-3%, 3-4%, 5-10%) so each tier is isolated. His demo sizes: 0-1% = 555K, 1-2% = 515K, 5-10% = 2.6M; same-size bands are NOT the same people.
- **The percentage maths (Andrew Southworth, EfesAdLab).** Percentage = rank-ordered slice of the selected country's Meta-addressable adults, top X% by similarity to your seed. Both sources illustrate it with a "population × 1%" sum. **Do not copy the sum.** The multiplier they use is a country's total population, which includes children, non-users and duplicate or dormant accounts, so it overstates the pool. The mechanic (rank the country, keep the top X%) is right; the arithmetic is not. Read the real number off the builder's estimated audience size for your country, and note it changes as your seed grows.
- **Accuracy-vs-volume seed trade (Andrew Southworth).** He would take 100,000 people at 15-second video views over 1,000 people at 95% views, then test both. Cheap tests: run each lookalike for around five dollars, kill losers, keep winners.
- **The lead-event wrap (Blake Bauer Business / Marketer Tawhida).** Lead events carry no dollar value, so build a custom audience of all leads first, then the lookalike off that custom audience. Website windows at the 180-day max for the most data.
- **"Tested it and it failed" (EfesAdLab).** The client-facing rule for the whole lookalike debate: run the A/B, report the result, never outsource the verdict to YouTube.

## Contrarian / disputed takes

- **1% default vs 10%/broad default.** Jamal calls 1% "the general one that everybody does" and it has worked for him. EfesAdLab says the rule flipped after iOS 14: broader tiers now tend to win, converging on plain broad (age, gender, location only). Bauer sides with broad: "starting with that 10% is usually going to be your best audience." The spread test dissolves the argument: run 1/5/10 and let the account decide.
- **Hard boundary vs soft suggestion.** Bauer: deploy via the manual "further limit the reach" toggle so the lookalike is enforced. Jamal: post-Andromeda, Meta treats the audience section as a suggestion anyway, so use the lookalike as a seed inside an Advantage+ campaign. CONFLICT with our verified base (brain-meta-ads-manual-control-no-advantage): Advantage+ Audiences stay OFF, and Piliero's documented gotcha is that "use as a suggestion" turns your list into a broad seed. We side with the verified base: hard boundary in manual campaigns, or skip lookalikes.
- **Leads as seed.** Jamal: never seed from all leads, buyers only. Nnamani reports his best-ever conversion run seeding from ~15,000 CRM leads spanning 3 years. A large lead list can work; buyers-first remains the safer default with more backers.
- **Minimum seed size.** Bauer and Tawhida both build a lookalike live off a tiny seed (Bauer's demo shows 3 unique customers) and conclude there is no enforced minimum any more. **That reading is wrong, and it is the dangerous kind of wrong.** Meta's documented requirement has not moved: the source audience needs **at least 100 people from a single country**, and Meta recommends 1,000-50,000 for a usable result. The builder letting you click Create is not the same as Meta populating an audience — a sub-100 seed can sit at "Populating" or come back too small to deliver, having cost you the days you spent waiting. Southworth's account behaviour (100 per country, failures Meta does not explain) is the accurate picture. Treat 100 as the hard floor, a few hundred quality entries as the realistic working floor, and low thousands as where lookalikes start behaving.
- **Still worth it at all?** The verified base says lookalikes are dead as PRIMARY levers, creative is the targeting. Nobody in this set overturns that; the strongest honest position is EfesAdLab's: a testable secondary lever against a broad control, kept only if it beats broad in your account.

## Execution playbook

**IF/THEN operating rules**

- IF you have any buyer list THEN seed from the filtered top slice, top 25% by revenue or closed deals only, never the full average list (Jamal).
- IF lead gen with no purchase value on the event THEN wrap all leads in a custom audience first and build the lookalike off that (Bauer, Tawhida).
- IF no customer data at all THEN fall back in order: website visitors, 75/95% viewers of 2-minute-plus videos, 10+ time engagers in 365 days (Jamal); tiny accounts take the broadest engager definition so the seed has volume (Nnamani).
- IF unsure which tier THEN build 1%, 5% and 10%, one per ad set, and compare (Bauer, Tawhida); never stack tiers in one ad set (Nnamani, Jamal).
- IF deploying a lookalike THEN use the manual "further limit the reach" toggle, not "suggested audience" (Bauer, backed by the verified base), and strip all interest layering, keeping only country, age, gender (Southworth, Bauer, Tawhida).
- IF the audience was just created THEN wait until it shows a real estimated size, up to 24 hours, before spending (Southworth, Nnamani).
- IF the lookalike loses to broad after a fair test THEN kill it and record "we tested it and it failed" (EfesAdLab); IF it wins THEN keep it and expect it to improve as the seed audience grows (Southworth).

**Default numbers the experts use**

- Seed filter: top 25% of customers by revenue (Jamal).
- Engagement seed thresholds: 10+ engagements in 365 days; 75% or 95% video completion on videos 2 minutes or longer (Jamal).
- Windows: website 180 days max, page/social engagement 365 days, lead forms 90 days (Meta cap), purchases 60 days for the pixel default (EfesAdLab, Nnamani, Jamal, Bauer).
- Tiers: 1/5/10 spread (Bauer, Tawhida) or 1/3/10 (Jamal). Read each tier's size off the builder rather than calculating it.
- Seed size: **100 matched people from one country is Meta's documented minimum**; 1,000-50,000 is its recommended range; a few hundred quality entries is the realistic working floor.
- Populate time: up to 24 hours (Nnamani).
- Test spend: cheap, around five dollars per lookalike before first kill/keep read (Southworth).

**Pre-flight checklist**

1. Seed chosen for THIS campaign goal (customers for sales, not followers for sales).
2. Seed filtered: buyers/closed deals first, top slice only.
3. One lookalike per ad set, tiers split, nothing stacked.
4. "Further limit the reach" manual mode on; suggested-audience mode off.
5. Interests stripped; only country, age band, gender remain.
6. Audience shows "ready" with a real estimated size.
7. A broad control ad set exists so the lookalike has something to beat.

**Top 5 failure modes and fixes**

1. **Average seed in, average lookalike out.** Full customer list or all form fills as seed. Fix: top 25% by revenue or closed deals only (Jamal).
2. **Stacked tiers or sources in one ad set.** No way to know what worked. Fix: duplicate the ad set, one lookalike each (Nnamani, Jamal).
3. **Interest layering on top of the lookalike.** Double restriction strangles delivery. Fix: the lookalike IS the targeting; strip interests (Southworth, Bauer, Tawhida).
4. **Left in "suggested audience" mode.** Meta treats the lookalike as a hint and drifts broad without you choosing it. Fix: manual "further limit the reach" toggle (Bauer; verified base gotcha).
5. **Spending before the audience populates.** Early delivery skews on a half-built audience. Fix: wait up to 24 hours for "ready" and a real size (Southworth, Nnamani).

## Applied to your business

Fill these in first: ad account `<YOUR_AD_ACCOUNT_ID>`, pixel `<YOUR_PIXEL_ID>`, CRM `<your CRM>`, country or countries you sell into `<your target country>`, current control CPL `<your best CPL today>`, target CPL `<your target CPL>`.

**Which of your offers this feeds**

- **Your widest-geography offer** (national or online delivery): the natural lookalike testing ground, because a country-wide similarity slice has room to breathe.
- **Any location-locked offer** (a city event, a service area): a seed DONOR more than a seed consumer. Paid attendees are your highest-value seed material, but a `<your radius>`km campaign clips a national lookalike down to almost nothing, so seed from it and spend elsewhere.
- **Warm-only or outbound offers**: no cold lookalike campaigns at all. Do not build what you will not run.

**Consensus translated into execution moves**

1. **Seed from closed-won, not the whole CRM.** Export paying customers as the seed list with Jamal's filter applied: buyers only, never the full contact database and never all form fills. Check the export clears the 100-per-country floor before you build. (Upload mechanics: `brain-meta-list-audiences-and-crm-sync`.)
2. **Run lookalikes as a challenger, never the plan.** Whatever is working today is the control. A lookalike enters as one ad set per tier (1/5/10 spread) against that control, judged on CPL against `<your target CPL>`, with a kill/scale gate you set before launch — no verdict below `<your minimum test spend>`, 7 days, and at least 3 conversions.
3. **Hard boundary deployment only.** "Further limit the reach" manual mode, Advantage+ Audiences off, interests stripped. Bauer and the Piliero suggestion-mode gotcha point the same way: in suggestion mode Meta treats your seed as a hint and drifts broad without telling you.
4. **Check the signal before leaning on pixel-event seeds.** A purchase- or high-value-event seed is only as good as the event feeding it. Confirm the event is actually firing and matching before you build on it; until it has real volume, list-based seeds from your CRM are the reliable default.
5. **Point the first test at your widest-geography offer.** A 1% national lookalike is a workable audience; the same tier inside a city radius collapses to nothing.

**What may NOT apply to you**

- **Jamal's Advantage+ suggestion workflow.** If you run manual campaigns with Advantage+ Audiences off, his framing is the automation-era view, recorded but not followed.
- **E-commerce purchase-event seeds and value-based lookalikes.** With no purchase value on your events, use the lead-event wrap instead: build a custom audience of buyers or leads first, then the lookalike off that.
- **Tiny-seed lookalikes.** The 3-person build is a builder quirk, not a tactic, and it does not clear Meta's 100-per-country minimum. Seed from real buyer segments.
- **Nnamani's all-leads seed win.** Tempting if you hold a big contact database, but most of it is unqualified. Seed discipline stays buyers-first; an all-leads version is at most a later, clearly-labelled test.

## Related brains

- `brain-meta-audiences-2026`: Meta ads audiences 2026 (the full audience system survey)
- `brain-meta-website-and-engagement-audiences`: Meta website and engagement audiences (pixel segments, video views, engagers, recency)

## Pairs with / boundaries

- `brain-meta-audiences-2026` is the parent survey; this brain is the lookalike deep-dive under it.
- `brain-meta-list-audiences-and-crm-sync` owns customer list upload mechanics: CSV headers, hashing, match rates, CRM-to-Meta sync. This brain only decides WHAT to seed, never how to upload it.
- `brain-meta-website-and-engagement-audiences` owns building the custom audiences themselves (retargeting, recency windows, engagement segments). Here they matter only as lookalike seed material.
- `brain-meta-ads-manual-control-no-advantage` is the verified evidence base; where a source here conflicts with it (Advantage+ suggestion mode), that brain wins. OUT of scope here: upload flows, retargeting strategy, Advantage+ audience settings, broad-targeting doctrine beyond the lookalike comparison. Check it
when a question spans topics.

## Deeper references

- `references/synthesis.md`: full thematic synthesis
- `references/quote-library.md`: verbatim quotes with attribution
- `references/experts.md`: who was mined and why (popular vs hidden-gem)
- `examples/course-lookalike-session.md`: worked Q&A session, the brain applied end-to-end to a first online-course lookalike test

Router key `sk-lndvvx` — resolved by the skills index on load.
