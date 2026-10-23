#!/usr/bin/env python3
"""Download only the pinned Git submodule; never install global plugins or update main."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run',action='store_true')
    args=parser.parse_args()
    lock=json.loads((ROOT/'conductor/conductor.lock.json').read_text())
    path=lock['submodule_path']
    if path != '.agents/plugins/conductor':
        raise ValueError('Unexpected submodule path; inspect the pin before proceeding.')
    entry=subprocess.run(['git','ls-files','--stage','--',path],cwd=ROOT,text=True,capture_output=True,check=True).stdout.split()
    if entry[:2] != ['160000',lock['commit']]:
        raise ValueError('Gitlink and lock disagree; no fetch attempted.')
    commands=[['git','submodule','sync','--',path],['git','submodule','update','--init','--depth','1','--',path]]
    for command in commands:
        print(' '.join(command),flush=True)
        if not args.dry_run:
            subprocess.run(command,cwd=ROOT,check=True,timeout=180)
    if args.dry_run:
        print('Preview only: no network, checkout or installation performed.')
        return 0
    return subprocess.run([sys.executable,'scripts/check_setup.py','--require-submodule'],cwd=ROOT).returncode
if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (OSError,ValueError,subprocess.CalledProcessError,subprocess.TimeoutExpired) as exc:
        print('Bootstrap did not complete: '+str(exc),file=sys.stderr)
        raise SystemExit(1)
