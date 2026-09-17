# Production flow and evidence

Start from the actual media and requested output. Source intake may be local or Drive; a local image does not need a fabricated Drive ID. Do not move, delete, share or change source permissions as part of a creative inspection.

1. **Intake:** identify selected files, ownership/context and any proxy/download need. For a large collection, choose a representative pilot suited to the task rather than downloading everything.
2. **Triage:** inspect dimensions, duration/frame rate for video, audio where present, orientation and visible quality. Extract representative frames. A metadata probe cannot establish whether speech is intelligible or an image is sharp.
3. **Content:** identify the useful idea, proof and constraints, then select the route. Record a concise reason and the relevant renderer; skill names in the data are routes, not proof of installed capabilities.
4. **Framing:** measure real face/body/product boxes, crop/reframe as needed, record the sample and measurement method. Missing face detection remains unresolved. Do not use the example box as an automatic fallback.
5. **Placement:** select a profile and supply its `placement_context`, including template conditions and the evidence/assumptions behind selection. Declare every overlay rectangle and video start/end. Static plans omit video timing. An empty overlays list is valid when none are intended.
6. **Build:** use the renderer suited to the task. Export platform variants where layout or delivery requirements differ. Record actual files and commands.
7. **Review:** inspect real desktop/mobile crops and video frames, transitions, text, faces and audio. Compare the render with the plan and measure the actual export. Keep a record of which file/revision was checked.

`check-production-manifest.py` validates a **plan**: nonempty required sections, finite dimensions/timing, route/profile consistency, profile conditions, rectangle containment and supplied face overlap. Video and static routes have different export declarations. It does not open media, execute commands from the manifest, verify a sample-frame path or treat QC booleans as evidence. A forged `qc.safe_zone_pass=true` has no effect on its verdict.

Use `examples/production-manifest.example.json` as a fictional video plan shape. The final `export.profile` is intent; run the export checker on the actual video. Static plans use `carousel_feed_static` with `format` set to `png`, `jpg` or `pdf`, followed by real image/document review. A planning pass is useful before rendering, not an approval of finished media.

Delivery is a separate, authorized operation. Discover the current uploader and its limits, preserve existing session authorization, and read back any actual upload or publishing result. These local checks do not create a schedule or grant permission to use a public file host.
