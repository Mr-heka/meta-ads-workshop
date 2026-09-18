# Example session: one worked Q&A grounded in this brain

Demonstrates how an answer should look when this brain is loaded: grounded in the
synthesis, the IF/THEN playbook, the default-numbers table and the quote library.
Every quote below is verbatim from the mined transcripts.

## User question

> My <city> workshop campaign shows 22 leads at a $41 CPL in Ads Manager this week,
> which looks great. But GHL only has 14 new workshop enquiries against the same
> spend. Is Meta lying, and do I cut the campaign because the real CPL is way higher?

## Brain-grounded answer

**Meta isn't lying, it's over-crediting. Don't cut yet. Reconcile the two numbers,
check what view-through is doing, then decide on the GHL number, not the reported one.**

1. **The gap is expected, not a bug.** Standard attribution over-reports by design.
   Both Denney and Shiver put it the same way: "Facebook will credit more of the
   results that it had a hand in than the actual sales it made." Ads Manager's 22 is
   the optimisation dial; GHL's 14 is closer to truth. Treat the reported CPL as
   directional (playbook: *Top 5 failure modes* #1).

2. **Run the pre-flight before judging the campaign.** First: is the pixel/CAPI
   firing cleanly and not double-firing? A pixel bug fakes the whole picture (Shiver:
   8 reported calls, 2 real). Second: what setting is the account on, and is 1-day
   view on? For our booked-call/lead model that is the setting most likely to be
   inflating the 22 (*Pre-flight checklist* steps 1-2).

3. **Check the view-through share.** Open Compare Attribution Settings and read the
   gap. If a big slice of those 22 came from 1-day view, they are people who scrolled
   past the ad and enquired anyway. Shiver's rule for a lead-gen model: "she has 7-day click
   and one day view... you can see at this bottom campaign, almost 10% a little bit
   more than 10% of the leads came from one day view." Our default number: if
   view-through is **>25% of conversions**, strip to 7-day-click-only (*Default
   numbers*; playbook IF/THEN rule 1).

4. **Reconcile, don't conflate.** The 22 and the 14 are two different measurements,
   not a right and a wrong one. The CRM is the scoreboard: real workshop CPL this week is
   spend ÷ 14, and that is the number a kill/scale call rides on. This is exactly the
   lead-gen case Stewart wired as cost-per-signed-client (*Applied to your business*
   #3; playbook *Top 5 failure modes* #2).

5. **Decide on the primary metric only.** If the GHL CPL is still inside target, the
   campaign is fine and the Ads Manager gap is just over-attribution you now
   understand. If GHL CPL is over target, then cut. Either way CTR and hook rate
   explain, they never decide (Denney + wider verified evidence; playbook IF/THEN rule 7).

6. **Do not reach for Incremental Attribution or a holdout here.** IA is a reading
   tool here, not a switch to flip, and formal geo-holdouts need volume we don't run
   at city-locked $2-8k/month. If you ever want the true-lift read, the cheaper proxy
   is a turn-down test, and the deep mechanics live in the sibling deep brain
   (*Pairs with / boundaries*; playbook IF/THEN rule 5).

**Where this came from**: consensus points 2 and 5; the *Pre-flight checklist* and
*Top 5 failure modes*; the *Default numbers* view-through red-flag; *Applied to our
business* points 3 and 5; quotes from `references/quote-library.md`.
