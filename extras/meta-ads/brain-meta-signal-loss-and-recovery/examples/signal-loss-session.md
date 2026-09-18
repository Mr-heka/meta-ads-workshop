# Worked session: "Why are my Meta conversions under-reporting vs GHL?"

A worked Q&A for the exact question this brain exists to answer: Meta's in-platform
conversion count is lower than what GHL shows, and the operator wants to know what
is broken and what to do. Every quote below is copied verbatim from
`references/quote-library.md`. Grounded in the frameworks in `SKILL.md` and applied
to your own account (`<YOUR_AD_ACCOUNT_ID>`, pixel `<YOUR_PIXEL_ID>`).

Use it as a template. The operator arrives with a gap, not a diagnosis. Run the
steps in order, and separate loss you can recover from loss you cannot.

---

## The query

> "My GHL pipeline shows 18 leads from the workshop campaign this week, but Meta only
> reports 11. That is a big miss. Is my pixel broken? Do I need to reinstall CAPI?"

## Step 1: Anchor on GHL as the source of truth first

GHL is the CRM, so the GHL count is the real number. 18 leads happened; Meta caught
11. That is a ~39% under-report, which lands inside the cross-source-agreed planning
band, so a gap of this size is expected before it is a fault.

> "if you're only relying on browser events, you're missing 30 to 40% of conversions" (It'smeJacob)

Do not diagnose off Meta's 11. Reconcile against GHL, then decide whether the gap is
normal or excessive.

## Step 2: Understand what is actually being stripped

The lead events fire client-side in the browser first, and that is the fragile layer.

> "client-side conversions they mean they get blocked. They're JavaScript running in the browser." (DENNEY BROS)

So part of the gap is browser-only loss: ad blockers, iOS, and cookie limits killing
the script before or as it fires. That is the recoverable slice, and it is why the
number under-reports even when nothing is "broken".

## Step 3: Check placement across the whole GHL funnel, not just the landing page

The single most common self-inflicted leak on a GHL stack is incomplete placement.
The pixel and CAPI parameters have to sit on every funnel step, form, and calendar,
not only the first page.

> "the most overlooked pro tip like most people even doesn't know is that you need to go in your calendars" (It'smeJacob)

If the Lead event is missing from a GHL Form or the booking calendar, those leads
never reach Meta at all, and that alone can explain a chunk of the 7 missing.

## Step 4: Confirm the two-layer stack is live, do not reinstall blindly

The operator's instinct is "reinstall CAPI". Before touching anything, confirm the
architecture: a first-party client-side pixel to catch what the browser allows, plus
CAPI to backfill what it cannot.

> "no one's going to block a first-party cookie. And so, the first trick is like shifting from third-party cookies to first-party cookies for the client-side piece." (DENNEY BROS)

> "you can also augment that with CAPI or conversion API or server-side tracking. And that backfills it. Because now you're sending events from your server to Meta's server. And that cannot be blocked." (DENNEY BROS)

Assume here that CAPI on `<YOUR_PIXEL_ID>` has been checked and is confirmed sending, so
"reinstall CAPI" is not the fix. CAPI is already the backfill layer. The open gap in
our stack is the first-party client-side layer (a first-party tracking subdomain we
do not yet run), which is what stops ad blockers stripping the loader.

## Step 5: Set the right expectation, CAPI will not close the reporting gap

Even with CAPI running perfectly, Meta's reported number stays behind the truth,
because CAPI is an optimisation tool, not a reporting fix.

> "it enhances the optimizations phase but it doesn't do anything for the reporting phase" (Perpetual Traffic)

So turning CAPI on (or reinstalling it) would not have made Meta report 18 of 18. The
complaint is a reporting-gap complaint, and CAPI does not solve reporting.

## Step 6: Accept the permanent floor

Split the ~39% gap into recoverable and permanent. The recoverable slice is
ad-blocker stripping (fix: first-party subdomain) and any missing placement on a form
or calendar. The permanent slice is consent and OS opt-outs.

> "there is a certain portion that Meta and Facebook are just never going to capture no matter what" (Perpetual Traffic)

The goal is not to make Meta report 18 of 18. It is to recover the ad-blocker and
placement slice, then plan cost-per-lead off the GHL count.

## Step 7: The answer to give

> Meta under-reporting the workshop leads by ~39% against GHL is not a broken pixel,
> and CAPI is already live, so reinstalling it is not the move. First, confirm the
> Lead event fires on every GHL funnel page, form, and calendar, because homepage-only
> placement silently drops booking and form leads. Second, the biggest recoverable
> leak we do not yet have is a first-party tracking subdomain (CNAME) so ad blockers
> stop stripping the loader before it fires. Some of the remaining gap is permanent
> (consent and OS opt-outs) and cannot be recovered. After those fixes, expect Meta to
> still sit roughly 20% behind GHL, so plan cost-per-lead off the GHL number, never
> off Meta's reported count.

This answer uses no vendor "recovers X%" figure as an expected result and makes no
outcome promise. The only planning number is the 30-40% cross-source band, flagged
as what it is.

## Where each step is grounded

- Source-of-truth-first, 30-40% band: It'smeJacob (`SKILL.md`, IF/THEN rule 1).
- Client-side scripts get blocked: DENNEY BROS / Blotout (`SKILL.md`, consensus 1).
- Placement on every step/form/calendar: It'smeJacob (`SKILL.md`, failure mode 4).
- First-party layer plus CAPI backfill as a two-layer stack: DENNEY BROS / Blotout (`SKILL.md`, consensus 3 and 4).
- CAPI fixes optimisation not reporting: Perpetual Traffic (`SKILL.md`, IF/THEN rule 2).
- Permanent unrecoverable slice: Perpetual Traffic (`SKILL.md`, consensus 6).
