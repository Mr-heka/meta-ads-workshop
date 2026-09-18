# Synthesis: Meta website and engagement audiences (pixel segments, video views, engagers, recency)

Built 2026-07-05 from 10 sourced videos, 8 usable after exclusions (see bottom).
All sources inside the 12-month freshness window. Cross-checked against the verified
evidence base in `brain-meta-ads-manual-control-no-advantage/references/synthesis.md`;
conflicts flagged inline and the verified base wins.

---

## Theme 1: Meta now auto-retargets inside nominally cold campaigns (CONSENSUS among strategy sources)

The defining post-Andromeda fact: warm delivery happens whether you build for it or not.

- **Ben Heath** showed live account data: a campaign with zero custom audiences and open US targeting spent just under $80k, with only $47-48k on genuinely new audience. Roughly 40% of spend went to engaged audience plus existing customers, and more than half of the 942 purchases came from those warm segments, at a lower cost per purchase than new audience.
- **Nick Theriot** runs retargeting inside the same single CBO campaign as everything else (account at ~$3,600/day, $26 cost per purchase trailing 7 days) and identifies retargeting ads after the fact by their higher frequency, not by a targeting label.
- Both conclude the old top/middle/bottom-funnel campaign split is largely obsolete: Meta finds the warm pools itself.

**Consensus** between the two highest-authority sources in the set. The tutorial-tier builders (V.S.L, Shoney Mac, Sheldon) still build separate warm ad sets; see Theme 10 for the dispute.

## Theme 2: Custom audiences are still essential to build, even when Meta auto-retargets (CONSENSUS)

Nobody in the set says "stop building audiences". Even the consolidators keep them for three jobs.

- **Ben Heath**: (1) you cannot define Engaged Audience and Existing Customers segments for reporting without them, (2) some scenarios still need locked retargeting (customer-only offers, ascension messaging), (3) uploaded external data fills the gap beyond Meta's native lookback limits. The pixel stays mandatory regardless, for conversion tracking alone.
- **Jon Rognerud**: build four foundational custom audiences first (website visitors, Instagram engagement, Facebook page engagement, customer list) as data pools that feed Meta clean signal, not just as direct retargeting targets.
- **Christian Jamal**: the website custom audience is "probably the most valuable in your entire account"; his standard build is two audiences at 180 days, all visitors plus converters, retarget the first while excluding the second. Cited client result: SPF Screens over $1M revenue by month 5 at 3.1x ROAS with a meaningful chunk from that retargeting layer.

**Consensus.** The dissent is only Theriot, who runs no custom audiences at all (see Theme 10).

## Theme 3: The hard retention-window limits: 90 / 180 / 365 days (CONSENSUS on the numbers)

Meta's maximum lookback per source, stated identically across independent sources:

- **Lead form engagement: 90 days max** (Ben Heath; Jake Sheldon independently: "If anyone's come through a lead form, it only goes back 90 days anyway").
- **Website visitors: 180 days max** (Ben Heath; Christian Jamal builds at 180; Shoney Mac calls 180 "the max window Meta allows" for website audiences).
- **Facebook page and Instagram engagers: 365 days max** (Ben Heath; Christian Jamal notes engagement audiences update daily inside that window and each interaction type, likes, comments, saves, follows, DMs, profile visits, can be isolated).
- **Video viewers: 365 days** (Christian Jamal: Meta sorts video watch data "in a 365-day window, which is double what most custom audiences actually allows"; V.S.L leaves video retention at the 365 default).
- Beyond these windows Meta has no native visibility, so uploaded lists are the only way to reach older customers or engagers (Ben Heath). List uploads themselves belong to the list-audiences sibling brain.
- **Jake Sheldon's** practical default sits inside the limits: about 90 days as the retargeting rule of thumb for most sources.

**Consensus.** No source contradicts another on a single number.

## Theme 4: Video-view audiences: the best warm source, but the threshold is contested

- **Shoney Mac** calls his 25%-of-video audience (365 days, most recent 50 videos) his single best-performing warm audience across lead magnet funnels and live workshops: lowest cost per lead and highest lead volume of his five stacks. Rule: exclude videos under 15 seconds, because 25% of a 5-second video is ~1.25 seconds of meaningless signal. You can combine Facebook and Instagram videos into one audience by switching source tabs without deselecting prior picks. Label the audience with its creation month to track how backdated the video pool is.
- **V.S.L** and **Digital Growth Tutor** both build at the 50% watch threshold. V.S.L combines two source videos and leaves retention at 365 days; Digital Growth Tutor demonstrates a 30-day retention example for tighter recency.
- **Christian Jamal** goes higher again: a 75% watch audience off a long-form testimonial or case-study video, then direct conversion ads to it. His floor rule: percentage thresholds only mean anything when the video is at least 2 minutes long. Watch-percentage options in the builder run from 3% to 95%.
- **Anti-consensus point everyone shares**: the 3-second / 3% view is worthless. Jamal: "a 3-second view tells you absolutely nothing about that potential lead."

**Contested on threshold (25 vs 50 vs 75), consensus on principle**: pick a percentage that represents real attention relative to video length, never the 3-second tier.

## Theme 5: The "use as suggestion" toggle decides whether retargeting is real (CONSENSUS, cross-verified)

- **Ben Heath**: custom audiences sit in the "suggestion audience" part of targeting, not the "controls" section (hard constraints like location). Meta can target your warm audience or ignore it. For a genuinely locked retargeting ad set: Audience > "further limit the reach of your ads" > "switch setup" (Meta shows warnings), add the custom audience, and make sure "use as suggestion" is NOT ticked, otherwise it silently reverts to hybrid behaviour.
- **V.S.L** teaches the same mechanic from the builder side: Advantage+ audience must be manually turned off before the custom-audience selector even appears ("further limit the reach of your ads" > Continue), and the "will also reach similar audience when it's likely to improve performance" toggle must stay unticked.
- **Cross-check with our verified base**: this matches Piliero's gotcha in brain-meta-ads-manual-control (untick "use as a suggestion" on retargeting lists or Meta turns your list into a broad seed). Fully consistent, no conflict.

**Consensus**, and the single most load-bearing UI detail in this brain.

## Theme 6: Recency layering: stack audiences by how recently they acted (attributed method, partially contested)

- **Shoney Mac's "Shy 255 method"**, the only fully-specified recency architecture in the set: five warm ad sets. (1) 7-day stack: IG + FB page + website visitors last 7 days, ~5-10% of budget, his "favorite adset of all time". (2) 30-day stack, same three sources, excludes the 7-day stack. (3) Website 180 days. (4) Video views 25% at 365 days, ~25% of budget. (5) Broad organics 365 (IG + FB engagers) excluding the other four. Exclusions between layers are for clean attribution, not overlap-cost fear. No pixel or traffic history? Drop the website audience and run four ("Shy 245"). New custom audiences take roughly 2-3 hours to populate.
- **Jake Sheldon** runs a simpler recency posture: ~90 days lookback, retargeting always on year round, because ongoing lead-gen ads keep refilling the pool with fresh non-converters.
- **Digital Growth Tutor** shows the short-recency variant: 50% video viewers at 30-day retention for a tight, recent pool.

**Contested on granularity**: Mac's five-layer stack vs Heath's position that Meta reallocates across warm recency automatically inside one hybrid ad set (Theme 10). The window numbers themselves are uncontested.

## Theme 7: Openers-who-didn't-submit are the warmest audience in the account (CONSENSUS between the two who cover it)

- **Christian Jamal**: lead-form audiences have three build options and most advertisers use only "submitted". People who opened but didn't submit are "hands-down the warmest retargeting audience in your entire account"; retarget them with a different angle or stronger offer. Submitted leads become seed material (lookalike ground, sibling brain).
- **Jake Sheldon**: his personal favourite retargeting source is people who came from an ad but didn't submit the form, his lowest cost per lead and acquisition; second favourite is website visitors who didn't convert.
- Remember the constraint from Theme 3: lead-form audiences only reach back 90 days.

**Consensus.** Note for LP-only advertisers: the equivalent segment is landing-page visitors minus converters.

## Theme 8: Retargeting creative must name the prior action or awareness stage (CONSENSUS on principle)

- **Nick Theriot** organises retargeting by the 5 stages of market awareness, not funnel position. Aware-stage (bottom) creative needs only offer, price, urgency, discount. His five bottom-funnel angles: new sale/offer, offer ending soon, design-going-away (only if genuinely limited), quantity break with a real stock count, and new-drop announcements. Product-aware (warmer middle) creative handles objections: reply-to-comment ads, real-customer UGC, contracted authority figures, feature-based competitor comparisons. Twice-repeated ethics warning: never fake scarcity or authority; faking a doctor endorsement risks lawsuits and wire fraud.
- **Jake Sheldon**: the second biggest retargeting mistake is generic messaging. His fix is the direct callout: "Hey, I saw that you didn't fill out your form all the way. What happened? Here's an extra discount," the cart-abandonment pattern applied to lead gen. The first biggest mistake is not running retargeting at all.
- **V.S.L** sequences the same idea across video: 50% viewers of an awareness video get testimonial ads, full watchers of the testimonial get the sales ad. A three-step video-view funnel (his worked example pool: 75,760 completion-viewers of one awareness video).

**Consensus**: the audience mechanics only pay off when the message acknowledges what the person already did.

## Theme 9: The Audience Segments breakdown is the reporting layer that makes all of this visible (CONSENSUS)

- **Jon Rognerud**: campaign view > Breakdown > Audience Segments. Compare cost per lead, cost per purchase, conversion rate and ROAS by segment; "If you're not reviewing segment breakdowns, well, you're basically optimizing blind here." It also exposes whether prospecting campaigns are wastefully hitting existing customers.
- **Ben Heath**: same report, plus the setup step most people miss. If it shows "all unknown", go to Advertising Settings and define Engaged Audience and Existing Customers via the shortcuts panel, selecting custom audiences (e.g. all website visitors 180 for engaged; a customer list or purchase-event-triggered audience for existing). This is a second reason custom audiences must exist even in a fully consolidated account.
- **Ben Heath's** attribution caveat when reading the numbers: Hyros tracked £96,000 generated from one campaign of which £58,000 was not reported by Meta at all, largely recurring billing Meta cannot see. Segment ROAS is directional, not gospel.

**Consensus.** The two sources describe the same feature independently.

## Theme 10: Separate warm ad sets vs one hybrid: the structural dispute of the set (CONTESTED)

- **Consolidation camp. Ben Heath**: default to one hybrid ad set mixing warm and cold. Reasons: Meta reallocates budget dynamically as warm pools grow; one ad set at 50 conversions/week optimises better than two at 25 each; separate warm and cold ad sets end up in auction overlap reaching the same people anyway because custom audiences are only suggestions. **Nick Theriot** goes further: no custom audiences at all, Advantage+ audience on, "We're allowing the creative to do the targeting for us." Facebook's creative analysis (words spoken, on-screen text, who is shown) substitutes for manual audience selection.
- **Separation camp. Shoney Mac**: five explicit warm ad sets with layered exclusions and per-layer budget shares. **V.S.L**: locked video-view audiences in sequenced funnels. **Jake Sheldon**: dedicated always-on retargeting with source-specific messaging.
- **Resolution both camps accept**: lock the audience (Theme 5 mechanics) when the message genuinely must not reach cold, e.g. customer-only offers or upsell/ascension creative (Heath's own exception).
- Related trap from **Shoney Mac**: use Custom Audiences, never Saved Audiences, for retargeting. Custom audiences let people flow out when the window lapses; a saved audience traps them "for eternity". He calls this a major way people mess up the setup.

**CONFLICT FLAG vs our verified base**: Theriot's "Advantage+ audience, no custom audiences" recommendation conflicts with the manual-control doctrine in brain-meta-ads-manual-control-no-advantage and our campaign playbook (Advantage+ Audiences OFF, switch to original). Heath's hybrid default also leans on suggestion-audience expansion, the same mechanism our kill-list disables on cold campaigns. We side with the verified base: manual campaigns, original audiences, exclusions in place. What survives from Heath and Theriot regardless of that call: do not build a separate retargeting CAMPAIGN structure, keep conversion volume consolidated per learning unit, and treat their auto-retargeting data as proof that exclusion architecture (sibling brain) matters more than warm ad-set proliferation.

---

## Excluded sources

- **Weskill ("42. Audience Targeting Cold vs Warm")**: flagged thin. Generic cold-vs-warm explainer with no Meta mechanics, thresholds or UI; its "10x more effective" number is unsourced. Not used in any theme.
- **Easy Click Fix ("How to Create Custom Audiences in Facebook Ads Manager")**: scope flagged. Centred on customer-list CSV uploads, which belong to the list-audiences sibling brain; only generic Audiences-tab navigation was on-scope. Not used in any theme.

Usable sources: 8 of 10.
