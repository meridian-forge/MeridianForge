"""
Real estate import template definition.

Defines the standard fields Meridian Forge accepts
for property analysis imports.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RealEstateImportField:
    """
    Import field definition.
    """

    canonical_name: str

    required: bool

    aliases: tuple[str, ...]


REAL_ESTATE_IMPORT_FIELDS = (
    RealEstateImportField(
        canonical_name="purchase_price",
        required=True,
        aliases=(
            "price",
            "purchase price",
            "purchase cost",
            "cost",
        ),
    ),
    RealEstateImportField(
        canonical_name="monthly_rent",
        required=True,
        aliases=(
            "rent",
            "monthly rent",
            "monthly income",
        ),
    ),
    RealEstateImportField(
        canonical_name="property_tax",
        required=False,
        aliases=(
            "tax",
            "taxes",
            "property taxes",
        ),
    ),
    RealEstateImportField(
        canonical_name="insurance",
        required=False,
        aliases=(
            "ins",
            "insurance cost",
        ),
    ),
    RealEstateImportField(
        canonical_name="hoa",
        required=False,
        aliases=(
            "hoa",
            "hoa fees",
        ),
    ),
    RealEstateImportField(
        canonical_name="state",
        required=False,
        aliases=(
            "location",
            "state",
        ),
    ),
)
