from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.workflows.acquisition_context import (
    AcquisitionRunContext,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


def test_acquisition_run_context():

    opportunity = AcquisitionInput(
        property_address="123 Main St",
        purchase_price=250000,
        market="Jacksonville",
        source="Zillow",
    )

    review = WeeklyInvestorReview(
        cards=[
            InvestorDecisionCard(
                rank=1,
                property_address="123 Main St",
                recommendation="BUY",
                confidence=0.91,
                strengths=[
                    "Strong cash flow",
                ],
                risks=[],
            ),
        ]
    )

    context = AcquisitionRunContext(
        opportunity=opportunity,
        review=review,
    )

    assert context.opportunity.market == "Jacksonville"
    assert context.review.cards[0].recommendation == "BUY"
