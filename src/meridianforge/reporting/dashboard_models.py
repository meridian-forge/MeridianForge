"""
Monday dashboard domain models.
"""

from dataclasses import dataclass, field

from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)


@dataclass(slots=True)
class MondayDashboard:
    """
    Summary of a Monday acquisition run.
    """

    total_reviewed: int

    buy_count: int

    watch_count: int

    pass_count: int

    top_opportunity: InvestorDecisionCard | None

    buy_cards: list[InvestorDecisionCard] = field(
        default_factory=list,
    )

    watch_cards: list[InvestorDecisionCard] = field(
        default_factory=list,
    )

    pass_cards: list[InvestorDecisionCard] = field(
        default_factory=list,
    )
