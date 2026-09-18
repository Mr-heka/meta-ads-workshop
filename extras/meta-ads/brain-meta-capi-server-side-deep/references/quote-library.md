# Quote Library: Meta Conversions API server-side tracking deep-dive

All quotes verbatim from the mined transcripts (excluded sources omitted). Grouped by theme.

## Why the pixel alone is not enough

> "But now it's so much and these new things, data loss, ad blockers, iOS, that's what sparked the creation of the conversion API and how it became a core part of advertising." - Rasmus TrueROAS, *The Truth About Meta Conversions API (Nobody Talks About This)*

> "Most of the time about 60 or 70% they will make the correct assumption of whether someone made a purchase." - Ronan Nuttgens, *Meta Conversions API Explained, Complete Setup (For High-ticket Lead-gen)*

> "Browser pixels fail because of ad blockers and iOS tracking restrictions. To fix your attribution, you must use the conversions API to send purchase data directly from your Woo Commerce server to Meta." - Launch Stack Labs, *How to Set Up Meta Conversions API (CAPI) for WooCommerce Purchases*

> "The conversion API is the solution because conversion API can bypass the ad blocker ITP or iOS updates and you can still track the data in a safe way" - Hridoy Banik, *5 Common Meta Pixel & Conversion API Mistakes That Ruin Your Tracking*

> "If you're running meta ad campaign and you do not have a proper metapixel and conversion API connection, you are running your ads nowhere." - Hridoy Banik, *5 Common Meta Pixel & Conversion API Mistakes That Ruin Your Tracking*

> "When browser extensions block the Meta Pixel JS script on your website and tracking data is not sent, server-side integration can provide data for these events." - Garazd Creation, *Odoo Meta Conversions API Setup*

> "But because of various browser restrictions and browser extensions, Facebook started pushing us to use conversions API." - Analytics Mania, *Facebook Conversions API gateway tutorial*

> "CAPI only works with server and from the server, CAPI is able to send events to Meta." - Hasib Ashad, *Meta Conversions API with GoHighLevel - The Complete A-to-Z Setup*

> "First party data is basically when you're sending stuff from your home like if you send it directly to the server and you're sending it from your home" - Rasmus TrueROAS, *The Truth About Meta Conversions API (Nobody Talks About This)*

> "One, you need it to recover the lost events. Two, you need it to be able to send firstparty data" - Rasmus TrueROAS, *The Truth About Meta Conversions API (Nobody Talks About This)*

## Direct API vs Gateway vs GTM server-side

> "You can use the Conversions API Gateway for a codeless setup that usually takes less than an hour." - Meta for Business, *Get started with the Meta Conversions API to optimize your ad performance*

> "If you want a more customized setup and are comfortable working with code, you can choose a direct integration." - Meta for Business, *Get started with the Meta Conversions API to optimize your ad performance*

> "So with conversions API gateway, the setup would look like this. You would still have the Facebook pixel which sends data directly to Facebook but also it would start sending data to some custom domain of yours." - Analytics Mania, *Facebook Conversions API gateway tutorial*

> "Because this request was blocked, Facebook pixel was not loaded properly on a page. And since it was not loaded on a page, it means that there was no request to conversions API either." - Analytics Mania, *Facebook Conversions API gateway tutorial*

> "So I would say you can expect the improvement at best of 1 or 2%." - Analytics Mania, *Facebook Conversions API gateway tutorial*

> "Facebook conversions API gateway does not extend cookie lifetime while we're serverside tagging you can definitely do that if you want" - Analytics Mania, *Facebook Conversions API gateway tutorial*

> "This update is mainly for the advertisers who never got KPI set up at all." - Creative Testing Lab, *Meta Killed the CAPI Setup Problem (Here's How)*

> "What this does kill is the commodity layer of KPI setup services." - Creative Testing Lab, *Meta Killed the CAPI Setup Problem (Here's How)*

> "I always use Google Tag Manager because it always supports pixel and conversion API tags. So I can maintain both of them um in the same place." - Hridoy Banik, *5 Common Meta Pixel & Conversion API Mistakes That Ruin Your Tracking*

## event_id deduplication

> "For dduplication to take place, you need to be sending back an event ID that is unique and is the same from your browser event as your server event." - Danyyil Giba, *How to Properly Install Facebook Pixel & Conversion API in GoHighLevel*

> "if things are being double counted, so you have two events that come through with different event IDs and they both think um a conversion happened, it's going to count it twice even though it was one conversion" - Ronan Nuttgens, *Meta Conversions API Explained, Complete Setup (For High-ticket Lead-gen)*

> "Most common reasons for this would be event ID mismatch, the pixel firing, uh multiple conversions for just one conversion, or multiple events sending up from different software." - Ronan Nuttgens, *Meta Conversions API Explained, Complete Setup (For High-ticket Lead-gen)*

> "thankfully, go high level actually takes care of dduplication for you under a few conditions, which I'll go over in the setup" - Ronan Nuttgens, *Meta Conversions API Explained, Complete Setup (For High-ticket Lead-gen)*

> "in instances like that, you should just turn off your browser data and rely solely on the conversions API. Out the two, I would much rather have the conversions API data in place than I would have the browser data." - Jack Newman, *How to Improve Your EMQ Score on Meta (Event Match Quality)*

> "if you're firing events from both the browser pixel and your serverside make.com pipeline, you must pass a matching event ID in your payload" - CreatorOpsMatrix, *Fix Facebook CAPI 400 Errors in Make.com*

> "You must add the event ID parameter using your Woo Commerce transaction ID. If you skip this, Meta will count every purchase twice." - Launch Stack Labs, *How to Set Up Meta Conversions API (CAPI) for WooCommerce Purchases*

> "The browser event will be marked as processed. The server event must be marked as dduplicated. Click both events to verify the event ids match exactly." - Launch Stack Labs, *How to Set Up Meta Conversions API (CAPI) for WooCommerce Purchases*

> "Meta actually prioritize the pixel events first. So whenever pixel level is not available then it will just take the conversion API." - Hridoy Banik, *5 Common Meta Pixel & Conversion API Mistakes That Ruin Your Tracking*

> "Now is there a way to dduplicate? Yes, which is the entire point uh of this video. But the classic ways of doing it is so inconsistent that the amount of people that are having duplicate events is crazy." - Elyes Hannachi, *How To Setup Meta/Facebook Conversion API For GoHighLevel Call Funnels (FULL SYSTEM GUIDE 2026)*

> "we have a smart deduplication system that retains the CAPI conversion with the value attached. The window for that is up to 5 minutes after the initial event is sent" - Make, *[Webinar] From lead capture to revenue signal*

> "However sometimes it takes time to be dduplicate. You can see here add to card view content is dd duplicated." - MIJAN - Web Analyst GTM & GA4, *How to Check if Facebook Pixel Conversion API (CAPI) Is Working Correctly*

## Signal richness and match quality

> "He can send the event name obviously, the email, the phone, the zip code, the IP address, an external ID." - Elyes Hannachi, *How To Setup Meta/Facebook Conversion API For GoHighLevel Call Funnels (FULL SYSTEM GUIDE 2026)*

> "Okay. But we can see 100% are receiving the IP address, user agent, things like that. 100% are um receiving the browser ID variable and things like that." - Jack Newman, *How to Improve Your EMQ Score on Meta (Event Match Quality)*

> "if you click on test services it will give you that you need to click event ID, phone number, email address and IP address. These are must haves uh if you are implemented implementing conversions API" - Localnichemarketing, *How to Set Up Facebook Conversions API (CAPI) in GoHighLevel*

> "you must normalize, meaning you lowercase and trim the whites space and then securely hash all of that user data" - CreatorOpsMatrix, *Fix Facebook CAPI 400 Errors in Make.com*

> "If you are not sending the customer information parameters then your event match quality score will be low and uh you cannot actually target the right customer at the right time." - Hridoy Banik, *5 Common Meta Pixel & Conversion API Mistakes That Ruin Your Tracking*

> "lead ID gives the highest match accuracy and is always our recommended starting point. Click ID and email are also very high accuracy" - Make, *[Webinar] From lead capture to revenue signal*

> "I quickly realized that the most important part was the Facebook click ID." - Rasmus TrueROAS, *The Truth About Meta Conversions API (Nobody Talks About This)*

> "click funnels does not. you have to write a piece of code that can pull that from uh click funnels level does. So it just depends on the platform." - Jack Newman, *How to Improve Your EMQ Score on Meta (Event Match Quality)*

## The CRM feedback loop (CAPI for CRM)

> "Starting this year, copy for CRM setup is now required to use the conversion leads performance goal on instant forms. This is not a recommendation anymore. It is now a requirement." - Make, *[Webinar] From lead capture to revenue signal*

> "for instant form campaigns using the conversion leads goal with CAPI CRM integration in place, advertisers saw a 21% lower cost per quality lead on average" - Make, *[Webinar] From lead capture to revenue signal*

> "every time you have the lead ID, every time you run instant forms, make sure you are going to store that lead ID within your CRM" - Make, *[Webinar] From lead capture to revenue signal*

> "According to Go Highlevel, the landing page ads won't be effective for feedback loop or proving your lead quality using conversions API." - Hasib Ashad, *Meta Conversions API with GoHighLevel - The Complete A-to-Z Setup*

> "This lead ID is essential for Meta to recognize this lead. So, Connect CRM update back to the original Facebook instant form lead." - Hasib Ashad, *Meta Conversions API with GoHighLevel - The Complete A-to-Z Setup*

> "So, your stage names do not need to be standard meta events when it comes to lead events specifically." - Hasib Ashad, *Meta Conversions API with GoHighLevel - The Complete A-to-Z Setup*

> "Meta uses AI in the backend to interpret that data from the payload." - Hasib Ashad, *Meta Conversions API with GoHighLevel - The Complete A-to-Z Setup*

> "You need to change this to a lead event because funnel event is just for conversion tracking purposes for uh your funnels if you're doing landing page campaign." - Hasib Ashad, *Meta Conversion API Setup With Lead Forms & GoHighLevel*

> "Meta actually matches the event to the right ad using FBlid which is Facebook click ID." - Hasib Ashad, *How Does Meta Conversions API Work?*

> "Basically, when a lead comes from meta to go high level using a lead form, that lead is automatically attributed as a paid ad lead or a social ad lead." - Hasib Ashad, *How Does Meta Conversions API Work?*

> "On average, this approach can lower cost per quality lead by 19% compared to instant form campaigns that use the leads performance goal." - Meta for Business, *Boost lead quality with Meta Conversions API for CRM*

> "That's the signal you're sending to Meta. And the value is basically a potential revenue you may get from this person or this lead." - Hasib Ashad, *Meta Conversion API Setup With Lead Forms & GoHighLevel*

## Feed only quality signal

> "Meaning if a shitty lead books in with you, maybe they answer the questions unfavorably, we don't want our pixel to know about that." - Scott Henry, *How to Setup Meta Pixel & Conversions API on GoHighLevel (Optimize for Website Schedules)*

> "We only want our pixel to be fed qualified leads that fit our offer and that answer favorably to whatever qualification questions we have." - Scott Henry, *How to Setup Meta Pixel & Conversions API on GoHighLevel (Optimize for Website Schedules)*

> "as long as it's not 0 to 10K a month, then we're going to feed the conversions API and reward the pixel cuz this is good data" - Scott Henry, *How to Setup Meta Pixel & Conversions API on GoHighLevel (Optimize for Website Schedules)*

> "By the way I've been getting a lot of questions about this. We don't have to send any badly information. Just talk about the positives here." - Hasib Ashad, *How Does Meta Conversions API Work?*

> "We recently burned 29,000 bucks on meta ads and got terrible results. I actually discovered why that was. It was something so silly it's embarrassing to show you" - Ken Greeff Codes, *How I fixed TERRIBLE results with the Meta Conversions API*

> "So, what we ended up doing was telling Meta, \"Hey, great. We got a registration. You're doing a good job. Go find more of those people.\" And we ended up with hundreds and hundreds of people, the spam accounts" - Ken Greeff Codes, *How I fixed TERRIBLE results with the Meta Conversions API*

> "And the thing is, if you don't do this, you are going to lose money. That is just what going to happen. That's what we did." - Ken Greeff Codes, *How I fixed TERRIBLE results with the Meta Conversions API*

> "Even if even if they became a customer, they were the best one, they spent all the money, they were the easiest clothes out of your life, the algorithm has no idea what to optimize for." - Elyes Hannachi, *How To Setup Meta/Facebook Conversion API For GoHighLevel Call Funnels (FULL SYSTEM GUIDE 2026)*

> "most bots, 95% of them, they're lazy. So they don't check the source code of the funnel. So they send the web hook through the inline script without the secret code and that's how we catch them." - Elyes Hannachi, *How To Setup Meta/Facebook Conversion API For GoHighLevel Call Funnels (FULL SYSTEM GUIDE 2026)*

## Optimisation timing and thresholds

> "there's no point actually optimizing for custom conversion events until like you're hitting 25 50 conversions per week on that specific event" - Elyes Hannachi, *How To Setup Meta/Facebook Conversion API For GoHighLevel Call Funnels (FULL SYSTEM GUIDE 2026)*

> "That's why um layer 1 gives us 80% of the results. And layer 2 is more for squeezing that little tiny part um that's left." - Elyes Hannachi, *How To Setup Meta/Facebook Conversion API For GoHighLevel Call Funnels (FULL SYSTEM GUIDE 2026)*

> "Some people argue that you need a 50 conversions event for conversions API to actually take effect. Some people say it's 200, some people say it's three or five or whatever it is." - Ronan Nuttgens, *Meta Conversions API Explained, Complete Setup (For High-ticket Lead-gen)*

> "So, one thing here, you need to run your ads for at least as long as it takes to get a subscription, right?" - Ken Greeff Codes, *How I fixed TERRIBLE results with the Meta Conversions API*

> "if you are running lead generation lead forms, you should not select maximize number of conversion leads in the beginning because in the beginning, Meta does not have any conversion data from your CRM" - Hasib Ashad, *Meta Conversions API with GoHighLevel - The Complete A-to-Z Setup*

> "Choose a stage that is somewhere between 1% and 40% of leads actually complete" - Make, *[Webinar] From lead capture to revenue signal*

> "the conversion event has to occur within 28 days of lead submission. That's the attribution window, so anything beyond that would not be picked up" - Make, *[Webinar] From lead capture to revenue signal*

> "if you are using your CRM um or updating your CRM once um or twice um in a week or maybe daily, then that's a good option to start optimizing your campaigns for that event. However, if you're not doing it regularly, then this will have no impact" - Localnichemarketing, *How to Set Up Facebook Conversions API (CAPI) in GoHighLevel*

## Verifying it works

> "So you can see is received from both side. This is the server and this is the browser." - MIJAN - Web Analyst GTM & GA4, *How to Check if Facebook Pixel Conversion API (CAPI) Is Working Correctly*

> "you can see check out event is fired and this is the post request you can see here 200. Okay, 200 means it successfully gone to meta." - MIJAN - Web Analyst GTM & GA4, *How to Check if Facebook Pixel Conversion API (CAPI) Is Working Correctly*

> "there is no browser event here because I used the ad broker. That is why you can see here from server it's receiving all this data." - MIJAN - Web Analyst GTM & GA4, *How to Check if Facebook Pixel Conversion API (CAPI) Is Working Correctly*

> "And as expected, it took 25 minutes for it to update. So, it was just constantly saying that there are no events, there are like no integrations, and the pixel is not set up." - Danyyil Giba, *How to Properly Install Facebook Pixel & Conversion API in GoHighLevel*

> "The pixel script doesn't send tracking data about the website activity of internal Odoo users." - Garazd Creation, *Odoo Meta Conversions API Setup*

> "Meta Events Manager allows you to test your Conversions API integration using the test events feature." - Garazd Creation, *Odoo Meta Conversions API Setup*

> "Change all debug settings to false and delete the test event code leaving only empty quotes. If you do not do this, your live sales will permanently be flagged as test events by Meta." - Launch Stack Labs, *How to Set Up Meta Conversions API (CAPI) for WooCommerce Purchases*

> "Open up meta events manager. Copy your unique test_event code and map that code right beneath the action source parameter in your JSON payload." - CreatorOpsMatrix, *Fix Facebook CAPI 400 Errors in Make.com*

> "diagnostic flags that call out common problems like invalid lead IDs, no recent CRM events in the last 24 hours, lead coverage below 60% or missing funnel stages" - Make, *[Webinar] From lead capture to revenue signal*

## Fixing broken setups

> "So that's how you have connected the same thing three times. So that's how you will see like duplicate data in your ads manager." - Hridoy Banik, *5 Common Meta Pixel & Conversion API Mistakes That Ruin Your Tracking*

> "If this is not the case, if this lead doesn't have these attribution information, then what will happen is the lead information won't go through." - Hasib Ashad, *How Does Meta Conversions API Work?*

> "If you're sending from landing pages, you need to make sure you're using go highle form service calendars. You can't use any external like jot forms or type forms or anything like that in your pages." - Hasib Ashad, *How Does Meta Conversions API Work?*

> "we see that um that the the client is optimizing the campaign for lead event inside the Facebook um dashboard. that uh there there is no lead event count inside the event manager. However, a submit application is being firing when a form was submitted" - Localnichemarketing, *How to Set Up Facebook Conversions API (CAPI) in GoHighLevel*

> "One important thing you guys need to know is you can't up on, you know which conversion location you want to do because after you publish it's not going to let you re-edit this." - Scott Henry, *How to Setup Meta Pixel & Conversions API on GoHighLevel (Optimize for Website Schedules)*

> "omitting the mandatory data array wrapper. Your entire event object has to be strictly wrapped inside this array." - CreatorOpsMatrix, *Fix Facebook CAPI 400 Errors in Make.com*

> "The event underscore time parameter must be a precise 10digit Unix timestamp." - CreatorOpsMatrix, *Fix Facebook CAPI 400 Errors in Make.com*

> "Sending a lowercase purchase instead of a capital P purchase will trigger a 400 error instantly." - CreatorOpsMatrix, *Fix Facebook CAPI 400 Errors in Make.com*

> "you must add a header with the key content type and the value application/json" - CreatorOpsMatrix, *Fix Facebook CAPI 400 Errors in Make.com*

> "The first time configuring this you may not select the pixel under CRM events. So it may just give you one default pixel or may not give you the pixel you configured for cappy at all." - Hasib Ashad, *Meta Conversion API Setup With Lead Forms & GoHighLevel*

## Measured impact and accuracy

> "Advertisers using both the Meta Conversions API and Pixel together have seen on average a 13% decrease in cost per conversion." - Meta for Business, *Get started with the Meta Conversions API to optimize your ad performance*

> "Meta's own data shows that advertisers using KPI for web events see an average 17.8% lower CPR compared to pixel-only tracking." - Creative Testing Lab, *Meta Killed the CAPI Setup Problem (Here's How)*

> "So according to Facebook, they say that the average cost per result improvement could be expected up to 13% just by implementing conversions API gateway the way that I showed you just now." - Analytics Mania, *Facebook Conversions API gateway tutorial*

> "And what we're seeing in our data through ROAS is that this helps ad optimization by 15 to 17%." - Rasmus TrueROAS, *The Truth About Meta Conversions API (Nobody Talks About This)*

> "So the real number that the business saw is 528 but what Facebook is showing us is more 535 and if we do the math it's basically 1.3% difference" - Danyyil Giba, *How to Properly Install Facebook Pixel & Conversion API in GoHighLevel*

> "Let me explain why lower than actual is better than higher than actual. Time and time again, I see when a single person can submit the same form on our website multiple times." - Danyyil Giba, *How to Properly Install Facebook Pixel & Conversion API in GoHighLevel*

> "the more you spend as you begin to spend thousands of dollars on ads and with all the data we're getting you get a really strong pixel" - Scott Henry, *How to Setup Meta Pixel & Conversions API on GoHighLevel (Optimize for Website Schedules)*

> "best practice if you're new to conversions API setup, don't put the schedule tracking in um the header tracking. Conversions API will do just as good as a job and it's going to be way more accurate" - Ronan Nuttgens, *Meta Conversions API Explained, Complete Setup (For High-ticket Lead-gen)*
