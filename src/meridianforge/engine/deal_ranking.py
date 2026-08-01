"""
Deal ranking engine.

Ranks evaluated investment opportunities.
"""

from meridianforge.models.domain.property import Property
from meridianforge.models.results.analysis_result import AnalysisResult
from meridianforge.models.results.deal_evaluation import DealEvaluation
from meridianforge.models.results.ranked_deal import RankedDeal


class DealRankingEngine:
    """
    Orders investment opportunities by score.
    """

    @staticmethod
    def rank(
        deals: list[
            tuple[Property, AnalysisResult, DealEvaluation]
            | tuple[Property, DealEvaluation]
        ],
    ) -> list[RankedDeal]:
        """
        Rank deals from highest to lowest score.

        Supports legacy two-item tuples and
        current analysis-aware tuples.
        """

        normalized: list[tuple[Property, AnalysisResult | None, DealEvaluation]] = []

        for deal in deals:
            if len(deal) == 2:
                property_data, evaluation = deal
                normalized.append(
                    (
                        property_data,
                        None,
                        evaluation,
                    )
                )
            else:
                property_data, analysis, evaluation = deal
                normalized.append(
                    (
                        property_data,
                        analysis,
                        evaluation,
                    )
                )

        ordered = sorted(
            normalized,
            key=lambda item: item[2].score,
            reverse=True,
        )

        return [
            RankedDeal(
                rank=index,
                property=property_data,
                analysis=analysis,
                evaluation=evaluation,
            )
            for index, (
                property_data,
                analysis,
                evaluation,
            ) in enumerate(
                ordered,
                start=1,
            )
        ]
