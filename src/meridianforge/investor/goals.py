"""
Investor goal definitions.

MF-347.1
"""

from dataclasses import dataclass


@dataclass(slots=True)
class InvestorGoals:
    """
    Long-term investment targets.
    """

    target_properties: int

    target_portfolio_value: float

    target_monthly_income: float
