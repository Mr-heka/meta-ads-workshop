# Measurement and offline calculations

Record account, currency, reporting dates, timezone, attribution settings, conversion definition and extraction time. Keep platform-reported conversions, analytics events, CRM outcomes and financial receipts distinct. Reconcile IDs, time windows, refunds, duplicates, conversion lag and counting rules before interpreting differences. Platform attribution may overcount, undercount or disagree with another model; it is not universally inflated and does not prove incrementality.

Use actual spend for unit costs. A budget is a spending limit or plan, not evidence that the money was spent. With actual spend of 15000 and 80 leads, CPL is 187.5 in that currency. A 15000 budget alone cannot prove that CPL or invalidate a reported 180 CPL.

## Calculator

Run the local supplied-data calculator with an explicit JSON file:

```sh
python3 scripts/metrics.py --file /absolute/path/campaign-observations.json
```

The path is an input selected for this task. The command creates no campaign or output file, has no implicit demo and does not access an account. Redirect or save its output only to a task-owned new file when needed.

Input requires `currency`, `period`, `source` and nonnegative `spend`. Optional numeric fields are `revenue`, `conversions`, `leads`, `impressions`, `clicks` and `margin_pct`; absent or null means unknown. Currency is a three-letter unit label, not an exchange-rate lookup. Counts are nonnegative integers, at most 10^12. Monetary values are at most 10^15; decimal inputs have at most 12 fractional places and 32 significant digits. These are calculator bounds, not platform limits. Margin is 0–100 and must exclude ad spend for the contribution calculation. Use reconciled observations from compatible scopes.

Output preserves known zero and reports unavailable metrics with reasons. Decimal quantities are decimal strings, with metric values rounded to six places. Do not reinterpret those strings as independently verified inputs. A zero denominator is unavailable, not infinite or a success. A rate above 100% prompts a cohort/counting check; multiple conversion events per click can be legitimate.

ROAS is attributed revenue / ad spend. CPA here means cost per the supplied conversion, which may not be a customer. Revenue × supplied margin minus ad spend is contribution after ads before omitted costs, not net business profit. The revenue gap to break even is a revenue amount, not the amount lost. The calculator does not recommend pausing or scaling from a ratio alone.

## Diagnosis and reporting

Begin with the observed change and comparable baseline. Examine reporting delays, mix, tracking, lead quality, creative, delivery and landing-page behavior as alternatives. High CTR with low reported conversion can arise from several causes; it does not prove the landing page is at fault. Find evidence that distinguishes the plausible causes before prescribing a fix.

A useful review separates spend pacing, qualified outcome cost, downstream conversion, creative/placement changes, frequency, rejection/delivery issues and measurement health. Match review cadence to spend and event delay. Reuse a current correctly scoped report when available. Compare scenarios and record uncertainty; use an appropriate incrementality experiment if causal lift is the question.

Report the input evidence, calculations, interpretation, proposed or completed action and next observation. Account access, imported figures, fixture tests and live paid-path verification are different evidence layers.
