#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./make_coder_prompt.sh task.md policy_P01.md policy_P02.md ...
#
# This script is intentionally dumb:
# - no inference
# - no rewriting
# - no summarization
# - pure concatenation into a fixed prompt template

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <task_file> <policy_file> [policy_file ...]" >&2
  exit 1
fi

TASK_FILE="$1"
shift
POLICY_FILES=("$@")

if [ ! -f "$TASK_FILE" ]; then
  echo "Task file not found: $TASK_FILE" >&2
  exit 1
fi

for p in "${POLICY_FILES[@]}"; do
  if [ ! -f "$p" ]; then
    echo "Policy file not found: $p" >&2
    exit 1
  fi
done

cat <<'EOF'
You are a code-generation agent.

GLOBAL RULES (NON-NEGOTIABLE):
- Implement exactly and only what is specified in the task.
- Do not invent requirements, structure, or behavior.
- Do not reinterpret policies.
- Do not add files, fields, methods, or logic not explicitly required.
- If something is unclear, do not guess—implement the minimal safe interpretation.
- Produce only code as output. No explanations.

APPLICABLE POLICIES (AUTHORITATIVE, VERBATIM):
EOF

for p in "${POLICY_FILES[@]}"; do
  echo
  echo "----- POLICY: $p -----"
  cat "$p"
done

cat <<'EOF'

TASK (AUTHORITATIVE, DO NOT REWRITE):
EOF

echo
cat "$TASK_FILE"

cat <<'EOF'

END OF INSTRUCTIONS.
EOF
