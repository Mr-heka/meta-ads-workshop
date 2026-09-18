# Experts Mined: Meta automated rules and experiments (rules engine, A/B tests, holdouts, bulk ops)

Popular vs hidden-gem drawn from the source index built at mining time (Gem = Y column). Angle and unique contribution drawn from the mined notes.

---

## Usable sources (9)

### Michael Diaz (hidden gem)
- **Video:** *4 Key Meta Ads Testing Principles You Need to Know!*
- **Angle:** practitioner walkthrough of manual split-testing discipline inside live accounts. Not the rules engine itself; the human-side rationale for *why* a systematic kill/scale rule is needed.
- **Uniquely adds:** the "change one variable at a time" law stated plainest, plus the clearest concrete case of Meta misallocating spend inside an ad set (top spender $200 at 0.49 ROAS vs an underspent ad at $36 for 2.68 ROAS) and the manual fix (kill the bad spenders to force budget onto the winner). Coined framing: "either you win or you learn."

### William Kast (hidden gem)
- **Video:** *You're Testing Your Meta Ads Wrong (Do This After Andromeda)*
- **Angle:** post-Andromeda split-test framework for agency clients spending 30k-300k/month. One ad set per high-level variable, three variations each.
- **Uniquely adds:** the post-Andromeda caveat that small tweaks no longer register as distinct ads, so you must change a *high-level* variable (benefit/angle), and the video-specific rule of split-testing only at the hook while keeping the body identical.

### Damini Tripathi
- **Video:** *How to Automatically SCALE your Facebook ADS? (FREE GUIDE)*
- **Angle:** Indian-market dashboard-level tutorial for automated scaling rules and CBO-vs-Advantage-Plus selection by budget tier. Heavy on UI steps and ₹ thresholds.
- **Uniquely adds:** a full scale-rule build (increase budget 20% when cost per purchase < ₹300 over 3 days, max cap, once every 12 hours) and a paired ROAS-kill rule (auto-off below 2). Note: leans on Advantage+ audiences/placements, which we override per our doctrine.

### Nick Theriot
- **Video:** *Top 3 Most Effective Ways To Test Facebook Ads In 2025*
- **Angle:** 10-year veteran scaling ecom clients; compares three testing structures and gives a low-touch operating rule for his preferred single-CBO method.
- **Uniquely adds:** the manual 7-day-window CPA kill rule (the human twin of our house rule), and honest acknowledgement that CBO allocation starves some ad sets ("it doesn't ensure that every adset gets spin"). Also the "5-10 minutes a day" management cadence.

### Chris Marrano
- **Video:** *Use These Facebook Ads Automated Rules To Hack Your Growth*
- **Angle:** ecom agency founder pairing an automated budget-scaling rule with a manual bid cap as a two-layer safety system.
- **Uniquely adds:** the two-constraint model (bid cap controls auction efficiency, automated rule controls budget growth), a concrete scale rule (10%/day, $1,000 cap, cost per result < CPA target over 14 days), and the distinction between the daily automated rule he teaches DIY advertisers and his agency's tighter 3-day human cadence.

### Leadstio
- **Video:** *Automating Your Meta Ads—Set Up Rules and Eliminate Manual Work*
- **Angle:** practitioner walkthrough distinguishing rule scope by level (ad/ad set/campaign) with real CPL kill-rule thresholds.
- **Uniquely adds:** the sharpest practical constraint in the set, cost-per-result conditions are not available at ad-set level and must run at campaign level. Also campaign-name filtering for channel-specific ceilings, and paired on/off rules for non-standard scheduling. The cleanest CPL-kill mirror of our house rule (define ~$50 normal CPL, kill at $100-$150).

### Tej
- **Video:** *How To Run A/B Tests on Meta Ads (Step-by-Step for Beginners)*
- **Angle:** beginner-friendly, purely UI-driven walkthrough of Meta's native A/B Test tool (not manual duplication).
- **Uniquely adds:** the full native A/B Test flow (Get Started > Make a copy > choose variable > name/metric/dates/constant budget), the "end the test early if a winner is found" advanced setting, the 1-2 week minimum before acting, and pause-loser/scale-winner as the post-test action.

### Belad Tech Weekly
- **Video:** *Stop Burning Cash: Setup These 3 Facebook Ads Automated Rules Now*
- **Angle:** end-to-end native Rules UI walkthrough with concrete example thresholds for the three classic rule types plus Meta's built-in template rules.
- **Uniquely adds:** the three-rule stack (kill-on-spend >$1,000, scale-on-performance, kill-on-underperformance with results <1 AND CTR <1%), and a rundown of Meta's pre-built templates (Enable Advantage+ Creative, Reduce Auction Overlap, Optimize Ad Creative, Reduce Audience Fragmentation). We take the custom-rule mechanics and skip the Advantage+ Creative template.

### Marketing Operators
- **Video:** *The Right Way to A/B Test Landing Pages on Meta Ads for Ecommerce*
- **Angle:** two experienced DTC media buyers debating practical A/B and holdout-style methodology from an operator's seat.
- **Uniquely adds:** the only holdout-adjacent content in the set. A documented failure case (splitting existing learned traffic to test a new offer doubled CAC; relaunching it as a fresh funnel worked), the rule of thumb for iterative-test-vs-new-funnel, deciding on revenue per session over conversion rate (15% lift, rolled out 100/0), and the velocity-over-precision "canary" philosophy.

---

## Excluded sources (3)

- **Chase Chappell, *The NEW Way To Test Facebook Ad Creatives*.** Flagged `thin: true`. Funnel-stage creative strategy only; nothing on rules, experiments, or holdouts.
- **HubSpot Marketing, *The Best Facebook Ads Testing Strategy*.** Era-flagged. Its sequential creative-then-audience-then-text-then-placement phasing is the exact approach Kast and others call obsolete post-Andromeda. One budget number quoted as a manual mirror only, not as a backer.
- **Mark Builds Brands, *how to test facebook ads post andromeda update*.** Era-flagged for scope. Passes freshness (dated 2025-11-26) but covers CBO creative-testing structure and a budget-sizing formula, nothing on the Rules engine, A/B/Experiments tool, or holdouts.

---

## Source quality notes

- **Usable sources: 9 of 12.** Below the 8-source comfort line? No, just clears it. But the usable pool is thinner than the headline 12 implies, so treat single-source claims (Leadstio's ad-set-level cost-per-result block; every Marketing Operators holdout claim) as high-value-but-verify, not settled consensus.
- **Freshness:** all retained sources sit inside the 18-month window. No freshness exceptions taken. Mark Builds Brands would have passed freshness but was dropped on scope, not age.
- **Thin sub-areas, stated honestly:**
  - **Holdout / lift / incrementality tests:** one source only (Marketing Operators), and even that is holdout-*adjacent* operator debate, not a lift-test walkthrough. This is the weakest-covered corner of the brain's scope.
  - **Bulk operations and duplication at scale:** near-absent. Diaz mentions duplicating-and-excluding a top performer and Nick Theriot mentions weekly ad-set uploads, but no source walks the bulk-edit/duplication tooling. Do not overstate this area.
  - **API automation of rules:** effectively zero. Every rules source is UI-driven. Consistent with our house note that API automation is light in sources and that our rules run natively in Meta or via server cron, not n8n.
- **Naming drift:** the native A/B/Experiments tool is called "A/B Test" (Tej) and "Intelligence"/"Intelligj" (Marketing Operators). Treat as the same feature family; verify the current in-account label.
