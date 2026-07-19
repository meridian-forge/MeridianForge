from typing import Any, Protocol


class AnalysisPipelineProtocol(Protocol):
    def analyze(
        self,
        opportunity: Any,
    ) -> Any:
        ...


class OpportunityRepositoryProtocol(Protocol):
    def get_all(
        self,
    ) -> list[Any]:
        ...


class BatchAnalysisEngine:
    """
    Executes analysis across multiple opportunities.

    Connects the opportunity repository with
    the Meridian Forge analysis pipeline.
    """

    def __init__(
        self,
        repository: OpportunityRepositoryProtocol,
        pipeline: AnalysisPipelineProtocol,
    ) -> None:
        self.repository = repository
        self.pipeline = pipeline

    def analyze_all(
        self,
    ) -> list[Any]:
        results: list[Any] = []

        opportunities = (
            self.repository.get_all()
        )

        for opportunity in opportunities:
            results.append(
                self.pipeline.analyze(
                    opportunity
                )
            )

        return results
