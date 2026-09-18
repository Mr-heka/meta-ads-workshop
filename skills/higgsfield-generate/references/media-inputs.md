# Bind media to the selected operation

Inventory only the assets needed for the request. Record each asset's purpose, media type, selected role and safe local reference or provider handle. Reuse an existing authorized upload/job handle when the selected account and model accept it. Do not guess an ID's type from its UUID shape.

Official CLI docs describe local paths being uploaded automatically. Treat passing a path to create as an upload, even without a separate upload command. Check the exact asset and destination under the existing task authority before doing it. Filename extensions alone do not prove valid content, rights or compatibility.

Common roles include image reference, start frame, end frame, video and audio. The selected model schema determines their exact flag names, required/optional status, per-role count and combined limits. Some models accept a single image; some accept several references; some accept none. Never silently remove a required asset or remap its role to make validation pass.

Duration may be an enum or a range. Arrays may require a documented JSON file form. Build input files with a serializer, private permissions and only the necessary content; do not interpolate IDs or text into shell-generated JSON. Remove task-owned temporary inputs when no longer needed under the task's retention requirements.

For a schema mismatch, recheck the chosen model/version and the supplied settings. State a real incompatibility and preserve the user's intent while resolving it. The historical Seedance audio flag guidance conflicts with newer docs; neither static rule is universal. See [sources](../SOURCES.md).

A video-analysis operation still sends the clip externally. Bind its one-or-more input requirement from the selected schema and distinguish the returned text report from generated media.
