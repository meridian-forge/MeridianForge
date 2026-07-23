"""
Portfolio prioritization model.

MF-337.3.1

Investor action classification.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PortfolioPriority:
    """
    Investor portfolio action.
    """

    property_address: str

    rank: int

    score: float

    action: str

    rationale: str
