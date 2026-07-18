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


class AnalysisWorkflow:

    def __init__(self) -> None:

        self.engine = UnderwritingEngine()

        self.criteria = AcquisitionCriteria()

    def execute(
        self,
        property_input: PropertyInput,
    ) -> dict[str, float]:

        result = self.engine.analyze(
            purchase_price=property_input.purchase_price,
            noi=property_input.noi,
            annual_cash_flow=property_input.annual_cash_flow,
            cash_invested=property_input.cash_invested,
            annual_debt=property_input.annual_debt,
        )

        score = calculate_score(
            result,
            self.criteria,
        )

        return {
            "cap_rate": result.cap_rate,
            "cash_on_cash": result.cash_on_cash_return,
            "dscr": result.dscr,
            "score": score,
        }
