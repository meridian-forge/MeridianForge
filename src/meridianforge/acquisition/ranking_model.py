"""
Acquisition ranking model.

MF-337.1

Represents ranked investment opportunities.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class RankingResult:
    """
    Ranked acquisition opportunity.
    """

    property_address: str

    rank: int

    score: float

    category: str

    recommendation: str
