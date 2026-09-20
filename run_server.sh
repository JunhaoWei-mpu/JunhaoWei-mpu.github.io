#!/usr/bin/env bash
set -eu
site_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$site_dir"
if command -v bundle >/dev/null 2>&1; then
  bundle_cmd="$(command -v bundle)"
else
  bundle_cmd="$(ruby -r rubygems -e 'print Gem.user_dir')/bin/bundle"
fi
if [ ! -x "$bundle_cmd" ]; then
  printf '%s\n' '请先安装 Bundler：gem install --user-install bundler'
  exit 1
fi
exec "$bundle_cmd" exec jekyll serve --host 127.0.0.1 --port 4000 --livereload
