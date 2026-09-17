# Worked session: fill a local workshop

A complete Q&A session showing this brain loaded against one worked scenario and answering end-to-end. Every expert quote below is copied verbatim from `references/quote-library.md`; every paraphrased claim names its expert. Account-specific placeholders come from the "Applied to your business" section of SKILL.md — swap in your own before using any of it.

Account IDs and internal CPL figures were removed 2026-07-28; the numbers below are illustrative of the *method*, not benchmarks to hit.

**Scenario.** The next in-person AI Workshop ($2,000 inc) is running in one host city, sold to non-technical business owners in the city's draw area. A CRM is wired. Ad account `<YOUR_AD_ACCOUNT_ID>`, pixel `<YOUR_PIXEL_ID>`, CAPI with the Purchase event verified live.

**Trigger fired:** "fill the [city] workshop" (canonical trigger in the SKILL.md description). Brain loaded before any campaign work started.

---

## Q1. "The city workshop is coming up. Build the Meta campaign to fill the room."

### Structure: one campaign, creative volume inside

The consensus shape, no funnel-stage ad sets, no retargeting splits:

> "we want one campaign with one ad set and then you're starting off with about four to six ads within that ad set." - Ollie The Ad Man, *How To Get 60 Roofing Leads A Month With Meta Ads - 5 Step Framework*

And once it exists, it persists:

> "We just continue to operate out of that single campaign. We don't keep creating new campaigns." - Nick Theriot, *How I Run Facebook Ads For High Quality Leads (2025)*

For us: one city campaign, CBO $50/day per the doctrine in SKILL.md, 4-6 ads live, cold and proof creatives blended in the one ad set (Samuel Darby's pattern). Manual control, original audiences, Audience Network off, per our verified base. Detailed targeting stays blank; the ad copy does the narrowing.

### Radius: pin the venue city, then seal the boundary

Per the campaign playbook cited in SKILL.md, the workshop city gets a locked 40-50km radius. TradeGrowth's paraphrased benchmark for a service city is about 30 miles, never a whole state, so 40-50km sits inside expert range. Then the leakage controls, in order of effort:

> "probably one of the biggest mistakes that most new advertisers make when it comes to running Facebook ads is they don't put in exclusion zones" - Daniel Dimsey, *How I Run Facebook Ads for Car Detailing in 2026 (NEW STRATEGY)*

> "what you want to do is tap on drop pin and then just drop another pin outside of your targeting location" - Daniel Dimsey, *How I Run Facebook Ads for Car Detailing in 2026 (NEW STRATEGY)*

> "But you're going to offclick this if you want to treat these circles as a rule. If you want Facebook to have the ability to show an ad in Longmont... I would allow Facebook to determine if it's worth it to show outside of my circles." - Derek Videll, *Get High Quality Leads with Meta Ads (FULL 2026 COURSE)*

So: pin on the host city, ring the radius with exclusion pins, untick the location suggestion toggle so the circle is a rule. Before launch, check the audience-size estimate in Ads Manager against Daniel Dimsey's paraphrased comfort floor of roughly 500,000 people in the radius; below that he routes clients to Google Ads because fatigue arrives fast.

### Destination: landing page, not instant form

The expert set splits here. Samuel Darby argues for the form:

> "my preference is to use the lead form especially for local because a lot a lot of the local inquiries people are in the moment there and then" - Samuel Darby, *META ADS Veteran Reveals Working Andromeda Strategy For Local Lead Gen*

Ollie The Ad Man argues the other way:

> "instead of sending them to a an onplatform Meta lead form and instead of sending them to a website where they can get lost and click on loads of different tabs and read loads of stuff about you and not actually take any action, we're going to send them to a dedicated landing page." - Ollie The Ad Man, *How To Get 60 Roofing Leads A Month With Meta Ads - 5 Step Framework*

Instant forms versus landing pages is decided in `brain-meta-instant-forms-vs-lp`; read it before choosing. Short version: for cheap, simple offers an instant form with a qualifying question can work; for high-ticket or considered offers, send traffic to a landing page. Whichever you choose, wire it to the CRM before it goes live and keep the landing page continuing the pitch.

### Lead quality: engineer it at the form

> "I recommend adding in three to four different questions here because it will qualify them as a real lead" - Daniel Dimsey, *How I Run Facebook Ads for Car Detailing in 2026 (NEW STRATEGY)*

> "This way they will manually type out their phone number here and it will severely reduce you getting dud leads at all" - Daniel Dimsey, *How I Run Facebook Ads for Car Detailing in 2026 (NEW STRATEGY)*

Applied: qualifying fields on the workshop LP in the Darby pattern named in SKILL.md (business type, team size, timeline) before contact fields, phone entered manually, so the CRM can segment fast-follow registrants from nurture. Nick Theriot's principle explains why it matters for the pixel:

> "Because there's no Facebook pixel on it, it's like nothing even happened. They failed their information, but nothing happened. No data was sent back to Facebook." - Nick Theriot, *How I Run Facebook Ads For High Quality Leads (2025)*

Qualified traffic is what your pixel should learn from, and with Purchase firing through CAPI, the qualified-signal loop now runs all the way to the sale.

### Follow-up: the campaign is only half the machine

> "If you call within the first five minutes, you'll win. But as you wait an hour or the next day, the lead is already dead." - Jonas Olson, *This Facebook Ads Strategy BLEW UP My Home Service Business (Copy Me)*

> "Wait, you haven't booked in yet. Next step, book a time for your free property visit on the calendar below. After booking, you'll be sent a confirmation email." - Ollie The Ad Man, *How To Get 60 Roofing Leads A Month With Meta Ads - 5 Step Framework*

We keep Ollie's redirect mechanic and swap his copy: our compliance walls ban "free" giveaway hooks, so the post-submit page pushes straight to checkout or booking with plain next-step language. The CRM fires instant SMS and email on submit; a human follows up the same business hours, built to Jonas Olson's 5-minute standard.

### Creative: anti-advertising, translated to a workshop

> "you actually want your ads to not look like ads at all. And this is why it's called the anti-advertising strategy." - Ollie The Ad Man, *How To Get 60 Roofing Leads A Month With Meta Ads - 5 Step Framework*

> "Your ad has a job above anything else, and that's to get them to stop scrolling. If you don't grab their attention within the first two to three seconds, nothing else really even matters." - Jonas Olson, *This Facebook Ads Strategy BLEW UP My Home Service Business (Copy Me)*

Applied per SKILL.md: real room photos, real attendees building, presenter-at-the-laptop shots, city-named call-outs ("[City] business owners"), never polished agency templates. The pattern that repeats across accounts is that the native, in-the-room register beats the polished testimonial cut by a wide margin on cost per lead — often several times over. Record your own two numbers rather than trusting anyone else's.

### Kill and scale rules, written down before launch

> "You need an ad to spend, I would say, approximately one to three times your target cost per lead before you can ultimately say that ad is no longer working." - Samuel Darby, *Maximise META Leads With Only $30 A Day [Full Andromeda Testing Guide]*

> "All we do to increase or decrease budget is just simply look at the last 3 days of data. And then I just increase that ad spend by 20% up or 20% down." - Nick Theriot, *How I Run Facebook Ads For High Quality Leads (2025)*

Our doctrine (SKILL.md): kill at 3x target CPL after 7 days on a lifetime view, scale plus or minus 20% per 3 days on a 3-day average, never same-day. Samuel Darby's paraphrased impression rule gives the fair-read floor: roughly 1,000 impressions per click-step, so 2,000-3,000 impressions per ad before judging a local lead funnel.

---

## Q2. "Registrations are coming in from Ballarat and Geelong. They will not drive in for a Saturday workshop. Fix it."

Classic geo leakage, failure mode 1 in the playbook. Big Little Gyms saw the same pattern:

> "we tend to find that we get better local targeting when we do that versus like if you only set the radius, sometimes it pulls people in from outside the radius and people from like 50 100 miles away are seeing your ads" - Big Little Gyms, *Facebook Ads for Gyms: The Ultimate Step-by-Step Guide*

Fix in the brain's stated order of effort: exclusion pins ringing the boundary first (Daniel Dimsey), then verify the location suggestion toggle is unticked (Derek Videll), then layer postcode lists over the radius (Big Little Gyms). No campaign rebuild, and never toggle the live campaign while doing it:

> "you never want to turn a campaign on and then turn the same campaign right back on. Even if it's for a few minutes" - Big Little Gyms, *Facebook Ads for Gyms: The Ultimate Step-by-Step Guide*

---

## Q3. "Week 3: CPL has doubled. Do we raise the budget to hold lead volume?"

No. In a small geography a climbing CPL is a saturation signal, and the lever is creative, not spend.

> "Frequency is a really really important number a lot of people ignore. Frequency is the rate at which people see your ad." - Big Little Gyms, *Facebook Ads for Gyms: The Ultimate Step-by-Step Guide*

Big Little Gyms' paraphrased thresholds: keep frequency under roughly 2, act by 2.5-3. The brain's IF/THEN rule is explicit: if frequency crosses ~2.5 or CPL is climbing in a small city, ship new creative concepts, do not raise spend. Your own local fatigue history is the proof to record (SKILL.md asks for it): CPL climbing several-fold across a month while creative sat still is the pattern to watch for. Ollie The Ad Man frames the move:

> "if our cost per lead isn't where we want it... instead of scaling the spend, we're going to scale efficiency, which means lowering down our cost per lead." - Ollie The Ad Man, *How To Get 60 Roofing Leads A Month With Meta Ads - 5 Step Framework*

Action: new 3-2-2 DCT concepts into the existing campaign per our weekly refresh doctrine, keep 4-6 ads live, judge each new ad only after Samuel Darby's 1-3x target CPL spend threshold.

---

## Where each answer came from

- Verbatim quotes: `references/quote-library.md` (themes: radius mechanics, simple structure, instant forms vs landing pages, lead quality filters, speed-to-lead, testing and kill rules, local creative style, small-geo saturation).
- Account doctrine and numbers (daily budget, 40-50km radius, funnel shape, kill and scale rules, local fatigue history): SKILL.md, Applied to your business.
- Nothing in this session was invented; anything not in the brain was left out of the answer.
