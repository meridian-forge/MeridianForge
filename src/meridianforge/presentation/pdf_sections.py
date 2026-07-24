"""
PDF section builder.

Creates structured investor-facing sections
from an InvestorPackage.
"""

from meridianforge.models.results.investor_package import (
    InvestorPackage,
)


class PDFSectionBuilder:
    """
    Build PDF content sections.
    """

    @staticmethod
    def build(
        package: InvestorPackage,
    ) -> list[tuple[str, str]]:
        """
        Convert investor package into sections.
        """

        sections: list[tuple[str, str]] = []

        review = package.review

        sections.append(
            (
                "Executive Summary",
                str(review),
            )
        )

        if package.recommendation:

            sections.append(
                (
                    "Investment Recommendation",
                    (
                        f"Action: "
                        f"{package.recommendation.action.value}\n"
                        f"Confidence: "
                        f"{package.recommendation.confidence:.0%}"
                    ),
                )
            )

            sections.append(
                (
                    "Strengths",
                    "\n".join(
                        package.recommendation.reasons,
                    )
                    or "No strengths identified.",
                )
            )

            sections.append(
                (
                    "Risks",
                    "\n".join(
                        package.recommendation.risks,
                    )
                    or "No risks identified.",
                )
            )

            sections.append(
                (
                    "Next Steps",
                    "\n".join(
                        package.recommendation.next_steps,
                    )
                    or "No next steps identified.",
                )
            )

        return sections
