"""
Investor decision workflow.

MF-356.1

Transforms investor review artifacts into
an actionable acquisition decision package.
"""

from meridianforge.models.results.ranked_opportunity import (
    RankedOpportunity,
)
from meridianforge.product.investor_decision_package import (
    InvestorDecisionPackage,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.ranking.opportunity_ranker import (
    OpportunityRanker,
)


class InvestorDecisionWorkflow:
    """
    Creates investor acquisition decision packages.
    """

    def __init__(
        self,
        ranker: OpportunityRanker | None = None,
    ) -> None:
        self.ranker = ranker or OpportunityRanker()

    def run(
        self,
        review: WeeklyInvestorReview,
    ) -> InvestorDecisionPackage:
        """
        Generate investor decision package.
        """

        ranked = self.ranker.rank(
            [review],
        )

        return InvestorDecisionPackage(
            ranked_opportunities=ranked,
            buy_candidates=review.buy_candidates(),
            watch_candidates=review.watch_candidates(),
        )
