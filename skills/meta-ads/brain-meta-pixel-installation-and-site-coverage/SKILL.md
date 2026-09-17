---
name: brain-meta-pixel-installation-and-site-coverage
description: "Use when the user says \"pixel not detected\", \"fires twice\", \"wrong event\", \"missing on checkout\", or asks how to install or test the Meta pixel across GHL, Next.js/Vercel, WordPress, Shopify, or a separate checkout domain. Route server-side CAPI setup to brain-meta-capi-server-side-deep and event selection to brain-meta-optimisation-event-strategy."
metadata:
  type: expert-brain
  topic: "Meta pixel installation and site coverage (base+event code every page type, Test Events, broken-install patterns)"
  aliases: "facebook pixel install, meta pixel install, fb pixel, data set, dataset, dataset vs pixel, base pixel code, base code, event code, pageview, pixel helper, meta pixel helper, test events, event setup tool, head tracking code, GHL pixel, gohighlevel pixel, next.js pixel, app router pixel, vercel pixel, wordpress pixel, shopify pixel, pixel not firing, pixel not detected, pixel fires twice, duplicate events, wrong event firing, checkout domain tracking, site coverage, pixel verification"
  domain: "advertising"
  built: "2026-07-06"
  sources: 10
---

# Brain: Meta pixel installation and site coverage (base+event code every page type, Test Events, broken-install patterns)⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

> Built by topic-brain-builder from 10 YouTube sources
> (5 hidden-gem creators surfaced on engagement,
> not views). Made by Selr AI.

## How to use this brain

When the user is working on Meta pixel installation and site coverage (base+event code every page type, Test Events, broken-install patterns), load this brain first. Ground answers in
the synthesis below and cite experts by name from the quote library. Prefer the
consensus view; surface a contrarian take when it's well-argued.

## What the experts agree on

- **"Pixel" is now "data set", but the install job is unchanged.** Base code still goes on every page, verification still matters, the label is cosmetic. (Derek Videll, Marketing Mark, Digital Growth Tutor, Media Ninja)
- **Base code loads site-wide, PageView fires for free, every other event is a deliberate add.** (Media Ninja, Marketing Mark, Derek Videll, InstinctHub)
- **In GHL the base pixel goes in the funnel's "head tracking code" field, per funnel, not once globally.** A funnel you did not touch has no pixel. (Media Ninja, Marketing Mark)
- **Verify before you spend, with two tools, per page.** Meta Pixel Helper to confirm the pixel is live and the ID matches, Test Events to watch each event fire on the real funnel. (Marketing Mark, Media Ninja, Softtrix, Jamie Stenton, Digital Growth Tutor)
- **Never launch a campaign on unverified events.** Broken event data shows up on "at least 50 to 60% of accounts" and quietly misdirects optimisation. (Jamie Stenton)
- **One data set per company, and you cannot delete them.** Create it under the ad account, rename duplicates to "do not use". (Derek Videll, Media Ninja, Marketing Mark)
- **A browser-perfect pixel still loses signal** to Safari ITP, ad-block and cross-device journeys; server-side is the coverage backstop. (Big Short Ads, Pro Data Track)

## Named frameworks & methods

- **The two install routes (everyone).** Manual code paste for custom sites / landing pages / funnel builders; partner or native integration for Shopify, Wix, WordPress, HubSpot. Some backends only want the numeric Pixel ID, not the full snippet.
- **The GHL head-tracking-code install (Media Ninja, Marketing Mark).** Funnel settings > "head tracking code" > paste base pixel > Save. One paste covers opt-in and thank-you inside that funnel. Repeat per funnel.
- **The Next.js App Router component pattern (InstinctHub).** Not a paste into `layout.tsx`. Three files sourced from Vercel's examples repo: a pixel component, a lib file directly inside `lib`, a script file in `public`. Render the component in the body of the root layout. Pixel ID injected via env var, set locally and in the Vercel project settings, then commit/push/build.
- **The Event Setup Tool no-code event (Media Ninja).** Events Manager > Event Setup Tool > enter URL > pick event type "URL contains/equals" > set event = Lead > URL equals the thank-you page. No currency/value for a lead.
- **Pixel Helper ID-match check (Media Ninja, Marketing Mark).** Match the last digits the extension shows against the Events Manager data-set ID, on each page. Works on any site, so it doubles as competitor intel.
- **The broken-install taxonomy (Jamie Stenton).** Three named patterns: not firing, fires twice, wrong event. Plus the fourth by inference: missing on the checkout/separate domain.
- **EMQ, Event Match Quality (Big Short Ads).** A data-quality score out of 10, raised by capturing name/email/phone at checkout. Belongs mostly to the CAPI brain.
- **Numbers experts actually name.** Re-test events every 15 days (Softtrix). Broken data on 50-60% of accounts (Jamie Stenton). Trackable share can swing ~90% to ~20% (Big Short Ads, illustrative). Even 90% coverage tells a wrong story about which ads win (Derek Videll).
- **Safari cookie lifetime, corrected.** Big Short Ads says Safari ITP cuts first-party cookies to "~24 hours". That is wrong as a general rule. **Safari ITP caps script-writable first-party cookies at 7 days.** The 24-hour cap is a narrower case: it applies to cookies set on a page the visitor reached through a navigation Safari has classified as cross-site tracking. So plan on **7 days** of pixel-set cookie life on Safari, treat 24 hours as the worst case for ad-click landings, and stop relying on cookie duration for anything longer than a week — capture hashed email and phone at the form instead.

## Contrarian / disputed takes

- **Manual paste vs native-first, as the default route.** Media Ninja treats manual code as the default for anything custom. Derek Videll pushes native-first (install the platform's app, set "share data" to maximum) for maximum data transfer, falling back to header-paste only when no native app exists. For our GHL + Next stack there is no native app, so both collapse to manual.
- **Is domain verification still needed?** Derek Videll says data sets no longer strictly require it but he still does it to maximise tracked-event percentage. Nobody else raises it, so it sits as one strong voice, not consensus. Most valuable when a checkout lives on a separate domain.
- **Do pixel events prove CAPI is fine?** Jamie Stenton uses working pixel events as a reliable proxy for working CAPI ("if your pixel events are firing correctly, your conversion API events will be firing correctly, too") while conceding a direct CAPI check exists. Pro Data Track's whole case study is the counter-example: the pixel looked installed while CAPI parameters (fbc/fbp, currency, content-ID) were malformed. Verify CAPI directly for money events, do not lean on the proxy.
- **Big Short Ads' "pixel doesn't work anymore" framing** is the outlier in tone. It is promotional and its ad-block / cross-device figures are illustrative, not sourced. The signal-loss point is real; the alarm is overstated.

## Execution playbook

**IF installing on a GHL funnel or page** THEN paste the base pixel into that funnel's "head tracking code" field and Save, per funnel (Media Ninja, Marketing Mark). Do not assume one paste covers other funnels.

**IF installing on a Next.js / Vercel App Router site** THEN do not paste into `layout.tsx`. Build the three-file component pattern from Vercel's examples repo, render the component in the body of the root layout, inject the pixel ID via env var set both locally and in Vercel project settings, then commit/push and let Vercel build (InstinctHub).

**IF the platform has a native app (Shopify, Wix, WordPress)** THEN use the partner/native route and, on Shopify, set "share data" to maximum (Derek Videll, Digital Growth Tutor). **ELSE** use manual code, or paste just the numeric Pixel ID if that is all the field wants (Media Ninja, Marketing Mark).

**IF a backend field asks for a "Pixel ID" not full code** THEN paste only the numeric ID from the base snippet (Derek Videll, Marketing Mark, Media Ninja).

**IF you need a Lead/action event on a thank-you or confirmation page** THEN use the Event Setup Tool, event = Lead, rule = URL equals the thank-you URL, no currency/value for a lead (Media Ninja).

**IF you cannot see your pixel in Events Manager** THEN switch the top dropdown from a specific ad account to the whole business portfolio (Marketing Mark).

**IF there is already a duplicate/legacy pixel** THEN do not try to delete it (you cannot). Rename the unwanted one to "do not use" and only ever attach ads to the correct one (Derek Videll).

**IF a checkout or payment step lives on a separate domain** THEN install and verify the pixel on that surface itself, test each payment method separately in Test Events, and consider domain verification for that domain (Jamie Stenton, Derek Videll).

**Default numbers:** re-test events every 15 days (Softtrix). Never launch on unverified events (Jamie Stenton). Target near-100% coverage; treat a 90% ceiling as a warning, not a pass (Derek Videll).

**Pre-flight checklist (before any campaign spend):**
1. Base pixel present on every page type of the funnel (opt-in, thank-you, checkout, separate domain).
2. Pixel Helper shows the pixel active and the ID matches Events Manager, on each page.
3. Test Events: PageView on load, the action event only on the correct step, and only once.
4. No duplicate firing of any event (open Test Events and confirm single fires).
5. The right data set is selected and it is the only "live" one for this business.
6. For money events, CAPI verified directly, not assumed from the pixel.

**Top 5 failure modes and fixes:**
1. **Pixel not detected on a page.** Cause: per-funnel head field left blank, or an App Router paste that "won't work". Fix: paste base into that funnel, or use the component pattern (Media Ninja, Marketing Mark, InstinctHub).
2. **Event fires twice.** Cause: two install sources (e.g. a plugin plus a manual snippet). Fix: remove the duplicate source and confirm deduplication is on (Jamie Stenton, Pro Data Track, Big Short Ads).
3. **Wrong event fires** (e.g. a form submit firing Lead and Purchase). Fix: rebuild the event mapping in the Event Setup Tool with the correct URL rule (Jamie Stenton, Media Ninja).
4. **Missing on checkout / separate domain**, seen as a platform-vs-Meta sales mismatch. Fix: install and Test-Events the checkout surface itself, per payment path (Big Short Ads, Jamie Stenton).
5. **Ads attached to the wrong (duplicate) pixel**, so tracking looks broken when it is only misattributed. Fix: rename duplicates "do not use", attach to the single correct data set (Derek Videll).

## Applied to your business

**Write your stack down before you audit anything:** ad account `<YOUR_AD_ACCOUNT_ID>`, dataset/pixel `<YOUR_PIXEL_ID>`, CRM `<your CRM>`, pages on `<your funnel builder>` plus `<your custom site, if any>`, checkout on `<where money is taken>`. Then confirm for yourself, in Events Manager, whether CAPI is live for that pixel and whether your money event exists. Do not assume either way.

**Which of your offers this feeds:**
- **Any funnel built in a page builder**: base pixel in each funnel's head-tracking field, Lead event on the thank-you step via the Event Setup Tool.
- **Your money offer**: whichever event represents a sale must stay verified. Verify CAPI directly for it, never via the pixel proxy.
- **Retargeting for a community or recurring offer**: depends on site-visitor and video-view coverage being complete across every funnel, not just the main one.
- **By-invite or noindex pages** (high-ticket, application-only): still install the base pixel for retargeting coverage, but do not optimise a paid event on them.

**Consensus translated into execution moves:**
1. **Audit every funnel's head-tracking field, one by one.** The per-funnel rule means a new landing page can silently ship with no pixel at all. Run Pixel Helper on every live page and confirm the ID matches `<YOUR_PIXEL_ID>` — check the last four digits by eye, page by page.
2. **On a custom-coded site, use a proper component pattern, never a paste into the root layout file.** Verify with Test Events on the live domain after each deploy.
3. **Run a 15-day Test Events cadence across all live funnels.** Watch for double-fires and wrong events as hard as for missing ones. Cheap insurance on any account that is already spending.
4. **Guard a single data set.** Decide which pixel is live, and if any legacy or duplicate exists, rename it "do not use" so no ad ever attaches to it. You cannot delete data sets.
5. **Verify your money event directly (CAPI plus pixel), not by proxy.** Pro Data Track's case is the reason: a pixel can look perfectly installed while its parameters are malformed.

**What may NOT apply to you:**
- **Shopify / Wix native-app installs** (Derek Videll, Digital Growth Tutor's WordPress plugin): irrelevant without that storefront. On a funnel builder plus a custom site you are always on the manual/component route.
- **Big Short Ads' "switch everything to server-side to survive" pitch**: the signal-loss point is real, the alarm is overstated, and server-side is a coverage layer, not an excuse to hand delivery over to automation.
- **Advertiser-catalogue content-ID mechanics (Pro Data Track)**: only relevant with a product catalogue. Route any catalogue work to `brain-meta-capi-server-side-deep`.

## Pairs with / boundaries

- **`brain-meta-capi-server-side-deep`** owns the server-side build (GTM, server containers, fbc/fbp formatting, deduplication mechanics, EMQ tuning). This brain stops at "the browser pixel loses signal, server-side backstops it".
- **`brain-meta-events-and-conversions`** owns Events Manager mechanics: standard vs custom events, custom conversions, the aggregated-event / event-priority config. This brain only covers getting the base pixel and a basic action event to fire per page.
- **`brain-meta-pixel-capi-signals`** is the survey-level parent; this is its deep install sibling. Start here for "where does the code go and why won't it fire", go there for the signals-layer overview.
- **Out of scope here:** campaign structure, budgets, audiences, attribution windows, and any optimisation-event strategy. Those route to the media-buyer and events brains.

## Related brains

- `brain-meta-capi-server-side-deep`: Meta Conversions API server-side tracking deep-dive
- `brain-meta-events-and-conversions`: Meta events and conversions (Events Manager, standard and custom events, custom conversions)
- `brain-meta-pixel-capi-signals`: Meta pixel and CAPI signals layer (end to end survey) Check it
when a question spans topics.

## Deeper references

- `references/synthesis.md`: full thematic synthesis
- `references/quote-library.md`: verbatim quotes with attribution
- `references/experts.md`: who was mined and why (popular vs hidden-gem)
- `examples/ghl-city-funnel-pixel-session.md`: worked session, new city workshop funnel shipped with no pixel, fix to launch gate

Router key `sk-1nfguk` — resolved by the skills index on load.
