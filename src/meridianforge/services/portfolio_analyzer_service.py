from __future__ import annotations

from pathlib import Path

from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.portfolio.analysis import (
    PortfolioAnalysisResult,
    PortfolioDealResult,
)
from meridianforge.portfolio.models import (
    PortfolioIngestionResult,
)
from meridianforge.services.acquisition_execution_service import (
    AcquisitionExecutionService,
)
from meridianforge.services.portfolio_intake_service import (
    PortfolioIntakeService,
)


class PortfolioAnalyzerService:
    """
    Analyze portfolio opportunities and produce portfolio-domain results.

    MF-502 contract preserved while adding file/directory entry points
    required by MF-506 workflow orchestration.
    """

    def __init__(self) -> None:
        self.intake = PortfolioIntakeService()
        self.execution = AcquisitionExecutionService()

        self.default_investor = InvestorProfile(
            name="Portfolio Investor",
            strategy=InvestmentStrategy.CASH_FLOW,
        )

    def analyze(
        self,
        portfolio: PortfolioIngestionResult,
    ) -> PortfolioAnalysisResult:
        """
        Analyze an already-ingested portfolio.
        """

        deals: list[PortfolioDealResult] = []

        for item in portfolio.opportunities:
            orchestration = self.execution.execute(
                item.opportunity,
                investor_profile=self.default_investor,
            )

            deals.append(
                PortfolioDealResult(
                    row_number=item.row_number,
                    opportunity=item.opportunity,
                    review=orchestration.review,
                )
            )

        return PortfolioAnalysisResult(
            deals=deals,
        )

    def analyze_file(
        self,
        file_path: Path,
    ) -> PortfolioAnalysisResult:
        """
        Analyze a single portfolio workbook or CSV.
        """

        ingestion = self.intake.ingest(
            file_path,
        )

        return self.analyze(
            ingestion,
        )

    def analyze_directory(
        self,
        directory: Path,
    ) -> PortfolioAnalysisResult:
        """
        Analyze every supported portfolio artifact inside a directory.
        """

        combined = PortfolioAnalysisResult()

        if not directory.exists():
            return combined

        for path in sorted(directory.iterdir()):
            if not path.is_file():
                continue

            if path.suffix.lower() not in {".xlsx", ".csv"}:
                continue

            result = self.analyze_file(
                path,
            )

            combined.deals.extend(
                result.deals,
            )

        return combined
