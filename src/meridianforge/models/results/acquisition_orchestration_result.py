"""
Acquisition orchestration result.

Represents complete investor workflow output.
"""

from dataclasses import dataclass
from pathlib import Path

from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)


@dataclass(slots=True)
class AcquisitionOrchestrationResult:
    """
    Complete acquisition intelligence output.
    """

    review: WeeklyInvestorReview

    package_location: Path | None = None
