"""
Acquisition intelligence service.

Converts investment pipeline outputs
into investor decision artifacts.
"""

from meridianforge.models.results.investment_pipeline_result import (
    InvestmentPipelineResult,
)
from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)


class AcquisitionIntelligenceService:
    """
    Creates investor-facing decisions
    from pipeline results.
    """

    def create_review(
        self,
        result: InvestmentPipelineResult,
    ) -> WeeklyInvestorReview:
        """
        Convert ranked deals into investor review.
        """

        cards = []

        for deal in result.ranked_deals:

            recommendation = "BUY" if deal.evaluation.qualified else "WATCH"

            confidence = min(
                deal.evaluation.score / 100,
                1.0,
            )

            cards.append(
                InvestorDecisionCard(
                    rank=deal.rank,
                    property_address=(deal.property.address.display()),
                    recommendation=recommendation,
                    confidence=confidence,
                    strengths=list(deal.evaluation.reasons),
                    risks=list(deal.evaluation.failed_criteria),
                )
            )

        return WeeklyInvestorReview(
            cards=cards,
        )
