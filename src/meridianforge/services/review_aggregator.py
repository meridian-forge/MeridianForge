"""
Review aggregation service.

Combines multiple WeeklyInvestorReview objects into a
single portfolio review suitable for Monday reporting.
"""

from meridianforge.product.decision_card import InvestorDecisionCard
from meridianforge.product.weekly_review import WeeklyInvestorReview


class ReviewAggregator:
    """
    Merge multiple investor reviews into one.
    """

    @staticmethod
    def combine(
        reviews: list[WeeklyInvestorReview],
    ) -> WeeklyInvestorReview:
        """
        Merge reviews and normalize ranking.
        """

        cards: list[InvestorDecisionCard] = []

        for review in reviews:
            cards.extend(review.cards)

        cards.sort(
            key=lambda card: (
                card.recommendation.upper() == "BUY",
                card.confidence,
            ),
            reverse=True,
        )

        for rank, card in enumerate(cards, start=1):
            card.rank = rank

        return WeeklyInvestorReview(
            cards=cards,
        )
