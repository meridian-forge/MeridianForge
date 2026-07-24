"""
Portfolio report tests.

MF-343.1
"""

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)

from meridianforge.portfolio.portfolio import (
    Portfolio,
)

from meridianforge.reporting.portfolio_report import (
    PortfolioReportBuilder,
)


def test_portfolio_report_builds_from_analytics():

    portfolio = Portfolio(
        name="Core Rentals",
        strategy="Long Term Hold",
    )

    analytics = PortfolioAnalytics(
        asset_count=2,
        total_purchase_price=500000,
        total_monthly_rent=5000,
        total_monthly_cash_flow=1200,
        annual_cash_flow=14400,
        average_cap_rate=0.075,
        average_dscr=1.55,
        portfolio_score=92.5,
    )

    report = PortfolioReportBuilder.build(
        portfolio,
        analytics,
    )

    output = report.render()

    assert report.portfolio_name == "Core Rentals"

    assert "Annual Cash Flow: $14,400" in output

    assert "Average Cap Rate: 7.50%" in output

    assert "Portfolio Score: 92.5" in output
