from __future__ import annotations

from meridianforge.portfolio.analysis import (
    PortfolioAnalysisResult,
)


class PortfolioReportFormatter:
    """
    Formats a ranked portfolio analysis into a readable
    Monday Morning report.
    """

    @staticmethod
    def format(
        analysis: PortfolioAnalysisResult,
    ) -> str:

        lines: list[str] = []

        lines.append("MERIDIAN FORGE PORTFOLIO REPORT")
        lines.append("=" * 40)
        lines.append("")

        lines.append(f"Properties analyzed : {len(analysis.deals)}")

        lines.append(f"BUY opportunities   : {analysis.buy_count}")

        lines.append(f"WATCH opportunities : {analysis.watch_count}")

        lines.append(f"PASS opportunities  : {analysis.pass_count}")

        lines.append("")
        lines.append("RANKED OPPORTUNITIES")
        lines.append("-" * 40)

        for rank, deal in enumerate(
            analysis.deals,
            start=1,
        ):

            decision = (
                "BUY"
                if deal.review.buy_candidates()
                else ("WATCH" if deal.review.watch_candidates() else "PASS")
            )

            lines.append(f"{rank}. {deal.opportunity.address}")

            lines.append(f"   Decision : {decision}")

            lines.append(f"   Row      : {deal.row_number}")

            lines.append("")

        return "\n".join(lines)
