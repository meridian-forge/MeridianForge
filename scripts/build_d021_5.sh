#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D021.5"
echo "Acquisition Report Generator"
echo "======================================"

PACKAGE="updates/packages/D021.5"

mkdir -p "$PACKAGE/files/src/meridianforge/reports"
mkdir -p "$PACKAGE/files/tests"


echo "Creating report generator..."

cat > "$PACKAGE/files/src/meridianforge/reports/acquisition_report.py" <<'PY'
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
                    (
                        "Monthly Cash Flow: "
                        f"${assessment.monthly_cash_flow:,.0f}"
                    ),
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
PY


echo "Creating tests..."

cat > "$PACKAGE/files/tests/test_acquisition_report.py" <<'PY'
from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)
from meridianforge.models.results.acquisition_result import (
    AcquisitionResult,
)
from meridianforge.reports.acquisition_report import (
    AcquisitionReport,
)


def test_report_generation() -> None:

    assessment = AcquisitionAssessment(
        purchase_price=215000,
        dscr=1.35,
        cap_rate=0.07,
        monthly_cash_flow=350,
    )

    result = AcquisitionResult(
        confidence=0.90,
        recommendation="BUY",
        assets_analyzed=1,
        metadata={
            "assessment": assessment,
        },
    )

    report = AcquisitionReport.generate(
        result,
    )

    assert "BUY" in report
    assert "215,000" in report
    assert "1.35" in report
PY


echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D021.5

Purpose:
Acquisition Report Generator

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D021.5 deployment handled by update engine"
EOF


chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

