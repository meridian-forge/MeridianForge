from __future__ import annotations

from meridianforge.acquisition.opportunity import Opportunity
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


class PortfolioAnalyzerService:
    """
    Analyze every opportunity in a portfolio and return
    a ranked portfolio-ready analysis result.

    Portfolio opportunities are already normalized acquisition
    domain objects. This service enriches them through the
    acquisition execution pipeline.
    """

    def __init__(
        self,
        execution_service: AcquisitionExecutionService | None = None,
    ) -> None:
        self.execution_service = execution_service or AcquisitionExecutionService()

    def analyze(
        self,
        portfolio: PortfolioIngestionResult,
        investor: InvestorProfile | None = None,
    ) -> PortfolioAnalysisResult:

        investor = investor or InvestorProfile(
            name="Family Office",
            strategy=InvestmentStrategy.CASH_FLOW,
        )

        deals: list[PortfolioDealResult] = []

        for item in portfolio.opportunities:

            opportunity: Opportunity = item.opportunity

            execution = self.execution_service.execute(
                opportunity,
                investor,
            )

            deals.append(
                PortfolioDealResult(
                    row_number=item.row_number,
                    opportunity=opportunity,
                    review=execution.review,
                )
            )

        deals.sort(
            key=lambda deal: (
                0
                if deal.review.buy_candidates()
                else (1 if deal.review.watch_candidates() else 2)
            )
        )

        return PortfolioAnalysisResult(
            deals=deals,
        )
