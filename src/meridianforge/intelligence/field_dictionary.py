"""
Known field aliases for property data normalization.
"""

FIELD_ALIASES: dict[str, list[str]] = {
    "purchase_price": [
        "price",
        "purchase price",
        "property price",
        "cost",
        "asking price",
        "list price",
        "sale price",
    ],
    "monthly_rent": [
        "rent",
        "monthly rent",
        "expected rent",
        "monthly income",
        "rental income",
        "rent zestimate",
    ],
    "property_tax": [
        "tax",
        "taxes",
        "property tax",
        "tax amount",
        "tax annual amount",
    ],
    "insurance": [
        "insurance",
        "insurance cost",
        "annual insurance",
    ],
    "hoa": [
        "hoa",
        "hoa fee",
        "monthly hoa",
        "association fee",
    ],
}
