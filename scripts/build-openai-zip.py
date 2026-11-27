#!/usr/bin/env python3
"""Build an allowlisted portable plugin ZIP from any working directory."""
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parent.parent
FILES = ('plugin.json', 'skills/momentum/SKILL.md', 'assets/icon.png', 'LICENSE')


def main():
    manifest = json.loads((ROOT / 'plugin.json').read_text())
    skill = (ROOT / 'skills/momentum/SKILL.md').read_text()
    version = re.search(r'^version: (.+)$', skill, re.MULTILINE).group(1)
    for path in ('plugin.json', '.claude-plugin/plugin.json'):
        if json.loads((ROOT / path).read_text())['version'] != version:
            raise ValueError(f'{path} version must match skill {version}')
    if manifest['$schema'] != 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json':
        raise ValueError('Expected portable plugin schema')
    interface = manifest['extensions']['com.openai']['interface']
    for key in ('logo', 'composerIcon'):
        if interface[key].removeprefix('./') not in FILES:
            raise ValueError(f'{key} is not in ZIP allowlist')
    output = ROOT / 'dist/momentum-openai-plugin.zip'
    output.parent.mkdir(exist_ok=True)
    with ZipFile(output, 'w', compression=ZIP_DEFLATED) as archive:
        for name in FILES:
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (ROOT / name).read_bytes())
    print(output)


if __name__ == '__main__':
    main()
