#!/usr/bin/env bash
# Smoke check for brain-meta-troubleshooting-diagnostics.
# Verifies the brain loads (files + frontmatter) and key trigger queries
# map to a playbook rule. Raw transcripts are not shipped with the brain.
# Run: bash scripts/smoke.sh   Exit 0 = pass, 1 = fail.
set -uo pipefail

BRAIN_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$BRAIN_DIR"
FAIL=0

check() { # $1 label, $2 result (0 ok)
  if [ "$2" -eq 0 ]; then echo "ok   $1"; else echo "FAIL $1"; FAIL=1; fi
}

# 1. Required files exist
for f in SKILL.md CHANGELOG.md references/synthesis.md references/quote-library.md \
         references/experts.md; do
  [ -f "$f" ]; check "file: $f" $?
done

# 2. Frontmatter loads: name + description present
grep -q '^name: brain-meta-troubleshooting-diagnostics' SKILL.md
check "frontmatter name" $?
grep -q '^description: >' SKILL.md
check "frontmatter description" $?

# 3. (Raw transcripts are not shipped; no source-count check.)

# 4. At least one worked example session
ls examples/*-session.md >/dev/null 2>&1
check "examples/ has a *-session.md" $?

# 5. Trigger query -> playbook rule mapping (spot checks)
grep -q 'IF an ad set is not spending THEN' SKILL.md
check "trigger 'ad set not spending' maps to non-delivery ladder" $?
grep -q 'IF the dashboard shows zero results THEN' SKILL.md
check "trigger 'zero results' maps to date/draft/payment/blocker checks" $?
grep -q 'IF CPM/CPL spiked THEN check relevance' SKILL.md
check "trigger 'CPM spiked' maps to relevance-before-Meta rule" $?
grep -q 'IF Ads Manager disagrees with the CRM THEN test every event live' SKILL.md
check "trigger 'Ads Manager vs CRM' maps to event-test rule" $?
grep -q "IF you're tempted to edit a live ad set THEN don't" SKILL.md
check "trigger 'want to edit live ad' maps to learning-phase rule" $?

# 6. Fabrication guard: every quote in the library and examples must be a
#    normalised substring of a mined transcript when transcripts are present locally (ellipsis segments checked
#    independently).
python3 - <<'EOF'
import glob, re, sys

def norm(s):
    s = s.replace('’', "'").replace('‘', "'")
    s = s.replace('“', '"').replace('”', '"')
    return re.sub(r'[^A-Za-z0-9]+', ' ', s).lower().strip()

blob = ' '.join(norm(open(f, encoding='utf-8', errors='replace').read())
                for f in glob.glob('sources/*.txt'))
if not blob.strip():
    print('quote check skipped: raw transcripts are not shipped with this brain')
    sys.exit(0)

quote_files = ['references/quote-library.md'] + sorted(glob.glob('examples/*.md'))
quotes = []
for path in quote_files:
    text = open(path, encoding='utf-8').read()
    text = text.replace('“', '"').replace('”', '"')
    for m in re.finditer(r'"([^"]+)"', text):
        q = m.group(1).strip()
        if len(q.split()) >= 5:
            quotes.append((path, q))

bad = []
for path, q in quotes:
    segs = [s for s in re.split(r'\.\.\.|…', q) if len(s.split()) >= 4]
    if not segs:
        continue
    if not all(norm(s) in blob for s in segs):
        bad.append((path, q))

print(f"quotes checked: {len(quotes)}")
for path, q in bad:
    print(f"FAIL quote not in sources ({path}): {q[:90]}")
sys.exit(1 if bad else 0)
EOF
check "all quotes trace to transcripts (skipped when none are present)" $?

echo
if [ "$FAIL" -eq 0 ]; then echo "SMOKE PASS"; else echo "SMOKE FAIL"; exit 1; fi
