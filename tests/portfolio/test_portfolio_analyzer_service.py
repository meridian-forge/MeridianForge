"""
Portfolio analyzer service integration tests.

MF-502
"""

from datetime import datetime
from pathlib import Path

from meridianforge.acquisition.opportunity import (
    Opportunity,
)
from meridianforge.portfolio.models import (
    PortfolioIngestionResult,
    PortfolioOpportunity,
)
from meridianforge.reporting.portfolio_report_formatter import (
    PortfolioReportFormatter,
)
from meridianforge.services.portfolio_analyzer_service import (
    PortfolioAnalyzerService,
)


def create_opportunity() -> Opportunity:
    return Opportunity(
        address="123 Main Street",
        city="Philadelphia",
        state="PA",
        zip_code="19143",
        purchase_price=200000,
        monthly_rent=2200,
        monthly_expenses=800,
        market="Philadelphia",
        source="test",
        created_at=datetime.now(),
    )


def test_portfolio_analyzer_creates_ranked_report():

    portfolio = PortfolioIngestionResult(
        opportunities=[
            PortfolioOpportunity(
                source_file=Path("sample.xlsx"),
                row_number=2,
                opportunity=create_opportunity(),
            )
        ]
    )

    service = PortfolioAnalyzerService()

    analysis = service.analyze(
        portfolio,
    )

    assert len(analysis.deals) == 1

    report = PortfolioReportFormatter.format(
        analysis,
    )

    assert "MERIDIAN FORGE PORTFOLIO REPORT" in report

    assert "123 Main Street" in report

    assert "Decision" in report
