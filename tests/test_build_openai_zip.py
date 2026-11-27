import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class BuildTests(unittest.TestCase):
    def test_rejects_marketplace_version_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('plugin.json', '.claude-plugin', 'skills', 'scripts', 'assets', 'LICENSE'):
                source = ROOT / name
                target = root / name
                if source.is_dir():
                    shutil.copytree(source, target)
                else:
                    shutil.copy2(source, target)
            marketplace = root / '.claude-plugin/marketplace.json'
            data = json.loads(marketplace.read_text())
            data['metadata']['version'] = '0.0.0'
            marketplace.write_text(json.dumps(data))
            result = subprocess.run(['python3', str(root / 'scripts/build-openai-zip.py')], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('marketplace.json', result.stderr)


if __name__ == '__main__':
    unittest.main()
