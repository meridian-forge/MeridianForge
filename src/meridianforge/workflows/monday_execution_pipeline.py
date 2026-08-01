from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.operations import OperationsRunResult
from meridianforge.operations.email_input_adapter import EmailInputAdapter
from meridianforge.portfolio.analysis import PortfolioAnalysisResult
from meridianforge.portfolio.intelligence.package import InvestorDecisionPackage
from meridianforge.services.operations_service import OperationsService
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
    MF-512.1

    Canonical Family Office operating workflow.

    Single analysis path:

    Input
      |
    OperationsService
      |
    PortfolioAnalyzerService
      |
    Portfolio Intelligence
      |
    Investor Decision Package
    """

    def __init__(
        self,
        deals_directory: Path,
        use_email: bool = False,
    ) -> None:
        self.deals_directory = deals_directory

        input_adapter = EmailInputAdapter() if use_email else None

        self.operations = OperationsService(
            deals_directory,
            input_adapter=input_adapter,
        )

        self.analyzer = PortfolioAnalyzerService()

        self.intelligence = PortfolioIntelligenceService()

    def execute(
        self,
    ) -> MondayPipelineResult:
        """
        Execute the complete Monday workflow.
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

    @classmethod
    def from_email(
        cls,
        deals_directory: Path,
    ) -> MondayExecutionPipeline:
        """
        Construct a pipeline that synchronizes Gmail before operations.
        """

        return cls(
            deals_directory=deals_directory,
            use_email=True,
        )
