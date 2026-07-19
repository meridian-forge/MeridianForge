#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge MF-213.0"
echo "Monday Analyzer Foundation"
echo "======================================"

ROOT="$(pwd)"

mkdir -p \
src/meridianforge/services \
tests/services \
updates/packages/MF-213.0/files/src/meridianforge/services \
updates/packages/MF-213.0/files/tests/services

cat > src/meridianforge/services/__init__.py <<'PY'
"""Meridian Forge service layer."""
PY

cat > src/meridianforge/services/monday_analyzer.py <<'PY'
from pathlib import Path
from typing import Any, Protocol


class AnalysisPipelineProtocol(Protocol):
    def analyze(self, opportunity: Any) -> Any:
        ...


class ReportBuilderProtocol(Protocol):
    def build(self, results: list[Any]) -> Any:
        ...


class ReportExporterProtocol(Protocol):
    def export_markdown(
        self,
        report: Any,
        output_file: Path,
    ) -> Path:
        ...


class MondayAnalyzer:
    """
    Executes the Monday investment analysis workflow.
    """

    def __init__(
        self,
        analysis_pipeline: AnalysisPipelineProtocol,
        report_builder: ReportBuilderProtocol,
        report_exporter: ReportExporterProtocol,
    ) -> None:
        self.analysis_pipeline = analysis_pipeline
        self.report_builder = report_builder
        self.report_exporter = report_exporter

    def run(
        self,
        opportunities: list[Any],
        output_directory: Path,
    ) -> Path:

        results: list[Any] = []

        for opportunity in opportunities:
            results.append(
                self.analysis_pipeline.analyze(
                    opportunity
                )
            )

        report = self.report_builder.build(results)

        output_file = (
            output_directory /
            "MeridianForge_Weekly_Brief.md"
        )

        return self.report_exporter.export_markdown(
            report,
            output_file,
        )
PY


cat > tests/services/test_monday_analyzer.py <<'PY'
from pathlib import Path

from meridianforge.services.monday_analyzer import (
    MondayAnalyzer,
)


class FakePipeline:
    def analyze(self, opportunity):
        return opportunity


class FakeBuilder:
    def build(self, results):
        return results


class FakeExporter:
    def export_markdown(self, report, output_file):
        return output_file


def test_monday_analyzer_runs(tmp_path: Path) -> None:

    analyzer = MondayAnalyzer(
        FakePipeline(),
        FakeBuilder(),
        FakeExporter(),
    )

    result = analyzer.run(
        ["Property A"],
        tmp_path,
    )

    assert result == (
        tmp_path /
        "MeridianForge_Weekly_Brief.md"
    )
PY


cp src/meridianforge/services/monday_analyzer.py \
updates/packages/MF-213.0/files/src/meridianforge/services/

cp tests/services/test_monday_analyzer.py \
updates/packages/MF-213.0/files/tests/services/


cat > updates/packages/MF-213.0/manifest.txt <<'TXT'
MF-213.0
Monday Analyzer Foundation

Files:
src/meridianforge/services/__init__.py
src/meridianforge/services/monday_analyzer.py
tests/services/test_monday_analyzer.py
TXT


cat > updates/packages/MF-213.0/release_notes.md <<'MD'
# MF-213.0 Monday Analyzer Foundation

Adds the first Monday workflow analysis service.

Capabilities:
- batch opportunity analysis
- report generation orchestration
- markdown export integration
MD


chmod +x scripts/build_mf213_0.sh

echo ""
echo "MF-213.0 build complete"
echo "Run:"
echo "./scripts/quality_gate.sh"
