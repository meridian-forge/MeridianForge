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

    assert result == (tmp_path / "MeridianForge_Weekly_Brief.md")
