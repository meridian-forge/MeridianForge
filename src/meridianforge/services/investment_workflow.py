"""
Investment workflow orchestration.

Provides the primary application entry point
for Meridian Forge investment analysis.
"""

from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.results.investment_workflow_result import (
    InvestmentWorkflowResult,
)
from meridianforge.services.investment_pipeline import (
    InvestmentPipeline,
)
from meridianforge.services.report_generation_service import (
    ReportGenerationService,
)


class InvestmentWorkflow:
    """
    Complete Meridian Forge investment workflow.
    """

    def __init__(
        self,
        investment_pipeline: InvestmentPipeline | None = None,
    ) -> None:

        self.pipeline = investment_pipeline or InvestmentPipeline()

    def analyze(
        self,
        records: list[dict[str, object]],
        investor_profile: InvestorProfile,
        asset_type: str = "REAL_ESTATE",
    ) -> InvestmentWorkflowResult:
        """
        Execute complete investment analysis.
        """

        pipeline_result = self.pipeline.analyze(
            records,
            investor_profile,
            asset_type,
        )

        report = ReportGenerationService.generate(
            pipeline_result.ranked_deals,
        )

        return InvestmentWorkflowResult(
            pipeline_result=pipeline_result,
            report=report,
        )
