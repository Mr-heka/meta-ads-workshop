# Worked example: "Why don't my Ads Manager numbers match the CRM?"

A short Q&A session showing how to use this brain. Every quoted line is verbatim from
`references/quote-library.md`; the reasoning around them is the brain's own synthesis.

---

**Q: Facebook says I got way more leads than my CRM shows. Which one is lying, and how
worried should I be?**

First, a mismatch is normal and does not mean either system is broken. The realistic
health benchmark is Danyyil Giba's measured reconciliation, not the vendor "you're losing
40%" story. On a real account he compared the two sides directly:

> "we spend that much money and we generated this many leads, 535. And if we look at the
> back end and those are the same dates, we got 528." - Danyyil Giba

That is a gap of about 1%. So the first question is not "why is there a gap" but "how big
is it". A single-digit-percent gap is fine. A 30-40% gap or Facebook running well *above*
the CRM is the signal to stop and investigate.

**Q: Mine is the other way. Facebook is HIGHER than the CRM. Is that better?**

No, that is the worse direction. A small under-report (CRM slightly above Facebook) is the
healthy state, because over-reporting means the same action is being counted more than
once and those duplicates are training the algorithm. Giba's rule:

> "Let me explain why lower than actual is better than higher than actual. Time and time
> again, I see when a single person can submit the same form on our website multiple
> times." - Danyyil Giba

If Facebook is above your CRM, treat it as a duplicate hunt, not a reporting quirk.

**Q: So what do I actually check first?**

Check for double-firing. It is the single most common cause of an inflated Facebook count,
per Jamie Stenton, who audits this for a living:

> "What you do want to check is that you're not getting multiple events being reported,
> multiple events happening cuz that is really really common" - Jamie Stenton

And this is not a cosmetic reporting problem. Broken event data actively steers budget:

> "A huge number of ad accounts are optimizing campaigns on completely broken event data."
> - Jamie Stenton

**Q: How do I know CAPI is even contributing, versus the browser pixel doing all the work?**

Look at the pixel's Integration tab, not the raw count. Rafael Hernandez's tell:

> "Instead, what you should be seeing is something like this where in integration it shows
> multiple and it says sent via conversion API and meta pixel." - Rafael Hernandez

If it shows only "Meta Pixel", the server rail is not live and your account is flying blind
server-side even though the browser test looks fine.

---

**The one-line answer:** a 1-3% CRM-vs-Ads-Manager gap is healthy and you want the CRM
slightly *above* Facebook; if Facebook is above the CRM, hunt duplicate fires; and confirm
the Integration tab shows both rails before you trust either number.

See `references/synthesis.md` Themes 2, 5 and 10 for the full argument, and
`brain-meta-capi-server-side-deep` for the dedup internals.
