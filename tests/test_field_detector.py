"""
Field detector tests.
"""

from meridianforge.intelligence.field_detector import (
    FieldDetector,
)


def test_detect_purchase_price() -> None:
    """
    Verify price fields are detected.
    """

    mappings = FieldDetector.detect(
        [
            "Property Price",
        ]
    )

    assert len(mappings) == 1
    assert mappings[0].target_field == "purchase_price"
    assert mappings[0].confidence == 0.90


def test_detect_multiple_fields() -> None:
    """
    Verify multiple fields are detected.
    """

    mappings = FieldDetector.detect(
        [
            "Price",
            "Monthly Rent",
            "HOA Fee",
        ]
    )

    targets = [item.target_field for item in mappings]

    assert "purchase_price" in targets
    assert "monthly_rent" in targets
    assert "hoa" in targets


def test_unknown_field_is_ignored() -> None:
    """
    Verify unknown columns are not mapped.
    """

    mappings = FieldDetector.detect(
        [
            "Something Random",
        ]
    )

    assert mappings == []
