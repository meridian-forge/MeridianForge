from meridianforge.decision.pipeline import (
    DecisionPipeline,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


def test_decision_pipeline_contract():

    opportunity = AcquisitionInput(
        property_address="123 Main St",
        purchase_price=250000,
        market="Jacksonville",
        source="Zillow",
    )

    review = DecisionPipeline().evaluate(
        opportunity,
    )

    assert review.cards

    card = review.cards[0]

    assert card.property_address
    assert card.recommendation in [
        "BUY",
        "REVIEW",
    ]
    assert 0 <= card.confidence <= 1
