from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.operations import (
    OperationsRunResult,
)
from meridianforge.operations.email_input_adapter import (
    EmailInputAdapter,
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
    Canonical Family Office operating workflow.
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

    def _build_result(
        self,
        operations_result: OperationsRunResult,
    ) -> MondayPipelineResult:
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

    def execute(
        self,
    ) -> MondayPipelineResult:
        operations_result = self.operations.execute()

        return self._build_result(
            operations_result,
        )

    def execute_from_email(
        self,
        inbox_directory: Path,
    ) -> MondayPipelineResult:
        """
        Execute the canonical Monday workflow using the email inbox as
        the operational input source.
        """

        operations = OperationsService(
            deals_directory=inbox_directory,
            input_adapter=EmailInputAdapter(
                inbox_directory,
            ),
        )

        operations_result = operations.execute()

        return self._build_result(
            operations_result,
        )
