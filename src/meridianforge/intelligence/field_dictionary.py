"""
Known field aliases for property data normalization.
"""

FIELD_ALIASES: dict[str, list[str]] = {
    "purchase_price": [
        "price",
        "purchase price",
        "purchase_price",
        "property price",
        "cost",
        "asking price",
        "list price",
        "sale price",
    ],
    "monthly_rent": [
        "rent",
        "monthly rent",
        "monthly_rent",
        "expected rent",
        "monthly income",
        "rental income",
        "rent zestimate",
    ],
    "address": [
        "address",
        "property address",
        "property_address",
        "street",
    ],
    "market": [
        "market",
        "city market",
        "location",
    ],
    "noi": [
        "noi",
        "net operating income",
        "net income",
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
