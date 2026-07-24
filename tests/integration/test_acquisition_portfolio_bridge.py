"""
Acquisition portfolio bridge tests.

MF-346.1
"""

from datetime import datetime

from meridianforge.acquisition.opportunity import (
    Opportunity,
)
from meridianforge.acquisition.result import (
    AcquisitionResult,
)
from meridianforge.integration.acquisition_portfolio_bridge import (
    AcquisitionPortfolioBridge,
)
from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)
from meridianforge.portfolio.portfolio import (
    Portfolio,
)


def create_analysis_result() -> AnalysisResult:
    """
    Create canonical underwriting result.
    """

    return AnalysisResult(
        purchase_price=200000,
        monthly_rent=2000,
        gross_monthly_income=2000,
        operating_expenses_monthly=800,
        net_operating_income_monthly=1200,
        mortgage_payment_monthly=700,
        monthly_cash_flow=500,
        annual_cash_flow=6000,
        cap_rate=0.08,
        cash_on_cash_return=0.10,
        dscr=1.5,
        debt_service_annual=8400,
        total_cash_required=50000,
        risk_score=10,
        recommendation="BUY",
        passed=True,
    )


def create_opportunity() -> Opportunity:
    """
    Create acquisition opportunity.
    """

    return Opportunity(
        address="123 Main",
        city="Philadelphia",
        state="PA",
        zip_code="19143",
        purchase_price=200000,
        monthly_rent=2000,
        monthly_expenses=800,
        market="Philadelphia",
        source="test",
        created_at=datetime.now(),
    )


def test_acquisition_result_converts_to_portfolio_asset():

    result = AcquisitionResult(
        opportunity=create_opportunity(),
        analysis=create_analysis_result(),
        score=90,
        ranking=1,
        recommendation="BUY",
        confidence=0.95,
    )

    asset = AcquisitionPortfolioBridge.convert(
        result,
    )

    assert asset.purchase_price == 200000

    assert asset.monthly_rent == 2000

    assert asset.monthly_cash_flow == 1200

    assert asset.cap_rate == 0.08

    assert asset.dscr == 1.5


def test_acquisition_adds_to_portfolio():

    portfolio = Portfolio(
        name="Core Rentals",
        strategy="Long Term Hold",
    )

    result = AcquisitionResult(
        opportunity=create_opportunity(),
        analysis=create_analysis_result(),
        score=90,
        ranking=1,
        recommendation="BUY",
        confidence=0.95,
    )

    AcquisitionPortfolioBridge.add_to_portfolio(
        portfolio,
        result,
    )

    assert portfolio.asset_count == 1
