"""
Analysis workflow orchestration.

Coordinates import, normalization, and investment analysis.
"""

from meridianforge.models.results.analysis_workflow_result import (
    AnalysisWorkflowResult,
)
from meridianforge.services.import_execution_service import (
    ImportExecutionService,
)


class AnalysisWorkflow:
    """
    End-to-end investment analysis workflow.
    """

    def __init__(
        self,
        import_service: ImportExecutionService | None = None,
    ) -> None:

        self.import_service = import_service or ImportExecutionService()

    def analyze_records(
        self,
        records: list[dict[str, object]],
        asset_type: str = "UNKNOWN",
    ) -> AnalysisWorkflowResult:
        """
        Analyze imported records.
        """

        import_result = self.import_service.execute(
            records,
            asset_type,
        )

        ranked_results = import_result.assets

        return AnalysisWorkflowResult(
            assets_analyzed=len(ranked_results),
            ranked_results=ranked_results,
            import_quality=(import_result.quality_report),
        )
