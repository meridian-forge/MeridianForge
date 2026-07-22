"""
Acquisition opportunity domain model.

Represents a property opportunity entering MeridianForge.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Opportunity:
    """
    Represents an acquisition opportunity.
    """

    address: str
    city: str
    state: str
    zip_code: str

    purchase_price: float
    monthly_rent: float
    monthly_expenses: float

    market: str
    source: str

    created_at: datetime

    @property
    def monthly_cash_flow(self) -> float:
        """
        Calculate monthly cash flow.
        """

        return self.monthly_rent - self.monthly_expenses

    @property
    def annual_cash_flow(self) -> float:
        """
        Calculate annual cash flow.
        """

        return self.monthly_cash_flow * 12

    @property
    def cap_rate(self) -> float:
        """
        Calculate simple cap rate.
        """

        if self.purchase_price == 0:
            return 0.0

        return self.annual_cash_flow / self.purchase_price
