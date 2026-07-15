"""
Income assumptions.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Income:
    monthly_rent: float
    other_monthly_income: float = 0.0

    @property
    def gross_monthly_income(self) -> float:
        return self.monthly_rent + self.other_monthly_income
