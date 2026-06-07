#!/usr/bin/env python3
"""Parse ARGUS_Tracker.md open items and print GitHub issue payloads.

This script is intentionally non-destructive by default. It can be used inside a workflow that
provides a GH_TOKEN to actually POST issues. For safety, the workflow is manual and requires
the `GH_TOKEN` secret to be set.
"""
import re
from pathlib import Path
import json
import requests
import os

ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / 'ARGUS_Tracker.md'

def parse_open_items(md: str):
    # crude parse: find the Open Items table under 'Open Items' or 'Open items'
    m = re.search(r'## Open Items\n\n\|([\s\S]*?)\n\n---', md)
    if not m:
        # fallback: find 'Open Items' section
        m = re.search(r'## Open Items\n\n([\s\S]*)', md)
    tbl = m.group(1) if m else ''
    rows = []
    for line in tbl.splitlines():
        if line.strip().startswith('|') and not line.lower().startswith('| ---'):
            parts = [p.strip() for p in line.strip().split('|')[1:-1]]
            if len(parts)>=4 and parts[0].isdigit():
                rows.append({'num':parts[0],'item':parts[1],'owner':parts[2],'target':parts[3],'status':parts[4] if len(parts)>4 else ''})
    return rows

def main(dry=True):
    md = TRACKER.read_text(encoding='utf8')
    rows = parse_open_items(md)
    if not rows:
        print('No open items found')
        return
    for r in rows:
        title = f"Open Item {r['num']}: {r['item'][:80]}"
        body = f"**Owner:** {r['owner']}\n**Target:** {r['target']}\n**Status:** {r['status']}\n\nFrom ARGUS_Tracker.md"
        print(json.dumps({'title':title,'body':body},ensure_ascii=False))
        if not dry and os.environ.get('GH_TOKEN'):
            repo = os.environ.get('GITHUB_REPOSITORY','howarddalerapp/ARGUS')
            resp = requests.post(f'https://api.github.com/repos/{repo}/issues',json={'title':title,'body':body},headers={'Authorization':f'token {os.environ.get("GH_TOKEN")}'})
            print('created',resp.status_code,resp.json().get('html_url'))

if __name__=='__main__':
    main(dry=True)
