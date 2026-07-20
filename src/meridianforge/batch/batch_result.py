"""
Batch processing result model.
"""

from dataclasses import dataclass, field

from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)


@dataclass(slots=True)
class BatchResult:
    """
    Result from processing multiple acquisition opportunities.
    """

    reviews: list[WeeklyInvestorReview] = field(
        default_factory=list,
    )

    @property
    def total_reviews(self) -> int:
        return len(self.reviews)
