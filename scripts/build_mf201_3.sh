#!/bin/bash

set -e

PACKAGE="updates/packages/MF-201.3"

echo "======================================"
echo "BUILD MF-201.3 INTAKE PIPELINE ORCHESTRATOR"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/intake" \
"$PACKAGE/files/tests/intake"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-201.3

Intake Pipeline Orchestrator

Adds:
- File processing workflow
- Folder processing workflow
- Intake pipeline tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-201.3

Connects detection, extraction, and normalization.

Creates the first end-to-end intake workflow.
EOF


cat > "$PACKAGE/files/src/meridianforge/intake/pipeline.py" <<'EOF'
from pathlib import Path

from meridianforge.intake.detector import detect_sources
from meridianforge.intake.extractors.registry import get_extractor
from meridianforge.opportunity.models import Opportunity
from meridianforge.opportunity.normalizer import normalize


def process_file(
    file_path: Path,
) -> Opportunity:

    extractor = get_extractor(file_path)

    extracted = extractor.extract(file_path)

    return normalize(extracted)


def process_folder(
    folder_path: str,
) -> list[Opportunity]:

    detections = detect_sources(folder_path)

    opportunities: list[Opportunity] = []

    for detection in detections:

        opportunity = process_file(
            Path(detection.filename)
        )

        opportunities.append(
            opportunity
        )

    return opportunities
EOF


cat > "$PACKAGE/files/tests/intake/test_pipeline.py" <<'EOF'
from pathlib import Path

from openpyxl import Workbook

from meridianforge.intake.pipeline import process_file
from meridianforge.opportunity.models import OpportunityType


def test_process_file(tmp_path: Path) -> None:

    file_path = tmp_path / "property.xlsx"

    workbook = Workbook()

    sheet = workbook.active

    sheet.append(
        [
            "Purchase Price",
            "250000",
        ]
    )

    workbook.save(file_path)

    result = process_file(file_path)

    assert (
        result.opportunity_type
        == OpportunityType.RENTAL_PROPERTY
    )
EOF


echo
echo "MF-201.3 PACKAGE CREATED"