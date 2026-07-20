from meridianforge.decision.pipeline import (
    DecisionPipeline,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


def test_decision_pipeline_creates_review():

    opportunity = AcquisitionInput(
        property_address="123 Main St",
        purchase_price=250000,
        market="Jacksonville",
        source="Zillow",
    )

    review = DecisionPipeline().evaluate(
        opportunity,
    )

    assert len(review.cards) == 1

    card = review.cards[0]

    assert card.property_address
    assert card.recommendation in [
        "BUY",
        "REVIEW",
    ]

    assert 0 <= card.confidence <= 1
