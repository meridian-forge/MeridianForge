"""
Sample Excel proforma fixture.

Represents normalized values extracted
from a provider investment spreadsheet.
"""


def sample_proforma_property() -> dict[str, object]:

    return {
        "source": "EXCEL",
        "provider": "JWB",
        "address": "789 Rental Drive",
        "purchase_price": 210000,
        "monthly_rent": 1850,
        "annual_taxes": 2400,
        "annual_insurance": 1500,
        "management_percent": 0.10,
        "vacancy_percent": 0.05,
        "loan_to_value": 0.75,
        "loan_term_years": 30,
    }
