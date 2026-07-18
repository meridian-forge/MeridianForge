#!/bin/bash

set -e

PACKAGE="updates/packages/MF-202.3"

echo "======================================"
echo "BUILD MF-202.3 CLI RUNNER"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/cli" \
"$PACKAGE/files/tests/cli"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-202.3

CLI Runner

Adds:
- Command line interface
- Analyze command
- Folder processing
- CLI tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-202.3

Creates the first Meridian Forge user workflow.

Command:

meridianforge analyze <folder>
EOF


cat > "$PACKAGE/files/src/meridianforge/cli/main.py" <<'EOF'
import argparse
from pathlib import Path

from meridianforge.intake.pipeline import process_folder
from meridianforge.analysis.analyzer import analyze
from meridianforge.ranking.engine import rank
from meridianforge.reporting.text_report import (
    generate_text_report,
)


def run_analyze(
    folder: str,
) -> None:

    opportunities = process_folder(
        folder
    )

    results = [
        analyze(item)
        for item in opportunities
    ]

    rankings = rank(
        results
    )

    report = generate_text_report(
        rankings
    )

    print(
        report.content
    )


def main() -> None:

    parser = argparse.ArgumentParser(
        prog="meridianforge",
    )

    subparsers = parser.add_subparsers(
        dest="command",
    )


    analyze_parser = subparsers.add_parser(
        "analyze",
    )

    analyze_parser.add_argument(
        "folder",
    )


    args = parser.parse_args()


    if args.command == "analyze":

        run_analyze(
            args.folder
        )


if __name__ == "__main__":

    main()
EOF


cat > "$PACKAGE/files/tests/cli/test_cli.py" <<'EOF'
from meridianforge.cli.main import main


def test_cli_import() -> None:

    assert main is not None
EOF


echo
echo "MF-202.3 PACKAGE CREATED"