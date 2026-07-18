from meridianforge.opportunity.models import Opportunity
from meridianforge.validation.checker import (
    validate_opportunity,
)


def test_missing_fields_detection() -> None:

    opportunity = Opportunity(
        source_file="deal.xlsx",
        fields={
            "purchase_price": "250000",
        },
    )

    result = validate_opportunity(opportunity)

    assert "rent" in result.missing_fields
