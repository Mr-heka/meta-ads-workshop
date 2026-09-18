# Caption opener pattern labels

These regular expressions classify only the first line of a supplied caption.
They are descriptive labels, not evidence that a pattern caused performance.
They never establish what appeared or was said in the audiovisual opening.

| Label | Python regex (`re.I`) |
|---|---|
| Contrarian command | `^\s*(stop|quit|never|don't|delete|forget|ignore)\b` |
| Question | `^\s*(why|how|what|when|who|which|can|do|is|are|have you|did you)\b.*\?` |
| Numbered claim | `\b\d+\s+(ways?|things?|tools?|mistakes?|reasons?|steps?|tips?|hacks?|signs?|lessons?|rules?)\b` |
| Discovery | `\b(i (just )?(found|discovered|built|tried|tested)|this (new )?(tool|app|ai|trick))\b` |
| Curiosity gap | `\b(nobody (talks about|tells you)|the secret|what no one|the real reason|most people (miss|don't know))\b` |
| How-to | `^\s*(how to|how i|here's how|the (easiest|fastest|simplest) way)\b` |

The playbook keeps source caption openers verbatim in `normalized.json` and
renders an escaped Markdown representation. A verified audiovisual opener is
reported only when the source carries both `verified_audiovisual_opener` and
`audiovisual_opener_verified: true`.

<!-- Provenance marker: sk-sdt8cm --><!-- Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠ -->
