# Example session: one worked triage grounded in this brain

Demonstrates how an answer should look when this brain is loaded: grounded in the
synthesis, the IF/THEN playbook and the quote library. Every quote below is
verbatim from the mined transcripts.

## User question

> Ads Manager says my workshop campaign got 42 leads this week, but GHL only shows
> 18 new contacts. CPL in Ads Manager looks fine, so should I just scale the budget
> before the numbers drift further apart?

## Brain-grounded answer

**No. A 42-vs-18 gap is a tracking-mismatch symptom, not a win. Freeze the budget,
event-test before you trust either number, then decide.**

1. **This is the tracking bucket, not the cost bucket.** Pre-flight step 1: name the
   problem type before fixing it. Ads Manager and the CRM disagreeing is the
   canonical mismatch case, and the CPL "looking fine" is exactly the trap, the
   number is only as real as the event feeding it.

2. **Test the events live before trusting the dashboard.** The gate is Stenton's:
   "Most advertisers install the meta pixel and assume that it's working. But you have to first set up all of your events and test that they're working correctly before you launch any campaigns".
   Walk Events Manager -> pixel -> Test Events -> channel Website, fire one real
   lead, and watch what actually fires.

3. **Hunt duplicate and miswired fires, that is the common failure.** A 42-vs-18
   split smells like a single action firing more than one event: "a contact form submissions are firing for both a lead event and a purchase event. When this happens, meta's algorithm starts optimizing your campaigns for the wrong things" (Stenton).
   And this is not rare: "we audit hundreds of accounts a year and we just see this on at least 50 to 60% of accounts" (Stenton). Confirm you are not
   getting multiple events reported for one submission.

4. **Do not optimise or scale off numbers you have not event-tested.** Playbook rule:
   IF Ads Manager disagrees with the CRM THEN test every event live before trusting
   any number, then route the wiring fix to the tracking siblings. Scaling now just
   buys more of a mis-counted result.

5. **Then hand off the fix.** This brain confirms the mismatch exists and whether it
   is a fire / duplicate / miswire. The actual rewiring lives in
   `brain-post-click-tracking-plumbing` and `brain-meta-pixel-capi-signals`. On your
   own account, verify pixel `<YOUR_PIXEL_ID>`: browser and server events are not
   double-counting the same lead.

**Where this came from**: consensus point 8; the *three event failure modes*
(Stenton) under *Named frameworks & methods*; the playbook rule *IF Ads Manager
disagrees with the CRM*; pre-flight steps 1 and 4; *Applied to your business* points
3 and 4; quotes from `references/quote-library.md`.
