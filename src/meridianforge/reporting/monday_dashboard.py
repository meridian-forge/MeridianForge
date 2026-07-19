from typing import Any


class MondayDashboardGenerator:
    """
    Generates the executive Monday dashboard
    from portfolio summary data.
    """

    def generate(
        self,
        summary: dict[str, Any],
    ) -> str:

        top = summary.get(
            "top_opportunity",
            None,
        )

        top_name = top.get("name", "N/A") if isinstance(top, dict) else "N/A"

        top_score = top.get("score", 0) if isinstance(top, dict) else 0

        return (
            "Meridian Forge Monday Dashboard\n"
            "================================\n\n"
            f"Opportunities Reviewed: "
            f"{summary.get('total_opportunities', 0)}\n"
            f"BUY Candidates: "
            f"{summary.get('buy_count', 0)}\n"
            f"WATCH Candidates: "
            f"{summary.get('watch_count', 0)}\n"
            f"Average Score: "
            f"{summary.get('average_score', 0)}\n\n"
            "Top Opportunity:\n"
            f"- {top_name}\n"
            f"- Score: {top_score}\n"
        )
