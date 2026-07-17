from meridianforge.services.property_extraction_service import (
    PropertyExtractionService,
)


def test_property_extraction_service() -> None:

    result = PropertyExtractionService.extract(
        "Price: $100000 Rent: $1200",
    )

    assert result.purchase_price == 100000
