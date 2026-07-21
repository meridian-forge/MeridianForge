"""
Investor profile model.

Defines investor preferences used for personalized decision intelligence.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class InvestorProfile:
    """
    Represents investor decision preferences.
    """

    name: str
    strategy: str
    risk_tolerance: str
    target_cash_flow: float = 0.0
    appreciation_priority: float = 0.0
    tax_focus: float = 0.0
