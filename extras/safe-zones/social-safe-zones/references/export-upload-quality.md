# Export properties and delivery

The two video profiles are Selr local targets: 1080×1920 vertical and 1080×1350 portrait, MP4/H.264, progressive, square pixels, yuv420p and BT.709 SDR metadata. AAC audio uses 48kHz, mono/stereo and 128–384kbps. The retained 6Mbps video-stream minimum is a house target; it is not a universal platform acceptance floor. Inspect the actual picture before deciding whether it is sufficient.

`check-export-quality.py` checks the real local file using top-level MP4 box parsing and `ffprobe`. It requires faststart, exactly one video stream, matching dimensions/codec/pixel format, progressive/square-pixel metadata, BT.709 metadata, finite video-stream bitrate, consistent nominal/average frame rate and the declared audio properties. Missing metadata fails rather than silently passing. Overall container bitrate cannot substitute for video bitrate. The header parser seeks across payloads without loading the entire file or matching fake `moov` text inside media data.

- `--source-fps` compares the supplied measured source rate with output. If omitted, source-rate matching is explicitly unverified. Frame-rate metadata agreement does not prove every timestamp or decoded frame is correct.
- Audio is required by default. `--allow-silent` permits an intentionally silent export; it does not excuse missing audio from a spoken reel. Metadata checks do not measure loudness, detect clipping or listen to the content.
- `--max-file-mb` accepts a delivery limit verified for the actual route. No scheduler cap or public hosting choice is assumed.
- A pass reports measured properties only. View decoded frames and transitions, listen to sound, check readability and compare source/output. BT.709 tags alone do not prove a correct color conversion. Platform ingestion and post-upload compression remain unverified until observed.

A starting encoder command, for already correctly framed and color-managed input:

```bash
ffmpeg -n -i input.mov -vf setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709 \
  -c:v libx264 -pix_fmt yuv420p \
  -b:v 10000k -maxrate 13000k -bufsize 20000k \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -ar 48000 -b:a 256k -movflags +faststart output.mp4
```

Confirm the tags survive encoding with the export checker; output flags alone did not retain every tag in the local fixture. `setparams` labels already color-managed frames; it does not convert color.

This command does not itself crop, deinterlace, fix rotation, convert HDR correctly or verify quality. Use the source properties to choose those operations. `-n` protects an existing output.

## Current source context

YouTube recommends MP4/H.264 progressive uploads, 48kHz audio and retaining the recording frame rate. Its 8Mbps standard-frame-rate and 12Mbps high-frame-rate figures for 1080p SDR are recommendations, not acceptance minima. [YouTube upload encoding guidance](https://support.google.com/youtube/answer/1722171)

TikTok's in-feed ad specification varies with format and placement; check it for the intended ad rather than treating a single local master as approval for every surface. [TikTok in-feed specifications](https://ads.tiktok.com/resources/help/article/tiktok-auction-in-feed-ads)

LinkedIn's ad guidance supports several aspect ratios and lists 75KB–500MB and 3 seconds–30 minutes. These ad specifications do not establish an intermediary uploader's limits or mandate a 4:5 crop for every organic post. [LinkedIn video ad specifications](https://business.linkedin.com/advertise/ads/sponsored-content/video-ads/specs)

## Uploader boundary

The reviewed local OmniSocials documents conflict: one says URL uploads are 50MB, another says uncapped, while the historic frontcam pipeline says 100MB. Its catbox script uploads a hardcoded old batch, and its scheduler reads Keychain credentials on import even in dry run. Do not run those scripts for a quality check or copy their old account IDs, host choice or one-Short-per-day account incident into a universal rule.

Route a requested upload through the current available tool, inspect the actual account and current API constraints, and use the authorized destination. A string containing `catbox` is not proof of access, privacy, successful upload or permission to host there. Do not automatically publish local media to a public host to satisfy a file-size checker. Existing explicit upload/publish authorization persists; ask only for a genuinely unresolved business decision while continuing local preparation.
