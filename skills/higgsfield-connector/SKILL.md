---
name: higgsfield-connector
description: "Connect Claude Code or Codex to Higgsfield AI for image and video generation. Adds the official Higgsfield remote MCP server (https://mcp.higgsfield.ai/mcp), drives the one-time OAuth sign-in, verifies the connection with a live read, then hands over to the bundled Higgsfield prompting skills. The user's only action is signing in to their Higgsfield account once. No API keys, no env vars, no copy-paste. Use when the user says 'connect Higgsfield', 'set up Higgsfield', 'install the Higgsfield kit', 'help me make AI ads', or 'I want to generate images and videos'."
allowed-tools: Bash, Read, Write, Edit
metadata:
  category: Creative & AI Generation
  tags: [higgsfield, image, video, soul-id, mcp, ads, oauth, autonomous]
  audience: non-technical business owner
  time-to-complete: 5 minutes
  cost-to-user: Higgsfield's own plan pricing (paid to Higgsfield; a free tier exists for testing)
  autonomy-bar: "User signs in to Higgsfield once. Agent does everything else."
---

# Higgsfield Connector

> **The standard**: the user signs in to Higgsfield once. Everything else is the agent.
>
> **No API keys.** No environment variables. No copy-paste. No JSON config edits.
>
> Auth is OAuth through the official remote MCP server at `https://mcp.higgsfield.ai/mcp`.
> One browser sign-in, then the agent verifies the connection and hands over to the
> prompting skills that ship alongside this one.

Works in **Claude Code** and in **Codex**. Every command below is given for both;
run the one for the agent you are.

---

## Autonomy bar

| User DOES | User DOES NOT |
|---|---|
| Sign in to higgsfield.ai when the OAuth window opens (email or Google, about 30 seconds) | Run any CLI command for the MCP connection (the four CLI skills need one terminal login) |
| Confirm in chat (at most one yes/no) | Edit any config file |
| Restart the agent once, only if asked | Copy or paste any token |
|  | Read any raw error message |

If at any point you are about to ask the user to copy or paste a value, **stop**.
There are no values to copy in this flow.

---

## How this skill works

User says any of:
- "Connect Higgsfield"
- "Set up Higgsfield"
- "Install the Higgsfield kit"
- "Help me make AI ads / images / videos"
- "I want to generate cinematic videos"

Agent runs Phases 0 to 6. The user has exactly two touchpoints: the safety gate
(one yes/no) and the OAuth sign-in window. That is the whole flow.

---

## Phase 0: Pre-flight (silent, mandatory)

Work out which agent you are and whether the connection already exists. Fix
silently where possible.

```bash
# Which agent is this?
which claude && echo AGENT=claude
which codex  && echo AGENT=codex

# Already wired? Then skip straight to Phase 5 and verify.
claude mcp list 2>/dev/null | grep -i higgsfield
codex  mcp list 2>/dev/null | grep -i higgsfield
```

A `higgsfield` line already present means do **not** add it again. Go to Phase 5.

If neither `claude` nor `codex` is on your PATH, that is a PATH problem, not a
verdict about the connection. Try from your own shell first; if it is missing
there too, ask the user to fully quit the app and open it again, then retry.
Do not tell them to reinstall anything.

---

## Phase 1: Safety gate (one short message)

Send ONE message. Wait for a single yes/no.

> **"Quick heads-up before I connect Higgsfield:**
>
> - **What you get:** image and video generation across Higgsfield's models (Soul,
>   Cinema Studio, Nano Banana, Kling, Veo, Seedance and more), plus the prompting
>   skills that came with this kit.
> - **What you do:** sign in to higgsfield.ai once when a browser window opens. That's it.
> - **Cost:** Higgsfield has a free tier for testing. Paid plans only apply if you
>   upgrade with them. Nothing here is billed by anyone else.
>
> **Ready? Say 'go' and I'll connect it."**

| User says | Agent does |
|---|---|
| 'go' / 'yes' / 'do it' | Proceed to Phase 2 |
| 'no' / 'wait' / questions | Answer calmly. Wait for explicit consent. Do not pressure. |
| 'I don't have an account' | *"No problem. When the sign-in window opens, click 'Sign up'. Takes 30 seconds with Google."* Then proceed. |

---

## Phase 2: Add the MCP server (one command, agent runs it)

Run silently, the line for your agent:

```bash
# Claude Code
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp

# Codex
codex mcp add higgsfield --url https://mcp.higgsfield.ai/mcp
```

Why `--scope user` in Claude Code: the connection persists across all of the
user's projects, not just the current folder. Codex registrations are global by
default.

If the command errors, retry once (Claude Code: with `--scope local`). If it
still fails, surface the error in plain English. Translate `ENOTFOUND`,
`EADDRINUSE` and friends; never dump raw text.

---

## Phase 3: OAuth sign-in (the only user moment)

Straight after registration the server reads **"Needs authentication"**. That is
expected. Tell the user:

> **"Adding it now. In a moment a browser window will open asking you to sign in
> to Higgsfield. Use Google for the fastest path. When you see the success page
> in the browser, come back and tell me 'done'."**

Then trigger the sign-in:

```bash
# Claude Code: the first Higgsfield tool call opens the OAuth window.
# Ask, in this session: "list the Higgsfield models you can access".
# If nothing opens after 30 seconds, run the login directly:
claude mcp login higgsfield

# Codex: run the login directly.
codex mcp login higgsfield
```

If the login needs a terminal you cannot give it, hand the user that one line
(`claude mcp login higgsfield` or `codex mcp login higgsfield`) to paste into
their own terminal, and nothing else.

If the browser window still does not open, ask the user to fully quit and reopen
the app (Cmd+Q on Mac; close the window AND the tray icon on Windows), then ask
the same question again. Some builds need a fresh launch to pick up a new HTTP
MCP server.

Wait for the user to confirm they signed in.

---

## Phase 4: Restart (only if needed)

Most builds pick up the new server without a restart. Verify the entry exists:

```bash
claude mcp get higgsfield     # Claude Code
codex  mcp get higgsfield     # Codex
```

If it reports "not found", the entry did not save: re-run Phase 2. If it is
listed, skip this phase.

---

## Phase 5: Live verification (silent)

Registration is not proof. A tool schema in your tool list is not proof either;
it can be stale from session start. The only confirmation is a live read.

```bash
claude mcp get higgsfield     # should read Connected, not Needs authentication
codex  mcp get higgsfield
```

Then exercise the connection with one read-only call. Tool names on the remote
server are discovered at run time and can change without notice, so list what is
available rather than assuming a name, and ask for something simple: the models
the account can use.

| Outcome | Action |
|---|---|
| A non-empty model list comes back | Success. Proceed to Phase 6. |
| Still "Needs authentication" | OAuth did not complete. Re-run Phase 3, once. |
| "Failed to connect" | URL or network issue. Check the URL ends in `/mcp`, re-run Phase 2. |
| Tool list empty after sign-in | No scopes granted. Ask the user to revoke and re-authorise from higgsfield.ai, Settings, Connected apps. |

After two attempts at the same step, stop and say plainly what is stuck. Do not
loop a third time.

Keep a few model names from the live read; they prove the connection in Phase 6.

---

## Phase 6: Hand-off (warm, useful, three starter prompts)

One final message. Name two or three models you actually saw in the live read,
and match the prompts to whatever business the user mentioned earlier if you can.

> **"Done. You're connected to Higgsfield. I can see [models]. Try one of these:**
>
> 1. *'Make me a photoreal product shot of [your product] on a clean studio background.'*
>    (uses the image-prompting brain and the product photoshoot skill)
> 2. *'Write me an 8-second ad video prompt for [your product], phone-vertical, one camera move.'*
>    (uses the video-prompting brain)
> 3. *'Show me the Soul ID workflow so I can train a consistent avatar of me.'*
>    (uses the Soul ID skill)
>
> When you want a prompt rewritten, polished, or adapted to another model, just ask."

---

## Skill behaviour after setup

These rules govern every later Higgsfield conversation.

### Route through the bundled prompting skills first
This kit ships six Higgsfield skills next to this one. Read the matching one
before calling the MCP:

| Job | Skill |
|---|---|
| Image prompts, edits, background swaps, character consistency, text in image | `brain-higgsfield-ai-image-prompting` |
| Video prompts, camera and motion language, drift diagnosis | `brain-higgsfield-ai-video-prompting` |
| Train and use a Soul Character (consistent face) | `higgsfield-soul-id` |
| Studio and lifestyle product images | `higgsfield-product-photoshoot` |
| Marketplace listing images and A+ style modules | `higgsfield-marketplace-cards` |
| Higgsfield's CLI workflows, job submission and retrieval | `higgsfield-generate` |

The four CLI skills (Soul ID, product photoshoot, marketplace cards, generate) use Higgsfield's own command-line tool, which is a separate install and a separate `higgsfield auth login` in your terminal; Soul training also needs a paid Higgsfield plan. Use the MCP connection for everything else.

### MCSLA for every video prompt
Model, Camera, Subject, Look, Action. Fewer than four given? Ask for the missing
one or fill it from context and say so.

### Lock seeds for a series
"More like that" or a variation: reuse the seed from the prior generation and
change one variable.

### Never echo credentials
OAuth tokens never appear in any output. There is nothing to print.

### Cost awareness
Free tier and a heavy job (ten-plus video generations, 4K upscales)? Warn once,
then run if they say yes.

---

## Troubleshooting

| Symptom | Diagnosis | Fix |
|---|---|---|
| `claude mcp` / `codex mcp` not found | Old build, or PATH | Update the app, fully quit and reopen, retry. |
| OAuth window never opens | Login not triggered | Run `claude mcp login higgsfield` or `codex mcp login higgsfield`; else hand the user that line. |
| 401 on the first tool call | OAuth did not complete | Sign in again. The browser may have blocked a popup. |
| Server missing after restart | Entry did not save | Re-run Phase 2. |
| Every generation says rate limited | Free tier exhausted | *"You've hit the free-tier cap. Upgrades are on Higgsfield's billing page. I'll pause here."* |
| A premium model says unavailable | Plan tier | *"That model is on a higher Higgsfield plan. Want me to use [a model from the live list] instead?"* |

Anything else: run Phase 5 again and read what it says. The flow self-heals;
re-running any phase on a connected machine is harmless.

---

## Setup checklist (agent tracks)

Do not tell the user "done" until every box is ticked:

- [ ] Phase 0: agent identified, no existing higgsfield entry (or skipped to verify)
- [ ] Phase 1: user said go
- [ ] Phase 2: registration command exited 0
- [ ] Phase 3: user confirmed the OAuth sign-in
- [ ] Phase 4: `mcp get higgsfield` lists the server
- [ ] Phase 5: a live model list came back non-empty
- [ ] Phase 6: three starter prompts, matched to the user's business, sent

---

## Reference

- Official MCP server: `https://mcp.higgsfield.ai/mcp`
- Higgsfield platform: https://higgsfield.ai
- MCP docs: https://higgsfield.ai/mcp
- Bundled skills: the six Higgsfield skills listed above, installed alongside this one

Made by Selr AI.

<!-- Provenance marker: sk-3c85fh --><!-- Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠ -->
