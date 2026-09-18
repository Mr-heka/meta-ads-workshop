# Worked session: click-to-WhatsApp ads for an in-person workshop

A real Q&A session showing this brain loaded and answering end to end. Every quote below is copied verbatim from `references/quote-library.md` and attributed the same way. Every number is the expert's own, named inline. Nothing here is new research.

## Scenario

An education business wants a WhatsApp/IG-DM enquiry channel for an in-person workshop, aimed at non-technical business owners. Rules of the account: one ad account only (`<YOUR_AD_ACCOUNT_ID>`), a CRM is wired, and CAPI plus a downstream Purchase event on the pixel (`<YOUR_PIXEL_ID>`) are verified live. Paid lead gen runs form-first (instant form → landing page), so this is an *additional* enquiry channel into the CRM, not a replacement for either.

The brain is loaded. The session runs.

---

## Q1. "Traffic gets the cheapest clicks. Why not run the workshop ad on Traffic and point it at WhatsApp?"

Because Traffic pays for the wrong thing. This is the single most repeated error in the mined set:

> "Facebook does not optimize traffic ads for conversation, it optimizes it for what? For clicks." — V.S.L Digital Marketing Hub, *Facebook Engagement Ads for WhatsApp, Messenger & Instagram Messages (Step-by-Step Guide)*

The working campaign types for WhatsApp, per Justin Lalonde:

> "the two campaigns you're typically going to be using for uh WhatsApp overall are going to be engagement and or sales" — Justin Lalonde, *How To Generate More WhatsApp Messages with Facebook Ads In 2026*

**Move for us:** Engagement (or Sales once the CRM event sync is proven), performance goal "Maximize number of conversations", conversion location set to the Message destination. Never Traffic for this campaign, since our KPI is workshop conversations, not clicks.

## Q2. "Fine, message objective it is. So the conversation count in Ads Manager is my success metric?"

No. The brain's second consensus point: raw message count is a vanity metric. Meta counts any reply to the auto-greeting as a conversion:

> "if someone sends that first message to reply to the automated greeting, then it triggers essentially the conversion event, which means Meta thinks, \"Hey, I've done a good job\"" — Justin Lalonde, *How To Generate More WhatsApp Messages with Facebook Ads In 2026*

Jeremy Haynes calls the decay that follows "pixel conditioning", and his worked maths shows why the reported number lies:

> "if only 10 of them were actually worth it, you actually had a $50 cost per qualified DM" — Jeremy Haynes, *The Best Way To Run Instagram DM Ads In 2026 (Nobody Teaches This)*

Dr. Matt Shiver judges these campaigns the same way:

> "I don't care what my cost per lead is with these campaigns. What I care about is the cost per call and the cost per sale" — Dr. Matt Shiver, *How to Run Instagram DM Ads in 2026 (Post Andromeda)*

**Move for us:** judge the campaign on qualified workshop enquiries and bookings recorded in the CRM, never on the conversations column.

## Q3. "How do I make Meta optimise on real enquiries instead?"

Send a genuine downstream event back. Lalonde's version uses a WhatsApp CRM sync:

> "Watti is going to be able to send this data back to Meta and back to your pixel and your conversion API so that you can see this on the ads manager" — Justin Lalonde, *How To Generate More WhatsApp Messages with Facebook Ads In 2026*

Haynes does it by firing a real web event on a qualifying step before the DM; HubSpot Marketing does it CRM-native, with every conversation auto-creating a contact. Same principle, three tools.

**Move:** the CRM-native route. Every DM enquiry auto-creates a CRM contact with the chat logged, and the qualified-lead/booking outcome feeds back through CAPI on the pixel. Optimise on that signal, not message count.

## Q4. "Targeting: do I stack interests like 'small business owners' and 'AI'?"

Majority verdict in the brain says no. Leave interests off and let the creative do the targeting:

> "I have run multiple campaigns spend tens of millions of ads and so far zero targeting has given me the best results so far right" — Godbless Iboyi • Growth With Paid Ads, *How to Run WhatsApp Business Ads in 2026 Using Facebook Ads Manager (Step By Step)*

Shiver keeps it broad with a minimum age of 25. One flag from the brain's Applied section: several creators praise Advantage+ Audiences, but our locked doctrine keeps Advantage+ Audiences OFF (Advantage+ Placements is the only Advantage+ setting we run). So: broad *manual* audience, city-locked to the workshop's catchment per the campaign playbook, interests blank, and the ad creative itself says who this is for (non-technical business owners).

## Q5. "What are the WhatsApp prerequisites before I build anything?"

Two hard gates from the consensus:

> "But note, the WhatsApp number must be on WhatsApp Business, not your not registered on your normal WhatsApp." — Godbless Iboyi • Growth With Paid Ads, *How to Run Facebook Ads to WhatsApp Group (Beginner's Step-by-Step Guide 2026)*

> "your WhatsApp and business number i.e. account should be connected to your meta business page i.e. Facebook page, only then you will be able to verify it and your ad will run" — My Online Master, *Click-to-WhatsApp Ads Tutorial: The Ultimate Agency Lead Gen Strategy*

Also prune placements. Amit Ghodke's rule:

> "so I advise you to remove this audience network and messenger. and keep your ads limited to Facebook and Instagram" — Amit Ghodke Videos, *How to Run WhatsApp Lead Ads | WhatsApp Lead Gen Ad Campaign*

**Move for us:** WhatsApp Business number connected to the business's Facebook Page and showing verified in Ads Manager before the build, Audience Network off, one channel per ad set.

## Q6. "What goes in the chat template?"

The template is where qualification starts, natively, before publish:

> "Here you can update your welcome message, add call to action buttons, add pre-filled questions, add frequently asked questions." — Digital Growth Tutor, *How to Create a WhatsApp Message Campaign in Meta Ads*

Depth rule: Shiver warns to keep in-chat qualification to 1-2 yes/no style questions because more drops throughput. And to trace which ad brings quality:

> "you want to have a individual keyword for every single ad that you have. So if you have 10 or 20 ads in here, they all should have different keywords" — Dr. Matt Shiver, *How to Run Instagram DM Ads in 2026 (Post Andromeda)*

**Move for us:** native chat template (no third-party autoresponder, which My Online Master and Innocent Popka both flag as a ban risk), greeting + pre-filled message + two qualifying questions (city, business type), a unique keyword per ad variation, saved as a reusable template. Answers land in GHL and enrol the contact in the workshop sequence.

## Q7. "Budget and testing?"

Lalonde's formula sets the number:

> "what is my cost per conversion target times the amount of creatives I want to run is my campaign budget I'm going to put" — Justin Lalonde, *How To Generate More WhatsApp Messages with Facebook Ads In 2026*

Testing shape from the consensus: 3-5 creative variations under one ad set and one template, duplicated with only the media swapped, published one at a time. Launch timing:

> "I always prefer my to run to start running by 12 a.m. the following day so that Facebook is going to utilize my entire budget within the whole 24 hours without trying to rush my budget" — Godbless Iboyi • Growth With Paid Ads, *How to Run WhatsApp Business Ads in 2026 Using Facebook Ads Manager (Step By Step)*

Patience window:

> "Meta recommends running your campaign for at least 7 days so the algorithm can learn about what's working and what is serving up your audience." — HubSpot Marketing, *How to Run WhatsApp Ads for Your Business (Full 7-Step System)*

Kill and scale rules, written down before launch: kill an ad at 2x target cost-per-call with no quality calls (Shiver); scale +20-30% every few days once frequency is under 3 (HubSpot Marketing, Shiver). All AUD targets are our own; the brain's rule is that the method transfers, the absolute currency benchmarks do not.

## Q8. "Should this replace the workshop landing page? And what about the online course?"

No, twice. The set's own counterweight:

> "My final thoughts are that messaging ads are not shortcuts. They are not magic and they are not automatically better than sales ads." — V.S.L Digital Marketing Hub, *Facebook Engagement Ads for WhatsApp, Messenger & Instagram Messages (Step-by-Step Guide)*

Per the Applied section: message ads suit location- and date-bound offers, where a fast "is this near me / what date / is it right for my business" chat beats a form, plus warm retargeting for a membership. A self-paced, price-filtered product stays on a landing page, and high-ticket offers are invite/outbound, not cold click-to-chat.

Once a real conversation starts, this brain stops. Hand the live chat-close to `brain-sales-pipeline-and-chat-close`, and the CAPI payload wiring depth to `brain-meta-capi-server-side-deep`.

---

## What the session produced

1. Engagement objective, "Maximize number of conversations", Message destination. Not Traffic.
2. WhatsApp Business number connected to the Page, verified in Ads Manager, before build.
3. Broad manual audience, city-locked, interests blank, Advantage+ Audiences OFF.
4. Native chat template: greeting, pre-filled message, two qualifying questions, unique keyword per ad.
5. Every enquiry auto-creates a CRM contact; qualified outcomes fire back via CAPI on the pixel.
6. Budget = target CPA x creatives (Lalonde); 3-5 variations, midnight start, 7-day minimum, kill at 2x cost-per-call (Shiver), scale +20-30% under frequency 3 (HubSpot Marketing).
7. Success judged on CRM enquiries and bookings, never the conversations column.
