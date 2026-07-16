"""
Normalization engine tests.
"""

from meridianforge.models.results.field_mapping import (
    FieldMapping,
)
from meridianforge.normalization.normalizer import (
    Normalizer,
)


def test_normalize_property_record() -> None:
    """
    Verify raw fields normalize correctly.
    """

    record = {
        "Property Price": "250000",
        "Monthly Rent": "2200",
    }

    mappings = [
        FieldMapping(
            source_field="Property Price",
            target_field="purchase_price",
            confidence=0.90,
        ),
        FieldMapping(
            source_field="Monthly Rent",
            target_field="monthly_rent",
            confidence=0.90,
        ),
    ]

    asset = Normalizer.normalize(
        record,
        mappings,
        asset_type="REAL_ESTATE",
    )

    assert asset.asset_type == "REAL_ESTATE"
    assert asset.attributes["purchase_price"] == "250000"
    assert asset.attributes["monthly_rent"] == "2200"


def test_unknown_fields_are_ignored() -> None:
    """
    Verify unmapped fields are not included.
    """

    record = {
        "Random Field": "123",
    }

    asset = Normalizer.normalize(
        record,
        [],
    )

    assert asset.attributes == {}
