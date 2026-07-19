from typing import Any


class RankingPipeline:
    """
    Ranks analyzed opportunities.

    Initial ranking uses a configurable score field.
    """

    def __init__(
        self,
        score_key: str = "score",
    ) -> None:
        self.score_key = score_key

    def rank(
        self,
        opportunities: list[Any],
    ) -> list[Any]:

        return sorted(
            opportunities,
            key=lambda item: self._score(item),
            reverse=True,
        )

    def _score(
        self,
        opportunity: Any,
    ) -> float:

        if isinstance(opportunity, dict):
            return float(
                opportunity.get(
                    self.score_key,
                    0,
                )
            )

        return 0.0
