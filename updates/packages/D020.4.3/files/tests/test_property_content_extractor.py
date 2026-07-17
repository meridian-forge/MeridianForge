from meridianforge.extractors.property_content_extractor import (
    PropertyContentExtractor,
)


def test_property_content_extractor() -> None:

    text = """
    3 bedroom rental.
    Purchase Price: $215,000
    Rent: $1,850
    Taxes: $2,400
    Insurance: $1,200
    """

    result = PropertyContentExtractor.extract(
        text,
    )

    assert result.purchase_price == 215000
    assert result.monthly_rent == 1850
    assert result.bedrooms == 3
