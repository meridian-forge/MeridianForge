from datetime import datetime

from meridianforge.acquisition.opportunity import (
    Opportunity,
)

from meridianforge.acquisition.result import (
    AcquisitionResult,
)

from meridianforge.acquisition.thesis_generator import (
    InvestmentThesisGenerator,
)

from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)


def test_thesis_generator_creates_summary():

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
        cap_rate=0.06,
        cash_on_cash_return=0.10,
        dscr=1.5,
        debt_service_annual=8400,
        total_cash_required=50000,
    )

    result = AcquisitionResult(
        opportunity=opportunity,
        analysis=analysis,
        score=100,
        ranking=1,
        recommendation="BUY",
        confidence=1.0,
        warnings=[],
    )

    thesis = InvestmentThesisGenerator.generate(
        result
    )

    assert thesis.recommendation == "BUY"
    assert len(thesis.highlights) == 3
    assert thesis.risks == []
