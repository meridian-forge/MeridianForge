"""
Investor profile model.

MF-347.1

Defines investor strategy preferences.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class InvestorProfile:
    """
    Investor operating preferences.
    """

    name: str

    strategy: str

    target_markets: list[str]

    risk_tolerance: str

    target_monthly_cash_flow: float
