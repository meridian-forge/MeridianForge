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
