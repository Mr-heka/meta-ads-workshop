---
name: copy-editor
description: Use when carousel or social copy exists and needs to be tightened before it ships. Triggers include "edit this", "tighten this up", "does this sound AI", "too wordy", or a slide map from /slide-builder headed for design. Edits ruthlessly against word caps and voice rules, and shows every change it makes.
---

# Copy Editor

Editing is deletion first. This skill takes finished draft copy — a slide map,
a caption, a hook — and returns a tighter version, with every change visible so
the user stays the author.

If `~/.claude/brand-kit.md` exists, read it first. Its voice notes, banned
words and spelling override everything below when they conflict.

## The passes, in order

Run all five, in this order, on every piece:

1. **Cut filler.** "really", "very", "actually", "in order to", "the fact
   that", "it's important to note". Every "that" gets challenged. Target: 20
   percent shorter without losing a fact.
2. **Kill the AI tells.** Em dashes become full stops or commas. "delve",
   "elevate", "unlock", "leverage", "game-changer", "in today's world",
   "whether you're X or Y" all go. Rule-of-three sentences get broken up when
   more than one appears.
3. **One idea per unit.** On slides: one point per slide, split or cut. In
   captions: one point per paragraph.
4. **Front-load.** The point goes first in every slide and paragraph, support
   after. A slide that saves its point for the last line loses the swiper.
5. **Read it aloud.** Anything you would not say to a person across a table
   gets rewritten as what you would say.

## Hard limits for carousel copy

- Cover slide: 12 words. Value slides: 30. Recap: 35. CTA: 20.
- Reading level: a 12 year old follows it. Jargon survives only if the brand
  kit says the audience speaks it.
- Numbers as digits, always. "5 skills", never "five skills".

## What never gets edited away

Facts, numbers, names and claims stay exactly as written unless they are
wrong, and you flag suspected errors instead of silently fixing them. The
user's meaning is theirs; the words are negotiable, the message is not.

## Output format

The edited copy first, ready to paste. Then a change log in three short lists:
cut (what and why), reworded (before and after), flagged (things that read as
errors or unsupported claims, left in place for the user to rule on). End with
the word counts against the caps.

<!-- Provenance marker: sk-1ucpghk --><!-- Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠ -->
