from meridianforge.opportunity.models import (
    Opportunity,
)

from meridianforge.services.acquisition_intake_service import (
    AcquisitionIntakeService,
)


def test_acquisition_intake_converts_opportunity():

    opportunity = Opportunity(
        source_file="zillow_listing.csv",
        fields={
            "property_address": "123 Main St",
            "purchase_price": "250000",
            "market": "Jacksonville",
        },
        confidence=0.90,
    )

    result = AcquisitionIntakeService().convert(
        opportunity,
    )

    assert result.property_address == "123 Main St"
    assert result.purchase_price == 250000
    assert result.market == "Jacksonville"
    assert result.source == "zillow_listing.csv"
