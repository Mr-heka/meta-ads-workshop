# Profile provenance and applicability

`data/social-safe-zones.json` is the canonical machine-readable source. Coordinates below describe the downloaded templates or Selr presets, not a live device measurement. Bounds are half-open. Keep the official PNG/ZIP bytes unchanged.

| Profile | x | y | width | height | Scope |
|---|---:|---:|---:|---:|---|
| Google vertical | 48 | 288 | 840 | 960 | Downloaded 1080×1920 ad template |
| Google horizontal | 38 | 183 | 1720 | 510 | Downloaded 1920×1080 ad template, notch excluded |
| Google square | 48 | 105 | 931 | 585 | Downloaded 1080×1080 ad template, notch excluded |
| TikTok standard LTR | 120 | 240 | 660 | 1020 | Downloaded vertical standard template, right notch excluded |
| TikTok standard RTL | 300 | 240 | 660 | 1020 | Downloaded vertical RTL template, left notch excluded |
| TikTok anchor, four lines, LTR | 121 | 267 | 718 | 638 | Downloaded vertical four-line anchor example only |
| TikTok anchor, four lines, RTL | 240 | 267 | 719 | 638 | Downloaded vertical four-line RTL anchor example only |
| Legacy “universal” key | 120 | 288 | 660 | 960 | Google vertical + TikTok standard LTR intersection only |
| Selr Instagram 4:5 grid preset | 114 | 215 | 852 | 920 | Historical crop assumptions, not official UI proof |
| Selr Instagram reel-cover preset | 80 | 500 | 920 | 668 | Historical crop/UI assumptions, not official UI proof |

Google derivation uses the largest fully transparent rectangle. TikTok standard derivation also treats the reviewed white, at-most-50%-alpha logo watermark as decorative template artwork; red/blue excluded bands and corner notches remain excluded. Anchor derivation uses the reviewed green-region color/alpha mask. The largest contained source rectangle is scaled inward using ceil(left/top) and floor(right/bottom). The checker re-derives these values and checks source hashes. Pixel classification is local interpretation of the downloaded artwork, not an official geometry API.

The vendored anchor packs also contain one-, two- and three-line examples, plus square and horizontal formats. They are preserved reference assets. No computed profile here claims to cover all of them. The legacy TikTok profile-photo preset now uses a conservative 46×46 square inside the historical 66-pixel diameter circle; a 66×66 bounding square has unsafe corners.

## Source context

TikTok's official in-feed guidance says safe placement varies with creative format, caption length, anchors, device and language direction. Check the matching current template and preview for the actual ad. [TikTok in-feed specifications](https://ads.tiktok.com/resources/help/article/tiktok-auction-in-feed-ads)

Google Ads supplies horizontal, vertical and square safe-zone templates. Their presence supports using the templates, not extending one layout to all Shorts/organic/Meta surfaces. [Google Ads video requirements](https://support.google.com/google-ads/answer/13547298)

Parent source review on 2026-09-05: Meta's referenced page redirected to login; Google image-asset page returned HTTP 429. No fresh Meta geometry or Google center-80 claim was verified. Center-80 remains a labelled Selr composition preset. Do not describe the absence of a downloaded Instagram template here as proof that Instagram publishes none.

For an unknown destination, continue with a clearly labelled local composition draft while resolving placement conditions. Do not call it universally safe. A more restrictive rectangle can protect composition, but cannot certify an unexamined platform's UI.

## Personal-brand bottom captions

When youtube-video-brand owns the edit, use its personal-caption-placement.md and personal-motion-preset.json: bottom-safe captions in both video modes, semantic face/mouth/hand/action boxes (plain clothing allowed), at most 15% enlargement, relevant full-screen fallback. The bottom band is destination-specific. Reel playback, cover crops, Stories/stickers, Shorts and landscape remain separate; an ad template is not organic-playback proof. Do not add a universal bottom coordinate or move captions to the top when clearance fails.
