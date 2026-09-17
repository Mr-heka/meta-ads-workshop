# Source Index

Every source used to build this skill. Raw transcripts are not included in this kit. Research and scraping conducted 2026-05-22.

## About Justin Brown / Primal Video

- Justin Brown runs **Primal Video**, an Australian YouTube channel teaching creators and business owners "how to grow an audience and scale your revenue with online video".
- Channel size stated as **1.8M subscribers** (approximate, from video 07's title and narration).
- Self-described mission: help "entrepreneurs and business owners amplify their business and brand with video."
- Flagship asset: the **Primal Video Method**, a downloadable/printable step-by-step editing process, also shipped as an AI prompt.
- Primal Video also operates a paid membership, **Primal Video Plus** (a $19 membership per video 11), which includes deeper tutorials and a "Justin AI" Q&A bot.
- Co-founded **Video Stats**, a YouTube link-tracking tool, with Mike (Primal Video) and Jack Bourne of Deadline Funnel.

## YouTube, 11 transcripts, all transcribed verbatim (not included in this kit)

| # | File / Title | Views (approx) | Published | URL |
|---|------|------:|------|-----|
| 01 | How To Edit Videos (Video Editing For Beginners - Complete Guide!) | 80,065 | 2024-07-02 | youtube.com/watch?v=6GnmzvqqzJw |
| 02 | The Ultimate Guide to Faster Video Editing (Beginners) | 34,826 | 2025-06-26 | youtube.com/watch?v=Z0QXKDUcnbM |
| 03 | 10 Mistakes NEW Video Editors Make (Video Editing for Beginners!) | 841,988 | 2020-01-05 | youtube.com/watch?v=74UFO1sBcD8 |
| 04 | Video Editing for Beginners (Using Windows PC!) | 2,546,646 | 2018-05-13 | youtube.com/watch?v=-wpFSpNbDW0 |
| 05 | How To Edit YouTube Videos With Descript Video Editor (Descript Tutorial!) | 25,822 | 2024-12-19 | youtube.com/watch?v=MjTkf5Qrx_I |
| 06 | How I Actually Decide Which Videos to Make | 2,504 | 2026-04-02 | youtube.com/watch?v=krTiMeHbrgg |
| 07 | The ACTUAL Tools We Use to Run a 1.8M Subscriber Channel | 3,477 | 2026-02-20 | youtube.com/watch?v=Hp3JQNZDE7Q |
| 08 | Best AI Caption Generator For Video (How To Add Subtitles To A Video!) | 18,554 | 2025-05-29 | youtube.com/watch?v=mq5YKZtEVlA |
| 09 | From 0 to 1,000 Subscribers FASTER: 9 Tips to Grow a New YouTube Channel | 1,047,145 | 2021-09-12 | youtube.com/watch?v=xAYRdittgT4 |
| 10 | Best Camera Settings for VIDEO (Dynamic & Sharp Videos!) | 8,824 | 2024-12-05 | youtube.com/watch?v=PLi23I39Z1s |
| 11 | I Finally Proved Views Don't Matter - Here's the Data | 3,262 | 2026-02-26 | youtube.com/watch?v=dttBN62Szg4 |

All transcripts: YouTube auto-transcripts, scraped via Apify `karamelo/youtube-transcripts`, 2026-05-22.

## What each video contributes to the skill

- **01, 02, 04**, the core 9-step Primal Video Method, demonstrated across CapCut, VN Video Editor, and Shotcut. The backbone of `editing-method.md`.
- **03**, the 10 beginner mistakes (the review checklist) and the edit-backwards technique. Backbone of `mistakes-and-review.md`.
- **05**, the Descript transcript-based editing workflow: AI shorten-word-gaps, remove-retakes, scenes, zoom cuts, templates.
- **06, 11**, the 5-lens topic-selection model and the "views do not matter, judge by business impact" principle.
- **07**, Primal Video's full 2026 production tool stack (ClickUp, Video Stats, VidIQ, Claude, Descript, eCam, StreamYard, n8n, Bento) and the 14-20h to 1-2h editing-time claim.
- **08**, caption tools and the caption workflow.
- **09**, channel-growth fundamentals (research, hook, thumbnail, email list).
- **10**, camera and recording baselines (4K, 24/30fps, exposure triangle, white balance, audio).

## Caveats

- The transcripts are YouTube auto-captions, so they contain transcription artifacts: "Descript" appears as "Dcript" / "Dscript", "n8n" as "NADN" / "NAD", "Captions" (the app) as "Caping", HTML entities like `&#39;` for apostrophes. Quotes in the reference files are cleaned for readability but not changed in meaning.
- View counts are as captured on 2026-05-22 and will keep rising; treat them as approximate.
- The "1.8M subscriber" figure is from video 07's title and is the only channel-size figure stated; treat as approximate.
- Editing-time figures (14-20h down to 1-2h) are Justin's own stated numbers from video 07.
- No web sources were used; the `sources/web/` directory is empty.

## Refreshing this brain

Primal Video publishes frequently and the tool landscape moves fast (Justin himself notes his AI tool "was Gemini, and who knows where it is 2 weeks from now"). To update: re-scrape the channel via Apify `streamers/youtube-scraper` plus a YouTube transcript actor (`karamelo/youtube-transcripts`), keep the new raw `.txt` files in your own sources folder, and update the framework references. Priority refresh targets: any new editing-process video, any new Descript or AI-editing video, and any new tool-stack roundup.
