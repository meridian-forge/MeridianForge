"""
Investor opportunity ranking.

Ranks investor decision cards.
"""

from meridianforge.models.results.ranked_opportunity import (
    RankedOpportunity,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)


class OpportunityRanker:
    """
    Rank investor opportunities.
    """

    def rank(
        self,
        reviews: list[WeeklyInvestorReview],
    ) -> list[RankedOpportunity]:
        """
        Flatten and rank review cards.
        """

        cards = []

        for review in reviews:
            cards.extend(review.cards)

        ordered = sorted(
            cards,
            key=lambda card: (
                card.recommendation.upper() == "BUY",
                card.confidence,
            ),
            reverse=True,
        )

        return [
            RankedOpportunity(
                rank=index,
                property_address=card.property_address,
                recommendation=card.recommendation,
                confidence=card.confidence,
            )
            for index, card in enumerate(
                ordered,
                start=1,
            )
        ]
