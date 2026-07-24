"""
Portfolio prioritizer.

MF-337.3.2

Converts rankings into investor actions.
"""

from meridianforge.acquisition.portfolio_priority import (
    PortfolioPriority,
)
from meridianforge.acquisition.ranking_model import (
    RankingResult,
)


class PortfolioPrioritizer:
    """
    Assign investor actions.
    """

    @staticmethod
    def prioritize(
        rankings: list[RankingResult],
    ) -> list[PortfolioPriority]:
        """
        Convert rankings into actions.
        """

        priorities: list[PortfolioPriority] = []

        for ranking in rankings:

            if ranking.category in [
                "A+",
                "A",
            ]:
                action = "BUY NOW"
                rationale = "Strong acquisition metrics."

            elif ranking.category == "B":
                action = "REVIEW"
                rationale = "Meets baseline but requires review."

            elif ranking.category == "C":
                action = "WATCH"
                rationale = "Potential opportunity if conditions improve."

            else:
                action = "REJECT"
                rationale = "Does not meet acquisition criteria."

            priorities.append(
                PortfolioPriority(
                    property_address=(ranking.property_address),
                    rank=ranking.rank,
                    score=ranking.score,
                    action=action,
                    rationale=rationale,
                )
            )

        return priorities
