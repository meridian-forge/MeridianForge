"""
Acquisition report generator.

Creates investor-readable investment summaries.
"""

from meridianforge.models.results.acquisition_result import (
    AcquisitionResult,
)

from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)


class AcquisitionReport:
    """
    Generates acquisition analysis reports.
    """

    @staticmethod
    def generate(
        result: AcquisitionResult,
    ) -> str:
        """
        Generate investment report.
        """

        assessment = result.metadata.get(
            "assessment",
        )

        if not isinstance(
            assessment,
            AcquisitionAssessment,
        ):
            assessment = None

        lines = [
            "================================",
            "MERIDIAN FORGE",
            "INVESTMENT ANALYSIS REPORT",
            "================================",
            "",
            "INVESTMENT DECISION",
            "-------------------",
            f"Recommendation: {result.recommendation}",
            f"Confidence: {result.confidence:.0%}",
            "",
        ]

        if assessment:

            lines.extend(
                [
                    "FINANCIAL PERFORMANCE",
                    "---------------------",
                    (
                        "Purchase Price: "
                        f"${assessment.purchase_price:,.0f}"
                    ),
                    (
                        "Monthly Cash Flow: "
                        f"${assessment.monthly_cash_flow:,.0f}"
                    ),
                    (
                        "DSCR: "
                        f"{assessment.dscr:.2f}"
                    ),
                    (
                        "Cap Rate: "
                        f"{assessment.cap_rate:.2%}"
                    ),
                    "",
                ]
            )

        if result.warnings:

            lines.extend(
                [
                    "RISK REVIEW",
                    "-----------",
                    *result.warnings,
                    "",
                ]
            )
        else:

            lines.extend(
                [
                    "RISK REVIEW",
                    "-----------",
                    "No warnings identified.",
                    "",
                ]
            )

        lines.extend(
            [
                "NEXT ACTION",
                "-----------",
                "Proceed with detailed due diligence.",
            ]
        )

        return "\n".join(lines)
