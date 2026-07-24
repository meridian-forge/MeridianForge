"""
Operating loop integration tests.

MF-346.3
"""

from datetime import datetime

from meridianforge.acquisition.opportunity import (
    Opportunity,
)
from meridianforge.acquisition.result import (
    AcquisitionResult,
)
from meridianforge.integration.operating_loop import (
    MeridianForgeOperatingLoop,
)
from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)
from meridianforge.portfolio.portfolio import (
    Portfolio,
)


def create_result() -> AcquisitionResult:

    opportunity = Opportunity(
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

    analysis = AnalysisResult(
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

    return AcquisitionResult(
        opportunity=opportunity,
        analysis=analysis,
        score=95,
        ranking=1,
        recommendation="BUY",
        confidence=0.95,
    )


def test_operating_loop_processes_acquisition():

    portfolio = Portfolio(
        name="Core Rentals",
        strategy="Long Term Hold",
    )

    state = MeridianForgeOperatingLoop.process_acquisition(
        portfolio,
        create_result(),
    )

    assert state.asset_count == 1

    assert state.lifecycle.status == "GROWING"

    assert state.lifecycle.next_action == "Evaluate next acquisition"
