# Prompt and settings handoff

Read Higgsfield's own prompt guide (published CLI skill material at https://github.com/higgsfield-ai/cli) for creative construction. Preserve the subject, action, framing, light, style and sound that the brief needs. Keep model IDs, durations, resolutions and media bindings in settings, not inside the pasteable prompt.

For each reference, state its intended role and bind the actual selected asset. Typed names do not attach files. A product label, screenshot or quote must come from supplied or verified material; use an editor/composite when exact reproduction is required.

Pass prompt text as one literal argument through a structured process API where available. Never concatenate untrusted prompt text, filenames or URLs into shell code. Quote shell arguments correctly when a shell is required; use the selected CLI's documented input-file/stdin form only after its help establishes it. Do not assume a JSON string is shell escaping.

A provider error about a missing prompt is not automatically a question for the user. Draft from the existing brief when it supplies enough information. Ask only for the missing detail that changes the result.
