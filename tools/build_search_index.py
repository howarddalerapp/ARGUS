#!/usr/bin/env python3
"""Build a simple search_index.json from selected markdown files.

Usage: python tools/build_search_index.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
FILES = [
    ROOT / 'ARGUS_Project_Plan.md',
    ROOT / 'ARGUS_Security_Plan.md',
    ROOT / 'ARGUS_Network_Architecture.md',
    ROOT / 'ARGUS_Operations_Guide.md',
    ROOT / 'ARGUS_Tracker.md',
    ROOT / 'ARGUS_Transition_Plan.md',
]

def text_from_md(p: Path) -> str:
    text = p.read_text(encoding='utf8')
    # crude strip of code blocks and frontmatter
    import re
    text = re.sub(r'```[\s\S]*?```', ' ', text)
    text = re.sub(r'#+', ' ', text)
    return ' '.join(text.split())[:2000]

def title_from_md(p: Path) -> str:
    for line in p.read_text(encoding='utf8').splitlines():
        line=line.strip()
        if line.startswith('#'):
            return line.lstrip('#').strip()
    return p.stem

def main():
    out = []
    for p in FILES:
        if not p.exists():
            continue
        out.append({
            'id': p.stem.lower().replace('argus_',''),
            'title': title_from_md(p),
            'path': f'/ARGUS/{p.stem.replace("ARGUS_","").lower()}.html',
            'content': text_from_md(p),
        })
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / 'search_index.json').write_text(json.dumps(out, indent=2), encoding='utf8')
    print('Wrote', DOCS / 'search_index.json')

if __name__=='__main__':
    main()
