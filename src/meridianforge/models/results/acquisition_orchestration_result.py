"""
Acquisition orchestration result.

Represents the complete output from the
acquisition analysis workflow.
"""

from dataclasses import dataclass
from pathlib import Path

from meridianforge.decision.intelligence.decision_recommendation import (
    DecisionRecommendation,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)


@dataclass(slots=True)
class AcquisitionOrchestrationResult:
    """
    Complete acquisition workflow output.

    Includes:
    - Weekly investor review
    - Generated package location
    - Decision recommendation
    """

    review: WeeklyInvestorReview

    package_location: Path | None = None

    recommendation: DecisionRecommendation | None = None
