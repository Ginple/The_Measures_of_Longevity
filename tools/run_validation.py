"""Compatibility entry point for the repository's single validation contract.

The validator prints a current receipt without overwriting historical receipts.
Optional source/history checks remain separate and are not implied by this run.
"""
from pathlib import Path
import subprocess
import sys

P = Path(__file__).resolve().parents[1]

if __name__ == '__main__':
    raise SystemExit(subprocess.call([sys.executable, str(P/'scripts/run_validation.py'), *sys.argv[1:]], cwd=P))
