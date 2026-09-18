#!/usr/bin/env bash
# Smoke test for brain-meta-attribution-truth.
# Run after any edit: bash scripts/smoke.sh
# Checks (1) the trigger description still answers the canonical questions,
# (2) the load-bearing sections exist, (3) the cross-referenced sibling brains
# actually exist at their paths, (4) every quote in the quote library is still a
# verbatim (normalised) substring of a mined transcript, when transcripts are present locally.
set -u
BRAIN_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$(cd "$BRAIN_DIR/.." && pwd)"
FAIL=0

# 1. Canonical trigger phrases must survive in the SKILL.md description.
for phrase in \
  "why does Meta show more purchases than my dashboard" \
  "what attribution window should I use" \
  "should I turn view-through" \
  "is my ROAS real" \
  "what is incremental attribution" \
  "7-day click or 1-day view" ; do
  if ! grep -qi "$phrase" "$BRAIN_DIR/SKILL.md"; then
    echo "FAIL trigger phrase missing from SKILL.md: $phrase"
    FAIL=1
  fi
done

# 2. Load-bearing sections must exist.
for section in \
  "## How to use this brain" \
  "## What the experts agree on" \
  "## Execution playbook" \
  "## Pairs with / boundaries" ; do
  if ! grep -qF "$section" "$BRAIN_DIR/SKILL.md"; then
    echo "FAIL section missing from SKILL.md: $section"
    FAIL=1
  fi
done

# 3. Cross-referenced sibling brains must exist at their paths, so broken
#    Pairs-with / Related-brains links get caught here rather than at runtime.
for sibling in \
  "brain-meta-attribution-measurement-deep" \
  "brain-meta-ads-manual-control-no-advantage" ; do
  if ! grep -q "$sibling" "$BRAIN_DIR/SKILL.md"; then
    echo "FAIL sibling brain no longer referenced in SKILL.md: $sibling"
    FAIL=1
  elif [ ! -f "$SKILLS_DIR/$sibling/SKILL.md" ]; then
    echo "FAIL referenced sibling brain missing on disk: $sibling"
    FAIL=1
  fi
done

# 4. Every blockquote in the quote library must be a normalised substring
#    of at least one transcript (ellipsis splits each quote into fragments,
#    every fragment must match).
python3 - "$BRAIN_DIR" <<'EOF' || FAIL=1
import re, sys, glob, os
brain = sys.argv[1]
def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()
corpus = [norm(open(f, encoding='utf-8', errors='replace').read())
          for f in glob.glob(os.path.join(brain, 'sources', '*.txt'))]
if not corpus:
    print('quote check skipped: raw transcripts are not shipped with this brain')
    sys.exit(0)
lib = open(os.path.join(brain, 'references', 'quote-library.md'), encoding='utf-8').read()
quotes = re.findall(r'^> "(.+?)" -', lib, re.M | re.S)
bad = 0
for q in quotes:
    frags = [f for f in re.split(r'\.\.\.|…', q) if norm(f)]
    if not all(any(norm(f) in t for t in corpus) for f in frags):
        print(f'FAIL quote not verbatim in any transcript: "{q[:80]}..."')
        bad += 1
print(f'quote check: {len(quotes)} quotes, {len(quotes)-bad} verbatim, {bad} failed')
sys.exit(1 if bad else 0)
EOF

if [ "$FAIL" -ne 0 ]; then
  echo "SMOKE: FAIL"
  exit 1
fi
echo "SMOKE: PASS"
