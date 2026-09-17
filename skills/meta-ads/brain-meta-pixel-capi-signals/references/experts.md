# Experts Mined - Meta pixel and CAPI signals layer (end to end survey)

12 creators, 14 videos, mined 2026-07-06. Gem flags come from the source index built at mining time
(hidden gem = small channel, top-decile engagement).

## Skills With Ashwin - hidden gem

Whiteboard-style concept-first explainer plus a live WordPress build. Uniquely strong on
articulating the full attribution loop in plain terms (300 clicks, 3 sales, where the loop
breaks without CAPI) and the only source to show a live EMQ score in the UI (8.1/10) with
a fix threshold (he puts it at below 4-5; the library standard is stricter and overrides
him, a 6.0 floor and a 7+ target). Also the clearest on dedup fallbacks: event ID first, then
external ID and FBP.

## Abdul Kayium (GA4, GTM, Server Side Tracking) - hidden gem

Tool-demo angle for non-technical marketers who find GTM too complex. Unique add: the
point-and-click visual trigger pattern (click the submit button, tool auto-detects form
fields) and the side-by-side browser/server view in Test Events. Also the cleanest
statement of silent signal loss: ads look active and spend while conversions go missing.

## It'smeJacob - hidden gem (era-flagged)

Troubleshooting-first GHL installer. Unique add: the checklist of commonly-skipped GHL
install locations (forms settings, funnel event sections, calendar confirmation settings
each need their own pixel ID). Era flag: presents iOS 14 as current context and asserts a
30-40% loss figure without sourcing, so he is excluded from synthesis theme backing; his
GHL mechanics are corroborated by Giba, Hernandez and Localnichemarketing.

## Dr. Matt Shiver - popular

The best source in the set for signal-quality-as-cost-lever. A real $10,395 campaign where
reschedule refires inflated 16 calls to a reported 29 ($355 reported vs $2,500 true cost
per qualified call). Unique adds: the tag-gate fix (IF/ELSE on a "pixel fired" tag), the
7-day rule (late-resolving events go CAPI only), qualified-event gating via survey
questions, and the direct tie to Andromeda spend allocation.

## Danyyil Giba - popular

Beginner-focused GHL install with the set's only measured pixel-only vs pixel+CAPI
accuracy comparison across two real accounts (1.3% over-report vs 2.5% under-report on
$7,745 and ~$16,000 spend). Unique add: the argument that slight under-reporting is the
healthy direction, and the click-to-load-to-submit drop-off example (20 clicked, 16
loaded, 7 submitted).

## Christian Jamal - popular

Installer's-eye view for non-technical owners. Deliberately strips CAPI out of pixel
setup and treats it as a separate advanced task (the set's one contrarian sequencing
take). Unique adds: manual head-code install over partner integrations for
predictability, and Pixel Helper verification.

## Rafael Hernandez - popular

Agency-operator GHL depth. Unique adds: the Integration-tab diagnostic ("multiple" vs
pixel-only as the server-side truth check), the funnel-events vs lead-events distinction,
CRM positive funnel stages for "maximize number of conversion leads", the
don't-combine-lead-goals rule, and the honest cost expectation (CPL up, cost per
qualified lead down).

## HoldenAcademy - popular

Systeme.io specialist. Unique add: the repeated action-not-intent event mapping logic
across four funnel pages (lead-magnet page is View Content, only the post-submit page is
Lead, only the purchase thank-you is Purchase), plus Systeme's native domain-level CAPI
field. Reader note: title says 2025, inside the freshness window, UI current.

## Localnichemarketing - popular

Agency-auditor angle for GHL. Unique adds: the named EMQ must-have parameter list (event
ID, phone, email, IP), the Submit Application default-event audit finding, and the caveat
that pipeline-stage CAPI events only earn optimisation if the CRM is updated daily or a
few times weekly.

## Pixel Flow - popular (vendor, 3 videos)

Vendor of a no-code pixel+CAPI bridge, covering Framer (x2) and Squarespace. Unique adds:
explicit event-ID dedup mechanics, same-session blocking (one Lead per user per 24 hours),
the fact that Framer has no built-in CAPI path and Squarespace is pixel-only natively, and
the remove-the-native-pixel rule when adding a third-party bridge. Caveat: all percentage
claims (60-70% coverage, 25-40% lift, 2-3x ROAS) are its own marketing numbers, not
verified; use direction only.

## Jamie Stenton - popular

Agency auditor. Unique adds: the 50-60% broken-accounts base rate from auditing hundreds
of accounts a year, the three failure modes (no fire, double fire, wrong event), and the
test-every-payment-path rule. His "pixel fires correctly means CAPI fires correctly"
shortcut is the set's one disputed QA take.

## Easy Click Fix - popular (thin)

Pure WooCommerce plugin walkthrough, no mechanics. Only contribution: the official
Facebook for WooCommerce plugin auto-enables CAPI on connect, plus the advanced matching
toggle. Flagged thin; corroboration only.

---

## Source quality notes

- **Usable sources: 12 of 14 videos** (11 distinct usable creators). Excluded from
  synthesis backing: Easy Click Fix (thin), It'smeJacob (era-flagged). Both still appear
  in the quote library and here, labelled.
- **Freshness**: all 14 pass the 12-month rule. HoldenAcademy is the oldest (2025-08),
  UI verified current by the reader.
- **Vendor weighting**: 3 of the 12 usable videos are from one vendor (Pixel Flow), and a
  fourth (Abdul Kayium) demos the same vendor's tool. Cross-platform install facts from
  them are solid; every quantitative claim from them is a marketing number and is
  labelled as such in synthesis.md.
- **Thin areas, said plainly**: Squarespace and WooCommerce each rest on a single source;
  Systeme.io on one; no source covered Shopify, GTM server containers, or custom-code
  CAPI on a Next.js/Vercel stack (the sibling `brain-meta-capi-server-side-deep` is the
  place for that depth). GHL is the best-covered platform (4 videos).
- **Numbers hygiene**: the widely repeated "30-40% lost without CAPI" figure traces only
  to vendor marketing and one unsourced assertion. The only measured comparison in the
  set (Giba) found 1-3% gaps. Both are reported; synthesis sides with the measured one.
