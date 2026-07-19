from meridianforge.workflow.analysis_pipeline import (
    InvestmentAnalysisPipeline,
)
from meridianforge.workflow.result import AnalysisResult
from meridianforge.workspace.models import OpportunityRecord


class AnalysisRunner:
    """
    Executes Meridian Forge analysis
    against queued opportunities.

    Converts a queue of opportunities
    into analyzed investment results.
    """

    def __init__(
        self,
        pipeline: InvestmentAnalysisPipeline,
    ) -> None:
        self.pipeline = pipeline

    def run(
        self,
        opportunities: list[OpportunityRecord],
    ) -> list[AnalysisResult]:

        results: list[AnalysisResult] = []

        for opportunity in opportunities:
            result = self.pipeline.analyze(opportunity)
            results.append(result)

        return results
