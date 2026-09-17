# Example session: one worked Q&A grounded in this brain

Demonstrates how an answer should look when this brain is loaded: grounded in the
synthesis, the IF/THEN playbook, the default-numbers table and the quote library.
Every quote below is verbatim from the mined transcripts.

## User question

> Set up a kill rule for the Perth workshop campaign. It normally runs a $6-8 CPL
> and I keep forgetting to check it, so I want it to auto-pause if it blows out. What
> condition and what level, and does it reset learning when it fires?

## Brain-grounded answer

**Build it as a campaign-level cost-per-result rule: turn off when CPL crosses 3x
target on a 7-day lifetime-view window. Auto-pause doesn't reset learning, an edit
would, so kill by pausing, never by touching the live winner.**

1. **Use the classic kill shape, not a raw spend cap.** The lead-gen kill rule is
   IF cost per result > ceiling THEN turn off. Leadstio's plain version: "in general
   you able to choose like okay cost per result greater than 150 and you can turn off
   this campaign." A raw spend cap like Belad's $1,000 is a blunt backstop and sits
   far above a typical small per-event budget, so CPL is the trigger, spend is not
   (*Applied to your business*, "What does NOT apply"; playbook IF/THEN rule 2).

2. **Set the ceiling at 3x target, not a hair over.** Our target CPL on the Workshop
   is $6-10, so the kill threshold is roughly **$18-30**. That is the house number:
   3x target CPL, matching Leadstio's own 2-3x logic ($50 normal → kill at $100-150).
   Under 3x you panic-kill a campaign mid-ramp (*Default numbers*, kill ceiling).

3. **Read it over 7 days, lifetime view, not today.** Theriot's window is the house
   window: "the only time we're turning things off is if on a 7-day window that
   particular adset has a very high CPA hurting the performance for that particular
   campaign." A one-day spike is noise; campaigns take 2-3 days to ramp. Set the
   rule's time range to 7 days and action frequency to once daily (*Default numbers*,
   kill window; *Top 5 failure modes* #3).

4. **Put it at campaign level and filter by name.** Cost-per-result conditions may
   not accept ad-set scope (Leadstio, single-source, verify in-account), so run it at
   campaign level. Filter the one rule to the Perth workshop by campaign-name string
   match so each city-event carries its own ceiling instead of building a rule per
   campaign (*Named frameworks*, CPL-multiple kill rule; playbook IF/THEN rules 2-4).

5. **Auto-pause does not reset learning; a direct edit would.** The rule turns the
   entity off, it does not change budget or creative on the live winner. That is why
   the kill is a pause: our rule is "IF you have a live winner THEN never edit it
   directly." If you later want to scale the survivor, do it by budget only, capped,
   never by editing in place (playbook IF/THEN rules; *Applied to your business* #2).

6. **Pair the kill with a turn-on rule if you want exact scheduling.** If the point
   is "watch it only during the event push", Leadstio's pattern is to pair two rules:
   "you can create one rule for turning on campaign another rule for turning off
   campaign and here you have more possibilities than in regular scheduling settings."
   For a single always-on ceiling you don't need this, but it's the lever if you do.

**Where this came from**: consensus point 3; the CPL-multiple kill rule and the
7-day-window kill under *Named frameworks & methods*; *Default numbers* (kill ceiling
and kill window); *Applied to your business* execution move #1; quotes from
`references/quote-library.md`.
