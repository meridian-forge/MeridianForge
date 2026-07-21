"""
Monday dashboard builder.
"""

from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.reporting.dashboard_models import (
    MondayDashboard,
)


class MondayDashboardBuilder:
    """
    Builds dashboard from investor review.
    """

    @staticmethod
    def build(
        review: WeeklyInvestorReview,
    ) -> MondayDashboard:

        buy_cards = [
            card for card in review.cards if card.recommendation.upper() == "BUY"
        ]

        watch_cards = [
            card for card in review.cards if card.recommendation.upper() == "WATCH"
        ]

        pass_cards = [
            card for card in review.cards if card.recommendation.upper() == "PASS"
        ]

        top = None

        if review.cards:
            top = max(
                review.cards,
                key=lambda card: card.confidence,
            )

        return MondayDashboard(
            total_reviewed=len(review.cards),
            buy_count=len(buy_cards),
            watch_count=len(watch_cards),
            pass_count=len(pass_cards),
            top_opportunity=top,
            buy_cards=buy_cards,
            watch_cards=watch_cards,
            pass_cards=pass_cards,
        )
