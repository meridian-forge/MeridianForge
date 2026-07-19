"""
Investor workflow service.

Transforms internal analysis outputs
into investor-facing review artifacts.
"""

from meridianforge.models.results.deal_evaluation import (
    DealEvaluation,
)
from meridianforge.models.results.ranked_deal import (
    RankedDeal,
)
from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)
from meridianforge.product.investor_review import (
    InvestorReview,
)


class InvestorWorkflowService:
    """
    Creates investor reviews from ranked opportunities.
    """

    def create_review(
        self,
        ranked_deal: RankedDeal,
    ) -> InvestorReview:
        """
        Convert ranked deal into investor review.
        """

        evaluation: DealEvaluation = ranked_deal.evaluation

        recommendation = "BUY" if evaluation.qualified else "WATCH"

        confidence = evaluation.score / 100

        strengths = list(evaluation.reasons)

        risks = list(evaluation.failed_criteria)

        return InvestorReview(
            rank=ranked_deal.rank,
            property_address=ranked_deal.property.address.display(),
            recommendation=recommendation,
            confidence=confidence,
            strengths=strengths,
            risks=risks,
        )

    def create_decision_card(
        self,
        review: InvestorReview,
    ) -> InvestorDecisionCard:
        """
        Convert investor review into decision card.
        """

        return InvestorDecisionCard(
            rank=review.rank,
            property_address=review.property_address,
            recommendation=review.recommendation,
            confidence=review.confidence,
            strengths=review.strengths,
            risks=review.risks,
        )
