import pytest

from meridianforge.batch.batch_request import (
    BatchRequest,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


def test_batch_request_accepts_opportunities():

    request = BatchRequest(
        opportunities=[
            AcquisitionInput(
                property_address="123 Main St",
                purchase_price=250000,
                market="Jacksonville",
                source="Zillow",
            ),
        ]
    )

    assert len(request.opportunities) == 1


def test_batch_request_requires_opportunities():

    with pytest.raises(ValueError):

        BatchRequest()
