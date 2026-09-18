---
name: higgsfield-generate
description: >-
  Operate an already selected Higgsfield CLI workflow: map media roles, submit or retrieve jobs, and manage Marketing Studio inputs. Use after the Higgsfield hub selects the CLI surface, or when the user explicitly requests Higgsfield CLI operations.
argument-hint: "[operation or creative brief]"
metadata:
  reviewed: "2026-09-05"
  verification: local guide review; provider runtime unverified
---

# Higgsfield CLI operations

Turn the selected creative brief into a checked CLI operation and a reviewed result. Creative direction, model selection and final acceptance belong to the user's brief. For Higgsfield's own prompt cookbook and sub-skills, see Higgsfield's published CLI skill material at https://github.com/higgsfield-ai/cli. This guide owns CLI command mapping, input handling and job recovery. It does not choose a provider for an ordinary image request.

## Prepare the operation

1. Carry forward the user's selected model, assets, destination and existing production authority. Resolve only missing information that changes the result or an unresolved consequential action. Keep prompt preparation moving. A request to analyse a clip can involve an external upload and a charged job even when the output is text.
2. Identify the installed CLI version and relevant local help. Do not install or upgrade automatically. If the command is absent, finish the local brief and report the missing dependency. Authentication recovery uses the existing supported login flow; never read token storage or ask the user to paste a token.
3. Before account-scoped work, bind the intended account/workspace using the selected version's supported status and workspace commands. Read-only discovery can contact the provider. Help, command names and JSON shapes are version-specific; the [dated sources](SOURCES.md) state what has and has not been established.
4. Read [model/schema mapping](references/model-catalog.md) and [media inputs](references/media-inputs.md). Inspect the chosen model's schema before preparing flags. Retain requested settings; report unsupported ones instead of silently changing model, duration, media roles or output format.
5. Treat local-path auto-upload, URL import, custom-avatar creation and generation as external actions. Use the already authorized exact assets and spending scope. Preserve applicable consent, likeness and privacy requirements. If a required bound is missing, park that action and finish independent preparation.
6. Before a charged operation, use a version-supported estimate that does not submit a job when available. Compare the chosen quantity/settings and estimated cost with the remaining authorized bound across all attempts. If cost cannot be bounded, proceed only when existing authority covers that uncertainty; otherwise park the charged step. Do not invent a cost command or treat a failed/unknown attempt as free.

## Submit, recover and inspect

Before an external action, keep a small operation record in the current task's private working files: a local operation key, task/authority reference, selected model/settings, safe asset references, version/schema identity, sanitized estimated cost and remaining spending bound, and eventual provider ID/status. Record actual cost when evidenced; keep it unknown when unavailable. Reserve the applicable amount for an uncertain attempt rather than assuming a refund or resetting the retry budget. Store only necessary sanitized fields. Do not save raw stdout/stderr, credentials, signed URLs or full account responses as evidence. This temporary task record is not permission to create persistent creative memory.

Use the selected version's validated command shape. The documented generic forms are `generate create`, `generate get`, `generate wait` and `generate list`; detailed usage and limits are in [job recovery](references/troubleshooting.md). Prefer an initial create that returns an ID when the selected version supports it, then record that ID before waiting. If using a combined create/wait command, keep its result recoverable and treat lost output as uncertain submission.

Submit once. A timeout, missing ID, failed parser or interrupted wait leaves remote state unknown. Retrieve by the known ID; use a bounded history search when necessary. Absence from an incomplete list is not proof that no job exists. Never automatically repeat upload/create. An authorized retry gets a new linked attempt and stays within the original asset and spend scope.

For agent-driven get/list polling, use a fixed deadline and attempt cap chosen before starting. The guide default is at most 20 observations over 10 minutes, with no observation sooner than 5 seconds after the previous one; honor a longer provider retry delay. These bound the agent's observations, not the opaque CLI's internal requests. Stop on an unknown status, an action-needed response, or either limit. A CLI wait must have a verified finite wait setting and a process-runner timeout within the remaining deadline. Its timeout does not prove cancellation of the remote job.

Return the requested artifact through the host's supported delivery tools. Inspect the whole image/video and listen when sound is present. Check the brief, product/identity fidelity, labels, dimensions, timing and audio where relevant. A completed job or working URL is not creative acceptance. If inspection is unavailable, state exactly what remains unreviewed.

For provider video analysis, present scores as provider-generated assessments. They do not measure actual viewer attention, neuroscience, campaign retention, virality or business performance. Keep observed clip details separate from the model's interpretation.

## Read the one relevant operation guide

| Operation | Guide |
| --- | --- |
| Prompt/settings handoff | [Prompt construction](references/prompt-engineering.md) |
| Model IDs, supported flags and defaults | [Schema mapping](references/model-catalog.md) |
| Images, video, audio, existing upload/job IDs | [Media roles](references/media-inputs.md) |
| Preset or custom presenter | [Avatars](references/marketing-avatars.md) |
| Product images, URL import or web product | [Products](references/marketing-products.md) |
| Hook and setting entities | [Setup items](references/marketing-setup-items.md) |
| Reference video and entity readiness | [Ad references](references/marketing-ad-references.md) |
| Brand identity imported from a site | [Brand kits](references/marketing-brand-kits.md) |
| Image-ad format and output settings | [DTC ads](references/marketing-dtc-ads.md) |
| Marketing Studio mode and incompatible inputs | [Modes](references/marketing-modes.md) |
| Errors, waits and uncertain submissions | [Recovery](references/troubleshooting.md) |

[Fictional decision cases](examples/operator-cases.md) illustrate the intended behavior.Neither the archive nor this guide proves executable or provider behavior.
