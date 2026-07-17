"""
Recommendation model.

Represents the acquisition decision outcome.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Recommendation:
    """
    Acquisition recommendation result.
    """

    decision: str

    confidence: float

    reason: str
