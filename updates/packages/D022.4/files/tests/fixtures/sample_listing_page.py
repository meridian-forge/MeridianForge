"""
Sample website listing fixture.

Represents property information extracted
from a provider listing page.
"""


def sample_listing_property() -> dict[str, object]:

    return {
        "source": "WEB",
        "provider": "Rent To Retirement",
        "address": "321 Market Street",
        "purchase_price": 230000,
        "monthly_rent": 2000,
        "property_type": "Single Family",
        "market": "Jacksonville FL",
        "year_built": 2025,
    }
