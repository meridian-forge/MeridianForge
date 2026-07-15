"""
Deal evaluation result model.

Represents whether a property matches
an investor profile.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class DealEvaluation:
    """
    Investor criteria evaluation result.
    """

    qualified: bool

    score: float

    reasons: list[str] = field(
        default_factory=list,
    )

    failed_criteria: list[str] = field(
        default_factory=list,
    )
