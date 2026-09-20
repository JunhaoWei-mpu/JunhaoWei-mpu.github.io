#!/usr/bin/env bash
set -eu
site_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$site_dir/scripts/preview.py"
