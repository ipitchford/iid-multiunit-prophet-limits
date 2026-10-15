#!/usr/bin/env bash
set -euo pipefail
# Install dependencies separately; never mutates an environment or old logs.
exec "${PYTHON:-python3}" -B "$(dirname "$0")/replay.py" "$@"
