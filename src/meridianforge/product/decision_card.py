"""
Investor decision card.

Human-readable investment decision artifact.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class InvestorDecisionCard:
    """
    Summary card for investor action.
    """

    rank: int

    property_address: str

    recommendation: str

    confidence: float

    reasons: list[str] = field(
        default_factory=list,
    )

    risks: list[str] = field(
        default_factory=list,
    )

    def is_buy_candidate(self) -> bool:
        """
        Determine if property is an active buy candidate.
        """

        return self.recommendation.upper() == "BUY" and self.confidence >= 0.75
