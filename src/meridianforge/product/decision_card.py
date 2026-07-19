"""
Investor decision card.

Human-readable investment decision artifact.
"""

from dataclasses import dataclass, field


@dataclass(slots=True, init=False)
class InvestorDecisionCard:
    """
    Summary card for investor action.
    """

    rank: int
    property_address: str
    recommendation: str
    confidence: float
    strengths: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)

    def __init__(
        self,
        rank: int,
        property_address: str,
        recommendation: str,
        confidence: float,
        strengths: list[str] | None = None,
        risks: list[str] | None = None,
        reasons: list[str] | None = None,
    ) -> None:
        self.rank = rank
        self.property_address = property_address
        self.recommendation = recommendation
        self.confidence = confidence
        self.strengths = strengths if strengths is not None else (reasons or [])
        self.risks = risks or []

    @property
    def reasons(self) -> list[str]:
        """
        Backward-compatible alias for strengths.
        """

        return self.strengths

    def is_buy_candidate(self) -> bool:
        """
        Determine if property is an active buy candidate.
        """

        return self.recommendation.upper() == "BUY" and self.confidence >= 0.75
