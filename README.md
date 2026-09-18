# The Meta Ads Workshop kit

The skills from The Meta Ads Workshop by Selr AI and 7x Advertising. Twenty-one
skills that teach an AI agent how Meta ads work, how to connect to your ad
account, how to read the numbers, and how to make more creative faster. Forty
more sit in `extras/` for when you want them.

A skill is a folder of instructions the agent reads before it acts. Installing
these does not connect anything, spend anything, or change your ad account. The
agent connects only when you ask it to, and it stops before anything that spends
money or sets an ad live.

## Install

Open [SETUP-PROMPT.md](SETUP-PROMPT.md), copy the prompt, and paste it into a
Claude Code or Codex chat. The agent clones this repository, reads each skill
under `skills/`, installs the 21 with its own supported method, reads them back
to you, then offers to connect your Meta ad account.

The [workshop page](https://drops.selrai.com.au/meta-ads-workshop) has the same
prompt, the slides and the session replay.

### Manual install

Copy any skill folder (the folder that holds a `SKILL.md`) into your agent's
skills directory, then start a new session.

| Agent | Skills directory |
|---|---|
| Claude Code | `~/.claude/skills/<skill-name>/` |
| Codex | `~/.codex/skills/<skill-name>/` |

A skill that is already installed under the same name should be compared, not
overwritten.

## The 21 skills in `skills/`

**Connect and behave**

| Skill | What it does |
|---|---|
| `meta-ads-connect` | Connects the agent to your Meta ad account. Meta's official MCP server first; Meta's official CLI as an optional extra for uploads and bulk work. |
| `meta-ads-guidelines` | The behaviour rules: everything created paused, confirm before spend, never print a token. |
| `higgsfield-connector` | Connects the agent to Higgsfield for image and video generation. One sign-in. |

**The Meta ads brains**

| Skill | What it does |
|---|---|
| `brain-meta-media-buyer-manual` | Structure, budgets, the learning phase, when to kill and when to scale. |
| `brain-meta-creative-strategist-manual` | Hooks, angles, formats and copy. Creative is the targeting. |
| `brain-meta-ad-library-competitive-research` | Mines the Meta Ad Library for the ads that have run longest and builds your swipe file. |
| `brain-meta-pixel-installation-and-site-coverage` | Installs and tests the pixel, and picks the right event to optimise for. |
| `brain-meta-troubleshooting-diagnostics` | "Not spending", "stuck in review", "CPL spiked": what to check, in order. |
| `brain-meta-budgets-bidding-learning` | CBO or ABO, bid strategies, why ads sit in learning. |
| `brain-meta-audiences-2026` | Broad or interests, lookalikes, Advantage+ audiences. |
| `brain-meta-campaign-objectives-2026` | Which objective to pick and why clicks do not become sales. |
| `brain-meta-instant-forms-vs-lp` | Instant form or landing page, and how to stop junk leads. |
| `brain-meta-attribution-truth` | Why Meta shows more sales than your CRM, and which number to trust. |
| `brain-paid-media-planning-and-forecasting` | How much to spend, break-even cost per customer, forecasting. |
| `brain-meta-account-health-and-policy` | Rejections, restricted topics, bans and appeals. |

**Creative volume with Higgsfield**

| Skill | What it does |
|---|---|
| `brain-higgsfield-ai-image-prompting` | Photoreal product and lifestyle images, consistent characters, background swaps. |
| `brain-higgsfield-ai-video-prompting` | Short ad video prompts written the way the models want them. |
| `higgsfield-soul-id` | Train a consistent avatar of a person (Higgsfield's own skill). |
| `higgsfield-product-photoshoot` | Studio and lifestyle product shots (Higgsfield's own skill). |
| `higgsfield-marketplace-cards` | Marketplace listing images (Higgsfield's own skill). |
| `higgsfield-generate` | Drive Higgsfield's CLI workflows (Higgsfield's own skill). |

## `extras/`: 40 more, install only what you want

Not installed by the setup prompt. Browse the folders, then ask your agent to
install a named one, or copy it in by hand.

```
extras/
  meta-ads/        23   deeper Meta brains: auction, CAPI, EMQ, exclusions, lookalikes,
                        message ads, placements, signal loss, retargeting, landing pages,
                        plus paid-ads (cross-channel planning) and ad-concept-miner
  creative-copy/    9   ad-creative (copy variations with a character-limit checker), direct
                        response copy, website copy, social content, hooks, CTAs, slide plans
  video/           11   captions, vertical reframing, hook scoring, ffmpeg editing, editing craft
  safe-zones/       1   social-safe-zones: checks text and logos against platform safe areas
```

## The two ways in

**Lane one, MCP.** Meta's official Ads MCP server at `https://mcp.facebook.com/ads`.
One browser sign-in, no token on your machine, no Python needed. Quick questions,
reports, checks, small safe changes. The connect skill registers it with
`claude mcp add` or `codex mcp add` and drives the sign-in. If you also use the
Claude chat app, the same server can be added there under Settings, Connectors,
Add custom connector, with the same URL.

**Lane two, the CLI.** Meta's official Ads CLI, the `meta-ads` package on PyPI.
Needs Python 3.12 or newer and an access token you create in your own Meta
developer account. Built for volume: many creatives, many copy variants,
audiences, uploads from your own files. The connect skill walks through it; do
it in your own time, not on the day.

## Requirements

- Claude Code or Codex.
- Nothing else for the MCP lane.
- Python 3.12 or newer for the optional CLI lane.
- The four Higgsfield "own" skills need Higgsfield's CLI; each says how to install it.
- Some `extras/` video skills call `ffmpeg` or a desktop editor; each says so at the top.

## What this kit will not do

It never stores a Meta token for you, never makes a raw Graph API call, never
installs a third-party Meta server, and never sets anything live without a yes
from you in the conversation. Deleting anything needs an unmistakable
instruction.

## Third-party skills

The four Higgsfield "own" skills are adapted from Higgsfield's published CLI
material and carry their own attribution. See [NOTICE.md](NOTICE.md).

Made by Selr AI.
