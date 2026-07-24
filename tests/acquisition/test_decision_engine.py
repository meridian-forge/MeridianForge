"""
Tests for acquisition decision engine.

MF-334.2
"""

from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)
from meridianforge.acquisition.decision_engine import (
    AcquisitionDecisionEngine,
)
from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)


def test_decision_engine_returns_buy():

    analysis = AnalysisResult(
        purchase_price=200000,
        monthly_rent=1800,
        gross_monthly_income=1800,
        operating_expenses_monthly=600,
        net_operating_income_monthly=1200,
        mortgage_payment_monthly=800,
        monthly_cash_flow=400,
        annual_cash_flow=4800,
        cap_rate=0.072,
        cash_on_cash_return=0.10,
        dscr=1.5,
        debt_service_annual=9600,
        total_cash_required=50000,
    )

    decision = AcquisitionDecisionEngine().evaluate(
        analysis,
        100,
        AcquisitionCriteria(),
    )

    assert decision.status == "BUY"

    assert len(decision.risks) == 0
