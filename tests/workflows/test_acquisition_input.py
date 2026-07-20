from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


def test_acquisition_input_creation():

    opportunity = AcquisitionInput(
        property_address="123 Main St",
        purchase_price=250000,
        market="Jacksonville",
        source="Zillow",
    )

    assert opportunity.property_address == "123 Main St"
    assert opportunity.purchase_price == 250000
    assert opportunity.market == "Jacksonville"
    assert opportunity.source == "Zillow"
