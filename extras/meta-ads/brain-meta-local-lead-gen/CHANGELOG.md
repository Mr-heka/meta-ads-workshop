# Changelog

## 2026-08-26 — Advantage+ Audience re-correction (cross-check 2026-08-26)
- **"That control no longer exists" reversed.** The Advantage+ Audience toggle exists and binds at the API layer: `advantage_audience` 0 and 1 both accepted on `OUTCOME_LEADS`, verified live 2026-08-25. What is true: ON fixes `age_max` at 65 (error 1870189) and includes degrade to suggestions; OFF makes includes bind (warm-list pattern).

## 2026-07-28 — consistency, currency + publishing pass
- **Frequency standardised to ONE ladder.** The file previously gave four different ceilings in four places (consensus point 6, an IF/THEN rule, the defaults list, and the business section). All four now point at a new **"Frequency: one ladder"** table — 2.5 warn / 3.0 rotate / 3.5 refresh / 4.0 immediate — plus the two supporting rules (needs 2+ signals moving together; under 3 new creatives a month is itself a flag).
- **Read-window standardised.** Darby's 1-3x-target-CPL and 2,000-3,000-impression figures are relabelled as fair-look context under the single house verdict gate ($100 spend + 7 days + 3 conversions), in both the defaults list and failure mode 4.
- **Carousel dispute resolved** and reconciled with `brain-meta-placements-and-formats`: not a default format, and Feed-only in its own ad set when run. Was "Unresolved; test if ever, never default".
- **"Switch to original audience" corrected (dated).** Advantage+ Audience is mandatory on Sales/Leads/App objectives; the remaining controls are named (location, minimum age, language, custom-audience exclusions, Special Ad Category), with a note that location is the one this brain actually depends on.
- **DCT / 3-2-2 container corrected (dated).** Dynamic Creative → Flexible ad format → removed as a standalone setup option March 2026, now "Flexible media" inside Advantage+ creative; "enhancements off but DCT on" is self-cancelling. Grid logic kept, the two real options spelled out.
- **"Meta holds roughly a million data points per user, told to me by a Facebook engineer at Menlo Park" labelled unverified folklore** in `references/synthesis.md` Theme 1, with a note that the broad-targeting argument stands without it.
- **Form-first doctrine propagated into the reference and example files** that still carried the old LP-only position (`references/synthesis.md` Theme 5, `references/experts.md`, `examples/local-event-fill-session.md`), including the explanation that the LP-only evidence was an unaccepted-ToS artefact.
- **Publishing scrub.** Account/pixel IDs replaced with placeholders in SKILL.md and the worked example; internal CPL figures, city campaign names and prices removed; "Applied to our business" renamed to "Applied to your business" and rewritten as reader-fill prompts. The INTERNAL-ONLY markers in SKILL.md and the example now state that the account facts have been removed, instead of warning that they are present.

## 2026-07-18
- Recalibration pass: form-first doctrine flip, Neiman fatigue bands, true CPLs, workshop-paused note (audit 2026-07-18).

## 2026-07-06
- Added examples/local-event-fill-session.md, a worked single-city workshop seat-fill Q&A session; linked from Deeper references in SKILL.md.

## 2026-07-05
- Brain built from 21 YouTube sources via topic-brain-builder. Engine: yt-dlp. Mix: {"new": 22, "evergreen": 6, "hidden_gems": 4, "channels": 23}.
