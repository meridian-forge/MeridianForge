"""
Operating expenses.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Expenses:
    taxes: float
    insurance: float
    hoa: float = 0.0
    maintenance: float = 0.0
    management: float = 0.0
