from meridianforge.workflows.acquisition_decision_workflow import (
    AcquisitionDecisionWorkflow,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


def test_acquisition_decision_workflow_creates_review():

    opportunity = AcquisitionInput(
        property_address="123 Main St",
        purchase_price=250000,
        market="Jacksonville",
        source="Zillow",
    )

    review = AcquisitionDecisionWorkflow().execute(
        opportunity,
    )

    assert len(review.cards) == 1

    card = review.cards[0]

    assert card.property_address
    assert card.recommendation in [
        "BUY",
        "REVIEW",
    ]
