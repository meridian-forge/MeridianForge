"""
Investor package builder.

Combines analysis outputs into a reusable
investor deliverable object.
"""

from meridianforge.decision.intelligence.decision_recommendation import (
    DecisionRecommendation,
)
from meridianforge.models.results.investor_package import (
    InvestorPackage,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)


class InvestorPackageBuilder:
    """
    Build investor-facing package.
    """

    @staticmethod
    def build(
        review: WeeklyInvestorReview,
        recommendation: DecisionRecommendation | None = None,
    ) -> InvestorPackage:
        """
        Create investor package.
        """

        return InvestorPackage(
            review=review,
            recommendation=recommendation,
        )
