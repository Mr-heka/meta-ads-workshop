# Worked example: new GHL city funnel shipped with no pixel

A worked session showing this brain loaded against a realistic scenario and answering end-to-end. Every expert claim below is quoted verbatim from `references/quote-library.md` or paraphrased with the expert named. No new sources, no new numbers.

**Scenario.** A city funnel for a $2,000 in-person AI workshop gets cloned in the funnel builder for a second city run. Ads are queued on `<YOUR_AD_ACCOUNT_ID>`. A quick check with the Meta Pixel Helper on the new opt-in page shows nothing. Question on the table: why is the pixel missing, how do we fix it, and can the campaign launch today?

**Brain trigger.** "Pixel not detected" on a funnel-builder page is a direct hit on this brain's description. Loaded before answering. The server-side rail and the checkout Purchase event are a separate surface and stay out of scope here.

---

## Q1: The pixel works on the original funnel. Why is it missing on the clone?

Because GHL installs are per funnel, not global. This is the single biggest gotcha in the brain, and two independent practitioners describe the exact same path:

> "I'm on go high level and in go high level, I just have to come into my funnel or my website and I have to do this on a perfunnel basis, per website basis." - Marketing Mark, *How To Set Up & Install Your Meta Pixel (EASY 2026 Guide)*

Media Ninja describes the same route: funnel settings, the "head tracking code" field, paste the base pixel, Save, and one paste covers the opt-in and thank-you pages inside that funnel. A funnel you did not touch has no pixel. Cloning a funnel and assuming coverage carried over is exactly how a new city funnel ships blind.

## Q2: Fix it. Where does the code go?

Base pixel snippet for data set `<YOUR_PIXEL_ID>` into the new funnel's "head tracking code" field, then Save. Derek Videll's orientation for anyone new to funnel builders:

> "This is not the visual top part of your website. This is the code section of your website called the header." - Derek Videll, *How To Setup a Meta Dataset / Pixel [2026 Update]*

PageView needs no extra work once the base code is in:

> "Pretty much the second you have the pixel installed on any part of your website, on any page, the page view event will always fire. You don't have to set up this event. This is automatically done for every single website and every single pixel case." - Media Ninja, *How To Install The Facebook Pixel And Track Events In 2026*

## Q3: The workshop funnel needs a Lead event on the thank-you page. How?

Event Setup Tool, no code. Media Ninja's exact configuration:

> "So, for this type of event, I'm going to be tracking a URL, where specifically the event is a lead event, and the URL equals to my thank you page URL." - Media Ninja, *How To Install The Facebook Pixel And Track Events In 2026*

Rule = URL equals the new funnel's thank-you URL. No currency or value on a lead (Media Ninja).

## Q4: How do we prove it before spend?

Two tools, every page, per the brain's strongest consensus theme.

**Tool one, Meta Pixel Helper:**

> "It's called the Metapixel Helper. It's a Google Chrome extension. So, you can just search Metapixelhelper Chrome extension on Chrome and install it." - Marketing Mark, *How To Set Up & Install Your Meta Pixel (EASY 2026 Guide)*

Open the opt-in page and the thank-you page separately, confirm the pixel shows active, and match the ID the extension displays against Events Manager. It must read `<YOUR_PIXEL_ID>`, nothing else. Media Ninja checks the ID match on each page separately, not once for the site.

**Tool two, Test Events:** paste the funnel URL, click through the real flow. PageView on load of both pages, Lead only after the form submits on the thank-you page, and only once. Jamie Stenton's specific check while watching:

> "What you do want to check is that you're not getting multiple events being reported, multiple events happening cuz that is really really common" - Jamie Stenton, *How to Test Your Meta Pixel Events (Fix Broken Facebook Tracking)*

Side note if the data set is not visible in Events Manager during any of this, Marketing Mark's trap applies:

> "if you come in here and you're not seeing it, it might be because you have another ad account. Um, but if you don't have any ad accounts, you should see it." - Marketing Mark, *How To Set Up & Install Your Meta Pixel (EASY 2026 Guide)*

Switch the top dropdown from the ad account to the whole business portfolio.

## Q5: Ads are queued. Can we launch today?

Only after the verification in Q4 passes. The brain's hard gate:

> "you have to first set up all of your events and test that they're working correctly before you launch any campaigns and that's really key" - Jamie Stenton, *How to Test Your Meta Pixel Events (Fix Broken Facebook Tracking)*

This is not caution for its own sake. Stenton's audit base rate:

> "A huge number of ad accounts are optimizing campaigns on completely broken event data. Now, we audit hundreds of accounts a year and we just see this on at least 50 to 60% of accounts." - Jamie Stenton, *How to Test Your Meta Pixel Events (Fix Broken Facebook Tracking)*

And the cost of launching anyway:

> "When this happens, meta's algorithm starts optimizing your campaigns for the wrong things and that's when accounts quietly start burning through your money." - Jamie Stenton, *How to Test Your Meta Pixel Events (Fix Broken Facebook Tracking)*

So the sequence is: paste, map the Lead event, verify with both tools, then launch. Same day is fine if all checks pass; the checks are not skippable.

## Q6: What stops this happening on the next city funnel?

Two standing habits from the playbook:

1. **The 15-day re-test cadence** across all live funnels:

> "I would recommend every 15 days you need to test those events to check whether they are working correctly or not." - Softtrix, *How to Test Facebook Pixel Events for Accurate Conversion Tracking*

2. **Guard the single data set.** If a clone or an old setup ever spawns a duplicate pixel:

> "there does not seem to be a way that you can delete them. So, you only want one per company." - Derek Videll, *How To Setup a Meta Dataset / Pixel [2026 Update]*

Rename any duplicate to "do not use" (Derek Videll) and only ever attach ads to `<YOUR_PIXEL_ID>`.

---

## Session outcome

- Root cause named from the brain's consensus, not guessed: per-funnel head field left blank on a cloned funnel.
- Fix, event mapping, and two-tool verification all executed from the playbook's GHL route.
- Launch held behind the verify gate, per Jamie Stenton, then cleared.
- New city funnels added to the 15-day Test Events cadence (Softtrix).

**Boundary respected:** this funnel's Lead event is a browser-pixel job. Anything touching the online-course Purchase event or CAPI parameter checks routes to `brain-meta-capi-server-side-deep`; this brain stops at the browser install.
