"""
Acquisition report generator.

Creates human-readable investment summaries.
"""

from meridianforge.models.results.acquisition_result import (
    AcquisitionResult,
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
        Generate text report.
        """

        assessment = result.metadata.get(
            "assessment",
        )

        lines = [
            "MERIDIAN FORGE ANALYSIS REPORT",
            "",
            f"Recommendation: {result.recommendation}",
            f"Confidence: {result.confidence:.0%}",
            "",
            "Assets Analyzed:",
            str(result.assets_analyzed),
            "",
        ]

        if assessment:

            lines.extend(
                [
                    "Financial Summary",
                    "-----------------",
                    f"Purchase Price: ${assessment.purchase_price:,.0f}",
                    f"DSCR: {assessment.dscr:.2f}",
                    f"Cap Rate: {assessment.cap_rate:.2%}",
                    ("Monthly Cash Flow: " f"${assessment.monthly_cash_flow:,.0f}"),
                    "",
                ]
            )

        if result.warnings:

            lines.extend(
                [
                    "Warnings",
                    "--------",
                    *result.warnings,
                    "",
                ]
            )

        return "\n".join(lines)
