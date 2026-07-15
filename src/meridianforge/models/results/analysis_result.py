"""
Analysis result model.

Represents the complete output of the underwriting engine.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class AnalysisResult:
    """
    Canonical underwriting output.
    """

    purchase_price: float

    monthly_rent: float

    gross_monthly_income: float

    operating_expenses_monthly: float

    net_operating_income_monthly: float

    mortgage_payment_monthly: float

    monthly_cash_flow: float

    annual_cash_flow: float

    cap_rate: float

    cash_on_cash_return: float

    dscr: float

    debt_service_annual: float

    total_cash_required: float

    risk_score: int = 0

    recommendation: str = "REVIEW"

    warnings: list[str] = field(default_factory=list)

    passed: bool = False
