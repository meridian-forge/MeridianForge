"""
Weekly investor review report.
"""

from dataclasses import dataclass, field

from meridianforge.product.decision_card import InvestorDecisionCard


@dataclass(slots=True)
class WeeklyInvestorReview:
    """
    Weekly review presented to the investor.
    """

    cards: list[InvestorDecisionCard] = field(
        default_factory=list,
    )

    def buy_candidates(self) -> list[InvestorDecisionCard]:
        return [card for card in self.cards if card.is_buy_candidate()]

    def watch_candidates(self) -> list[InvestorDecisionCard]:
        return [card for card in self.cards if not card.is_buy_candidate()]
