#!/usr/bin/env python3
"""Open the built homepage through a local HTTP server, without desktop file associations."""
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
if not (SITE / 'index.html').is_file():
    raise SystemExit('请先运行 bundle exec jekyll build。')
url = None
for port in range(4000, 4010):
    candidate = f'http://127.0.0.1:{port}/'
    try:
        with urlopen(candidate, timeout=.5) as response:
            existing = response.read().decode('utf-8')
        if 'Junhao Wei' in existing and 'AcadHomepage' in existing:
            url = candidate
            break
        continue
    except Exception:
        pass
    with socket.socket() as probe:
        try:
            probe.bind(('127.0.0.1', port))
        except OSError:
            continue
    log_path = Path(tempfile.gettempdir()) / 'junhao-homepage-preview.log'
    with log_path.open('a') as log:
        process = subprocess.Popen(
            [sys.executable, '-m', 'http.server', str(port), '--bind', '127.0.0.1', '--directory', str(SITE)],
            stdin=subprocess.DEVNULL, stdout=log, stderr=log, start_new_session=True,
        )
    for _ in range(30):
        try:
            with urlopen(candidate, timeout=.5) as response:
                if response.status == 200:
                    url = candidate
                    break
        except Exception:
            time.sleep(.1)
    if url:
        break
if not url:
    raise SystemExit('本地预览服务未能启动；请检查 4000–4009 端口。')
print('Preview:', url)
if '--no-open' not in sys.argv:
    for name in ['google-chrome', 'chromium', 'chromium-browser', 'firefox']:
        browser = shutil.which(name)
        if browser:
            subprocess.Popen([browser, '--new-window', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            break
