"""
Acquisition decision model.

MF-334.1

Represents the recommendation generated
after scoring and risk evaluation.
"""

from dataclasses import dataclass, field

from meridianforge.acquisition.risk import (
    RiskFlag,
)


@dataclass(slots=True)
class AcquisitionDecision:
    """
    Final acquisition recommendation.
    """

    status: str

    score: float

    reasons: list[str] = field(
        default_factory=list,
    )

    risks: list[RiskFlag] = field(
        default_factory=list,
    )
