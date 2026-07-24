"""
Investor alert models.

MF-347.2
"""

from dataclasses import dataclass


@dataclass(slots=True)
class InvestorAlert:
    """
    Investor portfolio alert.
    """

    severity: str

    title: str

    message: str
