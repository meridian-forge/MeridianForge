"""
Sample real estate opportunity fixture.
"""


def sample_property() -> dict[str, object]:
    return {
        "address": "123 Example Street",
        "purchase_price": 215000,
        "monthly_rent": 1850,
        "property_management": 185,
        "insurance": 120,
        "taxes": 220,
        "maintenance": 100,
        "vacancy": 90,
    }
