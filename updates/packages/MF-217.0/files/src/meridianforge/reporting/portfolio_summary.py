from typing import Any


class PortfolioSummary:
    """
    Builds executive summary statistics
    from analyzed opportunities.
    """

    def summarize(
        self,
        opportunities: list[Any],
    ) -> dict[str, Any]:

        total = len(opportunities)

        buy_count = sum(
            1
            for item in opportunities
            if self._status(item) == "BUY"
        )

        watch_count = sum(
            1
            for item in opportunities
            if self._status(item) == "WATCH"
        )

        scores = [
            self._score(item)
            for item in opportunities
        ]

        average_score = (
            sum(scores) / len(scores)
            if scores
            else 0
        )

        top_opportunity = (
            opportunities[0]
            if opportunities
            else None
        )

        return {
            "total_opportunities": total,
            "buy_count": buy_count,
            "watch_count": watch_count,
            "average_score": average_score,
            "top_opportunity": top_opportunity,
        }

    def _status(
        self,
        item: Any,
    ) -> str:

        if isinstance(item, dict):
            return str(
                item.get(
                    "status",
                    "",
                )
            )

        return ""

    def _score(
        self,
        item: Any,
    ) -> float:

        if isinstance(item, dict):
            return float(
                item.get(
                    "score",
                    0,
                )
            )

        return 0.0
