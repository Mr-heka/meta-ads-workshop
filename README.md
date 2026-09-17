# The Meta Ads Workshop kit

The skills from The Meta Ads Workshop by Selr AI and 7x Advertising. Sixty-six
skill folders that teach an AI agent how Meta ads work, how to connect to your ad
account, how to read the numbers, and how to make more creative faster.

A skill is a folder of instructions the agent reads before it acts. Installing
these does not connect anything, spend anything, or change your ad account. The
agent connects only when you ask it to, and it stops before anything that spends
money or sets an ad live.

## Install

Open [SETUP-PROMPT.md](SETUP-PROMPT.md), copy the prompt, and paste it into a
Claude Code or Codex chat. The agent clones this repository, reads each skill,
installs them with its own supported method, reads them back to you, then offers
to connect your Meta ad account.

The [workshop page](https://drops.selrai.com.au/meta-ads-workshop) has the same
prompt, the slides and the session replay.

### Manual install

Copy any skill folder (the folder that holds a `SKILL.md`) into your agent's
skills directory. Categories are for browsing this repository only; the agent
wants the skill folder itself, not the category folder.

| Agent | Skills directory |
|---|---|
| Claude Code | `~/.claude/skills/<skill-name>/` |
| Codex | `~/.codex/skills/<skill-name>/` |

Start a new session after installing. A skill that is already installed under
the same name should be compared, not overwritten.

## What is inside

```
skills/
  meta-ads/        37 skills   the Meta ads brain library, the connection skill, the
                               guidelines, paid-media planning
  higgsfield/       7 skills   the Higgsfield connector, image and video prompting brains,
                               Soul ID, product photoshoot, marketplace cards, CLI workflows
  video/           11 skills   captions, reframing, overlays, hook scoring, editing craft
  safe-zones/       1 skill    social-safe-zones, with the platform templates it checks against
  creative-copy/   10 skills   ad creative, hooks, CTAs, copy editing, direct response,
                               social content
```

### Start with these

| Skill | What it does |
|---|---|
| `meta-ads-connect` | Connects the agent to your Meta ad account. Meta's official MCP server first; Meta's official CLI as an optional extra for uploads and bulk work. |
| `meta-ads-guidelines` | The behaviour rules: everything created paused, confirm before spend, never print a token. |
| `brain-meta-media-buyer-manual` | The media buyer manual: structure, budgets, the learning phase, when to kill and when to scale. |
| `brain-meta-creative-strategist-manual` | Hooks, angles, formats and copy. Creative is the targeting. |
| `brain-meta-ad-library-competitive-research` | Mines the Meta Ad Library for the ads that have run longest and builds your swipe file. |
| `brain-meta-pixel-installation-and-site-coverage` | Installs and tests the pixel, and picks the right event to optimise for. |
| `higgsfield-connector` | Connects the agent to Higgsfield for image and video generation. One sign-in. |

## The two ways in

**Lane one, MCP.** Meta's official Ads MCP server at `https://mcp.facebook.com/ads`.
One browser sign-in, no token on your machine, no Python needed. Quick questions,
reports, checks, small safe changes. The connect skill registers it with
`claude mcp add` or `codex mcp add` and drives the sign-in.

**Lane two, the CLI.** Meta's official Ads CLI, the `meta-ads` package on PyPI.
Needs Python 3.12 or newer and an access token you create in your own Meta
developer account. Built for volume: many creatives, many copy variants,
audiences, uploads from your own files. The connect skill walks through it; do
it in your own time, not on the day.

## Requirements

- Claude Code or Codex.
- Nothing else for the MCP lane.
- Python 3.12 or newer for the optional CLI lane.
- Some video skills call `ffmpeg` or a desktop editor; each says so at the top
  of its `SKILL.md`.

## What this kit will not do

It never stores a Meta token for you, never makes a raw Graph API call, never
installs a third-party Meta server, and never sets anything live without a yes
from you in the conversation. Deleting anything needs an unmistakable
instruction.

## Third-party skills

Four of the Higgsfield skills, three HyperFrames video skills and one content
skill are adapted from open sources and carry their own attribution. See [NOTICE.md](NOTICE.md).

Made by Selr AI.
