# Runtime and legacy

## Dependencies and resolution

- `hyperframes` must be built at `packages/cli/dist/cli.js`. Scripts resolve it in this order: `HYPERFRAMES_ROOT`, repo root when the skill ships inside hyperframes, then your local HyperFrames checkout. Build with `bun install && bun run build`.
- Node is primary. Transcription invokes WhisperX through `uvx`; Theme’s `drawon` setpiece invokes `python3 scripts/gen-stroke-path.py` at compile time. Both avoid manual Python installs.
- Hyperframes supplies `remove-background` with `u2net_human_seg`; `sharp` handles image/alpha math; `puppeteer` handles layout, occlusion, and overflow; `ffmpeg` handles media.
- `transcribe.cjs` drives `uvx whisperx` for word timings and alignment, or uses an existing word-level `transcript.json`.
- The workflow runs locally end to end and requires no API key.
- `matte.cjs` and `transcribe.cjs` resolve `source.mp4`, glob an available clip, or read `hyperframes.json`; `hyperframes init --video X.mp4` needs no rename.
- `matte.cjs` extracts at native source fps and records `matte.fps`; `render-and-composite.sh` uses it to keep matte frames aligned.
- Matting weights are not bundled. First use downloads about 168 MB once to `~/.cache/hyperframes/background-removal/models/`; the broader hyperframes cache is `~/.cache/hyperframes/`. The model is Apache-2.0, and a fresh machine needs network for that download.

When a hard dependency is unavailable, stop that delivery, report the exact missing layer, and ask the user for the blocked external dependency.

## Legacy and retained interfaces

- The retired 54-template library still exists outside this skill. Route legacy-archive requests through the **embedded-captions** skill by name; no user-specific archive path is part of the contract.
- `modes/standard/_motion.md` remains the in-skill motion-verb reference catalog.
- Direct `plan.json` authoring remains supported for compositions outside the cinematic block compiler.
- Legacy `plan.template:"cinematic-cream"` resolves to `dna:"cream"`.
- Existing word-level `transcript.json` is a supported no-transcription input.
