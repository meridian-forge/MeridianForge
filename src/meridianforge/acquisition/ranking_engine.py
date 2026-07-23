"""
Acquisition ranking engine.

MF-337.2

Ranks multiple acquisition opportunities.
"""

from meridianforge.acquisition.ranking_category import (
    classify_rank_score,
)

from meridianforge.acquisition.ranking_model import (
    RankingResult,
)

from meridianforge.acquisition.result import (
    AcquisitionResult,
)


class AcquisitionRankingEngine:
    """
    Ranks acquisition opportunities.
    """

    @staticmethod
    def rank(
        results: list[AcquisitionResult],
    ) -> list[RankingResult]:
        """
        Rank acquisition results by score.
        """

        ordered = sorted(
            results,
            key=lambda result: result.score,
            reverse=True,
        )

        ranked: list[RankingResult] = []

        for index, result in enumerate(
            ordered,
            start=1,
        ):
            opportunity = result.opportunity

            property_address = (
                f"{opportunity.address}, "
                f"{opportunity.city}, "
                f"{opportunity.state} "
                f"{opportunity.zip_code}"
            )

            ranked.append(
                RankingResult(
                    property_address=property_address,
                    rank=index,
                    score=result.score,
                    category=(
                        classify_rank_score(
                            result.score
                        )
                    ),
                    recommendation=(
                        result.recommendation
                    ),
                )
            )

        return ranked
