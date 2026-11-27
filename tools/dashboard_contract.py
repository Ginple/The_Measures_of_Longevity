"""Structural checks for the requested static dashboard, not content certification."""
from html.parser import HTMLParser
from pathlib import Path

DASHBOARDS = ('STATE_DASHBOARD.HTML', 'STATE_DASHBOARD.html')
EXCLUDED_DIRS = {'.git', '.venv', 'venv', '__pycache__', 'build', 'dist', 'node_modules', '.pytest_cache'}


class DashboardParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = set()
        self.ids = set()
        self.fragments = []
        self.errors = []
        self.in_title = False
        self.title = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.add(tag)
        if tag == 'title':
            self.in_title = True
        if attrs.get('id'):
            if attrs['id'] in self.ids:
                self.errors.append('duplicate id: ' + attrs['id'])
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href', '').startswith('#'):
            self.fragments.append(attrs['href'][1:])
        # Links to sources can be remote; rendering assets must remain embedded.
        if tag in ('script', 'img', 'iframe', 'audio', 'video', 'source') and attrs.get('src'):
            if not attrs['src'].startswith('data:'):
                self.errors.append('external rendering asset: ' + attrs['src'])
        if tag == 'link' and 'stylesheet' in attrs.get('rel', '').lower().split():
            self.errors.append('external stylesheet: ' + attrs.get('href', ''))

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def check_dashboard(root):
    root = Path(root)
    errors = []
    for path in root.rglob('*'):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if path.is_file() and path.suffix.lower() in ('.html', '.htm') and rel.as_posix() not in DASHBOARDS:
            errors.append('unauthorized HTML: ' + rel.as_posix())
    contents = []
    for name in DASHBOARDS:
        path = root / name
        if not path.is_file():
            errors.append('missing dashboard: ' + name)
            continue
        try:
            contents.append(path.read_bytes())
        except OSError as exc:
            errors.append(f'unreadable dashboard: {name}: {exc}')
    if len(contents) != len(DASHBOARDS):
        return errors
    if (root / DASHBOARDS[0]).samefile(root / DASHBOARDS[1]):
        errors.append('dashboard paths do not refer to distinct files')
    if contents[0] != contents[1]:
        errors.append('dashboard copies differ')
    try:
        text = contents[0].decode('utf-8')
    except UnicodeDecodeError:
        return errors + ['dashboard is not UTF-8']
    parser = DashboardParser()
    parser.feed(text)
    parser.close()
    errors.extend(parser.errors)
    if not {'html', 'head', 'title', 'body', 'main', 'style'} <= parser.tags:
        errors.append('missing required page structure')
    if not parser.title.strip() or not text.lstrip().lower().startswith('<!doctype html>'):
        errors.append('missing title or HTML doctype')
    errors.extend('missing anchor: ' + frag for frag in parser.fragments if frag and frag not in parser.ids)
    return errors
