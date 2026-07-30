"""
Monday execution pipeline.

MF-505.1

End-to-end orchestration for the MeridianForge Monday workflow.
For now, this wraps the existing OperationsService so the CLI can
transition to a workflow layer without breaking the current
production pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.operations import OperationsRunResult
from meridianforge.portfolio.analysis import PortfolioAnalysisResult
from meridianforge.portfolio.intelligence.package import (
    InvestorDecisionPackage,
)
from meridianforge.services.operations_service import OperationsService


@dataclass(slots=True)
class MondayPipelineResult:
    """
    Result of the Monday execution pipeline.
    """

    operations: OperationsRunResult
    portfolio_analysis: PortfolioAnalysisResult
    intelligence: InvestorDecisionPackage | None
    dashboard_path: Path | None


class MondayExecutionPipeline:
    """
    Workflow-layer wrapper around the current Monday operations flow.
    """

    def __init__(
        self,
        deals_directory: Path,
    ) -> None:
        self.deals_directory = deals_directory
        self.operations = OperationsService(
            deals_directory=deals_directory,
        )

    def execute(
        self,
    ) -> MondayPipelineResult:
        operations_result = self.operations.execute()

        analysis = PortfolioAnalysisResult()

        return MondayPipelineResult(
            operations=operations_result,
            portfolio_analysis=analysis,
            intelligence=None,
            dashboard_path=operations_result.dashboard_path,
        )
