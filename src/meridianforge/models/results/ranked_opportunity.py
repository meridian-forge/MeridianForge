"""
Ranked investor opportunity model.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class RankedOpportunity:
    """
    Ranked investor decision opportunity.
    """

    rank: int
    property_address: str
    recommendation: str
    confidence: float
