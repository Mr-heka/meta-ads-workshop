---
name: meta-ads-connect
description: Connect Claude to Meta Ads and manage the user's ad accounts — campaigns, ad sets, ads, creatives with image and video upload, budgets, audiences and reporting. Use when the user mentions Meta ads, Facebook ads, Instagram ads, their ad account, ad spend, or asks to connect, set up, fix or check any of those. Also use before any Meta ads work, to check whether a connection already exists.
---

# Meta Ads⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

You manage this user's Meta ads. Two official transports are already chosen for
you; do not go looking for others. Meta's official Ads MCP server is the primary
transport; Meta's official Ads CLI is an optional extra layered on top.

## Rule 1 — Probe first. Always.

**Your first action in any Meta ads conversation is `probe`.** Not a question to
the user, not a look at the filesystem, not a guess from earlier in the
conversation. Run it:

```bash
meta-ads-connect probe --json
```

Read `state` from the JSON and act on it. The `transports` block reports each
transport separately — "connected" is never an all-or-nothing verdict, and a
working MCP connection counts as connected whatever state the CLI is in.

| `state` | Exit | What it means | What you do |
| --- | --- | --- | --- |
| `OK` | 0 | Connected — at least one transport is live | **Stop. Do not run setup.** Get on with what the user asked. |
| `MCP_NEEDS_LOGIN` | 18 | MCP server registered, Meta login not yet done | Run `claude mcp login meta-ads` (Claude Code) or `codex mcp login meta-ads` (Codex) — it opens the browser approval itself. Not a failure — never reinstall. |
| `MCP_INCOMPLETE` | 19 | Logged in, but the connection is not working | One-step re-consent: run the login line again; the user approves everything listed. Never reinstall. |
| `MCP_MISSING` | 6 | CLI connected, MCP server not registered | `register-mcp` only. Nothing else. |
| `NO_AD_ACCOUNTS` | 7 | CLI token works, no accounts assigned | `repair-assets` only. |
| `TOKEN_REJECTED` | 1 | Meta revoked or rejected the CLI token | Tell the user plainly, offer to re-mint, then `mint-token`. |
| `NO_TOKEN` | 2 | CLI installed, no token | `mint-token` only. **Do not reinstall.** |
| `NOT_INSTALLED` | 3 | Neither transport set up | Register the MCP server — see "Connecting" below. Do not start from `install`. |
| `RATE_LIMITED` | 4 | Meta is throttling | Wait, retry. Change nothing. |
| `NETWORK_ERROR` | 5 | Meta unreachable | Check connection, retry. Change nothing. |
| `META_ERROR` | 8 | Unrecognised Meta error | Run `doctor` and read what it says. |

**If `meta-ads-connect` is not on your PATH, that is not a verdict.** The helper
package is optional and its absence says nothing about the connection. Check the
primary transport directly:

```bash
claude mcp list          # Claude Code
codex mcp list           # Codex
```

A `meta-ads` line marked connected means the user **is** connected — behave
exactly as for `OK`. A line marked "Needs authentication" is `MCP_NEEDS_LOGIN`:
run the login (see "Connecting"). No `meta-ads` line at all means not
registered — go to "Connecting".

Never reconnect what is already connected. Restarting a finished setup is the
single most-reported failure of every previous version of this, and re-running
the probe is how you avoid it. If the user insists something is broken and the
probe says otherwise, run `doctor` — do not start setup on their say-so.

## Rule 2 — The MCP server is primary. The CLI is an optional extra.

- **Meta's official Ads MCP server is the primary transport and the default
  route for all ads work** — campaigns, ad sets, ads, creatives, budgets,
  audiences and lookalikes, reporting, and Meta's internal analysis tools:
  opportunity score, industry benchmarks, auction ranking benchmarks. Discover
  what it actually offers at run time (Rule 4) and drive that.
- **Meta's official Ads CLI is an optional enhancement**, never a requirement.
  Reach for it only when it is already installed and working and the task
  genuinely needs it. The one gap research has found so far: uploading image
  and video files from the user's own machine — the MCP's image and video
  tools were read-only when last checked. Re-check against the live tool list
  (Rule 4) before asserting a gap; if the CLI really is needed and not set up,
  say so plainly rather than silently working around it.
- **The raw Graph API is out of scope.** So are all third-party Meta MCP
  servers. If you find yourself about to `curl graph.facebook.com` or install
  something else, stop: the answer is one of the two above.

## Rule 3 — The MCP path stands alone.

The MCP path never requires the CLI, the Python package, a token, or a Python
interpreter. A machine with nothing installed but this skill can reach a fully
working connection.

Do not offer `meta-ads-connect install`, `mint-token` or `repair-assets` to a
user whose MCP connection is live: those commands belong to the optional CLI
path and solve problems that user does not have. A broken or absent CLI must
never be described as a broken connection while the MCP transport works.

## Rule 4 — MCP tool names are unstable. Discover them.

The MCP endpoint is unversioned and cannot be pinned. Its published tool count
went from 29 to roughly 93 (as observed mid-2026) with no version change, and it is now the primary
surface, so this rule carries the whole product: do not hardcode tool names or
assume a tool exists because it did last week — list what is actually available
and use that. If something the user asked for genuinely is not in the live tool
list, say so plainly rather than silently substituting.

## Rule 5 — Confirm before spending money.

Full write access is deliberate. Safety lives here, in how you behave, not in a
crippled grant.

- **Create everything paused.** Campaigns, ad sets and ads are created in a
  paused state unless the user has explicitly said to set them live in this
  conversation.
- **Confirm before anything that changes spend or sets something live.** That
  means: setting status to `ACTIVE`, changing a budget, changing a bid strategy
  or bid amount, and changing a schedule. State plainly what will change and
  what it will cost, then wait for a yes.
- **Deletions need an unmistakable instruction.** "Tidy up my campaigns" is not
  one. Ask which, name them back, and wait.
- Reading — insights, reporting, listing, benchmarks — needs no confirmation.
  Do not pester the user about read-only work.

## Rule 6 — Never print the token.

The MCP path stores no token, but the optional CLI path does, and it has spend
authority while transcripts get shared. Do not echo it, do not
`cat ~/.meta-ads/.env`, do not include it in a command you show the user, and
do not ask them to paste it to you. The kit moves it from browser to disk
itself, and `exec` is what puts it into an environment. If you ever need to
prove it exists, run `doctor`, which redacts it.

## Rule 7 — Your tool list is not the connection.

A `mcp__meta-ads__*` tool appearing in your tool list is **not** proof of a
working connection: the list can be stale from session start, and a complete,
valid-looking tool schema has been observed while the server was deleted and
unauthenticated. The only confirmation is a live read — list the ad accounts
and name them back.

The reverse also holds. MCP tools arrive **asynchronously**, roughly 13–20
seconds after a session starts, so their absence early in a session is not
evidence of a problem. Do not invent a connection problem for a user who does
not have one — wait a moment and check again, or run `probe`.

If a restart genuinely is needed, say it in a way that works on any machine:
fully quit Claude and open it again — closing the window may not be enough.

## Connecting

Only when `probe` returned `NOT_INSTALLED`, or `claude mcp list` shows no
`meta-ads` server. Tell the user first: this takes about a minute, they will
log in to Meta in their browser once, and Meta will ask them to approve access
for these scopes — ads management and reading, catalog management, business
management, their Pages list, Instagram basics, and Ads MCP management. Tell
them to approve everything listed and **not to deselect any ad accounts or
pages** on Meta's screen — a narrowed approval comes back as a broken
connection, not a safer one.

Step 1 — register. Preferred, when the helper package is installed:

```bash
meta-ads-connect register-mcp
```

Without the package — exactly as good. Use the line for the agent you are:

```bash
# Claude Code
claude mcp add --transport http --scope user meta-ads https://mcp.facebook.com/ads

# Codex (needs the user's own Meta app id, see below)
codex mcp add meta-ads --url https://mcp.facebook.com/ads --oauth-client-id THEIR_APP_ID
```

**Codex always needs an app id.** Meta's server does not allow the automatic
client registration Codex tries first; without an app id `codex mcp login`
fails with "Dynamic registration is not available for this client". That is
not a fault on the user's side. Walk them through "If registration fails with
a redirect_uri error" below to create the app (five minutes, free, no review),
add the Codex callback address Codex prints as a valid OAuth redirect URI, then
register with `--oauth-client-id`.

User scope matters: it makes the connection exist in every project folder, not
just the one this happened to run in. `register-mcp` also silently moves an
older local-scope registration to user scope — that is expected, not an error.

No token is minted anywhere in this flow, and nothing is created at Meta.

Step 2 — log in. Run it yourself; do not hand the user an instruction you
could have executed:

```bash
claude mcp login meta-ads   # Claude Code
codex mcp login meta-ads    # Codex
```

If the optional `meta-ads-connect` helper package happens to be installed,
`meta-ads-connect login` is an alternative that wraps the same command in a
pseudo-terminal. The helper package is optional and not included in this kit;
everything works without it.

In Codex there is no helper: `codex mcp login meta-ads` opens Meta's approval
screen in the browser itself, using the app id from registration. If it needs a terminal it cannot get, give the
user that one line to paste into their own terminal, and nothing else.

It opens Meta's approval screen in their browser, waits for the click, and
verifies the result by reading the registration back. `claude mcp login` needs
a controlling terminal, so if it cannot run as a tool call, give the user the
one line to paste into their own terminal — `claude mcp login meta-ads` — and
nothing else.

Step 3 — prove it. Verify with a live read: list the ad accounts through the
MCP and name them back to the user. The live read is what confirms the
connection — not the flow's own success message (Rule 7). If the read fails or
accounts the user expected are missing, treat it as `MCP_INCOMPLETE`: tell
them what is missing and offer the one-step re-consent, never a reinstall.

Step 4 — tell them what they can now do, then offer one first action. This step
is **not optional** and it is not a suggestion: run it every time a connect flow
ends in a successful live read.

- **Name the capability areas in plain English** — a handful of short groups,
  never a tool-by-tool inventory. Campaigns, ad sets and ads; budgets and
  scheduling; audiences and lookalikes; creatives; reporting and insights; and
  Meta's own benchmarks. **Check each group against the live tool list before
  you claim it** (Rule 4) — tool names shift under you, so describe what the
  user can do and never read tool names out.
- **Then offer exactly one first action, and make it read-only** (Rule 5): a
  performance snapshot, the campaigns currently running, an industry benchmark.
  **Never open** a new connection by offering anything that creates, changes
  spend, or sets something live.
- **Ground the offer in the live read you just did.** You have their ad accounts
  by name — put one of them in the offer instead of asking which account they
  meant.
- Then stop. One short list, one offer, and wait for their answer.

This is **connect time only**. A `probe` that came back `OK` means the user is
already connected and arrived with something else in mind — get on with what
they asked (Rule 1), and do not tour them.

Re-running any of this on a connected machine is harmless: registration and
login both detect the already-done case and say so.

To undo it entirely: `claude mcp remove meta-ads` (Claude Code) or
`codex mcp remove meta-ads` (Codex). Access can also be revoked
at Meta's end at any time under facebook.com → Settings & privacy → Business
integrations — tell the user this if they ask how to leave.

### If registration fails with a redirect_uri error

This is a known bug in Claude Code itself — not something the user did wrong,
and nothing to do with their Meta account. The way around it is to point the
connector at the user's own Meta app. It takes about five minutes, costs
nothing, and needs no approval from Meta. Walk them through it — do not try to
automate it: it needs their logged-in Meta session and fails silently under
automation.

1. Go to https://developers.facebook.com/apps and sign in with the Meta
   account they use for their ads.
2. Click "Create app". Any name is fine — "My Ads Connector" works.
3. When asked what the app should do, choose "Other", then "Business".
4. Open "App settings" → "Basic" and copy the App ID. It is a long number.
5. In the left menu, add the "Facebook Login" product. Under its settings,
   find "Valid OAuth Redirect URIs", add both of these, then save:
   - `http://localhost:8080/callback` — if registration still fails, Claude
     Code's error names the exact port to use in place of 8080.
   - `https://claude.ai/api/mcp/auth_callback`
6. Register with the App ID — either of these works:

   ```bash
   meta-ads-connect register-mcp --app-id THEIR_APP_ID
   claude mcp add --transport http --scope user --client-id THEIR_APP_ID meta-ads https://mcp.facebook.com/ads
   codex mcp add meta-ads --url https://mcp.facebook.com/ads --oauth-client-id THEIR_APP_ID
   ```

The app stays in development mode. No App Review and no business verification
are needed — those are only for apps that manage other people's ad accounts;
this one only manages their own.

If the `claude` command itself is not on PATH, that is a PATH problem, never a
verdict about the connection. Try the registration from your own shell first —
your environment usually has the command even when the user's terminal does
not. If it is missing there too, have the user fully quit Claude and open it
again — closing the window may not be enough — and retry. Do not tell them to
reinstall anything.

## The optional CLI path

Adds local image and video upload and bulk work: many creatives, many copy
variants, audiences, rules, one instruction. Never required for a working
connection — offer it, don't push it. It needs Python 3.12 or newer and a Meta
access token held on the user's machine. Two ways to set it up.

### Without the helper package (works anywhere Python 3.12+ exists)

Meta's official CLI is the `meta-ads` package on PyPI. Install it into its own
environment so it never collides with the user's other Python work:

```bash
python3 -m venv ~/.meta-ads/venv
~/.meta-ads/venv/bin/pip install meta-ads
~/.meta-ads/venv/bin/meta --version
```

The CLI reads two environment variables: `ACCESS_TOKEN` and `AD_ACCOUNT_ID`
(the `act_` number from Ads Manager). The token is the one hard step, and it is
the user's to do, in their own browser, in their own time:

1. Go to https://developers.facebook.com/apps and create an app: type
   "Business", any name. It stays in development mode; no App Review is needed
   to manage their own ad accounts.
2. Add the "Marketing API" product to the app.
3. In Business Settings, create a system user (admin), assign it the ad
   account, and generate a token with the `ads_management`, `ads_read` and
   `business_management` permissions. Meta shows the token once.
4. The user puts it in their own shell, never in this chat:
   `export ACCESS_TOKEN=...` and `export AD_ACCOUNT_ID=act_...`, or in a file
   only they read, such as `~/.meta-ads/.env` with `chmod 600`.

Then prove it, still without seeing the token:

```bash
~/.meta-ads/venv/bin/meta auth status
~/.meta-ads/venv/bin/meta ads adaccount list
```

Everything from here on is built from `--help` (next section). Rule 6 holds:
never echo the token, never ask for it, never put it on a command line you show.

### With the helper package (Claude Code, when it is installed)

The helper stores a system user token for the user and drives the browser
steps above. Only run the pieces that are actually missing:

```bash
meta-ads-connect install        # resolves a Python, installs the pinned CLI
meta-ads-connect mint-token     # drives the browser; saves the token directly
meta-ads-connect repair-assets  # fixes Business Manager / account assignment
meta-ads-connect probe          # confirm
```

Every one of these is safe to re-run and each tells you what to do next when it
fails.

If `mint-token` exits 64, the browser automation extra is not installed. Install
it and run `mint-token` again:

```bash
pip install 'meta-ads-connect[mint]'
playwright install chromium
```

If that cannot be installed, `mint-token` also prints a manual walkthrough — read
it out. It ends with a `meta-ads-connect store-token` command the user pipes
their token into, so the token still never passes through this conversation.
Never ask them to paste it to you.

`mint-token` exiting 2 means no token was created. Read out whatever it printed:
if the user has no Business Manager it prints how to create one, which takes two
minutes and is the prerequisite for the CLI path.

`repair-assets` exits 16 when it could only assign some of the ad accounts, or
none. It prints the manual steps — read them out; the user finishes in Business
Settings in under a minute. Exit 15 means they have no Business Manager and 17
means they have no ad account: both are things only they can create, and both
print a walkthrough.

`repair-assets` is worth running whenever a CLI user says an ad account is
missing, even if `probe` returned `OK`: `OK` means at least one transport works,
and the repair is what finds the accounts that are not reachable.

If `register-mcp` exits 13, that is the redirect_uri bug above — the command
prints the same bring-your-own-app walkthrough.

### Build CLI commands from `--help`, never from memory or docs.

The CLI's documentation and its shipped binary have disagreed before: the docs
said `--instagram-actor-id` where the binary wanted `--instagram-user-id`, and
early builds had no `meta auth` subcommand while 1.1.0 ships `meta auth status`
and nothing else under it. Versions move; anything you remember about this CLI
may predate the build in front of you.

**With the helper, run the CLI through `meta-ads-connect exec`.** The CLI is
installed into an environment this kit owns, so `meta` is deliberately not on
your PATH — that is what stops it colliding with the user's other Python work,
and what makes uninstalling a single `rm -rf`. `exec` finds the binary, puts the
token in the environment for that one invocation, and redacts the token from
the output:

```bash
meta-ads-connect exec -- --help
meta-ads-connect exec -- ads campaign create --help
meta-ads-connect exec -- ads adaccount list
```

**Without the helper, run the venv binary** (`~/.meta-ads/venv/bin/meta ...`)
in a shell where the user has already exported the two variables. Do not
`source` or `cat` their env file yourself, and do not put the token on a
command line.

So, before composing any non-trivial invocation, read the real flags:

```bash
meta-ads-connect exec -- ads campaign create --help
~/.meta-ads/venv/bin/meta ads campaign create --help     # without the helper
```

Build the command from what that prints. If a flag you expected is not there,
the binary is right and you are wrong.

## When something is wrong

```bash
meta-ads-connect doctor
```

It reports each component separately — each transport on its own line — and
names the next action for each. Use it instead of guessing, and instead of
asking the user to describe symptoms. Without the helper package, `claude mcp
list` (Claude Code) or `codex mcp list` (Codex) is the check for the primary
transport, and `meta auth status` is the check for the CLI.

The login has its own ladder, and it is bounded:

- `login` exits 20 — it could not drive the login from here. The user pastes
  one line into their own terminal: `claude mcp login meta-ads` (Claude Code)
  or `codex mcp login meta-ads` (Codex). That is the whole instruction.
- `login` exits 21 — the login ran and did not authenticate. The approval was
  abandoned or narrowed, or the browser never opened (the kit prints the
  consent link to open by hand). Offer **one** clean retry with the coaching
  from "Connecting": approve everything, deselect nothing. Neither exit ever
  means reinstall.
- After two attempts at the same step, stop. Run `doctor`: it writes a
  redacted diagnostic file and names it — read that file and work the failure
  it names. Never loop a third time.
- Connected but no ad accounts visible — that is Business Manager assignment,
  not a broken connection. Walk them through assigning the account in
  Business Settings (`repair-assets` prints the steps on the CLI path). Never
  send them back through a setup that already succeeded.
- Worked yesterday, rejected today — their Meta approval was withdrawn (it
  can be revoked under facebook.com → Settings & privacy → Business
  integrations). Say that plainly, then restore it with one `meta-ads-connect
  login` and one approval click.

Known cases worth recognising:

- **Python** — Meta's CLI needs 3.12 or newer. `install` picks a suitable one
  itself; without the helper, make the venv with `python3.13` or `python3.12`
  explicitly if the default `python3` is older. The MCP path does not care: it
  needs no Python at all.
- **Windows** — Meta's CLI has no build at all, so the CLI path needs WSL, and
  the kit says so rather than failing halfway through.

## What this kit will not do

Raw Graph API calls, third-party Meta MCP servers, and Ads Manager bulk CSV
import are all deliberately out of scope. Do not add them, and do not work
around their absence by installing something else.

<!-- Provenance marker: sk-dfhyy5 -->
