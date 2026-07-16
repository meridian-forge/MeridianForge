"""
Deal ranking engine.

Ranks evaluated investment opportunities.
"""

from meridianforge.models.domain.property import Property
from meridianforge.models.results.deal_evaluation import (
    DealEvaluation,
)
from meridianforge.models.results.ranked_deal import (
    RankedDeal,
)


class DealRankingEngine:
    """
    Orders investment opportunities by score.
    """

    @staticmethod
    def rank(
        deals: list[tuple[Property, DealEvaluation]],
    ) -> list[RankedDeal]:
        """
        Rank deals from highest to lowest score.
        """

        ordered = sorted(
            deals,
            key=lambda item: item[1].score,
            reverse=True,
        )

        return [
            RankedDeal(
                rank=index,
                property=property_data,
                evaluation=evaluation,
            )
            for index, (property_data, evaluation) in enumerate(
                ordered,
                start=1,
            )
        ]
