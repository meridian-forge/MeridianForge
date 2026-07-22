from meridianforge.workflow.analysis_pipeline import (
    InvestmentAnalysisPipeline,
)
from meridianforge.workflow.result import WorkflowResult
from meridianforge.workspace.models import OpportunityRecord


class AnalysisRunner:
    """
    Executes Meridian Forge analysis
    against queued opportunities.

    Converts queued opportunities
    into workflow analysis results.
    """

    def __init__(
        self,
        pipeline: InvestmentAnalysisPipeline,
    ) -> None:
        self.pipeline = pipeline

    def run(
        self,
        opportunities: list[OpportunityRecord],
    ) -> list[WorkflowResult]:

        results: list[WorkflowResult] = []

        for opportunity in opportunities:
            result = self.pipeline.analyze(opportunity)
            results.append(result)

        return results
