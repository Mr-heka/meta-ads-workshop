# Worked example: scoped contractor access on the single ad account

A recorded Q&A session showing this brain loaded against a worked scenario and answered end-to-end. Every quote below is copied verbatim from `references/quote-library.md` (same attribution format); every other expert claim is a paraphrase with the expert named. Business facts come from `SKILL.md` > Applied to your business. No new sources, no new numbers.

**Scenario.** A business is bringing on a freelance media buyer to run the next campaign for `<your flagship offer>`, with warm retargeting for `<your secondary offer>` in the same account. The business runs one ad account (`<YOUR_AD_ACCOUNT_ID>`), one pixel (`<YOUR_PIXEL_ID>`), `<your CRM>`, manual control only, with CAPI and the purchase event verified. The contractor starts Monday and has asked for access "to everything, so setup is easier".

**Brain loaded:** `brain-meta-business-manager-architecture` (SKILL.md, references/quote-library.md, references/synthesis.md Themes 7-8).

---

## Q1: "How do I give the media buyer access without opening up the whole Business Manager?"

**Answer (from the brain):** If the contractor has their own Business Manager, this is a partner-access situation, not an invite-a-person situation. The agency-operator consensus in the brain is unambiguous:

> "The better way, the way you should exclusively with no exceptions be doing it is arranging partner access" — Jamie Stenton, *Meta Ads Client Setup Guide (Agency & Freelancers) – Avoid Bans, Billing Issues & Access Mistakes*

> "it's really important you don't let clients add you like you are an employee because if they have any account issues, if they get any bans" — Jamie Stenton, *Meta Ads Client Setup Guide (Agency & Freelancers) – Avoid Bans, Billing Issues & Access Mistakes*

The mechanism, paraphrasing Jamie Stenton: we link the contractor's Business Manager via their Business/Partner ID (the `business_id=` value in their BM URL), assign only the specific assets they need at a chosen level, and click "assign assets" at the end or the whole thing silently fails.

Applied here: assign `<YOUR_AD_ACCOUNT_ID>` and the pixel `<YOUR_PIXEL_ID>` at ads-level access only. Nothing else. Derek Videll's rule from the client side, verbatim:

> "you will go to assign people on that page. You will assign it to you. You will give yourself full control. If it is an agency running ads for you, you just need to do ads" — Derek Videll, *How to Set Up Facebook Ads Manager 2025 [Meta Business Manager]*

If the contractor is a solo freelancer with no Business Manager of their own, fall back to a person-level invite at partial access, scoped to those same two assets. Máté Hunyor's split, paraphrased: partial access for a VA or contractor, full control only for a business partner.

## Q2: "They asked for full control so they can 'set things up properly'. Do I give it?"

**Answer:** No. The brain's least-privilege consensus is built for exactly this moment:

> "You will always will have the choice between partial access and full control. Okay? So meaning when you do this full control means you're inviting an admin. This is somebody who could delete your business or delete your page." — Justin Lalonde, *How to Create A Meta Business Portfolio In 2026 (Facebook Business Manager)*

Applied here: everything runs through a single ad account, so a full-control grant exposes the entire paid acquisition system, every offer and every retargeting audience included. The doctrine (SKILL.md, Applied to your business) is partial access plus specific assets for anyone who is not a core admin. There is no setup task on a campaign engagement that needs portfolio admin. If they hit a wall that genuinely needs an admin action, an internal admin performs that one action.

## Q3: "What do I lock down on our side before they start spending?"

**Answer:** Three checks from the brain's pre-flight list, in order.

**1. Security net first.** Before any new person touches the account:

> "First thing is to add another admin and turn on two-actor authentication. If your account gets restricted or something weird happens, you don't want to lose the whole business manager." — EfesAdLab, *Facebook Business Account Setup & Mistakes to Avoid (Ep. 2) | Meta Ads for Beginners 2026*

The downside case is not hypothetical. Dr. Matt Shiver's anecdote about an account takeover without that net:

> "I've heard people who've had that happen and they've spent like, you know, $40 to $50,000 and it took them months to get it back." — Dr. Matt Shiver, *Facebook Ads Manager Setup Guide (2026 Edition)*

Confirm 2FA is on for everyone in Security Center, including the incoming contractor, and that the backup admin sits on a separate login.

**2. Account spending limit.** Confirm one is set before the contractor's first campaign goes live:

> "All it takes is an extra zero in your budget to ruin your day or maybe your life." — EfesAdLab, *Facebook Business Account Setup & Mistakes to Avoid (Ep. 2) | Meta Ads for Beginners 2026*

**3. Signal check, not signal build.** If CAPI and the conversion event are already installed, this is a confirmation pass only: verify events are firing with the Meta Pixel Helper extension and Events Manager Test Events before spend, the verification step EfesAdLab and Genius Maker both insist on (paraphrased from the pixel-and-CAPI theme).

## Q4: "The engagement ends after this city campaign. What happens to their access then?"

**Answer:** Treat access as time-boxed from day one. Máté Hunyor is the source for the temporary-access pattern:

> "There are multiple ways to do it. You can enter an email address and then you can also give them temporary access. Maybe if it's someone from an agency and then they are doing an audit. You can just give them access to for 3 days or 7 days." — Máté Hunyor, *Meta Business Manager Tutorial 2026 | Step-by-Step Setup*

The built-in 3-7 day window fits a one-off audit; a campaign engagement runs longer, so the equivalent move is a calendar entry to remove the partner assignment the day the campaign wraps. Because access was granted per asset (Jamie Stenton's model, paraphrased), removal is per asset too: unassign the ad account and pixel from the partner and the relationship is cleanly severed, with no shared logins to chase.

---

## What the brain changed about the answer

Without the brain, the path of least resistance is the one the contractor asked for: an employee-style invite with broad access, because it is one screen and zero friction. The brain flips every part of that: partner access over employee access (Jamie Stenton), partial over full control (Justin Lalonde, Máté Hunyor), security net and spending limit confirmed before first spend (EfesAdLab, Dr. Matt Shiver), and a planned exit (Máté Hunyor). On a single-ad-account business like ours, that difference protects the only paid acquisition asset we have.

**Routing note:** what the contractor should actually run (campaign structure, budgets, audiences, creative) is out of this brain's scope; route those questions to `brain-meta-ads-manual-control-no-advantage`, `brain-meta-media-buyer-manual` and `brain-meta-creative-strategist-manual`.
