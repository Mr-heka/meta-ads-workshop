# Synthesis: Meta Local Lead Gen (radius/city targeting, small-geo saturation, local event fill)

Built 2026-07-05 from 21 mined transcripts (18 usable after era-flag exclusions, see bottom).
Cross-checked against the verified evidence base in `brain-meta-ads-manual-control-no-advantage/references/synthesis.md`. Where a local-lead-gen source conflicts with that base, the conflict is flagged in the theme and the verified base wins for a small manual account.

---

## Theme 1: Broad radius IS the targeting; the ad does the narrowing (CONSENSUS)

Every credible source in the set runs local lead gen the same way: draw the geography, set a minimum age at most, leave interests blank, and let the creative and copy signal who the ad is for. This matches the verified base (Theme 1: creative-is-the-targeting) exactly.

- **Samuel Darby**: argues Meta's own signal (including off-platform pixel data) knows the buyer better than any interest stack you could build, so the radius plus the creative is enough. *He supports this with a "roughly a million data points per user, told to me by a Facebook engineer at Menlo Park" line — **treat that as unverified folklore, not evidence**. It is second-hand, unattributed, unfalsifiable, and Meta has never published such a figure; it is a rhetorical prop that has circulated in ad-agency talks for years. The broad-targeting case stands perfectly well on the tested results below without it; do not repeat the claim.* Example: one campaign, one ad set, radius around a Canadian town, ages 18-40, 6-7 ads at $200/day, consistently good results, no retargeting.
- **TradeGrowth**: no interest or keyword targeting at all in 2026; the image and copy place the ad. Reports $3.52-$4 CPL as proof.
- **Nick Theriot** ($10M+ on lead ads for one client): enter the city, leave the rest broad; 577 leads in 7 days at ~$2,500/day with this shape.
- **roasbrez**: at typical local budgets ($50-100/day) there is "no reason" to run anything but cold, broad, creative-volume campaigns.
- **Cam Meunier**: the primary text itself feeds Meta's audience matching, so he loads it with website context.
- **Daniel Dimsey**: leaves age and gender fully open; Meta already knows 18-year-olds do not convert on home services.
- **Jonas Olson, Big Little Gyms, Ash Davis, Caden Thompson**: all frame Andromeda as ad-to-person matching that replaced manual audience segmentation.

Contested edge: **Big Little Gyms** still layers income-correlated zip codes and top-10-50% income brackets for gyms, while warning against over-narrowing (keep the audience at 50,000-100,000+). He is the only source in the set still doing demographic layering.

## Theme 2: Radius mechanics: pin-drop, size guardrails, geo leakage control (CONSENSUS on leakage, numbers vary)

Meta serves outside your drawn radius unless you force it not to. Three separate practitioners treat leakage control as the highest-leverage 10-second step in local setup.

- **Daniel Dimsey** (3 videos): drop a pin on the serviced suburb, set the radius, then ring the boundary with exclusion pins, because Facebook delivers outside the drawn area more often than people realise. Calls skipping exclusion zones the biggest new-advertiser mistake.
- **Derek Videll**: untick the "Reach more people likely to respond to your ad" suggestion toggle so the radius is a rule, not a suggestion. Lock age the same way.
- **Big Little Gyms**: layer zip codes on top of the radius; radius-only sometimes pulls people from 50-100 miles away. Supports exclude-pins with a 2-mile radius.
- Radius sizing benchmarks: **TradeGrowth** ~30 miles for a service city, never a whole state; **Big Little Gyms** ~7 miles suburban, 15-20 miles rural, 1-2 miles dense urban; **roasbrez** the furthest distance the business will actually travel for a job; **Cam Meunier** ran a 5-mile and a 2-3 mile ad set simultaneously to compare instead of guessing one.

Verified-base alignment: this is the local twin of the base's untick-use-as-suggestion gotcha (Piliero, from the verified-base brain). Same mechanism, same fix.

## Theme 3: Small-geo saturation: frequency, audience floor, refresh cadence (CONSENSUS on the problem, CONTESTED thresholds)

Small geographies fatigue fast. The set gives three concrete dials.

- **Big Little Gyms**: watch frequency, keep it under roughly 2 per day; flagged "almost three or higher" as saturation risk. Case data: frequency fell from 2.59/2.4 to under 2 and CPL held at $7-9.
- **Daniel Dimsey**: under ~500,000 people in the radius, ads fatigue quickly and CPMs climb; 100,000 is too small, 300,000 is "all right", and below the floor he routes clients to Google Ads instead. (Contested: Big Little Gyms is comfortable at 50,000-100,000+ for gyms.)
- **Ollie The Ad Man**: keep a minimum of 3 ads live (ideally 4-6) so the audience never fatigues on one creative.
- **Aqua Leads**: rotate 2-3 new ad variations per month against the standing winner, judged on CPL inside one ad set; leave a batch alone about a month before culling.
- **Samuel Darby** (sceptic's note): full Andromeda hand-off has not proven durable for him past a few months; a fatigue or data problem persists in the algorithm. Refresh stays on the advertiser.

Verified-base alignment: base says cold frequency max ~2.5 (Heath) and efficiency comes from creative refresh, not knob-turning. Consistent.

## Theme 4: One simple campaign, few ad sets, creative volume inside (CONSENSUS, two competing internal shapes)

Nobody credible in the set builds funnel-stage ad sets or retargeting splits for local any more.

- **Ollie The Ad Man**: one campaign, one ad set, 4-6 ads, campaign-level budget.
- **Caden Thompson**: one campaign, one ad set, pick a single funnel-stage event to optimise toward, add nothing.
- **Samuel Darby**: one campaign, one ad set, cold and warm creatives blended (review/testimonial ads alongside cold hooks).
- **Nick Theriot**: one persistent campaign for years; one client campaign reached $6.5M spend with 192 mostly-historical ad sets inside it. Never recreate campaigns unless the platform forces it.
- **TradeGrowth**: four things only: simple campaign, clear offer, filtering lead form, fast follow-up.

The two competing internal shapes (both post-Andromeda):
- **Samuel Darby's trio structure**: each ad set holds exactly 3 ads grouped by format (statics / UGC / carousel), because Meta's placement bias dumps budget into video and starves images when formats mix. Live example: static-text ad set at £8.99 CPL against a £15-16 target.
- **Nick Theriot's concept structure**: each ad set is one concept with 3 variants differing by a single variable (usually the visual); new concepts uploaded on one designated day per week.

Contested details: **Derek Videll** bans carousel ads for lead gen outright, while Darby runs a carousel trio ad set. Videll says never set an end date (an expired campaign cannot be reactivated); **Big Little Gyms** says set an end date rather than ever pausing manually. Both agree on the underlying rule: never toggle a live campaign off and back on.

## Theme 5: Instant forms vs landing pages (GENUINELY CONTESTED; decided in `brain-meta-instant-forms-vs-lp`)

The sharpest split in the set.

- **Pro instant forms**: Samuel Darby (local buyers act in the moment; leaving Meta loses them), Daniel Dimsey (default for home services), TradeGrowth (single conversion location, never mix website + instant forms), Blake Bauer (native, faster, prefilled; $73 CPL on $4,500/month spend).
- **Pro landing pages**: Ollie The Ad Man (instant forms prefill and produce low-intent leads; his dedicated mobile LP with multi-step form ran 86% mobile traffic, £42/lead on £2,500 spend), Nick Theriot (LP plus JotForm conditional logic so the pixel only ever fires on qualified leads).
- **Middle positions**: Joshua cmb and Caden Thompson frame it as the Hormozi friction dial: less friction = more volume, more friction = better quality. Derek Videll starts every dial at quantity, then walks back toward quality.

**Resolution.** Instant forms versus landing pages is decided in `brain-meta-instant-forms-vs-lp`; read it before choosing. Short version: for cheap, simple offers an instant form with a qualifying question can work; for high-ticket or considered offers, send traffic to a landing page. The landing page still matters either way: it continues the pitch behind the form or carries the form itself.

## Theme 6: Lead quality is engineered at the form, not the audience (CONSENSUS)

Every source that discusses quality uses the same lever set: qualifying questions with conditional logic, placed before contact fields.

- **Samuel Darby**: budget and timeline questions ("How much do you have to invest?" 1K/5K/10K/50K; "When are you looking to invest?" 30 days/3 months/6 months), then segment: under-5K six-months-out gets a free guide only; 10-20K three-months-out gets calls, SMS, email chase.
- **Nick Theriot**: conditional routing to a qualified thank-you page (pixel present) vs an unqualified page (no pixel), so Meta trains only on qualified traffic.
- **Daniel Dimsey**: 3-4 multiple-choice qualifiers plus a mandatory short-answer phone field (min 5, max 20 characters) forcing manual entry, killing stale autofilled numbers.
- **Blake Bauer**: first-position disqualifier ("Are you a homeowner within the Dallas area?") with conditional end pages; work-email filter for B2B forms.
- **Derek Videll**: Higher Intent slide-to-submit review screen yields zero bot leads; state the price threshold as a fact ("are you okay that our starting rate is $7,000 per job") rather than asking an open budget question.
- **Joshua cmb**: any CTA that does not create a contact record first is a bad CTA; capture name and phone before the booking flow.

Contested toggle: **Derek Videll** favours Higher Intent forms; **Daniel Dimsey** and **Blake Bauer** stay on More Volume (Dimsey: the review slider confuses elderly customers). Mirror of the Theme 5 friction dial.

## Theme 7: Speed-to-lead and CRM follow-up is half the system (CONSENSUS, strongest operational theme)

The set is unanimous: the ad account cannot outrun slow follow-up.

- **Jonas Olson** (17-year pest/lawn operator, 17 locations): call within 5 minutes and you win; an hour later the lead is dead. Buyers may need to see you 21-22 times before purchasing.
- **Big Little Gyms**: same ~5 minute window; automated instant text and email plus immediate phone follow-up.
- **Joshua cmb**: no CRM = leads lost; GoHighLevel at $97/month with instant SMS on form submit plus recurring nurture cadences (weekly/30-day/90-day).
- **TradeGrowth**: follow-up within 5 minutes with CRM connected is one of only four required funnel components.
- **Ollie The Ad Man**: post-submit redirect straight to a self-booking calendar page so the lead schedules before competitor quotes arrive.
- **Nick Theriot**: ActiveCampaign sequence, first email 15 minutes after opt-in then every 8 hours for 20-30 emails (~35-40% open rate, ~1% unsubscribe); plus a ThruPlay retargeting campaign of testimonials and objection content to leads from the last 7 days, deliberately high frequency, no CTA.
- **Ash Davis**: owning ads plus funnel plus follow-up is what feeds Meta conversion-to-client signals; lead vendors who never pass downstream data lose the Andromeda advantage.

## Theme 8: Testing thresholds, kill rules and scaling at local budgets (CONSENSUS on method, numbers form a ladder)

- Starting budgets: **Derek Videll** $25/day "the magic number"; **TradeGrowth** $20/day for 1-2 weeks; **Big Little Gyms** $30/day floor, ideally $50; **Samuel Darby** frames the whole tier as $30-35/day (~$1,000/month); **Daniel Dimsey** tiers by country ($50-100/day AU, $35-70 US, £25-50 UK); **Joshua cmb** $20-25/day per creative for a real read.
- Kill thresholds: **Samuel Darby** spend 1-3x target CPL before judging an ad, and judge by impressions per click-step (~2,000-3,000 impressions per ad for a local funnel), not raw spend; **Ollie** kill anything above the breakeven CPL (£50 breakeven, an ad at £60/lead gets cut); **Nick Theriot** 7-day CPL window against target (~$30): cut the $94 ad set, keep the $16.
- Scaling: **Nick Theriot** plus or minus 20% on the last 3 days of data, biased against decreasing; **Samuel Darby** step £30 to £45 to £60/day with 3-4 days between bumps; **Ollie** 10-20% per day when happy, or scale efficiency instead (kill the $150/lead ad, feed the $50/lead ad) when margins are thin.
- Stability rules: **Big Little Gyms** never turn a campaign off and back on, even for minutes.
- Diagnostics: **Samuel Darby** reads CPM as a signal: one outlier ad = creative problem (policy-adjacent keyword, image text penalty); every ad hot = ad-set problem (audience too small, event misconfigured). Facebook's internal confidence threshold is ~1,000 people reached per ad.

Conflict flags: **Ollie's** daily 10-20% bump is faster than the verified base (+20% per 3 days on a 3-day average, never same-day); Theriot's cadence matches the base, side with the base. **Ash Davis** argues post-Andromeda you should NOT kill an ad on cost-per-appointment alone while Meta actively spends on it (his 4-minute video ad produced 1 appointment in 30 days but kept serving, and monthly revenue rose). That contradicts the kill-rule discipline above; treat as a minority take, the kill rule stands.

## Theme 9: Local creative: anti-advertising, owner's face, local call-outs, offer-led copy (CONSENSUS)

- **Ollie The Ad Man**: the "anti-advertising" strategy: 10-20 photos of the owner next to the branded van, the crew, finished jobs with customers. Polished graphic templates read as cowboy-roofer behaviour and get skipped as ads.
- **Daniel Dimsey**: personal face-in-uniform ads print money; copy formula: introduce yourself, years serving the area, a few spots open, unstated discount, outcome-stated headline. Real photos over AI images (Facebook users are scam-wary of obvious AI).
- **Jonas Olson's 7-step framework**: scroll-stop creative (movement, before/after), local call-out ("Hey OKC homeowners"), name the specific pain already seen in that neighbourhood, brief non-technical solution, emotional why (kids, pets, the home asset), neighbourhood-level social proof, one CTA, PS urgency line.
- **Aqua Leads' 7-step video script** for interruption traffic: problem call-out, curiosity confirmation, sell the dream, throw rocks at the enemies, present the opportunity, take it away (disqualify), qualify-framed CTA plus urgency. His three-ad test: $18/$16/$12 CPL, kept the $12, added two new challengers next month.
- **TradeGrowth**: end-result offers beat trust language ("book a free roof inspection before small leaks become expensive" vs "professional reliable service"); the word "free" materially lowers CPL.
- **Ash Davis**: repurposed long-form educational content outperformed straight-sell ads on call quality and show-up rate; clients running content plus ads beat ads-only clients.
- **Samuel Darby**: landing page copy feeds Meta's classifier like on-page SEO; write "we're the top garage installer in this city"... "we've installed garages since 2015", not "we fix garages".

## Theme 10: Local economics: pay for reach, need ticket size, judge on revenue not CPL (CONSENSUS)

- **Ollie The Ad Man**: reframe spend as buying reach and impressions, not leads (100,000 reached, 271,000 impressions, 58 leads, £2,500 spend, £42/lead).
- **Aqua Leads**: Meta is paid per impression; CPL swings come from copy and funnel quality, not competitor clicks ($40 vs $12 CPL on identical targeting). Roughly 1 in 3 viewers, probably fewer, are ready to buy now, hence retargeting via three pixel placements (site, lead-form opens, page) with trust content a few times a week.
- **Joshua cmb**: interruption traffic only works with high average job value; a $10,000 painting job returned 10x on the month's spend, a $100-per-job detailer goes under on the same ads.
- **Big Little Gyms**: self-liquidating higher-ticket front end, not free trials: $200 spend, 20 leads at $10, 1 sale at $400 = 2x on spend while Meta bills in arrears.
- **Jonas Olson**: objective-level CPL benchmarks: click-to-call $15-40/lead (shut off above $100; best for emergencies), lead forms $12-40/lead (best for recurring services), traffic clicks $0.20-0.30 (awareness and retargeting feed only, no immediate ROI).
- **Ash Davis**: post-Andromeda his CPL and cost-per-appointment rose while revenue and ROI rose ($15,000 spend to $51,000 tracked Stripe revenue in his July example); judge the month on revenue, not lead unit costs.
- **Caden Thompson**: keep the optimisation event inside Meta's 7-day attribution window and feed it 15-30 events/month; back-calculate cost-per-sold-lead from pipeline ratios (10 leads at $10 = $100 per sold lead at a 10% close rate) when the true bottom event is too thin to optimise on.

---

## Exclusions

Excluded from the themes above per the era-flag rule (none of the 21 sources were flagged thin):

- **Kyran Rawson**, "How To Run Facebook Ads For SMMA Clients In 2026": era-flagged. Presents pre-Andromeda mechanics (one ad set per creative, evenly split manual budgets, isolated ad-set tests) as current 2026 best practice; Ash Davis and Samuel Darby both describe exactly this structure as superseded.
- **Rich From Anywhere**, "The BEST Way To Run Local Facebook Ads in 2026": era-flagged (soft). Early-Advantage+ setup with interest suggestions and Audience Network on, presented as current without acknowledging the algorithm shift; Audience Network on also conflicts with our verified settings kill-list. His city-exclusion geo-fencing idea survives in Theme 2 through Dimsey and Big Little Gyms anyway.
- **Mike Sherrard**, "The BEST Facebook Ad for Real Estate Agents in 2025": era-flagged in discovery notes, so held out of the themes. Still worth knowing as stable platform constraints rather than tactics: housing ads sit in Meta's Special Ad Category (no age/gender targeting, 15-mile minimum radius), and lead CRMs now connect natively inside Ads Manager without Zapier. His 3-day algorithm patience window and higher-intent form preference echo included sources.
