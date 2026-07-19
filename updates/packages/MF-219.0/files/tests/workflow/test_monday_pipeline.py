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
