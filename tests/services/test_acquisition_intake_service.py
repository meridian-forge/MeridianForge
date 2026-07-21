"""
Tests for acquisition intake service.
"""

from meridianforge.services.acquisition_intake_service import (
    AcquisitionIntakeService,
)


def test_acquisition_intake_creates_opportunity() -> None:
    """
    Validate raw acquisition conversion.
    """

    data = {
        "address": "456 Oak Avenue",
        "city": "Jacksonville",
        "state": "FL",
        "zip_code": "32210",
        "purchase_price": 200000,
        "monthly_rent": 1800,
        "monthly_expenses": 700,
        "market": "Jacksonville",
        "source": "CSV",
    }

    opportunity = AcquisitionIntakeService().create_opportunity(
        data,
    )

    assert opportunity.address == "456 Oak Avenue"
    assert opportunity.monthly_cash_flow == 1100
    assert opportunity.cap_rate == 0.066
