#!/bin/bash

set -e

PACKAGE="updates/packages/MF-202.2"

echo "======================================"
echo "BUILD MF-202.2 REPORT GENERATOR"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/reporting" \
"$PACKAGE/files/tests/reporting"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-202.2

Report Generator

Adds:
- Report models
- Text reporting
- Ranking summaries
- Report tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-202.2

Creates the first human-readable Meridian Forge investment report.

Purpose:

Convert analysis output into actionable review summaries.
EOF


cat > "$PACKAGE/files/src/meridianforge/reporting/models.py" <<'EOF'
from dataclasses import dataclass


@dataclass
class Report:

    title: str

    content: str
EOF


cat > "$PACKAGE/files/src/meridianforge/reporting/text_report.py" <<'EOF'
from meridianforge.ranking.models import RankingResult
from meridianforge.reporting.models import Report


def generate_text_report(
    rankings: list[RankingResult],
) -> Report:

    lines: list[str] = []

    lines.append(
        "Meridian Forge Investment Review"
    )

    lines.append(
        "================================"
    )


    for item in rankings:

        lines.append(
            (
                f"#{item.rank} "
                f"{item.opportunity_file} "
                f"- Score: {item.score:.1f}"
            )
        )


    return Report(
        title="Investment Review",
        content="\n".join(lines),
    )
EOF


cat > "$PACKAGE/files/tests/reporting/test_text_report.py" <<'EOF'
from meridianforge.ranking.models import RankingResult
from meridianforge.reporting.text_report import (
    generate_text_report,
)


def test_generate_report() -> None:

    rankings = [
        RankingResult(
            opportunity_file="property.xlsx",
            score=85,
            rank=1,
        )
    ]


    report = generate_text_report(
        rankings
    )


    assert (
        "property.xlsx"
        in report.content
    )
EOF


echo
echo "MF-202.2 PACKAGE CREATED"