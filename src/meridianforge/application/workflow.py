from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)
from meridianforge.acquisition.score import (
    calculate_score,
)
from meridianforge.analysis.underwriting_engine import (
    UnderwritingEngine,
)
from meridianforge.application.models import (
    PropertyInput,
)
from meridianforge.models.results.analysis_result import (
    AnalysisResult as CanonicalAnalysisResult,
)


class AnalysisWorkflow:
    """
    Application workflow boundary.

    Converts legacy underwriting output into the
    canonical analysis result model before passing
    data into acquisition intelligence services.
    """

    def __init__(self) -> None:
        self.engine = UnderwritingEngine()

        self.criteria = AcquisitionCriteria()

    def execute(
        self,
        property_input: PropertyInput,
    ) -> dict[str, float]:

        legacy_result = self.engine.analyze(
            purchase_price=property_input.purchase_price,
            noi=property_input.noi,
            annual_cash_flow=property_input.annual_cash_flow,
            cash_invested=property_input.cash_invested,
            annual_debt=property_input.annual_debt,
        )

        canonical_result = CanonicalAnalysisResult(
            purchase_price=property_input.purchase_price,
            monthly_rent=0.0,
            gross_monthly_income=0.0,
            operating_expenses_monthly=0.0,
            net_operating_income_monthly=0.0,
            mortgage_payment_monthly=0.0,
            monthly_cash_flow=legacy_result.cash_flow_monthly,
            annual_cash_flow=property_input.annual_cash_flow,
            cap_rate=legacy_result.cap_rate,
            cash_on_cash_return=legacy_result.cash_on_cash_return,
            dscr=legacy_result.dscr,
            debt_service_annual=property_input.annual_debt,
            total_cash_required=property_input.cash_invested,
            risk_score=0,
            recommendation="REVIEW",
            warnings=[],
            passed=False,
        )

        score = calculate_score(
            canonical_result,
            self.criteria,
        )

        return {
            "cap_rate": canonical_result.cap_rate,
            "cash_on_cash": canonical_result.cash_on_cash_return,
            "dscr": canonical_result.dscr,
            "score": score,
        }
