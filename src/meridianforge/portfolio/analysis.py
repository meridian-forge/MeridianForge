from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.acquisition.opportunity import Opportunity
from meridianforge.product.weekly_review import WeeklyInvestorReview


@dataclass(slots=True)
class PortfolioDealResult:
    """
    One analyzed property inside a portfolio.
    """

    row_number: int
    opportunity: Opportunity
    review: WeeklyInvestorReview


@dataclass(slots=True)
class PortfolioAnalysisResult:
    """
    Result of analyzing an entire portfolio.
    """

    deals: list[PortfolioDealResult] = field(default_factory=list)

    @property
    def buy_count(self) -> int:
        return sum(1 for deal in self.deals if deal.review.buy_candidates())

    @property
    def watch_count(self) -> int:
        return sum(1 for deal in self.deals if deal.review.watch_candidates())

    @property
    def pass_count(self) -> int:
        return sum(
            1
            for deal in self.deals
            if (
                len(deal.review.buy_candidates()) == 0
                and len(deal.review.watch_candidates()) == 0
            )
        )
