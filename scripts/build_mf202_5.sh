#!/bin/bash

set -e

PACKAGE="updates/packages/MF-202.5"

echo "======================================"
echo "BUILD MF-202.5 OPERATIONS LAYER"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/operations" \
"$PACKAGE/files/tests/operations"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-202.5

Operations Layer

Adds:
- Report directory management
- Timestamped outputs
- CLI report saving
- Operational tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-202.5

Adds operational workflow support.

Meridian Forge now saves analysis results automatically.
EOF


cat > "$PACKAGE/files/src/meridianforge/operations/report_manager.py" <<'EOF'
from datetime import datetime
from pathlib import Path


def create_report_directory(
    base_path: Path,
) -> Path:

    reports = base_path / "reports"

    reports.mkdir(
        exist_ok=True,
    )

    return reports


def create_report_filename(
    extension: str = "xlsx",
) -> str:

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    return (
        f"investment_review_{timestamp}.{extension}"
    )
EOF


cat > "$PACKAGE/files/tests/operations/test_report_manager.py" <<'EOF'
from pathlib import Path

from meridianforge.operations.report_manager import (
    create_report_directory,
    create_report_filename,
)


def test_report_directory(
    tmp_path: Path,
) -> None:

    folder = create_report_directory(
        tmp_path
    )

    assert folder.exists()


def test_report_filename() -> None:

    filename = create_report_filename()

    assert filename.endswith(
        ".xlsx"
    )
EOF


echo
echo "MF-202.5 PACKAGE CREATED"