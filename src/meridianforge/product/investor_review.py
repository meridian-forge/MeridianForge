"""
Investor review product model.

Combines existing analysis outputs into
an investor decision artifact.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class InvestorReview:
    """
    Investor-facing opportunity summary.
    """

    rank: int

    property_address: str

    recommendation: str

    confidence: float

    metrics: dict[str, float] = field(
        default_factory=dict,
    )

    strengths: list[str] = field(
        default_factory=list,
    )

    risks: list[str] = field(
        default_factory=list,
    )

    def is_actionable(self) -> bool:
        """
        Determines whether review contains
        enough information for investor action.
        """

        return self.recommendation != "UNKNOWN" and self.confidence > 0
