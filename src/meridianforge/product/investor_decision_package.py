"""
Investor decision package.

MF-356.1

Aggregates ranked opportunities and investor actions
into a single acquisition decision artifact.
"""

from dataclasses import dataclass, field

from meridianforge.models.results.ranked_opportunity import (
    RankedOpportunity,
)
from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)


@dataclass(slots=True)
class InvestorDecisionPackage:
    """
    Investor-facing acquisition decision package.
    """

    ranked_opportunities: list[RankedOpportunity] = field(
        default_factory=list,
    )

    buy_candidates: list[InvestorDecisionCard] = field(
        default_factory=list,
    )

    watch_candidates: list[InvestorDecisionCard] = field(
        default_factory=list,
    )

    @property
    def total_reviewed(self) -> int:
        """
        Total opportunities reviewed.
        """

        return len(self.ranked_opportunities)

    @property
    def buy_count(self) -> int:
        """
        Number of active buy candidates.
        """

        return len(self.buy_candidates)

    @property
    def watch_count(self) -> int:
        """
        Number of watch candidates.
        """

        return len(self.watch_candidates)
