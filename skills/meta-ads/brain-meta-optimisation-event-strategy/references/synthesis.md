# Synthesis: Meta ads optimisation event strategy

Built 2026-07-05 from 14 mined transcripts (15 discovered, 1 had no transcript).
Scope lock: which conversion event to optimise to at low volume, proxy events (booked call, schedule, qualified lead), standard events vs custom conversions as optimisation targets, value optimisation, training the algorithm with quality signals.
Cross-checked against the verified evidence base in `brain-meta-ads-manual-control-no-advantage/references/synthesis.md`; conflicts flagged at the bottom and the verified base wins.

---

## Theme 1: The results column is the real targeting. The pixel becomes what you train it on. (CONSENSUS)

Whatever event lands in the results column is what Meta goes and finds more of. Ad set targeting inputs are minor by comparison, so quality control means controlling which conversions are allowed to fire.

- **Dr. Matt Shiver**: targeting selection "matters a tiny bit, but what matters more is whatever hits this results column"; Meta optimises only around the event that hits it.
- **Localnichemarketing**: his "reality shift": the Meta pixel becomes what you train it on. A two-step funnel where everyone who enters is a Lead teaches Meta to fetch more low-quality entrants.
- **Evan Seech**: Meta is "just this big old AI machine", data in equals results out. He calls the practice "pixel conditioning".
- **Justin Lalonde**: frames it as clicker training, a reward system; too few fires per month leaves Meta "confused" about who to target.
- **Nexal Media | Ecom**: the event choice "tells Facebook exactly what you value".
- **Scott Henry**: "we only want our pixel to be fed qualified leads that fit our offer."

Concrete number: Localnichemarketing's audit found two page-view fires per single page view from a duplicated tag setup, corrupting the training data before any strategy question even mattered.

## Theme 2: Choose the event by sales-cycle lag versus the attribution window. (CONSENSUS)

The event is not chosen in the abstract. It is chosen by whether it fires soon enough after the click for Meta to learn from it.

- **Caden Thompson**: Meta's usable feedback loop is roughly 7 days; if the true lag from first interaction to conversion exceeds it, the bottom event's signal arrives too late to steer creative. Long lag means move the optimisation event up the funnel.
- **Meta (via the Make webinar)**: hard ceiling stated by Meta's product marketing manager, "the conversion event has to occur within 28 days of lead submission. That's the attribution window." Long sales cycles should not optimise for the final event.
- **Dr. Matt Shiver**: the browser pixel "is pretty good within a 7-day window" then degrades; he has seen leads book 60+ days after opt-in, so schedule events go through Conversions API only.
- **Caden Thompson's three archetypes**: local/immediate (plumber, chiro) = short lag, optimise to a qualified/sold lead event; SaaS = shorter cycle, bottom-funnel event; B2B/renovation = long lag, start at a middle event like lead or quote request.

Concrete number: Thompson's back-calculation method, 10 leads at $100 converting to 1 sold lead = $100 per sold lead; if 10 leads rise to $200, cost per sold lead has doubled even with no sold-lead event fed back to Meta.

## Theme 3: Meta's official four-part event-choice framework. (NAMED FRAMEWORK, highest-authority source in the set)

From Meta's own product marketing manager on the Make webinar. The one Meta-sourced framework in the brain.

1. Go down-funnel but not necessarily to the final stage (qualified lead or demo booked, not always purchase).
2. Pick a stage that between 1% and 40% of leads actually complete.
3. The event must occur within 28 days of lead submission.
4. The event must represent something genuinely valuable to the business, not just "lead received".

Supporting numbers from the same source: instant form campaigns on the conversion leads goal with CAPI-CRM saw 21% lower cost per quality lead on average; website form campaigns with CAPI saw 9.5% lower. CAPI for CRM "is effectively table stakes for our quality and value products", and for Instant Forms it is now a requirement for the conversion leads performance goal, not a recommendation.

## Theme 4: Volume thresholds before an event is trainable. (CONSENSUS on the principle; the exact floor varies)

Every source that names numbers agrees an event needs a minimum fire rate before Meta can optimise to it.

- **Justin Lalonde**: wait for 50+ conversions of the event inside a 7-day cycle before optimising to a custom conversion; for a call business, roughly 200+ calls per month justifies optimising to the custom call event.
- **Caden Thompson**: 15 to 30 qualified events per month is the working floor for a local lead-gen account; below that, fall back to a middle-of-funnel event and ladder down over time.
- **Localnichemarketing**: CRM/offline feedback loops only once volume and budget support them, not for newer or low-volume accounts.

Note on the classic 50-conversions-a-week learning-phase rule: the verified base (manual-control brain, Theme 4) treats it as Meta's official line whose back-propagated budget maths is absurd for small accounts. Here the sources use it differently, as a reason to optimise one step up the funnel where volume runs 2-3x higher, which is consistent with the verified base's consolidation logic. Era-flagged source Rihards Zeiča states the rule; the unflagged Justin Lalonde independently corroborates the 50-in-7-days figure.

## Theme 5: For lead gen, optimise to a proxy event deeper than raw Lead. (CONSENSUS, the core move of this brain)

The raw Lead/opt-in event trains the pixel on entrants, not buyers. The proxy ladder runs booked call (Schedule), submitted application, qualified lead, paid consult.

- **Localnichemarketing**: shift "from lead events to deeper funnel events such as... booked an appointment or paid the initial consultation fee". Expect cost per acquisition to rise while quality improves.
- **Scott Henry** (both videos): two-stage structure, Lead on opt-in, Schedule on booked call via CAPI, campaign optimised to Schedule, not Lead.
- **Dr. Matt Shiver**: for the Schedule event he uses CAPI only, never the pixel, estimating the pixel has a "10-20% chance" of attributing bookings past 7 days.
- **Evan Seech**: only the qualified route of the application reaches the confirmation page carrying the standard event code (schedule, submit application, or complete registration).
- **Caden Thompson**: for short-lag local businesses, aim directly at a booked-and-confirmed call event.

Concrete number: Seech's high-ticket call-funnel maths, $6K offer, $2K profit per customer, let the campaign spend 1x profit ($2,000) before a kill decision, 2x ($4,000) as the real go/no-go on cost per call and lead quality.

## Theme 6: Conditional gating: only qualified people are allowed to fire the event. (CONSENSUS, richest pattern set in the brain)

The mechanism behind Theme 5. Every practitioner gates the fire; they differ only in sophistication.

- **Dr. Matt Shiver**: qualifying question on the form; pixel event set to "none" on generic form submission; Complete Registration fires only on the conditional-logic qualified thank-you page. Native lead forms: "higher intent" form type, conditional questions routing qualified and unqualified answers to identical-looking end pages where only one fires.
- **Scott Henry**: if/else in the GHL booking workflow. Example gates: monthly revenue bracket, "do you own a marketing agency" plus "do you run ads". Unqualified leads can still book; the pixel is simply not fed that conversion.
- **Evan Seech**: escalating CAPI trigger patterns, (1) CRM stage change fires the event, (2) sales team manually tags "qualified" to trigger it, (3) Typeform answers scored 1-10 by AI and only 7+ fires the schedule event.
- **Dr. Matt Shiver** (mature accounts): a human-gated "send pixel" pipeline stage in GHL, so only verified bookings fire, filtering leads who lied on the application.
- **Localnichemarketing**: hard disqualifiers in the first two or three survey questions (back surgery rules out spinal decompression) so unqualified leads self-exit before any event fires.

Shiver's counterweight: "what you say in the ads is the most important part, more so than the conversion that you send back." Gating works alongside audience-qualifying copy, not instead of it.

## Theme 7: Standard events by default; custom conversions only past a volume threshold. (CONSENSUS, one deep source plus corroboration)

- **Justin Lalonde** (the definitive treatment in the set): standard events are shared across the entire advertiser ecosystem, so Meta pools cross-account data and can optimise even a brand-new account. Custom conversions are single-account learning only; Meta has no external reference for a self-named event. Rule: "in doubt, use standard events." E-commerce uses standard events "99% of the time"; the custom-event use cases are service businesses segmenting quality (e.g. a qualified-call event via Hyros) and health-restricted verticals limiting data pass-through.
- **Lalonde's staged path for call businesses**: optimise to the standard Schedule event (GHL workflow firing CAPI on booked appointment) while a custom qualified-call event accumulates volume, then pivot once it crosses 50-in-7-days.
- **Localnichemarketing**: used custom conversions as a repair tool (fixing duplicate tracking without GTM access), a legitimate secondary use distinct from optimisation targeting.

## Theme 8: Pixel plus CAPI, and when to lean server-side. (CONSENSUS)

- **Meta (via Make)**: CAPI-CRM is table stakes for quality and value products; required for the conversion leads goal on Instant Forms.
- **Dr. Matt Shiver**: pixel reliable inside ~7 days; CAPI (introduced 2019) is "the key right now" for anything longer. Schedule events: CAPI only.
- **Evan Seech**: the operational trigger, if the match rate for the optimised standard event is "8 or below" in Events Manager, switch to server-side via CAPI.
- **Scott Henry**: pixel and CAPI wired in tandem through GHL; access token and data set ID stored once; event names must match across page and workflow.
- **Localnichemarketing**: send CRM outcomes back after the sales cycle completes (example 14-15 days), including how many booked, how many converted and at what monetary value.

Match parameter ranking (Meta via Make): lead ID highest accuracy, always the starting point; click ID and email very high; phone strong; name, city, state, zip supplementary. "Start with lead ID and then layer on as many additional parameters as you have available."

## Theme 9: Value optimisation and the CRM feedback loop. (SINGLE AUTHORITATIVE SOURCE, thin coverage)

Only the Make webinar (Meta product marketing) covers value optimisation directly, so treat this theme as one voice, albeit the platform's own.

- Two optimisation goals now in the leads objective: maximise conversion leads (quality) and maximise conversion value (value optimisation, in beta rolling to GA).
- Value can attach to any event in the leads objective, not just purchases: monetary value, quality scores, or predicted GMV.
- Relative values should reflect actual business value, e.g. a booked demo worth twice an initial contact is valued 2x.
- Delayed value updates are supported via CAPI/CAPI-CRM dedup, up to a 5-minute window after the initial event.
- Implementation pattern demoed: store the Facebook Lead ID (or Click ID) in a CRM custom field, fire a CAPI-CRM event at each pipeline stage change including won/closed.
- Diagnostics: Test Event Tool for verification leads; CRM Event Health flags invalid lead IDs, no CRM events in the last 24 hours, lead coverage below 60%, missing funnel stages; events usually appear within an hour.

## Theme 10: Signal hygiene before any optimisation decision. (CONSENSUS)

- **Localnichemarketing**: eliminate duplicate and noisy events first (the double page-view audit); Events Setup Tool or GTM to keep tracking clean.
- **Scott Henry**: a dedicated calendar for ad traffic, "always always always always have a unique calendar", or Meta gets rewarded for organic and email bookings it did not drive. Select every available match parameter on both Lead and Schedule during CAPI setup "to create the strongest pixel". Conversion location at ad set level cannot be re-edited after publishing.
- **Evan Seech**: know which tracking mode each page runs (his confirmation page carried no schedule code at all where it should not; browser-side elsewhere, CAPI where it matters).
- **Meta (via Make)**: verify with the Test Event Tool before going live; watch per-key coverage in the Events Quality section.

## Theme 11: The volume-versus-quality lever. (CONSENSUS)

Moving the optimisation event up-funnel buys volume and junk; down-funnel buys quality and cost.

- **Caden Thompson**: "The further up the funnel, the more junk leads you get. The further down the funnel, the better quality leads you get." Benchmark point given: 100 lead-magnet opt-ins to 10 real leads. Qualifying questions are a lever to pull deliberately.
- **Localnichemarketing**: fewer, dearer, better; the CPA rise is the price of quality.
- **Dr. Matt Shiver**: phone verification on higher-intent forms cut volume too far for his use case, so he leaves it off. The lever cuts both ways.

## Theme 12: Judge the event strategy on rolling windows; the algorithm is not always right. (SINGLE SOURCE, adjacent support)

- **Michael Diaz**: decisions on rolling averages, never single days. Windows: 30-day story, 14-day recent, 7-day primary decision window, 3-day trajectory. After a change, leave the account alone 3 to 5 days (stop "shaking the snow globe"). And the check on blind pixel trust: "the algorithm is not always right. It will skew spend to things that are giving you terrible results," because Meta's incentive is platform spend, not advertiser profit.

This is adjacent to the locked scope (his video is optimisation discipline, not event selection) but it is the needed counterweight to Themes 1-6: you train the machine AND you audit what the training produces. Deep campaign-management detail stays with the media-buyer and manual-control brains.

---

## Conflicts with the verified evidence base (verified base wins)

1. **Tushar Dey**: claims that "after the Andromeda update came, majority of the portion is automated" and Meta handles retargeting on its own. The verified base's controlled evidence (Nick Theriot's manual 2.91 ROAS vs ASC 2.14 on identical ads; the settings kill-list; manual exclusions) says structure and exclusions stay manual. Side with the verified base. Dey's purchase-only-from-day-one stance is also era-flagged (opinion, not documented Meta behaviour).
2. **Nexal Media | Ecom**: keep automatic placements on for conversion objectives, including Audience Network. The verified base kill-list turns Audience Network OFF (the accidental-click trap) while running Advantage+ Placements otherwise. Side with the verified base: Advantage+ Placements ON, Audience Network excluded. Note this is only achievable via an ACCOUNT-level placement exclusion; unticking Audience Network in the ad set switches it to manual placements and turns Advantage+ Placements off.
3. **The 50-conversions rule**: no true conflict, but read it the verified base's way. Use it as a reason to pick a higher-volume event, never as a budget mandate (its back-propagated spend requirement is absurd for small accounts).

## Excluded sources (per thin/era flags)

- **Ben Heath** (thin): two-campaign structure and creator-sourcing tactics; does not address event selection. Campaign structure belongs to the sibling manual-control and media-buyer brains anyway.
- **Jared Robinson** (thin): post-Andromeda creative-volume strategy; only tangentially mentions KPIs, no event-selection content.
- **Tushar Dey** (era-flagged): purchase-only maximalism presented as post-Andromeda fact without evidence; retained ONLY as the contested take in the contrarian record, never as theme backing.
- **Rihards Zeiča** (era-flagged): the 50-conversions/week rule predates the current era; cited only where the unflagged Justin Lalonde independently corroborates, and superseded by Meta's newer 1-40% / 28-day framework where they differ. (Listed as Rihards Zeiļa in the source index built at mining time.)
- **Robert Dulski** (no transcript): the highest-scored hidden gem in discovery, but the video had no captions to mine. Not used anywhere.

Fully usable for theme backing: 10 of 15 discovered sources.
