# Worked example: first lookalike test for an online course

A complete session showing this brain loaded against a realistic scenario and
answering end-to-end. Every quote below is copied verbatim from
`references/quote-library.md` with the same attribution; every number traces to
the SKILL.md playbook or the Applied-to-our-business section. Nothing new is
introduced here.

## Scenario

A business sells a $500 online course to non-technical business owners,
nationally, from a single ad account `<YOUR_AD_ACCOUNT_ID>` with pixel
`<YOUR_PIXEL_ID>`. A CRM holds the buyer records, and both CAPI and the Purchase
event have been verified as firing. The proven broad-plus-soft-interest control
runs at roughly $3-$10 CPL. On the table: should the next course campaign test a
lookalike, and if so, built from what?

## The session

### Q1. "Are lookalikes even worth testing for the course, or do we just stay broad?"

Load the brain, answer from the live debate as reported, not from a hot take.
The expert position is genuinely split:

> "Not everybody likes look alike audiences, by the way. Some people say they're dead, but I have seen some success with them" - EfesAdLab, *Facebook Audiences - Custom, Lookalike & Saved (Ep. 3) | Meta Ads for Beginners 2026*

> "I've had plenty of times where look alikes have literally saved the day, where it's cut my cost per conversion in half" - Andrew Southworth, *Will Lookalike Audiences Make Your Music Meta Ads Better?*

Our verified base (`brain-meta-ads-manual-control-no-advantage`) says lookalikes
are dead as PRIMARY levers; creative is the targeting. So: yes, test it, but
only as a challenger. Broad stays the control, and the lookalike enters as
separate ad sets that have to beat that control on CPL. The $500 course is the
right offer for the test: AU-wide geography suits the percentage maths, where a
city-radius $2,000 workshop campaign would clip a national similarity slice
down to almost nothing. The workshop is seed donor, not seed consumer.

### Q2. "What do we seed it from? There are 3,900+ contacts in the CRM."

Not the 3,900. Seed quality is the whole game:

> "if the source sucks, the lookalike sucks. Or if the source is not relevant to the campaign you're running, the look alike is not going to be relevant" - Andrew Southworth, *Will Lookalike Audiences Make Your Music Meta Ads Better?*

Christian Jamal's filter is the sharpest in the set:

> "upload the list of your top 25% of customers by revenue. The people who spent the most. The repeat buyers. The ones with the highest lifetime value" - Christian Jamal, *How to Create a Lookalike Audience on Meta in 2026 (The Right Way)*

> "there's a massive difference between someone who fills out a form and someone who pulls out their credit card to pay you. You want Meta to find you more of the second group" - Christian Jamal, *How to Create a Lookalike Audience on Meta in 2026 (The Right Way)*

Translated to our stack: export closed-won from the CRM, paid $2,000 workshop
attendees and $500 course buyers, and seed from that list only. Never the full
contact database, never all leads.

The contested edge is on record: Paul Chinedu Nnamani reports his best-ever
conversion run seeding from roughly 15,000 CRM leads spanning 3 years. A big
lead list can work, but buyers-first has more backers and stays our default;
the all-leads version is at most a later, clearly-labelled test.

Pixel-event seeds (Purchase) are on the table once CAPI and the Purchase event
are verified as firing, but the rule is to let the Purchase event accumulate
enough volume to seed from first. The CRM buyer list stays the reliable default
until that volume builds. Upload mechanics (CSV headers,
hashing, match rates) belong to `brain-meta-list-audiences-and-crm-sync`, not
this brain.

### Q3. "What percentage tier? Just do 1%?"

Contested, so run the spread instead of picking a side. Jamal calls 1% the
general default everybody uses and it has worked for him, but the broad camp
disagrees:

> "Smaller lookalike audiences used to perform better before iOS 14, but after that the broader you go, the better they tend to perform. And that is the dream like being able to target broad" - EfesAdLab, *Facebook Audiences - Custom, Lookalike & Saved (Ep. 3) | Meta Ads for Beginners 2026*

The spread test dissolves the argument:

> "I would recommend if you don't want to test all them at once, create a 1%, create a 5%, and create a 10%. So that's going to give you the biggest spread" - Blake Bauer Business, *Facebook Ads Lookalike Audience Tutorial 2026 (Still Worth It?)*

And never stacked in one ad set:

> "how are you going to know which one is actually working if you put them all together, right" - Christian Jamal, *How to Create a Lookalike Audience on Meta in 2026 (The Right Way)*

Build: three challenger ad sets, 1% AU, 5% AU, 10% AU, one lookalike each,
alongside the broad control ad set. Remember the percentage is literal maths, a
rank-ordered similarity slice of the selected country:

> "if there are 278 million people available to target inside the US, a 1% lookalike means the most similar 2.78 million people to your source custom audience" - EfesAdLab, *Facebook Audiences - Custom, Lookalike & Saved (Ep. 3) | Meta Ads for Beginners 2026*

### Q4. "Any Ads Manager settings to watch?"

Four, straight off the pre-flight checklist.

**1. Hard boundary, not suggestion.** Deploy via the manual "further limit the
reach" toggle (Blake Bauer Business). Jamal argues the opposite:

> "With Advantage Plus campaigns, Meta treats your audience section as a suggestion, not a hard boundary" - Christian Jamal, *How to Create a Lookalike Audience on Meta in 2026 (The Right Way)*

That workflow conflicts with our verified base: manual campaigns only,
Advantage+ Audiences OFF, and the documented gotcha that suggestion mode turns
your list into a broad seed. The verified base wins. Hard boundary, or skip
lookalikes.

**2. Strip the interests.** The lookalike IS the targeting:

> "I would leave all of that though. I would try to, you know, limit the country, limit the age range for sure and the gender if that's applicable, but don't add in any interest beyond that" - Blake Bauer Business, *Facebook Ads Lookalike Audience Tutorial 2026 (Still Worth It?)*

Keep country (AU), a broad age band, gender only if relevant. Nothing else.

**3. Business Manager account.** Customer-list lookalikes need one:

> "By the way, you can't do this with personal ad account. You must have a business manager." - Paul Chinedu Nnamani, *How to Create Lookalike Audience in Facebook Ads (Using Your Customer List 2026)*

Confirm `<YOUR_AD_ACCOUNT_ID>` sits under a Business Manager in pre-flight.

**4. Wait for population.** New lookalikes start at 0 and grow. Nnamani allows
up to 24 hours and waits for "ready"; Southworth waits for a real estimated
size before spending a dollar.

### Q5. "When do we call it?"

Judged on CPL against the broad control, killed at 3x target CPL after 7 days
per the campaign playbook kill rule. Whatever the result, the record is
EfesAdLab's client-facing rule:

> "If your client asks like, \"Why are you not using lookalike audiences?\" It is much better to say, \"Because we tested it and it failed.\" Compared to someone on YouTube said, \"Do not use it.\"" - EfesAdLab, *Facebook Audiences - Custom, Lookalike & Saved (Ep. 3) | Meta Ads for Beginners 2026*

If a tier beats the control, keep it, and note Southworth's observation:

> "as your custom audiences get bigger and better over time, your lookalike audiences are going to get more and more useful because more high quality data means better algorithmic models" - Andrew Southworth, *Will Lookalike Audiences Make Your Music Meta Ads Better?*

A monthly community membership and a high-ticket consulting offer stay out of this entirely:
warm-only and outbound respectively per the playbook.

## What this session demonstrates

- Consensus answered first; contested takes surfaced and resolved against the
  verified base rather than by fiat.
- Every quote is verbatim from `references/quote-library.md`; every number
  traces to SKILL.md.
- Boundaries respected: seed selection decided here, upload mechanics deferred
  to `brain-meta-list-audiences-and-crm-sync`.
