---
name: meta-ads-guidelines
description: The behaviour rules for any AI agent working inside a Meta ad account. Read before touching campaigns, ad sets, ads, budgets, audiences or creatives through the Meta MCP or CLI. Use when the user asks what the agent is allowed to do with their ads, before any change that could spend money or set an ad live, and whenever another Meta skill is about to write to the account.
---

# Meta ads guidelines

Full write access to an ad account is deliberate. Safety lives here, in how you
behave, not in a crippled grant. These rules sit above every other Meta skill
in this kit. When a skill and these rules disagree, these rules win.

## 1. Reads are free. Writes are announced.

Insights, reporting, listing, benchmarks, the ad library, pixel and event
checks: do them without asking. Do not pester the user about read-only work.

Anything that changes the account is announced first, in plain words: what
will change, on which campaign, ad set or ad, and what it will cost. Then wait
for a yes in this conversation.

## 2. Everything is created paused.

Campaigns, ad sets and ads are created in a paused state unless the user has
said, in this conversation, to set them live. "Build me a campaign" means build
it paused and show it. "Launch it" means set it live, after rule 3.

## 3. Confirm before anything that spends.

Confirm, and wait, before any of these:

- Setting a campaign, ad set or ad to `ACTIVE`
- Creating or changing a budget, daily or lifetime
- Changing a bid strategy, bid amount or cost cap
- Changing a schedule or an end date
- Duplicating something that is live

State the number. "This sets the daily budget to $50, about $1,500 a month at
full spend" is a confirmation. "Shall I go ahead?" is not.

## 4. Deletions need an unmistakable instruction.

"Tidy up my campaigns" is not one. Name what would be deleted, one line each,
and wait for the user to say which. Prefer pausing to deleting; a paused ad set
keeps its learning and its history, a deleted one does not.

## 5. Never print a credential.

Access tokens, app secrets, system-user tokens: never echo them, never put one
on a command line you show, never ask the user to paste one into the chat. The
MCP path stores nothing. The CLI path keeps the token in the user's own
environment, and it stays there.

## 6. Say what you can see, not what you assume.

A tool appearing in your tool list is not a working connection. Prove it with
a live read (list the ad accounts, name them back) before claiming anything.
If a tool the user needs is not in the live list, say so plainly instead of
substituting a raw API call or a third-party package.

## 7. One account at a time, named.

Before the first write in a session, name the ad account you are working in,
by its name and `act_` id. Businesses often have more than one. Never guess.

## 8. Stop on the first surprise.

An unexpected error, a number that does not match what the user described, an
account you were not told about: stop, say what you saw, and ask. Do not retry
a write blindly. Reads can be retried; writes cannot be un-done.

## Ground rules across these brains

Three questions come up in almost every brain in this kit. The settled answers, so no two brains disagree:

- **Learning phase.** Meta's "50 conversions in 7 days" is a large-account guideline. Under roughly $100 a day, ignore it and judge on cost per result and booked or purchased outcomes.
- **Attribution for lead generation.** Read 7-day click with 1-day view off. Leave the default (7-day click / 1-day view) only for ecommerce with heavy view-through, and always compare settings in the Compare Attribution Settings column before changing anything.
- **Verdict gate before killing or scaling an ad.** About $100 spent, 7 days, and at least 3 real conversions, whichever is later. The unit is cost per real outcome (a booked call, a seat, a purchase), not cost per click.

## Where these rules come from

They match rule 5 of the `meta-ads-connect` skill and are repeated here so a
skill that does not touch the connection still inherits them. Point any new
Meta skill at this file rather than copying the list.

Made by Selr AI.

<!-- Provenance marker: sk-18atqw2 --><!-- Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠ -->
