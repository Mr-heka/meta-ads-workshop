---
name: reels-hook-score
description: "Create a local, source-traceable Instagram Reels cohort report from a CSV or JSON export."
version: 2.0 (2026-09-06)
---

# Reels hook score

`scripts/score.py` is an offline stdlib CLI. It reads one CSV or JSON export,
filters an explicit inclusive posting-date cohort, preserves the source bytes,
and writes a ranked dashboard, top/bottom CSVs, and a descriptive hook
playbook. It makes no live calls and makes no paid, archive, or repost action.

## Command

```sh
python3 scripts/score.py export.csv \
  --start 2026-08-01 --end 2026-08-31 \
  --rank-metrics hold_3s_rate,completion_rate --composite \
  --outdir /tmp/reels-august
```

The destination must not exist. The command validates the entire input before
creating an atomic output directory.

## Normalized input contract

Every row needs a non-empty unique `id`. `posted` is optional only for rows
that are retained as `missing_posted_not_ranked`; a supplied date must be ISO
`YYYY-MM-DD`. Dates outside `--start` through `--end` are retained in raw and
normalized evidence, but are outside the cohort.

Numbers are decimal JSON numbers or plain decimal strings only. Percent signs,
commas, NaN, infinity, negatives, and guessed count-versus-rate units fail.
Hold/completion `*_rate` fields are normalized fractions from `0` to `1`.
Per-view and viewer ratios are explicit non-negative event ratios and may exceed
`1`. Counts are parsed as exact JSON integers or exact decimal strings and emit
as JSON integers, so large counts do not cross a float intermediary. Measured
zero remains `0`; unavailable remains `null`. Values or derived ratios outside
the supported finite floating-point range, including positive underflow to
zero, are rejected before reservation. Counts themselves remain exact integers.

| Normalized field | Accepted source headers | Meaning |
|---|---|---|
| `id` | `id`, `reel_id`, `media_id` | unique source identifier |
| `posted` | `posted`, `posted_date`, `publish_date` | ISO posting date |
| `caption` | `caption`, `description`, `text` | source caption; first line becomes the caption opener |
| `url` | `url`, `permalink` | optional source URL |
| `views` | `views`, `plays` | non-negative count |
| `saves`, `shares` | same names | non-negative counts; divided by views only when both are supplied |
| `saves_per_view`, `shares_per_view` | same names | explicit non-negative event-per-view ratios; these may exceed `1` |
| `hold_3s_rate`, `hold_15s_rate`, `completion_rate`, `full_watch_rate` | same names | explicit normalized fractions |
| `watch_ratio` | same name | non-negative average-watch-to-duration ratio; may exceed `1` |
| `average_watch_seconds` + `duration_seconds` | same names | derives `watch_ratio` only from this named pair; it is distinct from completion |
| `watches_per_viewer` | same name | explicit non-negative total watches per known viewer |
| `replays_per_viewer` | same name | explicit non-negative replay events per known viewer |
| `replays` + `unique_viewers` | same names | derives `replays_per_viewer` only from this named pair |
| `verified_audiovisual_opener` | same name | optional actual opening observed by a reviewer |
| `audiovisual_opener_verified` | same name | must be boolean `true` when the audiovisual opener is supplied |

Each canonical field may have at most one accepted header in a row. Counts
must be integers. Zero views cannot carry positive save/share counts, and zero
unique viewers cannot carry positive replay counts. `rewatch_rate` is not an
accepted alias because its numerator is ambiguous. Unknown source fields are
retained in raw evidence and named in `provenance.json`; they are not silently
scored. The CLI does not infer units, scan arbitrary aliases, or copy a caption
into an audiovisual opener.

For JSON, the top-level array or the one recognized object container
(`reels`, `items`, `data`, or `results`) is recorded in `provenance.json`.
Wrapper metadata is retained exactly there and its field names are listed as
ignored source fields. JSON duplicate keys and non-standard constants such as
`NaN` or `Infinity` are rejected before an output directory is reserved.

## Ranking and interpretation

Use `--rank-metrics` with one or more supported metrics. Rows are ranked only
when every selected metric is measured, so each ranked row shares the same
metric basis. Rows with missing selected metrics stay visible in
`normalized.json` and the coverage section as unranked; they are never filled
with zero.

A one-metric rank uses that metric's cohort percentile and labels it with that
metric name. More than one metric
requires `--composite`; the arithmetic mean of those percentiles is labelled a
**heuristic cohort composite**, not a validated predictor. It is not a paid,
archive, or editorial instruction. Small cohorts and ties are reported.
`--composite` with only one metric is rejected. Dashboard highest and lowest
slices are disjoint; the smaller tail is shown when the cohort cannot fill both.

Pattern labels describe matches in caption first lines. A caption opener is
not evidence of an audiovisual opener; only a supplied, explicitly verified
field is labelled audiovisual.

## Output

The output directory contains `dashboard.md`, `top10.csv`, `bottom10.csv`,
`hook_patterns.md`, `normalized.json`, `provenance.json`, and the exact
`input.raw` bytes. Markdown and CSV display fields are escaped or
formula-neutralized, including leading whitespace/control formula forms;
`input.raw` preserves the original evidence. The final directory name is
claimed with an atomic no-overwrite reservation. Each output file uses atomic
no-replace publication, so a concurrently created file or symlink is never
replaced. For caught publication errors, the owned directory attempts to retain
`FAILED.json` without overwriting a pre-existing receipt; partial files remain
as evidence. A hard kill or power loss cannot guarantee a receipt.

The hook playbook uses fenced literal display excerpts, including controls and
newlines, so a source line beginning with Markdown syntax cannot become a
heading or list. Exact source strings remain in raw evidence.

## Source acquisition ownership

This CLI scores an already-exported local file. When a request starts with no
export, the agent driving the request owns acquisition: inspect the currently
available Instagram Insights/browser or connector tools and their permitted
export path at action time, then record the actual source and hash. Do not
invent an API, assume a provider is installed, or treat caption text as visual
verification. Normalize the resulting export to this contract before scoring.

<!-- Provenance marker: sk-1xazxx2 --><!-- Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠ -->
