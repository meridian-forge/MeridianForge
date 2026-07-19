"""
Investor report renderer.

Converts WeeklyInvestorReview into a readable investor report.
"""

from meridianforge.product.weekly_review import WeeklyInvestorReview


class InvestorReportRenderer:
    """
    Render investor-facing acquisition report.
    """

    def render(
        self,
        review: WeeklyInvestorReview,
    ) -> str:

        lines: list[str] = []

        lines.append("=" * 60)
        lines.append("MERIDIAN FORGE")
        lines.append("Investor Acquisition Review")
        lines.append("Weekly Acquisition Review")
        lines.append("=" * 60)
        lines.append("")

        for card in review.cards:

            lines.append(f"DEAL #{card.rank}")
            lines.append("")

            lines.append("Property:")
            lines.append(card.property_address)
            lines.append("")

            lines.append("Recommendation:")
            lines.append(card.recommendation)
            lines.append("")

            lines.append("Confidence:")
            lines.append(f"{card.confidence:.0%}")

            if card.strengths:

                lines.append("")
                lines.append("Investment Case:")

                for strength in card.strengths:
                    lines.append(f"  + {strength}")

            if card.risks:

                lines.append("")
                lines.append("Risks:")

                for risk in card.risks:
                    lines.append(f"  - {risk}")

            lines.append("")
            lines.append("Decision:")

            if card.is_buy_candidate():
                lines.append("Proceed to underwriting")
            else:
                lines.append("Monitor / Review")

            lines.append("")
            lines.append("-" * 60)
            lines.append("")

        return "\n".join(lines)
