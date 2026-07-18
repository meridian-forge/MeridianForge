#!/bin/bash

set -e

PACKAGE="updates/packages/MF-202.4"

echo "======================================"
echo "BUILD MF-202.4 EXCEL REPORT EXPORT"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/reporting" \
"$PACKAGE/files/tests/reporting"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-202.4

Excel Report Export

Adds:
- XLSX reporting
- Ranking worksheet
- Export tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-202.4

Adds Excel output for Meridian Forge reports.

Purpose:

Provide investment review files for weekly analysis.
EOF


cat > "$PACKAGE/files/src/meridianforge/reporting/excel_report.py" <<'EOF'
from pathlib import Path

from openpyxl import Workbook

from meridianforge.ranking.models import RankingResult


def export_excel_report(
    rankings: list[RankingResult],
    output_path: Path,
) -> None:

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Rankings"


    sheet.append(
        [
            "Rank",
            "Opportunity",
            "Score",
        ]
    )


    for item in rankings:

        sheet.append(
            [
                item.rank,
                item.opportunity_file,
                item.score,
            ]
        )


    workbook.save(
        output_path
    )
EOF


cat > "$PACKAGE/files/tests/reporting/test_excel_report.py" <<'EOF'
from pathlib import Path

from openpyxl import load_workbook

from meridianforge.ranking.models import RankingResult
from meridianforge.reporting.excel_report import (
    export_excel_report,
)


def test_excel_export(
    tmp_path: Path,
) -> None:

    output = (
        tmp_path
        / "results.xlsx"
    )


    rankings = [
        RankingResult(
            opportunity_file="deal.xlsx",
            score=90,
            rank=1,
        )
    ]


    export_excel_report(
        rankings,
        output,
    )


    workbook = load_workbook(
        output
    )

    sheet = workbook["Rankings"]


    assert sheet["B2"].value == "deal.xlsx"
EOF


echo
echo "MF-202.4 PACKAGE CREATED"