import pytest

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

    with pytest.raises(NotImplementedError):

        DecisionPipeline().evaluate(
            opportunity,
        )
