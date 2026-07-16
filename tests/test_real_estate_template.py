"""
Real estate import template tests.
"""

from meridianforge.importers.real_estate_template import (
    REAL_ESTATE_IMPORT_FIELDS,
)


def test_real_estate_template_contains_required_fields() -> None:
    names = [field.canonical_name for field in REAL_ESTATE_IMPORT_FIELDS]

    assert "purchase_price" in names
    assert "monthly_rent" in names


def test_real_estate_template_aliases_exist() -> None:
    price_field = next(
        field
        for field in REAL_ESTATE_IMPORT_FIELDS
        if field.canonical_name == "purchase_price"
    )

    assert "price" in price_field.aliases
