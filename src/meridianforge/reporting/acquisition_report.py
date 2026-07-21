"""
Acquisition report formatter.

Transforms acquisition intelligence outputs
into investor-readable text.
"""

from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)


class AcquisitionReportFormatter:
    """
    Formats acquisition decisions.
    """

    @staticmethod
    def format(
        review: WeeklyInvestorReview,
    ) -> str:
        """
        Create investor-facing acquisition report.
        """

        lines: list[str] = []

        lines.append("MERIDIAN FORGE ACQUISITION REVIEW")

        lines.append("=================================")

        if not review.cards:
            lines.append("No acquisition opportunities found.")

            return "\n".join(lines)

        for card in review.cards:

            lines.append("")
            lines.append("PROPERTY")
            lines.append("----------------")
            lines.append(card.property_address)

            lines.append("")
            lines.append("DECISION")
            lines.append("----------------")
            lines.append(card.recommendation)

            lines.append("")
            lines.append("CONFIDENCE")
            lines.append("----------------")
            lines.append(f"{card.confidence:.0%}")

            lines.append("")
            lines.append("STRENGTHS")
            lines.append("----------------")

            if card.strengths:
                for item in card.strengths:
                    lines.append(f"- {item}")
            else:
                lines.append("- None")

            lines.append("")
            lines.append("RISKS")
            lines.append("----------------")

            if card.risks:
                for item in card.risks:
                    lines.append(f"- {item}")
            else:
                lines.append("- None")

        return "\n".join(lines)
