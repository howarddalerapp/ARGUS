#!/usr/bin/env python3
"""Extract mermaid code blocks from ARGUS_Network_Architecture.md and render SVGs
Requires: npx @mermaid-js/mermaid-cli available (the script will call npx)
Produces: docs/assets/mermaid/diagram-{n}.mmd and diagram-{n}.svg
"""
import re
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / 'ARGUS_Network_Architecture.md'
OUT_DIR = ROOT / 'docs' / 'assets' / 'mermaid'
OUT_DIR.mkdir(parents=True, exist_ok=True)

if not MD.exists():
    print('Source markdown not found:', MD)
    raise SystemExit(1)

text = MD.read_text(encoding='utf8')

# find mermaid code blocks: ```mermaid ... ```
blocks = re.findall(r'```mermaid([\s\S]*?)```', text)
if not blocks:
    print('No mermaid blocks found')
    raise SystemExit(0)

# Check for npx availability
def has_npx():
    try:
        subprocess.run(['npx','--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except Exception:
        return False

if not has_npx():
    print('npx not available on PATH. The script will ONLY write .mmd files by default.')
    print('Mermaid .mmd files were written to', OUT_DIR, 'and can be rendered manually with:')
    print('  npx @mermaid-js/mermaid-cli mmdc -i docs/assets/mermaid/diagram-1.mmd -o docs/assets/mermaid/diagram-1.svg')
    # Write the .mmd files so user can render them elsewhere
    for i, block in enumerate(blocks, start=1):
        mmd = block.strip()
        mmd_path = OUT_DIR / f'diagram-{i}.mmd'
        mmd_path.write_text(mmd, encoding='utf8')
        print('Wrote', mmd_path)
    print('\nIf you want this script to attempt rendering, run:\n  python3 tools/render_mermaid.py --render\n')
    raise SystemExit(0)

import sys
do_render = '--render' in sys.argv

for i, block in enumerate(blocks, start=1):
    mmd = block.strip()
    mmd_path = OUT_DIR / f'diagram-{i}.mmd'
    svg_path = OUT_DIR / f'diagram-{i}.svg'
    mmd_path.write_text(mmd, encoding='utf8')
    print('Wrote', mmd_path)
    if do_render:
        # render using npx mermaid-cli; use --yes to avoid prompts where supported
        cmd = ['npx', '@mermaid-js/mermaid-cli', 'mmdc', '-i', str(mmd_path), '-o', str(svg_path), '--yes']
        print('Running:', ' '.join(cmd))
        try:
            subprocess.run(cmd, check=True)
            print('Rendered', svg_path)
        except subprocess.CalledProcessError as e:
            print('Render failed for', mmd_path, 'error:', e)

print('Done')
