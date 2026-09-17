# Changelog - video-editor

All notable changes to this skill, oldest at the bottom.

## [0.1.0] - 2026-06-08

Initial release. Local, free, scriptable video editing via **FFmpeg/FFprobe** +
**auto-editor** - no cloud, no account, no per-render cost.

**Grounded live 2026-06-08** against **FFmpeg n8.1.1** and **auto-editor 29.3.1**
(installed via `uv tool`; auto-editor `--stats` dry-run + a real silence-cut render
smoked end-to-end on a sample clip in ~0.15s).

### Added

- `SKILL.md` - Phase 0 tooling check, Phase 1 install (FFmpeg per-OS; auto-editor via
  `uv tool`/`pipx`/venv - **not** bare `pip`, which PEP 668 blocks on Arch/modern
  distros), and Phase 2 grounded recipes: inspect (`ffprobe`/`auto-editor info`),
  trim, concat/join (demuxer vs filter), **auto silence-cut** for podcasts/vlogs
  (`auto-editor --stats` dry-run → render, `--margin`, `--edit threshold`,
  `--when-silent speed`), captions (burn-in / soft-sub; auto-gen delegated to
  `hyperframes-media` Whisper → SRT), reframe/resize (16:9 ↔ 9:16 ↔ 1:1, crop vs
  blurred-pad), logo/watermark overlay, audio extract/replace/music-bed mix, speed
  change, thumbnail grab, and web compression (`-crf`/`-preset`/`+faststart`).
- Prompt-to-recipe mapping, behaviour guidelines (never overwrite source; dry-run
  destructive edits; prefer lossless `-c copy`), error-handling table, scope limits.
- `CHANGELOG.md` - this file.

### Why

Fills the "edit my *recorded* footage" gap: `higgsfield-connector` generates AI
footage and `hyperframes-cli` renders programmatic video, but neither edits a
recorded vlog/podcast/ad. This wraps the two best free local CLIs so Claude can
drive a full record → cut → caption → export pipeline with nothing uploaded and
no subscription.
