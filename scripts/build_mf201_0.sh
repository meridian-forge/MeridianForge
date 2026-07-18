#!/bin/bash

set -e

PACKAGE="updates/packages/MF-201.0"

echo "======================================"
echo "BUILD MF-201.0 SOURCE DETECTION ENGINE"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/intake" \
"$PACKAGE/files/tests/intake"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-201.0

Source Detection Engine

Adds:
- File scanner
- Source classifier
- Intake models
- Detection tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-201.0

Introduces the first layer of Meridian Forge Intelligence Intake.

Purpose:

Identify incoming investment documents and classify them before extraction.
EOF


cat > "$PACKAGE/files/src/meridianforge/intake/models.py" <<'EOF'
from dataclasses import dataclass
from enum import StrEnum


class SourceCategory(StrEnum):
    UNKNOWN = "UNKNOWN"
    MARKET_LISTING = "MARKET_LISTING"
    TURNKEY_PROVIDER = "TURNKEY_PROVIDER"
    SYNDICATION = "SYNDICATION"
    MANUAL = "MANUAL"


@dataclass
class SourceDetection:
    filename: str
    extension: str
    category: SourceCategory
    confidence: float
EOF


cat > "$PACKAGE/files/src/meridianforge/intake/file_scanner.py" <<'EOF'
from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".xlsx",
    ".xls",
    ".csv",
    ".pdf",
    ".json",
}


def scan_directory(path: str) -> list[Path]:
    directory = Path(path)

    if not directory.exists():
        return []

    return [
        file
        for file in directory.rglob("*")
        if file.is_file()
        and file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
EOF


cat > "$PACKAGE/files/src/meridianforge/intake/source_classifier.py" <<'EOF'
from pathlib import Path

from meridianforge.intake.models import (
    SourceCategory,
    SourceDetection,
)


def classify_file(path: Path) -> SourceDetection:
    name = path.name.lower()

    category = SourceCategory.UNKNOWN
    confidence = 0.50

    if "jwb" in name or "turnkey" in name:
        category = SourceCategory.TURNKEY_PROVIDER
        confidence = 0.90

    elif "syndication" in name or "offering" in name or "om" in name:
        category = SourceCategory.SYNDICATION
        confidence = 0.85

    elif "zillow" in name or "realtor" in name or "listing" in name:
        category = SourceCategory.MARKET_LISTING
        confidence = 0.90

    return SourceDetection(
        filename=path.name,
        extension=path.suffix.lower(),
        category=category,
        confidence=confidence,
    )
EOF


cat > "$PACKAGE/files/src/meridianforge/intake/detector.py" <<'EOF'
from meridianforge.intake.file_scanner import scan_directory
from meridianforge.intake.models import SourceDetection
from meridianforge.intake.source_classifier import classify_file


def detect_sources(path: str) -> list[SourceDetection]:
    files = scan_directory(path)

    return [
        classify_file(file)
        for file in files
    ]
EOF


cat > "$PACKAGE/files/tests/intake/test_file_scanner.py" <<'EOF'
from pathlib import Path

from meridianforge.intake.file_scanner import scan_directory


def test_scan_directory(tmp_path: Path) -> None:
    (tmp_path / "deal.xlsx").touch()
    (tmp_path / "notes.txt").touch()

    results = scan_directory(str(tmp_path))

    assert len(results) == 1
EOF


cat > "$PACKAGE/files/tests/intake/test_source_classifier.py" <<'EOF'
from pathlib import Path

from meridianforge.intake.source_classifier import classify_file
from meridianforge.intake.models import SourceCategory


def test_detect_turnkey_source() -> None:
    result = classify_file(Path("jwb_property.xlsx"))

    assert result.category == SourceCategory.TURNKEY_PROVIDER
EOF


echo
echo "MF-201.0 PACKAGE CREATED"