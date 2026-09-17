# Example session: picking the optimisation event for a low-volume online course

A worked end-to-end example of this brain answering a real question. Every quote below is verbatim from `references/quote-library.md` and traceable to the mined transcripts.

---

## The question

> *We sell a $500 online course. Ads land on a landing page with a form, checkout is on the next page. We get maybe 8-12 purchases a month from ads. Should the campaign optimise for Purchase, since that's what we actually want?*

## The brain's answer

**Verdict: no. At 8-12 purchases a month, Purchase is below every trainable floor in this brain. Optimise one step up the funnel (InitiateCheckout or a gated Lead) and ladder down to Purchase only when volume earns it.**

### Step 1: the optimisation event is the real targeting

Whatever hits the results column is what Meta clones. As Dr. Matt Shiver puts it, targeting "matters a tiny bit, but what matters more is whatever hits this results column right here". So the question is not what you want; it is which event gives Meta enough of the right examples to learn from.

### Step 2: check volume against the floors

The brain's default numbers table gives two floors:

| Floor | Source |
|---|---|
| 15-30 events/month minimum for the event to train | Caden Thompson |
| 50 in 7 days as the ideal | Justin Lalonde |

Thompson: "You want to look for about roughly, let's say, 15 to 30 events per month ideally." At 8-12 purchases a month, Purchase sits under the working floor and nowhere near the ideal. The deep event never trains; learning whipsaws (failure mode 2 in the playbook).

### Step 3: apply Meta's own event-choice framework

Meta's product marketing guidance (via the Make webinar): "Choose a stage that is somewhere between 1% and 40% of leads actually complete." And the ceiling: "the conversion event has to occur within 28 days of lead submission. That's the attribution window."

For a $500 course bought within days, every stage clears the 28-day window, so lag is not the constraint here; volume is. InitiateCheckout typically sits inside the 1-40% completion band relative to leads, which makes it the correct mid-stage proxy.

### Step 4: standard event, not a custom conversion

Lalonde's rule is blunt: "in doubt, use standard events". The custom-conversion switch only makes sense past volume: "if you can get 50 plus conversions of that event within a 7-day cycle, usually this is where it starts to make sense to switch to a custom conversion event". This account is an order of magnitude below that. InitiateCheckout and Purchase as standard events, nothing custom.

### Step 5: accept the trade the experts name

Optimising shallower buys volume and some junk. Localnichemarketing states the price of the reverse move: "You're definitely going to see increase in cost per acquisition, but the lesser the leads are the higher the quality will be." The ladder manages that trade deliberately: shallow enough to train now, stepping deeper as volume grows.

### Contrarian check

Tushar Dey argues the opposite: "No Warm Up From Day One Nothing Like That Just Start With Purchase." The brain era-flags this take and sides with the laddering camp: at 8-12 purchases a month the deep event never reaches trainable volume, and the corroborated 50-in-7-days maths backs the ladder.

### The recommendation handed back

1. Optimise the campaign to **InitiateCheckout** (standard event) now.
2. Keep the **Purchase** event firing and deduplicated (pixel + CAPI) so history accumulates.
3. Ladder down to Purchase when it fires 15-30+ times a month; treat 50-in-7-days as the ideal, not the entry bar.
4. Judge the switch on the 7-day rolling window against cost per qualified result, then hands off for 3-5 days (Michael Diaz's discipline).

## Brain sections used

- What the experts agree on: points 1, 5, 7
- Execution playbook: IF/THEN rules 2, 3, 7; default numbers table; failure mode 2
- Contrarian / disputed takes: purchase-only from day one
- `references/quote-library.md`: themes Volume thresholds; Meta's official event-choice framework; Standard events vs custom conversions
