"""
Investor package tests.

MF-345.3
"""

from pathlib import Path

from meridianforge.portfolio.intelligence.dashboard import (
    InvestorDashboard,
)
from meridianforge.reporting.investor_dashboard_report import (
    InvestorDashboardReportBuilder,
)
from meridianforge.reporting.investor_package import (
    InvestorPackageBuilder,
    InvestorPackageExporter,
)


def test_investor_package_creation():

    dashboard = InvestorDashboard(
        status="STRONG",
        health_score=95,
        priority="HIGH",
        decision="HOLD_AND_SCALE",
        recommended_action="Acquire assets",
        urgency="NORMAL",
        highlights=[
            "Strong cash flow",
        ],
        concerns=[],
    )

    report = InvestorDashboardReportBuilder.build(
        dashboard,
    )

    package = InvestorPackageBuilder.build(
        report,
        metadata={
            "period": "weekly",
        },
    )

    output = package.render()

    assert "Meridian Forge Investor Package" in output

    assert "weekly" in output


def test_investor_package_export(
    tmp_path: Path,
):

    dashboard = InvestorDashboard(
        status="STRONG",
        health_score=95,
        priority="HIGH",
        decision="HOLD_AND_SCALE",
        recommended_action="Acquire assets",
        urgency="NORMAL",
        highlights=[],
        concerns=[],
    )

    report = InvestorDashboardReportBuilder.build(
        dashboard,
    )

    package = InvestorPackageBuilder.build(
        report,
    )

    output = tmp_path / "investor_package.txt"

    result = InvestorPackageExporter.export_text(
        package,
        output,
    )

    assert result.exists()

    assert "Investor Package" in result.read_text()
