"""Run the technical device test suite without external dependencies."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tests", default="tests")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", args.tests, "-p", "test_*.py", "-v"],
        cwd=root,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())

