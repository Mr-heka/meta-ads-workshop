# Source evidence

Reviewed 2026-09-05. Local guide validation and public-document research only. No Higgsfield executable, installer, account, upload or generation was exercised.

| Source | What it establishes | Limit |
| --- | --- | --- |
| [Official CLI README at commit 8827135df7601667f66cd36ce84cf72106d690c4](https://github.com/higgsfield-ai/cli/blob/8827135df7601667f66cd36ce84cf72106d690c4/README.md) | Documented command families, version/help, global wait flags and distribution choices | Documentation, not implementation or a stable JSON schema |
| [Model snapshot at that commit](https://github.com/higgsfield-ai/cli/blob/8827135df7601667f66cd36ce84cf72106d690c4/MODELS.md) | Dated model/parameter/media examples | Current selected-model schema takes precedence |
| [Installer source at that commit](https://github.com/higgsfield-ai/cli/blob/8827135df7601667f66cd36ce84cf72106d690c4/install.sh) | Tag selection and install side effects | No binary integrity check; execution is outside this guide |
| [Release v1.1.24](https://github.com/higgsfield-ai/cli/releases/tag/v1.1.24) | Release/tag reference observed during research | Rendered release and tag dates conflict; no release date asserted |
| [Official skill repository](https://github.com/higgsfield-ai/skills) | Supplemental media and Marketing Studio examples | Mutable content; not pinned executable proof |

The reviewed CLI repository exposes docs and installer source, not its executable implementation. Installation must use its own reviewed procedure; a tag alone does not establish binary integrity. This guide does not run the mutable remote installer or prescribe a new installation mechanism.

The release README documents `higgsfield version`, command help, `generate create/get/wait/list`, `--json`, `--wait-timeout` and `--wait-interval`. The global documented defaults are 10 minutes and 3 seconds. Verify applicability on the installed command. A generic `--timeout` is not established for generation waiting.

Workspace selection syntax/precedence, `account status` JSON, upload response fields, complete job states, exit codes, cancellation behavior, history completeness and general idempotency remain unverified. Do not turn plausible examples into fixed execution contracts.

The dated model snapshot and newer media guidance disagree about Seedance audio-generation flags. Use the selected model's current schema; do not assert either static rule universally. Current availability, costs and quality rankings were not verified. A local operation key supports bookkeeping and does not create provider idempotency.
