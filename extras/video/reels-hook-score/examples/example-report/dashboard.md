# Reels cohort report: 2026-08-01 to 2026-08-31

Source: input.csv (`sha256`: `238582f16571adad6b0ad731f7cce2c010267f27c0fbae0b387b09baeeb9cbe0`)

## Scope and rank basis

Inclusive posted-date cohort: 2026-08-01 to 2026-08-31. 4 source rows; 3 in cohort; 2 ranked on the shared metric basis `hold_3s_rate, completion_rate`. Score is an unweighted percentile-mean heuristic, not a validated predictor or action recommendation.

## Ranked cohort

### Highest 2

| Rank | Caption opener display excerpt (raw source in normalized.json) | Verified audiovisual opener display excerpt | Heuristic composite percentile | hold_3s_rate | completion_rate |
|---:|---|---|---:|---:|---:|
| 1 | Stop using vague hooks | Speaker says: stop using vague hooks | 50.0 | 0.720 | 0.600 |
| 1 | How to make a clear first line | n/a | 50.0 | 0.490 | 0.780 |

## Unranked or out-of-cohort records

| ID | Status | Missing selected metrics | Caption opener |
|---|---|---|---|
| reel-c | outside_cohort | n/a | Outside the cohort |
| reel-d | in_cohort | completion\_rate | Caption retained but missing completion |

## Caption pattern labels

- Contrarian command: 1 ranked caption opener(s)
- How-to: 1 ranked caption opener(s)

## Interpretation limits

Missing values remain missing. Rows outside the date window, without a posting date, or without every selected metric are not ranked. Caption patterns are descriptive only. Values have no paid, archive, repost, or causal recommendation. Cohort size: 2; tied scores receive the same competition rank, while display order is deterministic by ID. Dashboard tables are capped; complete source evidence remains in input.raw and normalized.json.
