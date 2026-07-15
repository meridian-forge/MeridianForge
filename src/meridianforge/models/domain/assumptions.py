"""
Analysis assumptions.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Assumptions:
    vacancy_rate: float = 5.0
    appreciation_rate: float = 3.0
    rent_growth_rate: float = 3.0
