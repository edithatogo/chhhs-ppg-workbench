#!/usr/bin/env python3
"""Publish this committed repository privately using the user's existing gh sign-in."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

from check_publication import check, verify_content_review

ROOT=Path(__file__).resolve().parents[1]

def run(*cmd: str, capture: bool=False, env: dict | None=None) -> str:
    result=subprocess.run(list(cmd),cwd=ROOT,text=True,capture_output=capture,check=True,timeout=180,env=env)
    return result.stdout.strip() if capture else ''

def remote_matches(url: str, repo: str) -> bool:
    return url.removesuffix('.git').lower() in {'https://github.com/'+repo.lower(),'git@github.com:'+repo.lower()}

def verify_push_url(repo: str) -> None:
    urls=run('git','remote','get-url','--push','--all','origin',capture=True).splitlines()
    if len(urls) != 1 or not remote_matches(urls[0], repo):
        raise ValueError('Push destination differs from the reviewed private repository.')

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',default='edithatogo/chhhs-ppg-workbench')
    parser.add_argument('--dry-run',action='store_true')
    parser.add_argument('--content-review',type=Path,help='Private exact-commit confidential-content review receipt required for publication.')
    parser.add_argument('--resume',action='store_true',help='Retry a prior creation/push after verifying the existing origin and private remote.')
    args=parser.parse_args()
    if args.content_review is not None and not args.content_review.is_absolute():
        args.content_review=ROOT/args.content_review
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9._-]+',args.repo):
        raise ValueError('Use an explicit owner/repository name.')
    if not (ROOT/'.git').exists():
        raise ValueError('No local Git metadata. Restore from the supplied bundle first.')
    expected_head=run('git','rev-parse','--verify','HEAD',capture=True)

    if run('git','status','--porcelain',capture=True):
        raise ValueError('Working tree is not clean. Review/commit intended files; never bulk-add operational data.')
    if run('git','branch','--show-current',capture=True) != 'main':
        raise ValueError('Expected main; inspect the branch before publishing.')
    # Security checks also run in dry-run mode and precede every GitHub call.
    check(ROOT, mode='history')
    if not args.dry_run:
        verify_content_review(ROOT, args.content_review, args.repo)
    run(sys.executable,'scripts/check_setup.py')
    origin=None
    remotes=run('git','remote',capture=True).splitlines()
    if 'origin' in remotes:
        origin=run('git','remote','get-url','origin',capture=True)
        if not args.resume or not remote_matches(origin,args.repo):
            raise ValueError('Existing origin: use --resume only for this intended private repository. No changes made.')
    elif args.resume:
        raise ValueError('--resume requires the intended origin already configured; do not guess a remote.')
    if origin:
        verify_push_url(args.repo)
    if args.dry_run:
        print(f'Would verify gh account; create/verify PRIVATE {args.repo}; push main without force.')
        print('Security scan passed. Actual publication also requires --content-review.')
        print('No remote repository, authentication request or push performed.')
        return 0
    if not shutil.which('gh'):
        raise ValueError('GitHub CLI is not installed on this machine.')
    run('gh','auth','status','--hostname','github.com')
    login=run('gh','api','user','--jq','.login',capture=True)
    if login.lower() != args.repo.split('/')[0].lower():
        raise ValueError('Authenticated account is not the requested repository owner. No repository created.')
    if run('git','rev-parse','HEAD',capture=True) != expected_head:
        raise ValueError('HEAD changed after verification; repeat the review/checks.')
    if not origin:
        run('gh','repo','create',args.repo,'--private','--source',str(ROOT),'--remote','origin',
            '--description','Value-first CMO PPG workbench; four bounded MVP tracks; later CareOps integration.')
    remote=json.loads(run('gh','repo','view',args.repo,'--json','nameWithOwner,isPrivate',capture=True))
    if remote.get('nameWithOwner','').lower()!=args.repo.lower() or remote.get('isPrivate') is not True:
        raise ValueError('Remote identity/privacy readback failed. No content pushed.')
    if (run('git','rev-parse','HEAD',capture=True) != expected_head
            or run('git','status','--porcelain',capture=True)):
        raise ValueError('Repository changed after verification; no content pushed.')
    verify_push_url(args.repo)
    verify_content_review(ROOT, args.content_review, args.repo)
    push_env=dict(os.environ, PPG_CONTENT_REVIEW=str(args.content_review.resolve()))
    run('git','push','origin',expected_head+':refs/heads/main',env=push_env)
    local_head=expected_head

    remote_head=run('git','ls-remote','origin','refs/heads/main',capture=True).split()[0]
    if remote_head!=local_head:
        raise ValueError('Push returned but remote HEAD does not match the local commit.')
    print('Verified private remote and main commit: '+args.repo+' '+local_head)
    print('Conductor pin is published; bootstrap its checkout separately if still pending.')
    return 0
if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (OSError,ValueError,subprocess.CalledProcessError,subprocess.TimeoutExpired,IndexError) as exc:
        print('Publication not completed: '+str(exc),file=sys.stderr)
        print('If creation succeeded but push failed, resolve the reported connection issue and retry with --resume.',file=sys.stderr)
        raise SystemExit(1)
