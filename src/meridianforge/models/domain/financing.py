"""
Loan information.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Financing:
    down_payment: float
    interest_rate: float
    loan_term_years: int

    def __post_init__(self) -> None:
        if self.down_payment < 0:
            raise ValueError("Down payment cannot be negative.")

        if not 0 < self.interest_rate < 20:
            raise ValueError("Interest rate should be expressed as a percentage.")

        if self.loan_term_years <= 0:
            raise ValueError("Loan term must be positive.")
