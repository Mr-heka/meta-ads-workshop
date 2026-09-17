# Hooks and settings

A hook describes an opening angle; a setting describes scene context. They are provider entities when the selected Marketing Studio surface exposes them. They are not substitutes for the user's brief.

Inspect the installed `marketing-studio hooks` and `settings` help, then list the relevant existing entities under the selected account. Use exact returned identifiers; do not invent enum or JSON field names.

Bind hook/setting IDs only when the selected video model and mode accept them. The documented ad-reference path and composed hook/setting path are mutually exclusive in the historical contract; preserve that distinction and validate against the selected schema. Do not append incompatible inputs because both seem creatively useful.

Keep an entity's text separate from the prompt unless the user intentionally wants that wording repeated. Model behavior about prepending text is version-dependent; the rendered result decides whether the opening works.
