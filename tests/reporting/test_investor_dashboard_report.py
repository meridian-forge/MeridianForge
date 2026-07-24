"""
Investor dashboard report tests.

MF-345.2
"""

from meridianforge.portfolio.intelligence.dashboard import (
    InvestorDashboard,
)
from meridianforge.reporting.investor_dashboard_report import (
    InvestorDashboardReportBuilder,
)


def test_investor_dashboard_report_generation():

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
        concerns=[
            "Monitor leverage",
        ],
    )

    report = InvestorDashboardReportBuilder.build(
        dashboard,
    )

    output = report.render()

    assert "Meridian Forge Investor Dashboard" in output

    assert "HOLD_AND_SCALE" in output

    assert "Acquire assets" in output
