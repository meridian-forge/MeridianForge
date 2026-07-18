from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.opportunity.models import OpportunityType
from meridianforge.opportunity.normalizer import normalize


def test_normalize_rental_property() -> None:

    extracted = ExtractedData(
        source_file="property.xlsx",
        fields={
            "Purchase Price": "250000",
            "Monthly Rent": "2200",
        },
    )

    result = normalize(extracted)

    assert result.opportunity_type == OpportunityType.RENTAL_PROPERTY
    assert result.fields["purchase_price"] == "250000"
