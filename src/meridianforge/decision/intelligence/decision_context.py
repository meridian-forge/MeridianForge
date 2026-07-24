"""
Decision context model.

Provides normalized investment information
used by the Meridian Forge decision engine.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class DecisionContext:
    """
    Investment analysis context for recommendation generation.
    """

    property_address: str
    market: str

    purchase_price: float
    monthly_rent: float
    monthly_expenses: float

    noi: float
    cap_rate: float
    monthly_cash_flow: float

    investor_strategy: str

    risk_flags: list[str] = field(
        default_factory=list,
    )

    strengths: list[str] = field(
        default_factory=list,
    )

    @property
    def annual_cash_flow(self) -> float:
        """
        Annualized property cash flow.
        """

        return self.monthly_cash_flow * 12

    @property
    def is_cash_flow_positive(self) -> bool:
        """
        Determine if property generates positive cash flow.
        """

        return self.monthly_cash_flow > 0
