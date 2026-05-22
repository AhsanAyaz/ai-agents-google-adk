#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check for Python 3.11+
if ! python3 -c 'import sys; exit(0 if sys.version_info >= (3, 11) else 1)'; then
  echo "Error: Python 3.11+ is required for Google ADK 2.0.0."
  exit 1
fi

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env — fill in your GOOGLE_API_KEY before running."
fi

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip -q
pip install -r requirements.txt

echo ""
echo "Setup complete. Activate with: source agentspan_demo/.venv/bin/activate"
