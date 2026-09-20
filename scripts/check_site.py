#!/usr/bin/env python3
"""Check that the published artifact contains the intended homepage, not source/private files."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.assets = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in {'script', 'img', 'link'}:
            url = attrs.get('src') or attrs.get('href')
            if url:
                self.assets.append(url)

    def handle_data(self, text):
        self.text.append(text)


page = Page()
source = (SITE / 'index.html').read_text()
page.feed(source)
text = ' '.join(page.text)
for section in ['about-me', 'news', 'publications', 'honors', 'education', 'services']:
    assert section in page.ids, f'Missing section: {section}'
for link in page.links:
    if link.startswith('#'):
        assert link[1:] in page.ids, f'Broken anchor: {link}'
for asset in page.assets:
    if not urlparse(asset).scheme:
        # relative_url may include a project base path; the assets tree is stable.
        path = unquote(urlparse(asset).path)
        if '/assets/' in path:
            path = 'assets/' + path.split('/assets/', 1)[1]
        assert (SITE / path.lstrip('/')).is_file(), f'Missing asset: {asset}'
papers = json.loads((ROOT / '_data/publications.json').read_text())
for paper in papers:
    assert paper['title'] in text, f'Missing publication: {paper["title"]}'
assert 'Curriculum Vitae' not in text and '魏俊豪' not in text
assert 'Lorem ipsum' not in text and 'YOUR_GOOGLE_SCHOLAR_ID' not in source
for private_path in ['简历', '照片', 'Gemfile', '_config.yml', 'scripts', 'vendor', 'homepage-ready.zip', 'homepage-source.zip']:
    assert not (SITE / private_path).exists(), f'Source/private file in public output: {private_path}'
assert not list(SITE.rglob('*.pdf')), 'The public site must not contain the CV'
print(f'OK: {len(papers)} publications, all navigation targets and assets, no CV or private/source files.')
