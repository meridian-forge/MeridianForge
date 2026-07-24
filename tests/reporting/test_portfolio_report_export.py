"""
Portfolio report export integration tests.

MF-343.2
"""

from pathlib import Path

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.portfolio import (
    Portfolio,
)
from meridianforge.reporting.exporter import (
    ReportExporter,
)
from meridianforge.reporting.portfolio_report import (
    PortfolioReportBuilder,
)


def test_portfolio_report_exports_as_markdown(
    tmp_path: Path,
):

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

    output_path = tmp_path / "portfolio_report.md"

    exporter = ReportExporter()

    result = exporter.export_markdown(
        report,
        output_path,
    )

    assert result.exists()

    content = result.read_text(
        encoding="utf-8",
    )

    assert "Meridian Forge Portfolio Report" in content

    assert "Core Rentals" in content

    assert "Annual Cash Flow: $14,400" in content


def test_portfolio_report_exports_as_text(
    tmp_path: Path,
):

    portfolio = Portfolio(
        name="Growth Rentals",
        strategy="Appreciation",
    )

    analytics = PortfolioAnalytics(
        asset_count=1,
        total_purchase_price=250000,
        total_monthly_rent=2500,
        total_monthly_cash_flow=600,
        annual_cash_flow=7200,
        average_cap_rate=0.08,
        average_dscr=1.6,
        portfolio_score=88.0,
    )

    report = PortfolioReportBuilder.build(
        portfolio,
        analytics,
    )

    output_path = tmp_path / "portfolio_report.txt"

    exporter = ReportExporter()

    result = exporter.export_text(
        report,
        output_path,
    )

    assert result.exists()

    content = result.read_text(
        encoding="utf-8",
    )

    assert "Growth Rentals" in content

    assert "Portfolio Score: 88.0" in content
