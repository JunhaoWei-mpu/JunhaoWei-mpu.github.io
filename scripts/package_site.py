#!/usr/bin/env python3
"""Package the verified Jekyll source and built static site separately."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIRS = ['_data', '_includes', '_layouts', '_pages', '_sass', 'assets', '.github', 'scripts', 'docs']
SOURCE_FILES = ['_config.yml', '.gitignore', 'Gemfile', 'Gemfile.lock', 'LICENSE', 'README.md', 'TEMPLATE.md', 'run_server.sh', '打开主页.sh']

with zipfile.ZipFile(ROOT / 'homepage-source.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    for name in SOURCE_FILES:
        path = ROOT / name
        if path.is_file():
            archive.write(path, name)
    for name in SOURCE_DIRS:
        for path in (ROOT / name).rglob('*'):
            if path.is_file() and '__pycache__' not in path.parts:
                archive.write(path, path.relative_to(ROOT))

assert (ROOT / '_site/index.html').is_file(), 'Run Jekyll build before packaging'
with zipfile.ZipFile(ROOT / 'homepage-ready.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    for path in (ROOT / '_site').rglob('*'):
        if path.is_file():
            archive.write(path, path.relative_to(ROOT / '_site'))
    archive.writestr('.nojekyll', '')
    archive.write(ROOT / 'LICENSE', 'LICENSE')
    archive.write(ROOT / 'TEMPLATE.md', 'TEMPLATE.md')
print('Created homepage-source.zip (Jekyll source) and homepage-ready.zip (built static site).')
