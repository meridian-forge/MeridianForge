#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge MF-219.0"
echo "Monday Workflow Integration"
echo "======================================"

mkdir -p \
src/meridianforge/workflow \
tests/workflow \
updates/packages/MF-219.0/files/src/meridianforge/workflow \
updates/packages/MF-219.0/files/tests/workflow


cat > src/meridianforge/workflow/monday_pipeline.py <<'PY'
from pathlib import Path
from typing import Any, Protocol


class RepositoryProtocol(Protocol):
    def get_all(self) -> list[Any]:
        ...


class BatchAnalyzerProtocol(Protocol):
    def analyze_all(self) -> list[Any]:
        ...


class RankingProtocol(Protocol):
    def rank(self, opportunities: list[Any]) -> list[Any]:
        ...


class SummaryProtocol(Protocol):
    def summarize(
        self,
        opportunities: list[Any],
    ) -> dict[str, Any]:
        ...


class DashboardProtocol(Protocol):
    def generate(
        self,
        summary: dict[str, Any],
    ) -> str:
        ...


class MondayPipeline:
    """
    End-to-end Monday morning analysis workflow.
    """

    def __init__(
        self,
        repository: RepositoryProtocol,
        analyzer: BatchAnalyzerProtocol,
        ranking: RankingProtocol,
        summary: SummaryProtocol,
        dashboard: DashboardProtocol,
    ) -> None:
        self.repository = repository
        self.analyzer = analyzer
        self.ranking = ranking
        self.summary = summary
        self.dashboard = dashboard

    def run(
        self,
        output_file: Path,
    ) -> Path:

        analyzed = self.analyzer.analyze_all()

        ranked = self.ranking.rank(
            analyzed
        )

        summary = self.summary.summarize(
            ranked
        )

        dashboard = self.dashboard.generate(
            summary
        )

        output_file.write_text(
            dashboard,
            encoding="utf-8",
        )

        return output_file
PY


cat > tests/workflow/test_monday_pipeline.py <<'PY'
from pathlib import Path

from meridianforge.workflow.monday_pipeline import (
    MondayPipeline,
)


class FakeAnalyzer:

    def analyze_all(self):
        return [
            {
                "name": "Property A",
                "score": 95,
            }
        ]


class FakeRepository:

    def get_all(self):
        return []


class FakeRanking:

    def rank(self, opportunities):
        return opportunities


class FakeSummary:

    def summarize(self, opportunities):
        return {
            "total_opportunities": len(opportunities)
        }


class FakeDashboard:

    def generate(self, summary):
        return "Monday Dashboard"


def test_monday_pipeline(tmp_path: Path) -> None:

    output = (
        tmp_path /
        "dashboard.md"
    )

    pipeline = MondayPipeline(
        FakeRepository(),
        FakeAnalyzer(),
        FakeRanking(),
        FakeSummary(),
        FakeDashboard(),
    )

    result = pipeline.run(
        output
    )

    assert result.exists()
    assert result.read_text() == "Monday Dashboard"
PY


cp src/meridianforge/workflow/monday_pipeline.py \
updates/packages/MF-219.0/files/src/meridianforge/workflow/


cp tests/workflow/test_monday_pipeline.py \
updates/packages/MF-219.0/files/tests/workflow/


cat > updates/packages/MF-219.0/manifest.txt <<'TXT'
MF-219.0
Monday Workflow Integration

Files:
src/meridianforge/workflow/monday_pipeline.py
tests/workflow/test_monday_pipeline.py
TXT


cat > updates/packages/MF-219.0/release_notes.md <<'MD'
# MF-219.0 Monday Workflow Integration

Connects the complete Monday morning workflow.

Flow:
Repository
-> Batch Analysis
-> Ranking
-> Summary
-> Dashboard

Prepares Meridian Forge for first usable MVP workflow.
MD


chmod +x scripts/build_mf219_0.sh

echo ""
echo "MF-219.0 build complete"
echo "Run ./scripts/quality_gate.sh"
