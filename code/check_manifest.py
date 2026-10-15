"""Check every shipped file against MANIFEST.sha256, excluding Git/build caches."""
import hashlib
from pathlib import Path

root = Path(__file__).resolve().parent.parent
expected = {}
for line in (root / 'MANIFEST.sha256').read_text().splitlines():
    digest, name = line.split('  ', 1)
    relative = Path(name)
    if relative.is_absolute() or '..' in relative.parts or name in expected:
        raise RuntimeError('Unsafe or duplicate manifest path')
    expected[name] = digest
actual = {}
for path in root.rglob('*'):
    rel = path.relative_to(root)
    if '.git' in rel.parts or '__pycache__' in rel.parts:
        continue
    if path.is_symlink():
        raise RuntimeError(f'Symlink forbidden: {rel}')
    if path.is_file() and str(rel) != 'MANIFEST.sha256':
        actual[str(rel)] = hashlib.sha256(path.read_bytes()).hexdigest()
if actual != expected:
    raise RuntimeError('Manifest differs: ' + repr(sorted(set(actual) ^ set(expected))) +
                       '; mismatches=' + repr([p for p in actual if p in expected and actual[p] != expected[p]]))
print(f'PASS: {len(expected)} manifest entries; no unlisted payload files')
