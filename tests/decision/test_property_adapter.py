from meridianforge.decision.property_adapter import (
    AcquisitionPropertyAdapter,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


def test_acquisition_property_adapter_builds_property():

    opportunity = AcquisitionInput(
        property_address="123 Main St",
        purchase_price=250000,
        market="Jacksonville",
        source="Zillow",
    )

    result = AcquisitionPropertyAdapter().build(
        opportunity,
    )

    assert result.acquisition.purchase_price == 250000

    assert result.address.street == "123 Main St"

    assert result.metadata.provider == "Zillow"

    assert result.financing.loan_term_years == 30
