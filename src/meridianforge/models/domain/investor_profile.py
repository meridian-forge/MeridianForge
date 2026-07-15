"""
Investor profile domain model.

Defines investor goals and acquisition criteria.
"""

from dataclasses import dataclass, field

from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)


@dataclass(slots=True)
class InvestorProfile:
    """
    Defines investor preferences and constraints.
    """

    name: str

    strategy: InvestmentStrategy

    minimum_dscr: float = 1.20

    minimum_cap_rate: float = 6.0

    minimum_cash_on_cash: float = 8.0

    maximum_purchase_price: float = 500000

    preferred_states: list[str] = field(
        default_factory=list,
    )

    def __post_init__(self) -> None:
        """
        Validate investor requirements.
        """

        if self.minimum_dscr <= 0:
            raise ValueError("Minimum DSCR must be positive.")

        if self.minimum_cap_rate < 0:
            raise ValueError("Minimum cap rate cannot be negative.")

        if self.minimum_cash_on_cash < 0:
            raise ValueError("Minimum cash-on-cash cannot be negative.")

        if self.maximum_purchase_price <= 0:
            raise ValueError("Maximum purchase price must be positive.")

        self.preferred_states = [state.upper() for state in self.preferred_states]
