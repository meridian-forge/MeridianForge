"""
Markdown investor report renderer.

Converts WeeklyInvestorReview into markdown format.
"""

from meridianforge.product.weekly_review import WeeklyInvestorReview


class MarkdownInvestorReportRenderer:
    """
    Render investor reviews as markdown documents.
    """

    def render(
        self,
        review: WeeklyInvestorReview,
    ) -> str:

        lines: list[str] = []

        lines.append("# MERIDIAN FORGE INVESTOR REVIEW")
        lines.append("")

        for card in review.cards:

            lines.append(f"## Deal #{card.rank}")
            lines.append("")

            lines.append("**Property**")
            lines.append(card.property_address)
            lines.append("")

            lines.append("**Recommendation**")
            lines.append(card.recommendation)
            lines.append("")

            lines.append("**Confidence**")
            lines.append(f"{card.confidence:.0%}")
            lines.append("")

            if card.strengths:
                lines.append("## Investment Case")

                for strength in card.strengths:
                    lines.append(f"- {strength}")

                lines.append("")

            if card.risks:
                lines.append("## Risks")

                for risk in card.risks:
                    lines.append(f"- {risk}")

                lines.append("")

            lines.append("## Decision")

            if card.is_buy_candidate():
                lines.append("Proceed to underwriting")
            else:
                lines.append("Monitor / Review")

            lines.append("")

        return "\n".join(lines)
