# Worked example: the brain picking an objective (Sales vs Leads)

A real Q&A walkthrough of this brain choosing a campaign objective for two scenarios and defending the call from the mined experts. Use it as the pattern for how to answer an objective question: name the money-goal, run the funnel test, pick the objective, then guard the optimisation goal.

---

## Scenario A: the in-person workshop seat

**User:** "I'm running ads for a paid in-person workshop. Seat is booked through a landing page, then we close some of them on a call. Sales or Leads objective?"

**Brain's reasoning:**

1. **Name the money-goal in one sentence.** A booked seat, where the actual close often happens live or on a call, not at an online checkout.
2. **Run the funnel test (Christian Jamal + Paul Chinedu Nnamani).** "Sales only makes sense if your buyers completing the entire purchase online with no human follow-up" (Christian Jamal). Here the close involves human follow-up, so it fails the Sales test.
3. **Apply the 50-events rule (Christian Jamal).** "The sales objective needs about 50 purchase events per week per ad set just to exit the learning phase." An offline close never feeds a Purchase event back to Meta, so a Sales objective would starve on missing data.
4. **Pick Leads.** "for most service businesses, the right answer here is leads" (Christian Jamal). Confirmed by Paul Chinedu Nnamani: a business owner "either need lead or sales," and an offline-closing service business is the Leads case.

**Answer:** Leads objective, optimise to the lead event (not link clicks). Buying type stays on Auction. Switch the audience to Original per our manual doctrine.

**Guard rail:** if the optimisation goal is set to "maximize link clicks," the Leads campaign quietly becomes a Traffic campaign (Christian Jamal). Optimise to the actual lead event.

---

## Scenario B: the online course checkout

**User:** "Different offer. It's a $500 course that people buy straight from a checkout page, no call, no follow-up. Same answer?"

**Brain's reasoning:**

1. **Name the money-goal.** A completed online purchase, no human in the loop.
2. **Run the funnel test.** This is the exact case the experts carve out for Sales: the whole purchase completes online with no human follow-up (Christian Jamal). My Online Master agrees for an online checkout: "if you want orders, you must choose Sales as a campaign objective."
3. **Check the data can flow back.** Sales optimising to Purchase only works if the pixel fires a Purchase event. This is the prerequisite the 50-events rule assumes.

**Answer:** Sales objective, optimise to the Purchase event. Not Traffic, not Leads. Buying type stays on Auction. Audience switched to Original.

**Guard rail:** do not optimise to a cheaper proxy like "add to cart" or "view content." "we're optimizing for purchases, not just add to cart or view content. Meta needs to know where the money is made" (HubSpot Marketing, era-flagged, used as context only).

---

## Why the two answers differ (the one line to remember)

Same six-objective screen, opposite pick, because the funnel test splits them: **offline close = Leads, fully-online purchase = Sales.** The objective is locked at publish (My Online Master), so this decision is made before the campaign goes live, never patched after.

## The contested case, reconciled

My Online Master says "if you want orders, you must choose Sales... No one else has to go with any objective," which reads as a blanket rule. It is not a real conflict with Christian Jamal's "most service businesses should run Leads": My Online Master is walking a live online checkout (Scenario B), exactly the case the others reserve for Sales. Different default customer, same underlying test.
