"""
Stress testing scenario definition.

A Scenario describes changes applied
to a property during analysis.

It does not perform calculations.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Scenario:
    """
    Defines a stress test scenario.

    Percentage values are expressed as decimals.

    Examples:
        -10% rent = -0.10
        +25% expenses = 0.25
        +1% interest rate = 0.01
    """

    name: str

    rent_change_percent: float = 0.0

    expense_change_percent: float = 0.0

    interest_rate_change_percent: float = 0.0

    vacancy_change_percent: float = 0.0
