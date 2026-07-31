from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.operations import (
    OperationsRunResult,
)
from meridianforge.portfolio.analysis import (
    PortfolioAnalysisResult,
)
from meridianforge.portfolio.intelligence.package import (
    InvestorDecisionPackage,
)
from meridianforge.services.operations_service import (
    OperationsService,
)
from meridianforge.services.portfolio_analyzer_service import (
    PortfolioAnalyzerService,
)
from meridianforge.services.portfolio_intelligence_service import (
    PortfolioIntelligenceService,
)


@dataclass(slots=True)
class MondayPipelineResult:
    """
    Canonical workflow result for the Monday execution pipeline.
    """

    operations: OperationsRunResult
    analysis: PortfolioAnalysisResult
    intelligence: InvestorDecisionPackage | None


class MondayExecutionPipeline:
    """
    MF-506.2

    Canonical Family Office operating workflow.

    Orchestrates:
    - operations
    - portfolio analysis
    - portfolio intelligence
    """

    def __init__(
        self,
        deals_directory: Path,
    ) -> None:
        self.deals_directory = deals_directory

        self.operations = OperationsService(
            deals_directory,
        )

        self.analyzer = PortfolioAnalyzerService()

        self.intelligence = PortfolioIntelligenceService()

    def execute(
        self,
    ) -> MondayPipelineResult:
        """
        Execute the complete Monday workflow.

        Portfolio analysis is intentionally best-effort. The Monday
        operational workflow must continue even when an incoming file
        is not a valid portfolio workbook.
        """

        operations_result = self.operations.execute()

        try:
            analysis = self.analyzer.analyze_directory(
                self.deals_directory,
            )

        except Exception:
            analysis = PortfolioAnalysisResult()

        intelligence: InvestorDecisionPackage | None = None

        if analysis.deals:

            intelligence = self.intelligence.analyze(
                analysis,
            )

        return MondayPipelineResult(
            operations=operations_result,
            analysis=analysis,
            intelligence=intelligence,
        )
