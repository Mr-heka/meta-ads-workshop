# Example session: "Should I fill detailed targeting on this new ad account?"

A worked pattern showing this brain loaded and applied to a live ad-account
decision. Imitate the shape: trigger, load, ground, decide, cite, hand off.

## The trigger

User asks:

> "We just spun up a fresh ad account for the new offer. Zero conversion
> history. Should I fill in detailed targeting or go straight broad?"

That matches the description triggers "should I add interests" and "is
detailed targeting dead", so the agent loads this brain before answering.

## What the agent grounds on

From `SKILL.md`:

- Consensus point 1: Meta out-targets the advertiser **on any account with
  conversion history**. This account has none, so the headline rule does not
  bite yet.
- Playbook rule: "IF the account is new with no conversion data THEN fill
  detailed targeting as a starting signal and plan to remove it once
  conversions flow (Heath)."
- Heath's Controls vs Suggest-an-Audience framework: anything in the
  suggestion layer is take-it-or-leave-it signal, never a hard boundary, so
  filling it cannot fence Meta in.
- The contrarian block: Chappell says under $30k/month interest ad sets train
  the model; LYFE says go broad from day one. The weight of evidence sides
  with consolidation first, optional narrow interests early, broad once the
  pixel warms.

## The answer the agent gives

1. **Yes, fill it, temporarily.** New account, no conversion data, so detailed
   targeting is a starting signal for the algorithm, not a cage (Heath). Add
   one or two interest signals close to the buyer, not a stack.
2. **Set the hard controls properly first.** Location to the real operating
   area, age floor only with a practical reason, gender both unless
   purchase-relevant, exclusions attached (LYFE, Heath). These are the only
   fields that bind.
3. **Put the real targeting in the creative.** Call out the exact customer in
   the first 3-10 seconds; who appears on screen decides who Meta serves it to
   (Davis, Piliero).
4. **Plan the removal now.** Once conversions flow steadily, empty the
   suggestion layer and let the account run broad; diarise the check rather
   than leaving interests in forever.
5. **Run the pre-flight checklist** from the playbook before launch: location,
   age/gender rationale, exclusions, custom audiences built, one deliberate
   interest at most, creative carrying the callout, conversion signal clean.

## Boundaries respected

- The agent does not touch budgets, bidding or campaign structure; those route
  to `brain-meta-budgets-bidding-learning` and `brain-meta-media-buyer-manual`.
- Advantage+ Audiences stays OFF per the audiences rule (test both, record it)
  (`brain-meta-ads-manual-control-no-advantage`), even though one mined expert
  prescribes the Advantage+ container.
- Exclusion detail beyond "attach the standard stack" routes to
  `brain-meta-exclusion-architecture`.

## Why this is the right shape

The brain was used as a decision engine, not a quote dump: consensus first,
the contrarian split acknowledged, every operating rule attributed to a named
expert, and the answer lands as concrete account actions with a scheduled
follow-up. Reproduce that structure for any other audience question this brain
covers.
