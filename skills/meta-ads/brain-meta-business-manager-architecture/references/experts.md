# Experts Mined: Meta Business Manager Architecture (portfolios, permissions, domain verification, tokens, asset hygiene)

Per creator: name, popular vs hidden-gem (from the source index built at mining time), their angle, and what they uniquely add to this ops brain.

## Justin Lalonde (popular, strong engagement, 24k views)
- **Angle:** agency operator managing ~$20M/yr in ad spend, security-first and gotcha-dense.
- **Uniquely adds:** the sequenced security-first setup: ID-verify the personal profile at facebook.com/id *before* creating the portfolio; pick the "social issues, elections or politics" reason for the highest verification tier; force business verification via a placeholder Meta Developers app; the concrete ad-account limit numbers (1 unverified to 3-10 verified); create 3-5 ad accounts as redundancy against takedowns. The most valuable single source for the ban-avoidance and verification half of the scope.

## EfesAdLab (hidden gem, top-decile engagement, 21 views)
- **Angle:** beginner-focused but explicitly framed around "mistakes to avoid".
- **Uniquely adds:** the densest ban/security cluster: 2FA + backup admin as the first post-creation task, set a spend limit the moment payment is added, the new-account $25-50 spend cap explained, CAPI as a "must", manual base pixel = PageView only, and the "zero posts screams scam / 3-5 posts looks real" rule. The strongest single source for the ops/hygiene half of the brain.

## Dr. Matt Shiver (popular, 58k views, largest reach in the set)
- **Angle:** solo coach/consultant, beginner-friendly, security basics + practical linking mechanics.
- **Uniquely adds:** the $40-50K unauthorised-spend-after-hack anecdote that makes 2FA concrete; the backup-admin-on-a-separate-login recovery pattern; the meta-tag-is-fastest domain claim ("Meta says 72 hours, it takes 10 minutes"); the three domain methods with "HTML file, I never do this".

## Máté Hunyor (hidden gem, top-decile engagement, 1.3k views)
- **Angle:** practical agency-style walkthrough framing BM as a multi-client container.
- **Uniquely adds:** check for existing BM memberships first (you may already be in one); confirm the correct portfolio in the settings switcher before adding assets; time-boxed 3-7 day access for auditors; the separate finance-section permission; the deliberate USD currency choice for benchmark familiarity.

## ZoCo Marketing (popular, 18k views, strong engagement)
- **Angle:** general-purpose feature-tour of the full Business Portfolio settings.
- **Uniquely adds:** the "you're a real human" framing for the personal profile rule; 2FA set to "everyone" not just admins; the one-way "you can't remove this account from the business portfolio" warning; the politics/religion restricted-category flag at pixel creation; the LLC/EIN recommendation over a personal tax ID.

## Genius Maker (hidden gem, top-decile engagement, 3.5k views)
- **Angle:** hands-on screen-recorded beginner walkthrough (India-based) treating the whole BM-to-Shopify pixel pipeline as one linear checklist.
- **Uniquely adds:** the most specific UI field values (cover image 820x360, four-post minimum, DNS TXT host `@`, manual username or random-digit URL); the "delete an ad account and the slot is still exhausted" rule; the Shopify app's maximum/enhanced/conservative data-sharing tiers explained; Pixel Helper + Test Events verification.

## Jamie Stenton (popular, 7.4k views, strong engagement)
- **Angle:** agency/freelancer operator on the client-onboarding side of BM.
- **Uniquely adds:** the whole partner-access-vs-personal-access ban-avoidance mechanism, the single most important structural rule when someone else touches your assets; the Business/Partner ID via `business_id=` in the BM URL; the ban-cascade risk across all clients; the agency re-assigning received client assets down to individual employees; the "click assign assets or it fails" gotcha.

## Tareq Istiaq (hidden gem, top-decile engagement, 56 views)
- **Angle:** narrow, tactical single-purpose domain-verification tutorial for WordPress with a Shopify aside.
- **Uniquely adds:** the bare-domain no-prefix input rule ("do not add any prefix like https"); the WordPress header/footer code-snippet plugin route; the confirmation that the same meta tag works on Shopify via a header-injection app; the benefits list (AEM event prioritisation, dynamic ads, BM security).

## Derek Videll (popular, 13k views, strong engagement)
- **Angle:** beginner-oriented sequential first-time setup for a single business owner (not an agency).
- **Uniquely adds:** the sharpest UI gotcha ("business settings and not settings, they are different"); the ownership-hierarchy literacy (profile owns portfolio owns ad account, ads don't run from the profile); desktop-not-mobile for profitable ads; assign the agency "ads" only, not full control; create the pixel through the website builder (Shopify/Wix/Squarespace) or Events Manager > Partner Integrations.

## Digital Growth Tutor (retained despite low score, penalised: short + low engagement, 3.9k views)
- **Angle:** single-purpose micro-tutorial on the HTML-file domain-verification path.
- **Uniquely adds:** the concrete cPanel/`public_html` upload sequence that the broader setup videos skip. Kept for Theme 9 as the HTML-method detail source; nothing else usable.

---

## Source quality notes

- **Usable sources: 11 of 14.** Eleven contribute substantive, in-scope, verifiable material to the synthesis (Lalonde, EfesAdLab, Dr. Matt Shiver, Máté Hunyor, ZoCo Marketing, Genius Maker, Jamie Stenton, Tareq Istiaq, Derek Videll, Extentions Advertising, Digital Growth Tutor). This clears the 8-source floor comfortably.
- **Excluded, 3:**
  - *Dara Denney* (out of scope by content: Ads Manager campaign structure / Advantage+ Shopping, not BM architecture; also conflicts with our manual-control doctrine).
  - *AdsTrust Offical* (thin + era-flagged: vendor advertorial for an unofficial "BM2500" product; no verifiable BM-architecture mechanics; kept only for two ban-caution quotes flagged as unverified).
  - *Searchly Digital* (thin: short click-through, corroborates permissions but adds nothing unique; excluded from theme counts).
- **Freshness:** all sources pass the freshness rule (videos 18 months old or newer at build). No freshness exceptions were needed.
- **Method caveat (not a freshness issue):** Extentions Advertising demonstrates a third-party unpacked Chrome extension loaded via Developer Mode to auto-fill Meta's business-verification form with real business-identity documents and BM IDs. This is itself an account-security risk the brain warns against. The source is retained for its verification-flow narration, but the extension method is flagged as a gotcha, and the native developer-app route (Lalonde) or filling Meta's own form directly is preferred.
- **Thin sub-areas of the scope, stated honestly:**
  - **System-user tokens** are effectively uncovered. No source walks through creating a system user or generating a system-user access token in Business Settings. The token-hygiene coverage in this brain is limited to permission least-privilege, partner access, and CAPI-enabling integrations. For true system-user/token work, treat this brain as thin and defer to Meta's own developer docs plus the CAPI sibling brains.
  - **Catalogue hygiene** is lightly covered (only Genius Maker, via the Shopify auto-created catalogue rename). Deep catalogue/feed structure is out of scope here.
  - **WhatsApp asset linking** appears only in the thin Searchly Digital source, so it is not built into the themes.
