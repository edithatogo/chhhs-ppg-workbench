#!/usr/bin/env python3
"""Enable this repository's hooks without replacing another hook configuration."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def install(root: Path = ROOT) -> None:
    existing = subprocess.run(['git', 'config', '--get', 'core.hooksPath'], cwd=root,
                              capture_output=True, text=True, check=False)
    if existing.returncode not in (0, 1):
        raise ValueError('Cannot inspect existing hook configuration.')
    if existing.stdout.strip() not in ('', '.githooks'):
        raise ValueError('Existing custom hooksPath retained; integrate both checks explicitly.')
    if not existing.stdout.strip():
        path = subprocess.check_output(['git', 'rev-parse', '--git-path', 'hooks'], cwd=root,
                                       text=True).strip()
        hooks = Path(path) if Path(path).is_absolute() else root / path
        if hooks.exists() and any(p.is_file() and not p.name.endswith('.sample')
                                  for p in hooks.iterdir()):
            raise ValueError('Existing hooks retained; integrate both checks explicitly.')
    for name in ('pre-commit', 'pre-push'):
        path = root / '.githooks' / name
        if not path.is_file() or not path.stat().st_mode & 0o111:
            raise ValueError('Versioned executable hooks are missing.')
    subprocess.run(['git', 'config', '--local', 'core.hooksPath', '.githooks'], cwd=root, check=True)
    actual = subprocess.check_output(['git', 'config', '--local', '--get', 'core.hooksPath'],
                                     cwd=root, text=True).strip()
    if actual != '.githooks':
        raise ValueError('Hook activation readback failed.')


if __name__ == '__main__':
    try:
        install()
        print('Repository pre-commit/pre-push checks enabled; no existing hooks replaced.')
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        raise SystemExit(str(exc))
