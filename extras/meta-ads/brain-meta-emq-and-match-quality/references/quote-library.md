# Quote Library: Meta Event Match Quality (EMQ) and Advanced Matching

Verbatim quotes from the mined transcripts, grouped by theme. Transcription quirks (auto-caption errors like "dduplication", "event mass quality") are left exactly as spoken/captured.

## What EMQ is and how it's scored

> "The EMQ score is a 0 to 10 rating that Facebook assigns to each event type on your pixel. Not to your pixel overall, but to each individual event." - SignalBridge, *EMQ Score Explained: How Meta Controls Your Facebook Ad Costs*

> "EMQ 1 to 3, critical. You're basically sending blind data. Facebook can barely use your events." - SignalBridge, *EMQ Score Explained: How Meta Controls Your Facebook Ad Costs*

> "6.0. That's the magic number, or rather, it's the absolute threshold for failure" - CreatorOpsMatrix, *Fix EMQ 3.2 in Meta Ads (CAPI Setup Guide 2026)*

> "page view 6.1 out of 10 schedule 8.8 8 submit application 6.1 and then lead 9.3." - Jack Newman, *How to Improve Your EMQ Score on Meta (Event Match Quality)*

> "Event Match Quality indicates how effective the customized information parameters sent with your server event may be in matching events to meta accounts." - Habibur Rahman, *Improve Meta Pixel Event Match Quality (Full Guide)*

> "Event match quality EJ a score or rating used by meta to measure how accurately your server side conversion API events match with real user on Facebook or Instagram" - Germinate IT, *How to Boost Event Match Quality to 9/10+*

## Match keys and parameter stacking

> "An event with just an IP address, EMQ of two or three. Add a hashed email, jump to six or seven. Add phone number and click IDs, now you're at eight or nine." - SignalBridge, *EMQ Score Explained: How Meta Controls Your Facebook Ad Costs*

> "Adding hashed email alone can boost your EMQ by 1.5 to two points." - SignalBridge, *9+ EMQ Score: 7 Ways to Lower Your Facebook Ad Costs*

> "Email plus phone together typically push your EMQ from five or six to seven or eight immediately." - SignalBridge, *9+ EMQ Score: 7 Ways to Lower Your Facebook Ad Costs*

> "So here they have given a list of which user parameters they give higher priority to. Priority depends on the base." - Habibur Rahman, *Improve Meta Pixel Event Match Quality (Full Guide)*

> "Examples include hashed email, first name, phone number, city, IP address or click ID" - Meta for Business, *Increase your event match quality score by adding additional high-quality parameters*

> "These parameters help Meta accurately connect events to people using information such as hashed emails or phone numbers" - Meta for Business, *Increase your event match quality score by adding additional high-quality parameters*

> "Did you know advertisers that include additional high-priority parameters may see an increase in matched events and their event match quality score, which can lead to better ad performance and additional conversions reported" - Meta for Business, *Increase your event match quality score by adding additional high-quality parameters*

## Hashing and normalisation

> "The string must be hashed and of course you have to hash that data in the method that has 265 hashing method, so if you get the input like this, you have to normalize the output, all of it should be small letters" - Habibur Rahman, *Improve Meta Pixel Event Match Quality (Full Guide)*

> "when you will send email that time it's required hash, phone number required hash, first name record hash, last name hash, uh date of birth record hash and then gender record hash hash" - Germinate IT, *How to Boost Event Match Quality to 9/10+*

## CAPI as the structural layer

> "you have to have the conversions API to be sending back that serverside data if you want to show your EMQ score." - Jack Newman, *How to Improve Your EMQ Score on Meta (Event Match Quality)*

> "Out the two, I would much rather have the conversions API data in place than I would have the browser data." - Jack Newman, *How to Improve Your EMQ Score on Meta (Event Match Quality)*

> "Meta's documentation states that advertisers using CAPI alongside their pixel see an average EMQ improvement of two to three points over pixel-only setups." - SignalBridge, *9+ EMQ Score: 7 Ways to Lower Your Facebook Ad Costs*

> "If the browser events are blocked, meta will get the conversion API events and process the data from there." - PixelYourSite, *How to Set Up Meta CAPI with PixelYourSite + Tips to Boost EMQ Score*

> "if you know what 40 50% of all um people on the web use an ad blocker, everyone on on an iPhone" - TrackingFixes, *Shopify Meta CAPI Fix: Achieving 100% Deduplication & 8.x+ Match Scores*

> "I love to send from two side from metapixel and conversion API also because Facebook recommend recommended to send from metapixel and conversion API" - Germinate IT, *How to Boost Event Match Quality to 9/10+*

> "Server-side tracking failures, they happen completely silently. Unlike a standard browser pixel error, where you usually get a big flashy warning in the Events Manager" - CreatorOpsMatrix, *Fix EMQ 3.2 in Meta Ads (CAPI Setup Guide 2026)*

> "This is where server-side tracking with full parameter enrichment puts you." - SignalBridge, *EMQ Score Explained: How Meta Controls Your Facebook Ad Costs*

> "We won't use this conversion API getaway. We will use actually the direct integration because it's built in pixel your site and it works really well." - PixelYourSite, *How to Set Up Meta CAPI with PixelYourSite + Tips to Boost EMQ Score*

## FBC / FBP click identifiers

> "They persist for up to 400 days instead of just 7 days." - SignalBridge, *9+ EMQ Score: 7 Ways to Lower Your Facebook Ad Costs*
>
> **Factual correction (do not repeat the claim as stated).** He says this of Safari. 400 days is Chrome's cookie `max-age` cap, not Safari behaviour. Safari also caps server-set cookies at 7 days when the subdomain CNAMEs to a third-party tracking host. Quote 400 days for Chrome only; assume ~7 days on Safari.

> "the FBP, the Facebook browser ID, is auto-generated by the base pixel for every single visitor... But the FBC, the Facebook click ID, that only generates when a user physically clicks an advertisement" - CreatorOpsMatrix, *Fix EMQ 3.2 in Meta Ads (CAPI Setup Guide 2026)*

> "Step one, a user clicks an ad and Meta appends the FBCLID. Step two, your landing page captures that and stores it. Step three, an automation tool like a make.com webhook intercepts and parses the payload" - CreatorOpsMatrix, *Fix EMQ 3.2 in Meta Ads (CAPI Setup Guide 2026)*

> "If I give the click ID, it was high on the priority list, so if I tick this click ID from my tracking, then it is obvious that the even match quality that I am getting here will be close to almost none." - Habibur Rahman, *Improve Meta Pixel Event Match Quality (Full Guide)*

> "This means the server sends sending incorrect or change the click ID information. When this happens meta cannot properly attribution pes and reporting becomes inaccurate." - Pro Data Track, *How I Fixed Facebook Pixel, Conversion API & Catalog Match Rate Errors*

## Event deduplication

> "This pair of events will have the same event ID and meta will duplicate. If they receive both events they will process only one." - PixelYourSite, *How to Set Up Meta CAPI with PixelYourSite + Tips to Boost EMQ Score*

> "for dduplication to take place, you need to be sending back an event ID that is unique and is the same from your browser event as your server event." - Jack Newman, *How to Improve Your EMQ Score on Meta (Event Match Quality)*

> "These plugins and apps don't allow backend customizations. You cannot edit the code. So you cannot solve these problems correctly." - Pro Data Track, *Avoid Deduplication Errors on Meta Pixel & CAPI*

> "if you have a uh use use the Shopify apps, it it usually ends up that you have multiple tags or multiple things going on where it uh counts everything a few times over" - TrackingFixes, *Shopify Meta CAPI Fix: Achieving 100% Deduplication & 8.x+ Match Scores*

> "If you are facing uh even duplicate issues and all other complex problems like event mass quality going down event coverage decrease pricing and value issues catalog mass rate problems" - Pro Data Track, *Avoid Deduplication Errors on Meta Pixel & CAPI*

> "Facebook um received two events but they are counting only one events. That's mean Facebook ads can understand this only one person's their first product." - Pro Data Track, *Avoid Deduplication Errors on Meta Pixel & CAPI*

## Advanced matching implementation

> "only 81% of the total events that are being sent to meta are having that hashed email address variable sent." - Jack Newman, *How to Improve Your EMQ Score on Meta (Event Match Quality)*

> "go high level is not the only platform that does this. There's loads of others that do it." - Jack Newman, *How to Improve Your EMQ Score on Meta (Event Match Quality)*

> "Pixel your site has access to the Facebook login ID and we can send it with conversion API events which helps uh matching events to a user and improves EMQ score." - PixelYourSite, *How to Set Up Meta CAPI with PixelYourSite + Tips to Boost EMQ Score*

> "We can do the same from URL parameters and I have a video here and uh this will help the plug-in to take data from URL parameters." - PixelYourSite, *How to Set Up Meta CAPI with PixelYourSite + Tips to Boost EMQ Score*

> "we can send customer data in uh purchase event but we can't send it uh view content ABC FBP all everything if I it it is view content uh here I can send FBC FBP FP" - Germinate IT, *How to Boost Event Match Quality to 9/10+*

## Data integrity: real data, never fake

> "You can easily make a event match quality 10 out of 10 by sending fake or random data like random numbers or fake Gmail." - Pro Data Track, *EMQ Benchmarks for 2024/2025*

> "Meta might think think your signals are strong, but in reality it's just noise. So the goal isn't to look perfect. The goals is to track perfectly with a real meaningful data." - Pro Data Track, *EMQ Benchmarks for 2024/2025*

> "If the value doesn't exist, we simply leave it empty or use a valid default." - Pro Data Track, *EMQ Benchmarks for 2024/2025*

> "Partial events with missing parameters lower your EMQ score. Complete events with all parameters maximize it." - SignalBridge, *9+ EMQ Score: 7 Ways to Lower Your Facebook Ad Costs*

## Business impact, monitoring and diagnosis

> "Advertisers with an EMQ below six are paying 22% more per conversion than those with above eight." - SignalBridge, *9+ EMQ Score: 7 Ways to Lower Your Facebook Ad Costs*

> "Accounts with EMQ below 4 pay on average 22% more per conversion than accounts with EMQ above 8." - SignalBridge, *EMQ Score Explained: How Meta Controls Your Facebook Ad Costs*

> "Accounts that improve EMQ from the 4 to 6 range to 8 to 10 range saw CPA drop by 8 to 15% within the first 60 days." - SignalBridge, *EMQ Score Explained: How Meta Controls Your Facebook Ad Costs*

> "Remember, as I covered in my video on how the algorithm works, the learning phase requires approximately 50 conversion events per week." - SignalBridge, *EMQ Score Explained: How Meta Controls Your Facebook Ad Costs*

> "If your EMQ drops from nine to six and you don't notice for a month, that's a month of higher CPAs and degraded algorithm performance." - SignalBridge, *9+ EMQ Score: 7 Ways to Lower Your Facebook Ad Costs*

> "the reason for this it doesn't jump automatically to 10 of 10 is that it's on a rolling 48 hour window or so and that also depends on how many events you actually have" - TrackingFixes, *Shopify Meta CAPI Fix: Achieving 100% Deduplication & 8.x+ Match Scores*

> "100% of total events have an hashed email um IP address is at 90 which is a little bit low" - TrackingFixes, *Shopify Meta CAPI Fix: Achieving 100% Deduplication & 8.x+ Match Scores*

> "Hitting a score of 6.0 or higher proves your server payload successfully contains that hashed customer data and those critical identifiers" - CreatorOpsMatrix, *Fix EMQ 3.2 in Meta Ads (CAPI Setup Guide 2026)*

> "third, batching your server side events to run hourly. That last one is a particularly dangerous trap. We call it the batching penalty" - CreatorOpsMatrix, *Fix EMQ 3.2 in Meta Ads (CAPI Setup Guide 2026)*

> "low low match quality or low catalog measure rate missing content ID even not fire properly then don't wait this issue hard your ROS waste your budget" - Pro Data Track, *How I Fixed Facebook Pixel, Conversion API & Catalog Match Rate Errors*

## Event setup and funnel tagging

> "if you don't set up your event tracking correctly, nothing else really matters with your campaigns. They're not going to work. They are not going to perform." - Jamie Stenton, *How to Use Meta's Event Setup Tool (Fix Your Facebook Pixel Tracking)*

> "This has to be the website that the pixel is actually installed on, or it will not work." - Jamie Stenton, *How to Use Meta's Event Setup Tool (Fix Your Facebook Pixel Tracking)*

> "Now, until I click this finish setup button, it is not done. So, it's not complete until you click that finish setup." - Jamie Stenton, *How to Use Meta's Event Setup Tool (Fix Your Facebook Pixel Tracking)*

> "You need to navigate to the thank you page, then you just need to strip out all of these letters, all of the the random gibberish that might appear, and make sure it reads URL contains on that." - Jamie Stenton, *How to Use Meta's Event Setup Tool (Fix Your Facebook Pixel Tracking)*

> "If you do equal, it has to exactly match the URL that you have set." - Jamie Stenton, *How to Use Meta's Event Setup Tool (Fix Your Facebook Pixel Tracking)*

---

Quote count: 59. All verbatim from the mined transcripts (thin-flagged sources excluded).
