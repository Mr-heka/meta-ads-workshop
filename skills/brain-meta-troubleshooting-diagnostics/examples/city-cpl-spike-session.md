# Example session: one worked triage grounded in this brain

Demonstrates how an answer should look when this brain is loaded: grounded in the
synthesis, the IF/THEN playbook and the quote library. Every quote below is
verbatim from the mined transcripts.

## User question

> My <city> workshop campaign was pulling leads at $3.89 in week one. Three weeks
> in it's $23.64 and still climbing, and nothing in the account changed. Is Meta
> throttling us, is my account health tanking, or is something actually broken?
> Should I just move the budget to a fresh city to escape it?

## Brain-grounded answer

**Nothing's broken and Meta isn't throttling you. A 6x CPL climb with no account
change is the textbook relevance-penalty pattern, creative fatigue that Meta reads
as irrelevance. Triage the ad before you move a dollar, and do not run to a new
city.**

1. **Name the bucket first: this is a cost problem, not a delivery or tracking one.**
   Pre-flight step 1: confirm which of the four problem types it is before fixing.
   The ad set is still delivering, the dashboard isn't erroring, Ads Manager and GHL
   agree, so skip the non-delivery ladder and the tracking gate and go straight to
   the cost half of the map. The signature is exactly Anan's: "So you will see high cost per click, high CPMs or cost per 10,000 impressions and a skyhigh cost per lead."

2. **The cause is a relevance penalty, not a Meta fault.** Anan's mechanism: "Meta's algorithm optimizes for user retention. So, if people scroll past your ad after like 0.5 seconds of interacting with your ad, Meta learns that your ad is irrelevant and charges you more to compensate."
   Three weeks of the same creative into a 40-50km city radius means the same people
   keep scrolling past a now-familiar ad, and Meta re-prices that as irrelevance.
   Learn with Bilal's frame is the sanity check: Meta's only job is to deliver the
   message; CPL and sales are downstream symptoms of weak creative, offer or page,
   not a billing bug.

3. **Read the 3-second play rate to tell a dead hook from a dead offer before you
   touch anything.** Bunkar: "Stop testing creative on Facebook ads and look at this metric that will tell you in 24 hours whether your creative is doing well or failing."
   Add "3-Second Video Play Rate" plus a ThruPlay column via Customize Columns. "If your 3 second video play count is below 40% you need to change the hook. There is no need to change the offer or product."
   If 3-sec is high but completion is low: "If your 3 second play view count is coming high but completion rate is low, that is, the play through rate is coming low, it means your offer or body is weak, so you need to strengthen it."
   His live read was a winner at 55-56% versus a failing creative at 13-14%, that's
   the gap you're looking for.

4. **Diagnose with the 3-second rate, but make the kill/keep call on CPL.** Bunkar
   treats a sub-40% 3-second rate as enough to condemn the hook. The wider verified evidence
   (Ben Heath) is firm the other way: hook rate and CTR explain WHY, never decide
   WHAT to kill (his 16% hook-rate ad lost on cost-per-purchase to a 10% one).
   Reconcile: use the 3-second rate to decide what to fix (hook vs body vs offer),
   keep the final decision on our $6-10 CPL target. A rising view rate is also the
   way back down: "If your 3 second view rate is high... the algorithm has realized that this creative is engaging and it shows it to more people. Due to which your CPM also falls." (Bunkar).

5. **Check message-to-awareness match, then route, don't relocate.** Anan's awareness
   ladder: are we pitching "the setup" and features to a cold <city> owner still at
   the awareness stage? "When you talk about your products and services in your ads, but your audience is still in the awareness stage. You're speaking literally a different language."
   The fix is a pain-led rewrite (80/20 pain-to-offer landing page, test at least
   four days), not a testimonial dropped into a cold ad. Moving the budget to a fresh
   city just throws away the auction history and resets the fatigue clock somewhere
   new. Ship rotated creative concepts beside the winner and hand the fatigue
   mechanics to `brain-meta-auction-and-delivery`. Only if creative and message-match
   are clean does the hidden account-reputation score become the next prompt (Mouss,
   contested, directional only): "Same auction, same audience, different score. It means different ads spend different price".
   Pulling that report generally needs a Meta-rep relationship, so treat it as a check,
   not a cause. On account **`<YOUR_AD_ACCOUNT_ID>`** this is the classic fatigue pattern:
   new concepts, not more spend.

**Where this came from**: consensus points 7 and 8; the *3-second play-rate
diagnostic* (Bunkar) and the *awareness ladder* (Anan) under *Named frameworks &
methods*; the playbook rule *IF CPM/CPL spiked THEN check relevance before blaming
Meta*; pre-flight step 1; the contrarian take *kill on the 3-second rate vs kill on
cost-per-result*; *Applied to your business* point 2; quotes from
`references/quote-library.md`.
