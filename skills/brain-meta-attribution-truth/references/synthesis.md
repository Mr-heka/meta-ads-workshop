# Synthesis - Meta attribution truth (windows, view-through, incrementality, when ROAS lies)

Built 2026-07-06 from 15 mined YouTube transcripts. 13 usable after exclusions (see bottom).
Context lens: a small-business lead-gen advertiser running one manual Meta account at a few thousand dollars a month, where a CRM is the scoreboard, not a Shopify storefront. Nearly every source is ecommerce/ROAS-framed. The transferable principle is identical in every theme: reported conversions are a proxy, the truth is what the ad actually caused. Swap "purchase/ROAS" for "lead/booked-call/signed-client against a target CPA."

Cross-checked against `brain-meta-ads-manual-control-no-advantage` (our verified base). Where a source conflicts, the conflict is flagged and the verified base wins.

---

## Theme 1 - Attribution is credit assignment, and the default is 7-day click / 1-day view (CONSENSUS)

Attribution decides which ad, ad set, or campaign a conversion gets credited to, and it is set at the ad-set level. Every source that touches the mechanics lands on the same default and the same beginner recommendation: leave it alone.

- **Umar Tazkeer**: attribution is which specific ad a conversion event gets credited to. Default = 7-day click-through + 1-day view-through; leave default unless the built-in comparison reveals a large gap.
- **Dara Denney**: for beginners, highest-volume bidding with a 7-day click / 1-day view setting.
- **Jason Gan**: "the default setting is the best... unless you know what it really means... put it to the default setting."
- **Jamie Stenton**: standard = click within 7 days OR view within 24 hours, both count as full credit.
- **David Parrottino**: default standard window is 7-day click, 1-day view.

**Consensus.** The mechanic and the default are undisputed. Contest begins over view-through (Theme 3) and whether to trust the reported number as truth (Theme 4).

Verified-base note: matches our manual-control base, which prescribes 7-day click for lead-gen and switching to 7-day-click-only once view-through exceeds ~25% of conversions.

## Theme 2 - Shortening the click window is a learning mistake, not just a reporting one (CONSENSUS)

Cutting the click window to 1-day does not stop the sales happening. It stops them being counted and, worse, stops the algorithm learning from them.

- **Jason Gan** (clearest): if 10 conversions happen but only 3 land inside day one, "you lose the seven conversions that was actually caused by this ad" and "your campaign will not be learning good enough." The business still gets the sales; the campaign just goes blind to them.
- **Dr. Matt Shiver** (the carve-out): for impulse, low-ticket ecommerce ("anything less than like 20 bucks") a 1-day click test can be useful, because a same-day purchase after a click is a stronger causal signal than a week-old click followed by an email-driven sale.

**Consensus with a narrow carve-out.** Default to the wider (7-day) click window for lead-gen and considered purchases; 1-day click is a niche test for low-ticket impulse ecommerce only. Not us.

## Theme 3 - View-through is the real over-reporting risk, and it is contested (CONTESTED)

View-through credits the ad when someone merely *sees* it (no click) and converts within the window through any channel, even organic. This is where the reported number inflates hardest, and the experts split on whether to run it.

- **Umar Tazkeer**: view-through is "more dangerous" than click, because "there was no interaction with the ad" yet the conversion still gets attributed to Meta.
- **Dr. Matt Shiver** (turn it OFF for lead-gen): for booked-call and DM-heavy businesses, 1-day view falsely attributes DM-booked calls to ads the person merely scrolled past. Explicit rule: turn OFF 1-day view, keep 7-day click, decide 1-day engaged-view case-by-case on volume. Real account: >10% of booked-call attribution came purely from 1-day view on a DM campaign.
- **Caden Thompson** (turning it ON, reversing his own stance): held 7-day-click-only for a year because click data is more reliable, now enabling 1-day view because the Andromeda update collapsed full-funnel creative into one ad set, so the algorithm needs view signal to see no-click bottom-funnel interactions. Flags the risk himself: if returning-customer revenue is ~30%+ of AOV, view-through over-prioritises already-warm buyers over new prospects; watch for view-throughs to "spike like crazy" as the warning sign.
- **Common Thread Collective**: view-attributed conversions have ranged from 10-15% up to over 50% of total volume across accounts they manage, "a difficult measurement challenge."

**Contested.** Shiver says off for lead-gen, Thompson says on for data-starved full-funnel accounts. For our lead-gen model the weight (Shiver + Tazkeer + verified base) sides with treating view-through as the inflation source to watch, not trust. Verified base: strip to 7-day-click-only once view-through exceeds ~25% of conversions; Pawliw saw a reported 7-10x collapse to a real 2-3x when view-through was removed.

## Theme 4 - Standard attribution over-reports; reported ROAS is directional, never truth (CONSENSUS, the spine of this brain)

The single point every credible source agrees on: standard attribution claims more credit than the ad actually earned. It assumes causation when it only saw contribution.

- **Dara Denney**: "Facebook will credit more of the results that it had a hand in than the actual sales it made."
- **Dr. Matt Shiver**: verbatim same line: "Facebook will credit more of the results that it had a hand in than the actual sales it made."
- **David Parrottino**: "standard attribution assumes causation, not contribution"; it is "directional. It's never the truth."
- **Jamie Stenton**: standard settings "overestimate the amounts of sales that they've actually made"; can claim 100% credit for a one-touchpoint contribution.
- **Ryan Stewart** (the lead-gen translation): optimising to "lead" instead of "signed client" hides that lead volume decouples from revenue. Spent ~$40,000 with zero signed clients; the month with the MOST booked calls produced zero clients.
- **Common Thread Collective** / **Max Rosewater** (platform-sourced): rules-based windows "are proxies. They're directionally useful, but not accurate for actually understanding the incremental lift."

**Consensus, unanimous.** This is the brain's thesis. Reported ROAS (or reported CPL) is a directional optimisation signal, not a financial-truth number. The correction is incrementality (Theme 5).

## Theme 5 - Incrementality is the real question: "would this have happened anyway?" (CONSENSUS on the concept)

Incrementality asks whether the conversion would have happened without the ad. The lemonade-stand and geo-holdout framings reduce to the same one-sentence test.

- **Jamie Stenton** (best plain-English): lemonade stand does 10 sales/day baseline, 14 with a roadside sign, so "the true sales uplift of the sign is just four additional sales... It's not responsible for all 14."
- **David Parrottino**: "Incrementality answers a different question and that question is would this conversion have happened without meta ads." Test it: turn Meta down 50%; revenue drops 40% = real; drops 5% = Meta was capturing existing demand, not creating it.
- **Common Thread Collective**: define incrementality % as reported ROAS vs geo-holdout true ROAS. If platform says 2:1 and holdout measures 2:1, that's "100% incremental." Their own 7-day-click testing often reads above 120% (7-day click actually *under*-reports for them).
- **Max Rosewater** (platform definition): "a true incremental conversion means that a conversion would not have happened otherwise without the introduction of meta ad spend."

**Consensus on the concept.** How to measure it (Meta's built-in setting vs an external geo-holdout) is Theme 6. Deep practical incrementality at small spend lives in the sibling `brain-meta-attribution-measurement-deep` (P5); this brain surveys the concept and points there.

## Theme 6 - Meta's Incremental Attribution setting: a real feature, but adopt with a test (CONTESTED on trust/timing)

Incremental Attribution (IA) is a distinct ad-set-level model (not a time window) that predicts whether each conversion was ad-caused. **Correction to a claim that circulates widely, including in this brain's sources: it does not run continuous invisible holdout tests on your ad set.** Meta describes IA as a model, informed by the results of its own lift studies and experiments, that re-scores your existing conversions. Your traffic is not being split into control and treatment groups in the background. Describe it as "Meta's model of causation", not "a holdout you are already running". Rolled out ~April 2025. The dispute is not whether it exists but whether to trust it now, and whether to optimise on it or just read it.

**How to see it without switching your campaign (CONSENSUS method):** Ads Manager > Columns > "Compare Attribution Settings" > select 7-day click, 1-day view, and Incremental Attribution > Apply. Surfaces all three side by side. Backed by Tazkeer, Piliero, Shiver, Stenton, CTC.

**The gap it reveals (real numbers):**
- **Sam Piliero**: one account showed regular ROAS 15.77 vs incremental ROAS 2.85. Another: 199 standard purchases vs 54 incremental; 473 (7-day click) vs 417 (1-day view) vs 330 (incremental).
- **Jamie Stenton**: real client, spend ~£2,800, standard ROAS 4.8x (£136k) vs incremental 2.4x (£68.5k), roughly half.
- **Umar Tazkeer**: 12 standard vs 9 incremental (campaign 1); 2 vs 1 (campaign 2); 426 standard leads vs 423 incremental. Small gap in his lead-gen/D2C accounts.
- **Dr. Matt Shiver**: incremental yields "a fourth to maybe a third" of standard conversion volume.

**Meta's own claimed lift (platform-sourced, treat with skepticism):**
- **Sam Piliero** (interviewing Meta's Director of Signal Growth): "24% increase in incremental conversions versus our standard attribution model," from "thousands of conversion lift tests."
- **Max Rosewater** (interviewing Meta): "46% lift... validated based off 37 statistically significant lift studies across 30 advertisers in eight verticals."

**The split on when to adopt:**
- **Sam Piliero / CTC / Max Rosewater**: dip a toe via the compare column, ideally validate with a conversion lift test, only adopt IA for optimisation once it beats business-as-usual.
- **Dr. Matt Shiver / Jamie Stenton (April 2025 stance)**: stick with standard for optimisation for now, treat IA as a secondary data point. Shiver: "for 99% of people, I'm still encouraging the standard attribution." Reason: more optimisation events under standard help delivery; IA reduces recorded conversions and can starve learning.
- **Jamie Stenton**: "Facebook haven't released anything to say actually how they're measuring incremental attribution. So, it is just a data point." (Partly superseded: Piliero and Rosewater both got Meta's mechanism description directly.)

**Contested on trust and timing.** The compare-column read is universally endorsed and costs nothing. Switching optimisation to IA is where caution splits. IA also currently only supports highest-volume/maximise-conversions bidding (CTC); cost controls were "coming later" at recording. Early CTC A/B numbers land IA between the 1-day-click and 7-day-click figures (golf brand: 7-day 1.5, 1-day 1.1, IA 1.3).

## Theme 7 - Geo-holdout is the gold-standard truth test; hold your setting constant (CONSENSUS among the rigorous voices)

The advertisers who actually measure truth do not trust any in-platform number alone. They run a control-vs-treatment geo-holdout and derive a discount factor.

- **Common Thread Collective** (standing practice): run media in one geography, withhold in another, measure the delta. Convert reported to incremental ROAS with a factor: a 7-day-click-1-day-view 2:1 × 0.8 = 1.6 IROAS; a 7-day-click number might need a 1.2x factor because it under-reports.
- **David Parrottino**: geo-holdout worked example. Brand at $180k Shopify, $47k spend, Meta reports 2.8x, blended MER 3.8. Turn Meta down 50%: 40% revenue drop = incremental; 5% drop = capturing demand.
- **CTC (measurement design)**: "It's really hard to create an appropriate measurement system when you're changing the optimization settings all the time." Pick a setting, hold it constant, build the measurement on top.
- **CTC (cross-channel)**: normalise every channel to a single incremental-ROAS expectation via holdout, so Google branded search and Facebook prospecting are directly comparable.

**Consensus among the rigorous.** The discipline: pick one attribution setting, hold it, and layer a periodic holdout (or IA read) to learn your true discount factor. Deep holdout mechanics at small spend = sibling deep brain.

## Theme 8 - All platforms over-attribute; the CRM/blended number is the financial truth (CONSENSUS)

Meta is not uniquely dishonest. Every ad platform's job is to claim maximum credit, so the only honest scoreboard sits outside the platforms.

- **David Parrottino**: Google, TikTok, Snapchat, Pinterest, even Klaviyo "all overattribute revenue." Split the job: in-platform attribution for campaign optimisation, blended metrics (contribution margin, MER) for financial decisions.
- **Ben Heath** (the recurring-revenue gap): Hyros tracked £96,000 from a campaign, "but £58,000 of that was not reported by Meta" because Meta only saw the initial transaction, not recurring payments. Reported ROAS *under*-states here.
- **Dr. Matt Shiver** (CRM reconciliation, closest to us): cross-references Meta's reported conversions against Hyros. One account: a pixel double-fire made Facebook report 8 booked calls when only 2 happened, one of them unqualified. A fixed account matched Hyros exactly (10 schedules = 2 view + 8 click).
- **Ryan Stewart** (the lead-gen CRM crosswalk, most on-model): stitched Facebook + Calendly + GoHighLevel + ActiveCampaign into a true cost-per-signed-client report. Real number = ~$4,700 cost per client against a $4,000-8,000/month retainer. Cost per lead was decoupled from it entirely.

**Consensus.** For lead-gen, the CRM (GHL for us) is the source of truth; Ads Manager is the optimisation dashboard. Reconcile the two, do not conflate them.

## Theme 9 - Read Ads Manager honestly: decide on primary metrics, treat the rest as "why" (CONSENSUS)

Reading the account honestly is its own discipline: separate the small set of metrics you *decide* on from the larger set that only *explains*.

- **Dara Denney**: four primary metrics drive decisions (amount spent, purchases/CPL, cost per purchase, ROAS); everything else is "storytelling" context. And "the analysis needs to be done first before you start tweaking." CTR is unreliable under broad targeting; hook rate (~30% avg) and hold rate (7-8% avg) are useful "why" metrics but must be added manually.
- **Dara Denney** (the breakdown effect): Meta deliberately caps some high-ROAS-looking ads because force-feeding them budget reduces total profitability; she has tested throttling more spend and they underperform.
- **Ryan Stewart**: replace "hypothesis and conjecture based on the opinion of a single media buyer" with a data source of truth reviewed by humans.
- **Ben Heath** (bid goal shifts what ROAS means): maximise-value vs maximise-number changes which customers Meta chases, so "ROAS" in the account is not a fixed thing. For lead-gen, value-based optimisation means feeding back different lead values (roofing: $4,000 avg high-value lead vs $1,000 low-value) via different thank-you pages.

**Consensus.** Decide on the primary set only; use the storytelling metrics to diagnose, never to trigger a kill. Aligns with our verified base (Heath: decide on CPA/ROAS only; CTR/hook rate explain WHY).

## Theme 10 - Measurement failure scales from a campaign problem to a system-design problem (CONSENSUS among ecommerce-scale voices; partial applicability to us)

At scale, the ROAS-lies problem stops being about a window and becomes about what revenue even feeds your reporting.

- **Common Thread Collective** ("Starving Giants"): $50-150M brands pull back spend because reported website efficiency looks worse, when total impact across .com + Amazon + retail is flat or up. Ad dollar creates demand realised on multiple storefronts: "$1.20 on .com and then... another 60 cents on Amazon so it's $1.80 which is the difference between not profitable or profitable."
- **CTC**: across 191 YouTube incrementality studies (House data), the incrementality factor vs platform-reported result averaged 3.76x.
- **CTC** (existing-customer definition): a lapsed customer who "hasn't bought from you in years... is not your customer"; tighten remarketing exclusion windows to a realistic active cohort (~6-8 months).

**Consensus among ecommerce-scale voices.** Mostly out of scope for a single-channel lead-gen account at our spend, but the principle transfers: audit what revenue actually feeds your daily metric before trusting it. The multi-storefront and identity-resolution detail does NOT apply to us (one channel, one CRM).

---

## Consensus vs contested at a glance

| Claim | Status | Backers |
|---|---|---|
| Default is 7-day click / 1-day view; leave it unless comparison shows a gap | Consensus | Tazkeer, Denney, Gan, Stenton, Parrottino |
| Shortening the click window loses real, ad-caused conversions and starves learning | Consensus | Gan, Shiver (carve-out) |
| Standard attribution over-reports; reported ROAS is directional, not truth | Consensus (unanimous) | all 13 usable |
| Incrementality = "would it have happened anyway?" | Consensus on concept | Stenton, Parrottino, CTC, Rosewater |
| View-through on or off for lead-gen | Contested | OFF: Shiver, Tazkeer / ON for data-starved: Thompson |
| Trust Meta's IA setting for optimisation now, or read-only | Contested | Adopt-with-test: Piliero, CTC, Rosewater / read-only for now: Shiver, Stenton |
| Geo-holdout is the truth test; hold your setting constant | Consensus (rigorous voices) | CTC, Parrottino |
| CRM/blended number is the financial truth; every platform over-attributes | Consensus | Parrottino, Heath, Shiver, Stewart |
| Decide on primary metrics only; rest is "why" | Consensus | Denney, Heath, Stewart |

## Exclusions

- **No sources excluded as thin.** All 15 mined videos returned substantive notes.
- **Two flagged for era/scope, used with the flag noted, NOT dropped:**
  - **Caden Thompson** - his view-through reversal ties to the Andromeda "single ad set full-funnel" structure and is a personal-stance reversal, not settled consensus. Used only inside the contested Theme 3, labelled as such.
  - **Ben Heath** - the video is about the "maximise value of conversions" bid goal, not attribution windows. Used only for the reported-vs-true-value gap (Hyros recurring-revenue example) and value-based lead-gen framing, never cited as an attribution-window source.
- Promotional plugs in the Sam Piliero source (unrelated businesses) were excluded from extraction per the source notes.
