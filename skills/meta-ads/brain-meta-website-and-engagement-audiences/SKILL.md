---
name: brain-meta-website-and-engagement-audiences
description: "Use when the user asks how to retarget visitors, what video-view percentage or lookback window to use, \"custom vs saved audience\", \"what is use as suggestion\", or needs website, engager, form-opener, or video-viewer custom audiences. Route list uploads to brain-meta-list-audiences-and-crm-sync and lookalikes to brain-meta-lookalikes-and-seeds."
metadata:
  type: expert-brain
  topic: "Meta website and engagement audiences (pixel segments, video views, engagers, recency)"
  aliases: "website custom audiences, WCA, pixel audiences, retargeting audiences, remarketing audiences, warm audiences, video view audiences, video viewers, engagement audiences, page engagers, IG engagers, Instagram engagers, lead form openers, form abandoners, retention windows, recency windows, audience retention, custom audiences, audience segments breakdown, retargeting stack, 7-day stack"
  domain: "meta-ads"
  built: "2026-07-05"
  sources: 10
---

# Brain: Meta website and engagement audiences (pixel segments, video views, engagers, recency)⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

> Built by topic-brain-builder from 10 YouTube sources
> (4 hidden-gem creators surfaced on engagement,
> not views). Made by Selr AI.

## How to use this brain

When the user is working on Meta website and engagement audiences (pixel segments, video views, engagers, recency), load this brain first. Ground answers in
the synthesis below and cite experts by name from the quote library. Prefer the
consensus view; surface a contrarian take when it's well-argued.

## What the experts agree on

1. **Meta auto-retargets inside "cold" campaigns now.** Ben Heath's account data: a campaign with zero custom audiences spent ~40% of $80k on engaged audience plus existing customers, and over half its 942 purchases came from warm segments. Nick Theriot sees the same, identifying retargeting ads only by elevated frequency. (Heath, Theriot)
2. **Custom audiences are still worth building anyway**: they define the Engaged/Existing Customer reporting segments, enable locked retargeting when a message must not reach cold, and mark the boundary of Meta's native memory. (Heath, Rognerud, Jamal)
3. **The lookback limits are hard: lead-form 90 days, website 180 days, page/IG engagers and video viewers 365 days.** Stated independently by Heath, Jamal, Sheldon and Mac with zero disagreement.
4. **Custom audiences sit in "suggestion audience", not controls.** Real retargeting requires "further limit the reach of your ads", then unticking "use as suggestion", or Meta expands past your list. (Heath, V.S.L; matches Piliero in our verified manual-control base)
5. **The 3-second/3% video view is worthless as a signal.** Every source that touches video audiences picks a meaningful watch percentage instead. (Jamal, Mac, V.S.L, Digital Growth Tutor)
6. **Retargeting creative must name the prior action or awareness stage.** Generic re-ads are the number two retargeting mistake (number one is not running retargeting at all). (Sheldon, Theriot, V.S.L)
7. **Read performance through Breakdown > Audience Segments**, after defining Engaged Audience and Existing Customers in Advertising Settings, or you are "optimizing blind". (Rognerud, Heath)

## Named frameworks & methods

- **Shy 255 method** (Neil 'Shoney' Mac): five warm ad sets. 7-day stack (IG + FB page + website, last 7 days, ~5-10% of budget), 30-day stack (same sources, excludes the 7-day stack), website 180 days (Meta's max), video views 25% at 365 days (~25% of budget, his best performer), broad organics 365 (excludes the other four). No pixel? Drop the website layer and run "Shy 245". New audiences populate in ~2-3 hours.
- **The 90/180/365 window map** (Ben Heath, corroborated by Jamal and Sheldon): lead-form 90, website 180, engagers/video 365. Anything older needs an uploaded list (sibling brain).
- **Six-audience system** (Christian Jamal): website (all visitors + converters, 180 days), customer list, video viewers (75% of a 2-minute-plus video), lead form (three build options; openers-not-submitters is "hands-down the warmest retargeting audience in your entire account"), IG engagement, FB page engagement. Plus GHL automation: workflow trigger "tag is added" > action "Facebook add to custom audience", repeatable per pipeline stage.
- **Video-view threshold ladder**: 25% of 15-second-plus videos, most recent 50 (Mac); 50% of one or two chosen videos (V.S.L, Digital Growth Tutor, retention 365 or 30 days); 75% of long-form testimonial video (Jamal). Common floor: never the 3-second tier.
- **Three-step video-view funnel** (V.S.L): 50%+ viewers of awareness video get testimonial ads; full watchers of the testimonial get sales ads. Worked pool: 75,760 completion-viewers.
- **Five aware-stage retargeting angles** (Nick Theriot): new sale/offer, offer ending soon, design going away (only if genuinely true), quantity break with real stock count, new-drop announcement. Warmer product-aware layer: reply-to-comment objection ads, real-customer UGC, contracted authority, feature-based comparisons.
- **Locked-retargeting recipe** (Ben Heath): ad set > Audience > "further limit the reach of your ads" > "switch setup" > add custom audience > confirm "use as suggestion" is NOT ticked.

## Contrarian / disputed takes

- **Separate warm ad sets vs one hybrid.** Heath: one hybrid ad set, because Meta rebalances warm/cold automatically, 50 conversions/week in one ad set beats 25+25, and split ad sets overlap in auction anyway. Theriot: no custom audiences at all, creative does the targeting. Against them: Mac (five-layer stack with exclusions), V.S.L (locked sequenced funnels), Sheldon (dedicated always-on retargeting). Both camps agree on locking the audience when the message must not reach cold.
- **Theriot's Advantage+ audience stance conflicts with our verified base.** brain-meta-ads-manual-control-no-advantage and our campaign playbook run manual campaigns with Advantage+ Audiences OFF. We side with the verified base: keep his creative doctrine, reject his targeting setting.
- **Video watch threshold**: 25% (Mac) vs 50% (V.S.L, Digital Growth Tutor) vs 75% (Jamal). Resolved by video length: short-form supports lower percentages on 15s+ videos; percentage only means real attention on 2-minute-plus videos at the high end.
- **Recency window depth**: Sheldon's flat ~90-day rule of thumb vs Mac's layered 7/30/180/365 architecture vs Heath's "let Meta handle recency inside one ad set".

## Execution playbook

**IF/THEN operating rules**

- IF building any retargeting audience THEN create a Custom Audience, never a Saved Audience; saved audiences trap people "for eternity" while custom audiences roll people out as the window lapses (Mac).
- IF the ad must only reach the warm audience (member offer, upsell, community invite) THEN use the locked recipe: further limit the reach > switch setup > add audience > "use as suggestion" unticked (Heath, V.S.L). Otherwise Meta treats the list as a seed and goes broad.
- IF the audience source is video THEN exclude videos under 15 seconds at the 25% threshold (Mac) and only trust high percentages on videos 2 minutes or longer (Jamal). Never build on 3-second views.
- IF you need people older than the native windows (past attendees, old leads) THEN a pixel or engagement audience cannot reach them; that is list-upload territory (Heath; sibling brain).
- IF the Audience Segments breakdown shows "all unknown" THEN define Engaged Audience and Existing Customers in Advertising Settings via the shortcuts panel first (Heath).
- IF a lead-gen ad is generating traffic THEN retargeting runs year round, not as a bounded burst; the pool refreshes itself with new non-converters (Sheldon).
- IF writing retargeting creative THEN name the exact prior action ("I saw you didn't fill out your form all the way", Sheldon) or match the aware stage with offer/price/urgency only (Theriot). Never fake scarcity or authority (Theriot, twice).
- IF tempted to build a separate retargeting campaign THEN don't; keep conversion volume consolidated and let exclusions do the separation work (Heath, Theriot, consistent with our verified base's consolidation math).

**Default numbers the experts use**

- Lookback maximums: 90 days lead-form, 180 days website, 365 days engagers and video (Heath, Jamal, Sheldon).
- Practical retargeting default: ~90 days (Sheldon); tight recency layer: 7 and 30 days (Mac); short video-view recency: 30 days (Digital Growth Tutor).
- Video thresholds: 25% / 50% / 75% ladder by video length; 15-second minimum video (Mac); 2-minute floor for high percentages (Jamal).
- Budget shares in a layered stack: ~5-10% to the 7-day stack, ~25% to video views 365 (Mac).
- Population time for a new custom audience: ~2-3 hours (Mac); under 24 hours (V.S.L). Wait before judging size.
- Video pool: most recent 50 videos, both FB and IG sources in one audience (Mac).

**Pre-flight checklist**

1. Pixel firing and events verified before building website audiences (Mac's fallback: no pixel history, skip the website layer).
2. Audiences created as Custom, not Saved; retention window set deliberately, not left on default by accident.
3. Naming carries threshold + window + creation month (e.g. "50% video viewers 30 days", "June 25") (Digital Growth Tutor, Mac).
4. Engaged Audience and Existing Customers defined in Advertising Settings so segment reporting works (Heath).
5. For locked ad sets: "use as suggestion" confirmed unticked after saving (Heath).
6. Exclusions set: converters excluded from visitor retargeting (Jamal); tighter recency layers excluded from wider ones (Mac).
7. Retargeting creative references the specific prior action; no fake scarcity, no invented authority (Sheldon, Theriot).

**Top 5 failure modes and fixes**

1. **Retargeting ad set silently goes broad.** "Use as suggestion" left ticked, or Advantage+ audience never switched off. Fix: locked recipe, verify the toggle (Heath, V.S.L).
2. **Saved Audience used for retargeting.** People never exit the pool, recency dies. Fix: rebuild as a Custom Audience (Mac).
3. **Video audience built on junk signal.** 3-second views or 25% of a 6-second clip. Fix: threshold matched to video length, 15s minimum, 2-minute floor for high percentages (Mac, Jamal).
4. **Generic retargeting creative.** Same ad cold and warm, nothing acknowledging the visit or form-open. Fix: direct callout of the drop-off action, or aware-stage offer/urgency messaging (Sheldon, Theriot).
5. **Optimising blind on blended numbers.** Warm conversions credited to cold creative because segments were never defined. Fix: define segments, review Breakdown > Audience Segments before kill/scale calls, and remember Meta under-reports (Heath's £58k unreported; Rognerud).

## Applied to your business

Fill these in first: ad account `<YOUR_AD_ACCOUNT_ID>`, pixel `<YOUR_PIXEL_ID>`, CRM `<your CRM>`, site stack `<your funnel builder>` plus `<your custom site, if any>`, and your offer list with prices.

**Which of your offers this feeds**

- **A warm-only or membership offer:** retargeting (site visitors, video viewers, buyer-adjacent pools) is its entire paid role, and this brain is the mechanics manual for it.
- **A location-locked or event offer:** landing-page visitors who did not register are your openers-not-submitters segment, and recency stacks fit a campaign that runs for a few weeks and then ends.
- **A video-led offer (VSL or long-form sales video):** video-view audiences at 75% watched, per Jamal's long-form rule, once that video is actually live.

**Execution moves**

1. **Build the foundational set on `<YOUR_PIXEL_ID>` now**: website visitors 180 days (type 180 in the retention field, the default is 30), converters and purchasers, Instagram and Facebook engagers 365, video views 25% at 365 (Rognerud's four-pool logic, Mac's windows). Windows only start paying once the audiences exist, so build them before you need them.
2. **Define Engaged Audience and Existing Customers in Advertising Settings**, then judge every campaign through Breakdown > Audience Segments so warm conversions stop flattering cold creative (Heath, Rognerud).
3. **Run retargeting LOCKED**: further limit the reach, "use as suggestion" unticked. Member or upsell messaging must never leak to cold audiences (Heath's exact locked-retargeting scenario).
4. **Add a recency layer**: a 7/30-day stack (Mac) of landing-page visitors minus registrants, with Sheldon-style callout creative that names the drop-off out loud ("you looked at `<your event or offer>` and didn't grab a spot"). Keep it inside the existing campaign rather than spinning up a new one (Heath's consolidation rule).
5. **Wire tag-triggered audience sync from your CRM** (Jamal's build): tag added > Facebook > add to custom audience, one per stage (lead, attendee, member). This keeps purchaser exclusions and warm pools current with no CSV work.

**What may NOT apply to you**

- **Theriot's Advantage+ audience / no-custom-audiences setup**: if you run manual campaigns with Advantage+ Audiences off, his creative-by-awareness-stage thinking transfers but the setting does not.
- **Lead-form engagement audiences**: only if you run instant forms. If you do, build openers-not-submitters audiences (90-day cap) per form; Jamal calls that the warmest audience in the account.
- **Messenger-page audiences and older-skew page-first tactics** (Jamal): skip unless Messenger is genuinely one of your channels.
- **Discount and flash-sale retargeting angles** (Theriot's Valentine's sale pattern): if your urgency is real dates, venues or genuinely expiring pricing, use that instead of manufactured discounts. Never promise outcomes or refunds in retargeting copy.
- **Lookalike sizing tiers and list-upload row minimums** (Jamal): sibling-brain territory, routed to `brain-meta-lookalikes-and-seeds` and `brain-meta-list-audiences-and-crm-sync`.

## Related brains

- `brain-meta-audiences-2026`: Meta ads audiences 2026 (the full audience system survey)
- `brain-meta-exclusion-architecture`: Meta ads exclusion architecture (exclusions, overlap control, funnel sequencing) Check it
when a question spans topics.

## Pairs with / boundaries

- `brain-meta-audiences-2026` is the umbrella survey; this brain is its deep-dive on pixel, video, engager and recency audiences. Route broad-vs-interests and audience-size doctrine questions up to the umbrella.
- Exclusion mechanics (who to remove, overlap control, funnel sequencing) belong to `brain-meta-exclusion-architecture`; this brain only notes where an exclusion is part of an audience build.
- Customer list uploads, CSV hygiene and match rates belong to the list-audiences sibling; lookalike percentages and seeds belong to the lookalikes sibling.
- OUT of scope here: campaign structure and budget doctrine (brain-meta-media-buyer-manual / brain-meta-ads-manual-control-no-advantage), CAPI plumbing (brain-meta-capi-server-side-deep), creative production (brain-meta-creative-strategist-manual).

## Deeper references

- `references/synthesis.md`: full thematic synthesis
- `references/quote-library.md`: verbatim quotes with attribution
- `references/experts.md`: who was mined and why (popular vs hidden-gem)
- `examples/retargeting-session.md`: worked Q&A built only from verbatim quotes

Router key `sk-1ih8yis` — resolved by the skills index on load.
