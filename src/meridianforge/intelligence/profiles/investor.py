from dataclasses import dataclass


@dataclass
class InvestorProfile:
    """
    Defines investor decision preferences.
    """

    name: str
    goal: str
    risk_tolerance: str
    minimum_cash_flow: float = 0.0
    appreciation_priority: bool = False
