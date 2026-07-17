#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D023.2"
echo "Investment Report Enhancement"
echo "======================================"

PACKAGE="updates/packages/D023.2"

mkdir -p "$PACKAGE/files/src/meridianforge/reports"
mkdir -p "$PACKAGE/files/tests"


echo "Creating enhanced report generator..."

cat > "$PACKAGE/files/src/meridianforge/reports/acquisition_report.py" <<'PY'
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
PY


echo "Creating enhanced report test..."

cat > "$PACKAGE/files/tests/test_enhanced_report.py" <<'PY'
from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)

from meridianforge.models.results.acquisition_result import (
    AcquisitionResult,
)

from meridianforge.reports.acquisition_report import (
    AcquisitionReport,
)


def test_enhanced_report_content() -> None:

    assessment = AcquisitionAssessment(
        purchase_price=215000,
        monthly_cash_flow=300,
        dscr=1.25,
        cap_rate=0.065,
    )

    result = AcquisitionResult(
        recommendation="BUY",
        confidence=0.90,
        metadata={
            "assessment": assessment,
        },
    )

    report = AcquisitionReport.generate(
        result
    )

    assert "INVESTMENT ANALYSIS REPORT" in report
    assert "FINANCIAL PERFORMANCE" in report
    assert "BUY" in report
PY


echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D023.2

Purpose:
Investment Report Enhancement

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D023.2 deployment handled by update engine"
EOF

chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

