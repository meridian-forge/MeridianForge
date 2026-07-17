"""
Sample provider email fixture.

Represents property information embedded
directly inside an email body.
"""


def sample_email_property() -> dict[str, object]:

    return {
        "source": "EMAIL",
        "provider": "Rent To Retirement",
        "address": "456 Investment Avenue",
        "purchase_price": 225000,
        "monthly_rent": 1950,
        "property_type": "Single Family",
        "market": "Jacksonville FL",
    }
