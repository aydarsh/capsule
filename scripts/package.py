#!/usr/bin/env python3
"""Validate the distributable skill and build a ZIP using only Python stdlib."""
import argparse
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'capsule-travel'


def validate():
    entry = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    assert entry.startswith('---\n'), 'Missing frontmatter'
    header = entry.split('---', 2)[1]
    assert re.search(r'^name: capsule-travel$', header, re.M), 'Skill name mismatch'
    assert re.search(r'^description: .+', header, re.M), 'Missing description'
    manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
    assert manifest['name'] == 'capsule'
    assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
    for document in SKILL.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', document.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            resolved = (document.parent / target.split('#')[0]).resolve()
            assert resolved.is_relative_to(SKILL.resolve()), f'Non-portable reference: {target}'
            assert resolved.is_file(), f'Missing reference: {target}'
    files = sorted(p for p in SKILL.rglob('*') if p.is_file())
    assert all(not p.is_symlink() for p in files), 'Package must be self-contained'
    assert all(p.suffix in {'.md', '.yaml'} for p in files), 'Unexpected skill asset'
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    files = validate()
    print(f'Package validated: {len(files)} skill files')
    if args.check:
        return
    output = ROOT / 'dist' / 'capsule-travel.zip'
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, str(Path(SKILL.name) / path.relative_to(SKILL)))
        archive.write(ROOT / 'LICENSE', 'capsule-travel/LICENSE')
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert 'capsule-travel/SKILL.md' in archive.namelist()
    print(output)


if __name__ == '__main__':
    main()
