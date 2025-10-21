#!/bin/bash
# Simple script to run Gnomodoro application

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Add src to PYTHONPATH and run the application
PYTHONPATH="$SCRIPT_DIR/src:$PYTHONPATH" python -m gnomodoro "$@"
