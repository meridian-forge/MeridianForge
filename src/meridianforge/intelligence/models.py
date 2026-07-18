"""
Investment intelligence domain models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class InvestorProfile:
    """
    Defines investor priorities.
    """

    goal: str

    cashflow_weight: float = 0.40
    appreciation_weight: float = 0.30
    tax_weight: float = 0.20
    risk_weight: float = 0.10

    def __post_init__(self) -> None:

        weights = [
            self.cashflow_weight,
            self.appreciation_weight,
            self.tax_weight,
            self.risk_weight,
        ]

        if any(weight < 0 for weight in weights):
            raise ValueError("Weights cannot be negative.")

        if round(sum(weights), 5) != 1:
            raise ValueError("Investor weights must total 1.0.")
