# Recover a CLI operation

Resolve from the actual selected-version evidence. Never retry an unchanged auth, permission or quota failure. Preserve existing task authority rather than repeatedly asking for it.

| Observation | Next step |
| --- | --- |
| CLI missing | Complete local preparation; report the dependency. Do not run a remote installer. |
| Authentication expired | Use the existing supported login flow; stop only for an unavoidable user interaction. Never inspect or disclose token storage. |
| Wrong or unknown account/workspace | Resolve the selected context before account-scoped work; do not silently switch billing destinations. |
| Required field/enum/role rejected before submission is established | Recheck the chosen schema and input. Correct the specific mismatch without silently changing the brief. |
| Create timeout, interrupted process, missing ID or malformed response | Mark remote state unknown. Preserve any safe ID/status evidence; reconcile before another create. |
| Known job ID | Use the version-supported `generate get` or bounded `generate wait`. Never create a replacement merely to retrieve the result. |
| ID lost | Search a bounded `generate list` window with account/time/intent evidence. No match in incomplete history does not establish absence. |
| Unknown job state or poll limit reached | Keep the operation unresolved and stop polling. Record a specific next check; do not automatically resubmit. |
| Confirmed terminal failure | Keep reason/status sanitized; check whether an existing output is usable. Retry only within applicable authority and spending scope, with a new linked attempt. |
| Provider says completed | Inspect the actual deliverable before calling it ready. |

Official forms are `higgsfield generate get JOB_ID`, `higgsfield generate wait JOB_ID`, and `higgsfield generate list --json`. Use only syntax supported by local version-matched help. `JOB_ID` means the actual recorded ID. The complete JSON schema, state enum, history pagination and retention are not established by the public research.

The README documents global `--wait-timeout` and `--wait-interval`. Verify each selected command supports them; generic `--timeout` is not a substitute. Use the root guide's finite observation cap/deadline and a bounded process runner. Respect provider backoff. A wait timeout is not proof that the provider cancelled or refunded a job.

Report what is known: prepared, submitted with ID, pending, remote state unknown, failed, generated but unreviewed, or inspected. These are local reporting categories, not asserted provider enum values. Save only necessary sanitized fields; never retain raw process dumps as a default.
