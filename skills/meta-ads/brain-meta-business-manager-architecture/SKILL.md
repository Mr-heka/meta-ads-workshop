---
name: brain-meta-business-manager-architecture
description: Use when setting up or auditing Meta Business Manager or Portfolio, or when the user asks how to add assets, verify a domain, grant team or agency access, choose permissions, enable 2FA, add a backup admin, handle new-account spend limits, or avoid setup restrictions. Route bans and ad rejections to brain-meta-account-health-and-policy.
metadata:
  type: expert-brain
  topic: "Meta business manager architecture (portfolios, permissions, domain verification, tokens, asset hygiene)"
  aliases: "Meta Business Manager, Facebook Business Manager, BM, Business Portfolio, Meta Business Portfolio, Meta Business Suite, Business Settings, business.facebook.com, portfolio setup, ad account setup, asset hygiene, permission hygiene, partner access, domain verification, facebook-domain-verification, DNS TXT verification, meta tag verification, business verification, verified business, ad account limit, 2FA, two-factor, backup admin, system user token, pixel setup, CAPI setup, account ban, ad account restriction, clean account setup"
  domain: "advertising"
  built: "2026-07-06"
  sources: 14
---

# Brain: Meta business manager architecture (portfolios, permissions, domain verification, tokens, asset hygiene)⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠

> Built by topic-brain-builder from 14 YouTube sources
> (8 hidden-gem creators surfaced on engagement,
> not views). Made by Selr AI.

## How to use this brain

Drop-in install: place this folder at `~/.claude/skills/brain-meta-business-manager-architecture/`. No setup, no dependencies, no config. Claude loads it automatically when a Meta Business Manager question matches the description above.

When the user is working on Meta business manager architecture (portfolios, permissions, domain verification, tokens, asset hygiene), load this brain first. Ground answers in
the synthesis below and cite experts by name from the quote library. Prefer the
consensus view; surface a contrarian take when it's well-argued.

## What the experts agree on

1. **The personal profile is the root of trust and must be a real human.** The portfolio is created from a personal Facebook profile that sits above everything; use a real, name-and-DOB-accurate profile, never a fake "business" second profile (Justin Lalonde, ZoCo Marketing, Genius Maker, Derek Videll). Lalonde adds: ID-verify that profile at facebook.com/id first.
2. **Lock security first: 2FA + a backup admin before anything else.** Add a second admin on a separate login and turn on two-factor for everyone the moment the portfolio exists (EfesAdLab, Dr. Matt Shiver, ZoCo Marketing). This is the recovery net against a hack or restriction wiping out the whole BM.
3. **Verify the business early.** It raises the ad-account creation limit (1 unverified → 3-10 verified) and reduces random restrictions (Justin Lalonde, EfesAdLab, Extentions Advertising).
4. **Link assets in order: Page → Ad Account → Instagram → Pixel.** A Facebook Page is mandatory to run ads; an Instagram account is not (Dr. Matt Shiver, Derek Videll, Máté Hunyor, EfesAdLab).
5. **Ad-account creation is one-way and limit-gated.** Time zone and currency are permanent, deleting an account does not refund the creation slot, and adding an account to a portfolio cannot be undone (Genius Maker, ZoCo Marketing, Dr. Matt Shiver).
6. **New accounts hit a ~$20-50/day early spend cap that lifts with clean payment history** (EfesAdLab, Justin Lalonde). Set your own account spending limit when you add the card (EfesAdLab).
7. **Least-privilege permissions.** Partial access + specific assets for staff/VAs, full control only for true admins (partner/family), time-boxed access for auditors (Justin Lalonde, Máté Hunyor). Agencies use **partner access, never personal/employee access** (Jamie Stenton).
8. **Domain verification and CAPI are core hygiene.** Three verification methods (meta tag fastest, DNS TXT fallback, HTML file), bare domain with no prefix (Tareq Istiaq, Dr. Matt Shiver, Digital Growth Tutor, Genius Maker). CAPI on always; verify pixel firing with Pixel Helper + Test Events before spending (EfesAdLab, Genius Maker).

## Named frameworks & methods

- **The one-human-root rule** (Lalonde): profile ID verification before portfolio creation. Status yellow "pending" → green "confirmed" in ~1-2 days.
- **Developer-app verification trigger** (Lalonde): create a placeholder app in the Meta Developers console (only verified businesses can publish apps) to force Meta to surface "Start Verification" under Security Center. Costs nothing.
- **Ad-account limit numbers** (Lalonde): unverified = 1 ad account; verified = "usually 3, up to 10". Verification took him 3 tries over 2-3 weeks; each review is 24-72 hours.
- **Redundancy accounts (source claim, not recommended)** (Lalonde): create 3-5 ad accounts up to your verified limit as backups against takedowns. Do not follow this. Stockpiling spare accounts fragments learning, and Meta reads a pool of idle backup accounts as ban-evasion behaviour. Run one clean, verified account and protect it.
- **Partner-access model** (Jamie Stenton): client links the agency BM via the agency's Business/Partner ID (`business_id=` in the BM URL), assigns each asset at "ads and insights only" / "partial control" / "full control", must click "assign assets". Agency then re-assigns each client asset down to the individual employee.
- **Three domain-verification methods** (Dr. Matt Shiver, Genius Maker, Digital Growth Tutor, Tareq Istiaq): meta tag (fastest, ~10 min despite Meta's 72-hour warning), DNS TXT (`facebook-domain-verification` value, host `@`), HTML file (upload to `public_html` via cPanel). Location: Business Settings > Brand Safety and Suitability > Domains.
- **Shopify data-sharing tiers** (Genius Maker): in the Facebook & Instagram app, "maximum" = Pixel + Advanced Matching + CAPI; "enhanced" = Pixel + Advanced Matching + CAPI; "conservative" = pixel only. Pick maximum.
- **Page-legitimacy minimum** (EfesAdLab, Genius Maker): 3-5 real posts (Genius Maker says 4+) plus logo, cover, website, contact and a custom username before the first ad. Cover image 820x360.

## Contrarian / disputed takes

- **Business-verification method (real disagreement).** Lalonde uses a native placeholder developer-app to trigger verification. Extentions Advertising instead loads a **third-party unpacked Chrome extension** in Developer Mode to auto-fill Meta's verification form with real business documents and BM IDs, plus a bundled template. Side with the native/direct route: an unvetted extension touching business-identity data is itself the kind of security risk this brain warns against.
- **How many ad accounts to create.** Lalonde says spin up 3-5 for redundancy; Genius Maker warns that deleting an account still burns the slot, so you should never create/delete casually. Reconciled: plan your slots deliberately up to the verified limit, do not experiment with them.
- **Which domain method to demo.** Dr. Matt Shiver prefers the meta tag and says "I never do" the HTML file; Digital Growth Tutor demos exactly that HTML file; Genius Maker uses DNS TXT. Not a real conflict: all three work, pick by the access you have to the site.
- **Unofficial "enterprise BM" products (flagged, not endorsed).** AdsTrust markets a "BM2500/BM25000" for up to 2,500 ad accounts. This is not official Meta terminology; all capacity/pricing/"priority trust" claims are unverified vendor marketing. Their only useful point is a caution: "priority trust does not mean immunity... Restrictions, reviews, and enforcement can still happen."

## Execution playbook

**IF/THEN operating rules (attributed):**
- IF creating a Business Portfolio THEN create it from a real, name-accurate personal profile, and ID-verify that profile at facebook.com/id first (Lalonde).
- IF the portfolio was just created THEN before payment or campaigns, add a second admin on a separate login and turn 2FA on for everyone in Security Center (EfesAdLab, Dr. Matt Shiver, ZoCo).
- IF you want more than one ad account or fewer random restrictions THEN complete business verification early; expect 24-72h per review and possibly multiple tries (Lalonde, EfesAdLab).
- IF adding assets THEN do Page → Ad Account → Instagram → Pixel, and confirm you're in the correct portfolio in the settings switcher first (Máté Hunyor, Derek Videll).
- IF creating an ad account THEN set time zone and currency deliberately, they are permanent; never delete an account to reclaim a slot (Genius Maker, ZoCo).
- IF you add a payment method THEN set an account spending limit in the same step (EfesAdLab).
- IF a new account stops spending at ~$25-50/day THEN that is the trust ramp, keep payments clean and it lifts automatically (EfesAdLab, Lalonde).
- IF giving a VA/staffer access THEN partial access + only the specific assets they need; full control only for a partner/family admin (Lalonde, Máté Hunyor).
- IF an agency or auditor needs access THEN partner access via Business ID (not employee access) for the agency, time-boxed 3-7 day access for a one-off auditor (Jamie Stenton, Máté Hunyor).
- IF verifying a domain THEN enter the bare domain (no https/www), use the meta tag for speed, fall back to DNS TXT, then Connect Assets to the Page (Tareq Istiaq, Dr. Matt Shiver, Genius Maker).
- IF installing the pixel THEN use partner integration if the platform has one, manual code only for custom sites, turn CAPI on, then verify with Pixel Helper + Test Events before spending (EfesAdLab, Genius Maker).
- IF the Page is new THEN post 3-5 real pieces and fill logo/cover/website/contact/username before running any ad (EfesAdLab, Genius Maker).

**Default numbers experts use:** ad-account limit 1 (unverified) → 3-10 (verified); business review 24-72h; new-account spend cap ~$20-50/day; domain meta-tag verify ~10 min; cover image 820x360; minimum Page posts 3-5; auditor access window 3-7 days.

**Pre-flight checklist (clean setup):**
1. Real personal profile, ID-verified at facebook.com/id.
2. Portfolio created; correct portfolio confirmed in the switcher.
3. 2FA on for everyone + a second admin on a separate login.
4. Business Info complete (legal name, address, phone, website, tax ID) and business verified.
5. Page added (3-5 posts, full profile, custom username), then ad account (time zone + currency locked), then Instagram, then pixel.
6. Domain verified (bare domain, meta tag), Connect Assets to Page.
7. CAPI on; pixel firing confirmed in Pixel Helper + Test Events.
8. Account spending limit set; permissions least-privilege; agency on partner access only.

**Top 5 failure modes and the fix:**
1. **Making a fake "business" profile.** Fix: use one real ID-verified personal profile as the root (Lalonde, ZoCo).
2. **No 2FA / no backup admin, then a hack or restriction locks out the whole BM** (the $40-50K anecdote). Fix: 2FA everyone + separate-login backup admin first (Dr. Matt Shiver, EfesAdLab).
3. **Wrong time zone/currency, or deleting an ad account to "reset".** Fix: both are permanent; deleting burns the slot, so plan deliberately (Genius Maker, ZoCo).
4. **Letting an agency in as an employee, cascading a ban across every client.** Fix: partner access via Business ID only, scoped per asset (Jamie Stenton).
5. **Running ads on a thin Page or an unverified domain / browser-only pixel.** Fix: 3-5 posts, verify the domain, turn CAPI on, confirm firing before spend (EfesAdLab, Genius Maker, Tareq Istiaq).

## Applied to your business

This brain is the account-hygiene foundation under every paid campaign you run. Write your own facts down before applying it, then keep the answers consistent.

**Which of your funnels this feeds:** all paid Meta acquisition, namely `<your front-end offer + price>`, `<your secondary offer + price>`, and warm retargeting for `<any recurring or membership offer>`. It is upstream of everything else: if the portfolio, domain, permissions and CAPI are not clean, no campaign performs or measures correctly.

**Your fixed facts (write them once, never contradict them):** ad account `<YOUR_AD_ACCOUNT_ID>`, pixel `<YOUR_PIXEL_ID>`, Page `<YOUR_PAGE_ID>`, `<your CRM>`, `<your landing-page stack>`. Decide up front whether you run manual control or Advantage+ and record that too.

**Consensus translated into moves:**
1. **Keep CAPI verified green (Theme 10).** The job here is keeping the server-side feed healthy (token validity, deduplication, an alert if events stop) before scaling spend. A conversion Meta cannot see is a conversion it cannot optimise toward. Deep work routes to `brain-meta-capi-server-side-deep`.
2. **Verify every revenue domain, bare-domain + meta tag.** Each domain you send paid traffic to (`<your landing-page domains>`) gets verified under Brand Safety and Suitability, then Connect Assets to `<YOUR_PAGE_ID>`. On hosted page-builders and custom Next/React sites the header meta-tag method is usually the fit; DNS TXT is the fallback.
3. **Least-privilege even on one account.** Running everything through a single ad account makes permission hygiene matter more, not less: partial access + specific assets for anyone who is not a core admin, 2FA on everyone, a backup admin on a separate login.
4. **Keep Pages legit before any launch.** An established Page is maintenance, not build, but any new Page must clear the 3-5-post + full-profile bar before its first ad.
5. **Protect the single account like the asset it is.** Set and confirm the account spending limit, never delete or recreate the ad account, and treat any restriction as a recovery event where the verified-business paper trail (Lalonde) speeds reinstatement.

**What does NOT apply to a single-account owner-operator, and why:**
- **Multiple redundancy ad accounts (Lalonde).** Run one account. Spare backups fragment learning and read to Meta as ban-evasion behaviour.
- **Agency partner-access onboarding (Jamie Stenton).** Only relevant if you take on client portfolios, or if you grant a contractor scoped access, in which case use partner/time-boxed access, never employee access.
- **Shopify pixel/catalogue auto-install (Genius Maker) and e-commerce catalogue hygiene.** Skip it if you are lead-gen rather than e-commerce; your pixel install is a direct/CAPI install and DPA/catalogue setup is out of scope.
- **The unofficial "BM2500" enterprise product (AdsTrust).** Not real Meta infrastructure; ignore entirely.
- **Advantage+ shopping/audience automation** implied by campaign-structure sources. If you have chosen manual control, that choice governs; route those questions to `brain-meta-ads-manual-control-no-advantage`.

## Pairs with / boundaries

- **`brain-meta-pixel-capi-signals` and `brain-meta-capi-server-side-deep`** own the deep pixel/CAPI/event-signal work. This brain covers only *installing and verifying* the pixel and turning CAPI on as setup hygiene; signal strategy, EMQ and server-side plumbing live there.
- **`brain-meta-ads-manual-control-no-advantage`, `brain-meta-media-buyer-manual`, `brain-meta-creative-strategist-manual`** own campaign structure, budgets, audiences and creative. Anything about *what to run* (not *how the account is built*) routes to them.
- **`brain-post-click-tracking-plumbing`** owns UTMs, fbclid, cross-domain and lead-source-to-CRM. Domain *verification* is here; post-click *tracking* is there.
- **`brain-meta-account-health-and-policy`** owns ad rejections, restricted topics, special categories, and ban recovery/appeals. This brain owns ban *avoidance through clean setup* (2FA, verification, partner access, least privilege); once an account is actually restricted or an ad is rejected, that policy/recovery brain takes over.
- **Explicitly OUT of scope here:** system-user token creation (thin in the sources, defer to Meta developer docs), catalogue/feed structure, audience building, campaign settings, creative, and post-restriction recovery/appeals. This brain stops at a clean, verified, permission-hygienic account ready to advertise.

## Related brains

- `brain-post-click-tracking-plumbing`: Post-click tracking plumbing (UTMs, fbclid, cross-domain, thank-you events, lead source to CRM)
- `brain-meta-audiences-2026`: Meta ads audiences 2026 (the full audience system survey)
- `brain-meta-exclusion-architecture`: Meta ads exclusion architecture (exclusions, overlap control, funnel sequencing)
- `brain-meta-account-health-and-policy`: Meta account health and policy (rejections, restricted topics, bans and recovery)

## Deeper references

- `references/synthesis.md`: full thematic synthesis
- `references/quote-library.md`: verbatim quotes with attribution
- `references/experts.md`: who was mined and why (popular vs hidden-gem)
- `examples/contractor-access-session.md`: worked Q&A session (scoped contractor access on our single ad account)

Router key `sk-tit0fy` — resolved by the skills index on load.
