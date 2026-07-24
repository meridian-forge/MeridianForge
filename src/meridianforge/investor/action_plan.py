"""
Investor action plan model.

MF-347.2
"""

from dataclasses import dataclass


@dataclass(slots=True)
class InvestorAction:
    """
    Single investor action item.
    """

    priority: int

    title: str

    reason: str


@dataclass(slots=True)
class InvestorActionPlan:
    """
    Collection of investor actions.
    """

    actions: list[InvestorAction]
