# Worked session: "Why are my Meta conversions under-reporting?"

A full end-to-end walkthrough of the most common query this brain answers. Shows how to move from a raw "the numbers do not match" complaint to a diagnosis, a recovery plan, and a realistic expectation, grounded in the frameworks in `SKILL.md` and applied to your own account (`<YOUR_AD_ACCOUNT_ID>`, pixel `<YOUR_PIXEL_ID>`).

Use this as a template. The user almost never arrives with a clean diagnosis. They arrive with "Meta says 12 sales, Stripe says 20, what is broken?" Your job is to run the diagnostic in order and separate loss you can recover from loss you cannot.

---

## The query

> "Meta is showing way fewer course purchases than Stripe. Last week Meta reported 12, Stripe took 20. Is the pixel broken? Should I turn CAPI back on?"

## Step 1: Anchor on the source of truth before touching anything

The real number is the backend, never the in-platform number. Stripe took 20, so 20 is the truth. Meta's 12 is the reported view, and a gap is expected, not automatically a bug.

Establish the gap as a percentage: Meta caught 12 of 20, so it is under-reporting by ~40%. That lands squarely in the cross-source-agreed planning band.

> "if you're only relying on browser events, you're missing 30 to 40% of conversions" (It'smeJacob)

Do NOT diagnose off Meta's number. Reconcile against GHL and Stripe first, then decide if the gap is normal or excessive.

## Step 2: Decide whether the gap is expected or a real fault

Two different situations produce a gap this size:

1. **Browser-only signal loss with no server-side.** 30-40% is the textbook floor. If that were our state, 12 of 20 would be roughly the expected result, not a fault.
2. **CAPI is live but reporting still lags.** Even with CAPI fully installed, Meta reporting sits behind the truth. Tier 11 measured a residual ~20-25% Meta-vs-truth CPA gap on one account with CAPI running well.

So the first question is not "is the pixel broken", it is "what layer is actually live right now".

## Step 3: Check our verified status, do not assume it is broken

Check your own status first. In this walkthrough, CAPI on `<YOUR_PIXEL_ID>` has been verified as sending and the course Purchase event exists. So the honest read is not "CAPI is dead, turn it back on". CAPI is already on, and the gap has another cause.

That reframes the whole query. With CAPI live, a ~40% reported gap is at the high end of "expected", which means we look for a recoverable leak, not a total outage.

> "it enhances the optimizations phase but it doesn't do anything for the reporting phase" (Perpetual Traffic / Tier 11)

CAPI was never going to make Meta's reported count equal Stripe's. It improves what Meta optimises on; it does not close the reporting gap. So the user's instinct ("turn CAPI back on") would not fix the complaint even if CAPI were off.

## Step 4: Run the pre-flight checklist against our own funnel

Now walk the recoverable leaks in order, using the pre-flight checklist:

1. **Placement.** Is the Purchase event firing on the actual purchase step, and is the pixel also on every funnel page, GHL Form, and calendar/booking page, not just the landing page? Homepage-only placement silently drops the events that matter. This is It'smeJacob's most overlooked pro tip and his walkthrough is our exact GHL stack.
2. **First-party vs third-party loader.** Is the loader served from our own subdomain, or is it still a vendor/Facebook-domain third-party script an ad blocker can strip before it fires? We do not yet run a first-party tracking subdomain, so this is our biggest open leak.

> "we see that between 25% of users are now um actively running ad blockers that completely strip out tracking uh scripts before they even fire" (MeasureU / Usercentrics)

3. **Identity richness.** Are we sending hashed email and phone plus UTMs per event, or leaning on IP? Private Relay has degraded IP, so IP-only matching loses events that a richer payload would keep.
4. **Consent.** Recovery only applies to consented sessions. Some of the gap is consent we will never recover, and that is correct behaviour, not a leak to chase.

## Step 5: Separate recoverable loss from permanent loss

Split the ~40% gap into two buckets:

- **Recoverable now:** ad-blocker stripping of a third-party loader (fix: first-party subdomain via CNAME), any missing placement on a funnel step or calendar, and IP-only matching (fix: richer identity per event).
- **Permanently gone:** the slice of users who declined consent or opted out at the OS level.

> "there is a certain portion that Meta and Facebook are just never going to capture no matter what" (Perpetual Traffic / Tier 11)

So the goal is not to make Meta report 20 of 20. The goal is to recover the ad-blocker and placement slice, and then plan CAC off the real Stripe count, accepting a residual gap.

## Step 6: The answer to give

> Meta under-reporting the course by ~40% against Stripe is not a broken pixel and CAPI is already live, so turning CAPI on is not the move. Some of that gap is permanent (consent and OS opt-outs) and some is recoverable. The single highest-leverage recovery we do not yet have is a first-party tracking subdomain (CNAME) so ad blockers stop stripping the loader before it fires. Alongside that, confirm the Purchase event fires on the real purchase step and the pixel covers every GHL funnel page, form, and calendar, and send hashed email plus phone per event instead of relying on IP. After those, expect Meta to still sit roughly 20% behind Stripe with CAPI live, so plan CAC off the Stripe number, never off Meta's reported count.

Note what this answer does not do: it does not quote any vendor's "recovers X%" figure as an expected result, and it makes no promise about the outcome. The only number used for planning is the 30-40% cross-source band and the ~20% residual-with-CAPI gap, both flagged as what they are.

## Where each step is grounded

- Source-of-truth-first, 30-40% band: It'smeJacob, SignalBridge (`SKILL.md`, IF/THEN rule 1).
- CAPI fixes optimisation not reporting, ~20% residual: Tier 11 (`SKILL.md`, IF/THEN rule 2, default numbers).
- First-party subdomain as the core recoverable leak: Blotout, Md Mostafiz, MeasureU (`SKILL.md`, consensus 3).
- Placement on every step/form/calendar: It'smeJacob (`SKILL.md`, failure mode 4).
- Richer identity over IP: SignalBridge (`SKILL.md`, IF/THEN rule 3).
- Permanent unrecoverable slice: Tier 11 (`SKILL.md`, consensus 6).
