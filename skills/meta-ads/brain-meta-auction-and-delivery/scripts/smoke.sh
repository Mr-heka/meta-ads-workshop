#!/usr/bin/env bash
# Smoke check for brain-meta-auction-and-delivery.
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
grep -q '^name: brain-meta-auction-and-delivery' SKILL.md
check "frontmatter name" $?
grep -q '^description:' SKILL.md
check "frontmatter description" $?

# 3. (Raw transcripts are not shipped; no source-count check.)

# 4. At least one worked example session
ls examples/*-session.md >/dev/null 2>&1
check "examples/ has a *-session.md" $?

# 5. Trigger query -> playbook rule mapping (spot checks)
grep -q 'IF an ad set spends nothing THEN' SKILL.md
check "trigger 'ad set not spending' maps to AdAmigo ladder rule" $?
grep -q 'IF CPL rises on a running winner THEN' SKILL.md
check "trigger 'CPL rose' maps to rotate-beside-winner rule" $?
grep -q 'IF frequency passes ~2 on cold THEN' SKILL.md
check "trigger 'frequency too high' maps to frequency rule" $?
grep -q 'IF a campaign is under 7 days old and soft THEN do nothing' SKILL.md
check "trigger 'week-one dip' maps to settle-window rule" $?

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
