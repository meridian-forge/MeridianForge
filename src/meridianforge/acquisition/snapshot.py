"""
Underwriting snapshot model.

MF-336.3

Structured investment metrics
for investor reporting.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class UnderwritingSnapshot:
    """
    Key underwriting metrics.
    """

    purchase_price: float

    monthly_rent: float

    annual_cash_flow: float

    cap_rate: float

    cash_on_cash_return: float

    dscr: float

    monthly_cash_flow: float
