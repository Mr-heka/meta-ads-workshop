# Worked example: is the online-course Purchase event double counting?

> A realistic session showing this brain loaded against a real question and answered end-to-end. Scenario grounding comes from SKILL.md "Applied to your business" (account `<YOUR_AD_ACCOUNT_ID>`, pixel `<YOUR_PIXEL_ID>`, a CRM holding the records, a verified Purchase event). Every expert claim and number below is taken from `references/quote-library.md` or SKILL.md; no new facts, no new sources.

## Scenario

Online course, $500. Checkout runs on our own site pages with a browser pixel Purchase event plus a direct server-side Purchase send from our backend (the Ken Greeff pattern named in SKILL.md execution move 2). Weekly check-in: Ads Manager is reporting noticeably more course Purchases for the week than GHL shows paid orders. The question lands exactly on this brain's trigger phrasing: "is our pixel double counting".

## Session

**User:** Ads Manager is showing more course purchases than the CRM has orders this week. Is our pixel double counting?

**Brain (loaded, grounded in synthesis and quote library):**

Over-reporting on a Pixel + CAPI setup has a short, documented cause list. Ronan Nuttgens names it directly:

> "Most common reasons for this would be event ID mismatch, the pixel firing, uh multiple conversions for just one conversion, or multiple events sending up from different software." - Ronan Nuttgens, *Meta Conversions API Explained, Complete Setup (For High-ticket Lead-gen)*

Mapped to that stack, there are three concrete suspects for the course Purchase event on `<YOUR_PIXEL_ID>`:

1. **event_id mismatch.** The browser Purchase and the server Purchase carry different IDs, so Meta cannot pair them. Danyyil Giba states the dedup rule:

> "For dduplication to take place, you need to be sending back an event ID that is unique and is the same from your browser event as your server event." - Danyyil Giba, *How to Properly Install Facebook Pixel & Conversion API in GoHighLevel*

2. **The same pixel connected more than once.** Hridoy Banik's classic GHL failure mode:

> "So that's how you have connected the same thing three times. So that's how you will see like duplicate data in your ads manager." - Hridoy Banik, *5 Common Meta Pixel & Conversion API Mistakes That Ruin Your Tracking*

3. **Two systems both sending Purchase.** Our server Purchase comes from our own backend. If any second sender also fires Purchase (a CRM workflow, a leftover test integration), that is Ronan's "multiple events sending up from different software" case, and the brain's rule is to consolidate to one sending system (Hridoy Banik).

**User:** How do I actually check that without guessing?

**Brain:**

The brain treats verification as a protocol, not a vibe. Run it in order.

**Step 1: Test Events pair check.** Fire a test purchase and look for the pair, one Purchase from browser and one from server. The pass condition is explicit:

> "The browser event will be marked as processed. The server event must be marked as dduplicated. Click both events to verify the event ids match exactly." - Launch Stack Labs, *How to Set Up Meta Conversions API (CAPI) for WooCommerce Purchases*

"Deduplicated" status alone is not the finish line. Click into both events and confirm exact ID equality, the Launch Stack Labs standard SKILL.md already applies to this Purchase event.

**Step 2: Ad-blocker isolation.** Repeat the flow with a blocker on. Only the server event should still arrive, which proves the CAPI send is genuinely independent of the pixel:

> "there is no browser event here because I used the ad broker. That is why you can see here from server it's receiving all this data." - MIJAN - Web Analyst GTM & GA4, *How to Check if Facebook Pixel Conversion API (CAPI) Is Working Correctly*

**Step 3: Confirm the test event code is gone from production.** The Purchase event went through QA before going live, so verify the test code was stripped everywhere:

> "Change all debug settings to false and delete the test event code leaving only empty quotes. If you do not do this, your live sales will permanently be flagged as test events by Meta." - Launch Stack Labs, *How to Set Up Meta Conversions API (CAPI) for WooCommerce Purchases*

**Step 4: Don't panic at lag.** If Events Manager looks empty or stale mid-check, wait before declaring anything broken:

> "And as expected, it took 25 minutes for it to update. So, it was just constantly saying that there are no events, there are like no integrations, and the pixel is not set up." - Danyyil Giba, *How to Properly Install Facebook Pixel & Conversion API in GoHighLevel*

**User:** Say the event IDs don't match. What's the fix?

**Brain:**

Two sanctioned fixes, in this order for our stack.

**Fix A (preferred): force the shared event_id at the source.** The server Purchase comes from our own backend, so we control the ID. Use the order's own transaction identifier as the event_id on both the browser and server sends, the same pattern Launch Stack Labs applies with the WooCommerce transaction ID. While the payload is open, keep Meta's must-haves in it. Localnichemarketing lists them:

> "if you click on test services it will give you that you need to click event ID, phone number, email address and IP address. These are must haves uh if you are implemented implementing conversions API" - Localnichemarketing, *How to Set Up Facebook Conversions API (CAPI) in GoHighLevel*

And if the raw Graph API call starts returning 400 during the rebuild, one classic trap from the CreatorOpsMatrix checklist:

> "Sending a lowercase purchase instead of a capital P purchase will trigger a 400 error instantly." - CreatorOpsMatrix, *Fix Facebook CAPI 400 Errors in Make.com*

**Fix B (fallback): go CAPI-only for this event.** If the two IDs can never be forced to match, Jack Newman's rule applies:

> "in instances like that, you should just turn off your browser data and rely solely on the conversions API. Out the two, I would much rather have the conversions API data in place than I would have the browser data." - Jack Newman, *How to Improve Your EMQ Score on Meta (Event Match Quality)*

For a duplicate-connection finding (suspect 2), the fix is Hridoy Banik's: connect the pixel once, remove every other connection point, then re-run Step 1.

**User:** Once it's fixed, should Ads Manager and the CRM match exactly?

**Brain:**

No, and dead even is not the target. The brain's under-vs-over reporting benchmark (Danyyil Giba, in SKILL.md's named frameworks) is that pixel-only setups over-report while a proper Pixel + CAPI setup under-reports slightly, the healthy direction because duplicates get excluded. His pixel-only observation:

> "So the real number that the business saw is 528 but what Facebook is showing us is more 535 and if we do the math it's basically 1.3% difference" - Danyyil Giba, *How to Properly Install Facebook Pixel & Conversion API in GoHighLevel*

And his reasoning for why under is the good direction:

> "Let me explain why lower than actual is better than higher than actual. Time and time again, I see when a single person can submit the same form on our website multiple times." - Danyyil Giba, *How to Properly Install Facebook Pixel & Conversion API in GoHighLevel*

So after the fix: the CRM stays the revenue truth, Ads Manager sitting slightly under the CRM is the healthy state, and Ads Manager above the CRM is the cue to re-run this session.

## Where the session hands off

The moment the Purchase signal is verified true (Deduplicated status, exact ID equality, blocker-proof server events, no test code in production), the question stops being "is the signal true". What to do with the campaign, budget or optimisation goal belongs to `brain-meta-ads-manual-control-no-advantage` and `brain-meta-media-buyer-manual`, per the boundaries in SKILL.md.
