"""
Decision recommendation model.

Represents the investment decision produced
by Meridian Forge intelligence services.
"""

from dataclasses import dataclass, field
from enum import StrEnum


class RecommendationAction(StrEnum):
    """
    Available investment recommendations.
    """

    BUY = "BUY"
    WATCH = "WATCH"
    PASS = "PASS"


@dataclass(slots=True)
class DecisionRecommendation:
    """
    Investor-facing recommendation output.
    """

    action: RecommendationAction

    confidence: float

    reasons: list[str] = field(
        default_factory=list,
    )

    risks: list[str] = field(
        default_factory=list,
    )

    next_steps: list[str] = field(
        default_factory=list,
    )

    def __post_init__(self) -> None:
        """
        Validate recommendation confidence.
        """

        if not 0 <= self.confidence <= 1:
            raise ValueError("Confidence must be between 0 and 1.")
