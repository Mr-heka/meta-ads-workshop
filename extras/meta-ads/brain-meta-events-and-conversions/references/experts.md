# Experts Mined: Meta events and conversions (Events Manager, standard and custom events, custom conversions)

Per the source-index scoring at mining time: 1 hidden gem, 7 standard channels. All 8 videos under 12 months old at build (2026-07-06).

## Justin Lalonde: popular (strongest strategic source)
- **Angle:** performance media buyer framing the standard-vs-custom decision as a data-volume and network-effect problem, not a click-path problem.
- **Uniquely adds:** the only source with decision thresholds. 50+ conversions in a 7-day cycle before switching optimisation to a custom event; ~200+ booked calls/month before a qualified-call custom event makes sense; the "99% of e-commerce stays on standard events" rule. Also the shared-data argument (standard events pool cross-business signal, custom events only see your own account) and the two worked examples: Hyros qualified-call events and the "Q purchase" (AOV $150+) custom event.

## Jamie Stenton (Digital Marketing Expert): popular (2 videos, deepest operational source)
- **Angle:** agency operator (audits hundreds of accounts a year) doing screen-level walkthroughs on real client accounts.
- **Uniquely adds:** the 50-60% broken-tracking audit statistic, the full Test Events walk-the-funnel method including testing each payment path (Google Pay, card, PayPal), the "nothing saves until Finish setup" gotcha, the hidden Event Setup Tool entry point (Manage integrations > Meta Pixel > Manage), and pixel-install troubleshooting (dialog not appearing = broken install; strip plugin, hard-code, or reinstall via GTM). His "pixel firing = CAPI firing" claim is flagged contested in synthesis.md.

## E & T Academy: popular
- **Angle:** practitioner comparison of standard events vs custom conversions on a real non-ecommerce lead-gen funnel (supplement lead form).
- **Uniquely adds:** the clearest rationale for "contains" over "equals" URL rules (trailing-slash variants silently undercount), the deliberate-redefinition pattern (labelling a form-submission thank-you page "Purchase"), the value-assignment options (checkout value vs no value), and verifying the wiring by reading conversion counts at ad level (14 purchases in his demo).

## Shah Wajahat Ali: popular
- **Angle:** general practitioner covering the full chain end to end: pixel creation, both install paths, custom conversion, campaign hookup.
- **Uniquely adds:** the 30-minute propagation delay (new pixels AND every new custom event), the thank-you-page gating rule (page must be unreachable except via the conversion action, or tracking inflates), and the WordPress partner-integration install demo.

## My Online Master: popular
- **Angle:** the most granular UI walkthrough of the no-code Event Setup Tool itself.
- **Uniquely adds:** track-a-button vs track-a-URL modes with the full event-type picker list, the fact that standard event names cannot be customised in the tool, automatic merging of duplicate standard events on one page, Meta Pixel Helper as the pre-check, and the honest ceiling call ("still very basic level tracking", CAPI is the advanced layer).

## Digital Blezz: HIDDEN GEM (small channel, top-decile engagement)
- **Angle:** rough, heavily-accented D2C class walkthrough (part 7 of a series); low polish, clear procedural sequence.
- **Uniquely adds:** the thank-you/order-received URL recipe from the e-commerce side ("checkout/order-received" contains rule), per-product conversion values (25/35/45), and the framing that a custom conversion exists to define the campaign's optimisation goal separate from raw events. Transcript quality is poor (auto-translation artifacts like "convention" for "conversion"); quotes preserved verbatim as required.

## Behind Tools: popular (THIN, excluded from synthesis)
- **Angle:** generic scripted click-path tutorial for creating a pixel.
- **Uniquely adds:** nothing beyond Shah Wajahat Ali's coverage. No operator credentials, no client data, no numbers, no custom conversions, no testing. Lowest score in the set (24.1). Quotes kept in the library under a thin-source label for the raw click path only.

---

## Source quality notes

- **Usable sources: 8 of 8 mined, exactly at the curriculum floor of 8.** That is the minimum, not a comfortable base; stated plainly as the locked curriculum row requires.
- **7 of 8 carry real weight.** Behind Tools is thin (excluded from synthesis, retained only for the pixel-creation click path). Effective depth is closer to 7 sources, and 2 of those 7 are the same creator (Jamie Stenton), so independent voices number 6.
- **Freshness:** no exceptions. All 8 passed the 12-month rule at discovery.
- **Thin areas within scope:** event priority / aggregated event setup got NO direct coverage in any of the 8 transcripts; the curriculum row names it but the mined material is silent on it, so this brain cannot speak to it from sources. Datasets-vs-pixels naming is also only implicit (sources say "pixel" throughout). Custom events via code (as distinct from custom conversions) are defined by Lalonde but never demonstrated.
- **Quote yield:** 36 golden quotes against the 40+ target; the material did not support more without padding.
- **Transcript quality:** Digital Blezz's transcript is heavily garbled by auto-translation; its verbatim quotes read oddly but are preserved word-for-word.
