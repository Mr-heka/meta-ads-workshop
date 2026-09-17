# Worked session: standard event vs custom conversion

A single Q&A thread showing how this brain answers the core decision. Every quotation
below is copied verbatim from `references/quote-library.md` (third-party speech,
preserved word for word). The connective prose is ours.

---

**Q: I run a coaching business. Should I set up a standard event or a custom conversion for my booked calls?**

Start from the definitions, because the two layers do different jobs. Justin Lalonde,
reading Meta's own wording:

> "Standard events helps optimize for conversions and build audiences. Now, custom events, these are actions not covered by standard events."

For most advertisers the default is the standard event, and the reason is data pooling,
not convenience. Lalonde again:

> "So, I usually prefer for most businesses to start by using standard conversion events as they share data with many other businesses out there."

A coaching or service business is exactly where the exception starts to apply:

> "usually this is where it starts to make sense to switch to a custom conversion event. So, in other words, you're an info product or coaching or service-based business."

So the answer is layered: keep optimising to a standard event now, and build the custom
conversion as the thing you grow into once call volume justifies segmenting quality.

---

**Q: Why not just default everyone to custom conversions? They look more precise.**

Because precision without volume starves the algorithm, and because a custom conversion
only ever sees your own account. Lalonde on where custom conversions genuinely belong:

> "In my experience for most e-commerce businesses, you're never really going to use custom conversion events. 99% of the time, you're going to be using standard events."

The mechanism underneath is a feedback loop, which is why clean, pooled signal matters:

> "Meta works with like a clicker system, kind of like a dog training system, right? It's a reward system. An event fires, Meta thinks it's doing a good job, it's going to try to find you more of those people because it wants to have more fires."

---

**Q: Fine, I need purchase-like tracking on my booking thank-you page. How do I build the custom conversion?**

It is a URL rule off a gated thank-you page. Two rules decide whether it works.

First, match on "contains", never "equals". E & T Academy:

> "always indicate what contains because there may be some certain slight variations of the URL. If you don't add a contains and you just do a equals sometimes there certain purchases will happen but you will not be able to track them"

Second, set a value if the action carries one, so reporting reads in dollars. Digital Blezz:

> "We need to set the convention value. We need to track how much we are getting, that is, if one product is 25, the next product may be 35, the next product may be 45"

("convention" is an auto-translation artifact for "conversion" in that source; the quote
is preserved verbatim.)

---

**Q: Anything that will silently ruin the numbers once it is live?**

Two things. The thank-you page must be unreachable except via the real action, or every
stray visit inflates your count. Shah Wajahat Ali:

> "This page will load only when someone submits the lead form. After that, every time this page is loaded here, the conversions will be tracked here."

And test before you spend, because broken tracking is the norm, not the exception. Jamie Stenton:

> "A huge number of ad accounts are optimizing campaigns on completely broken event data. Now, we audit hundreds of accounts a year and we just see this on at least 50 to 60% of accounts."

Bottom line for the coaching case: optimise to a standard event today, build the custom
conversion as a gated "contains" URL rule for reporting, and walk the funnel in Test Events
before a single dollar of spend relies on it.
