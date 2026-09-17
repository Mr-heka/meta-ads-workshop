# Worked example: cold campaign spending on past buyers

A hypothetical but representative session showing this brain applied end-to-end.
The scenario is invented for illustration; every rule, number and citation comes
from the brain's synthesis and quote library.

---

## The ask

> "Our cold lead campaign keeps reaching past customers, cost per lead has
> climbed over three weeks, and we also run a separate retargeting campaign
> for the same offer. The exclusion list is attached. Why isn't it working?"

## Step 1: Check the plumbing before blaming the exclusions

First question: are engaged and existing-customer segments defined in
advertising settings? If not, the new/engaged/existing spend breakdown reads
"all unknown" and every claim about warm leakage is a guess (failure mode 5
in SKILL.md). Define them, then read the split at ad set level.

Second: calibrate expectations. Some warm spend in a cold campaign is normal,
not a defect:

> "About a third of my budget on both of these campaigns went to retargeting. Okay? So, even if you go broad, you're going to get retargeting." - Dr. Matt Shiver

In this scenario the breakdown showed 55% of spend on engaged plus existing.
That is well past the expected one-third-to-40% band, so something real is
wrong. Two suspects, checked in order: the exclusion does not bind, or the
lists are stale.

## Step 2: Does the exclusion bind at all?

The ad set was on Advantage+ audience with the buyer list added as an
exclusion. That puts the list in the suggestion zone:

> "Basically, Meta can choose to target your warm audience or choose to ignore it." - Ben Heath

Chelsea Gardner's gating condition applies: exclusion fields only work as
intended with detailed targeting off, original custom audiences, "Limited"
mode. Fix: switch the ad set to original audiences, re-attach the buyer and
converter lists as exclusions there. For any audience that must bind as an
include (not relevant here, but the same trap), Heath's hard-constraint click
path is the tool: further limit reach > switch setup > list under controls >
untick "use as a suggestion".

## Step 3: Are the lists stale?

The buyer exclusion was a pixel-based purchase audience. Pixel windows cap at
90 days (lead forms), 180 (website), 365 (page engagement), so every buyer
older than the window had already fallen out of the exclusion and leaked back
into cold delivery (failure mode 3). Fix: export the full buyer list from the
CRM, upload it, exclude the uploaded list, and schedule a refresh after every
sales cycle. The standing suppression list (do-not-contact, hostile
commenters) rides along on every ad set per Gardner's method.

## Step 4: Kill the self-competition, do not patch it

The separate retargeting campaign for the same offer was the CPL culprit, not
the exclusion list. Two campaigns chasing overlapping people break Meta's
impression-frequency planning and starve learning:

> "So, why have two ad sets or two campaigns targeting the same people with the same offer when you can have one?" - Ben Heath

The consolidation math decides it: one ad set clearing about 50 conversions a
week beats two at 25. Do not add cross-exclusions between the two campaigns
to separate them; consolidate instead (failure mode 4).

## Step 5: Rebuild to the two-ad-set structure

Final shape, per LYFE's structure: one campaign, one broad prospecting ad set
with the uploaded buyer list, converter list and standing suppression list
excluded and only true hard controls set (location, age if genuinely
required), plus one retargeting ad set on the custom audiences. At this spend
level a separate retargeting campaign is not restored.

## Step 6: Verify a week later

Re-read the new/engaged/existing split. In this scenario warm spend settled
near 38%, inside the expected band, and learning stopped resetting. Expected
movement, not a promised one; the same rebuild on a smaller account moves
slower. If warm leakage had stayed high, the next check is list freshness
(step 3) before anything else.

## What made this fast

- The spend breakdown separated normal warm leakage (about a third) from a
  real defect (55%).
- Knowing the suggestion-zone rule sent the fix to the ad set mode, not to
  ever-longer exclusion lists.
- The consolidation rule solved the CPL climb; exclusions alone never would
  have.
