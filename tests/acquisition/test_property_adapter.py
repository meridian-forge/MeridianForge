"""
Tests for acquisition property adapter.

MF-333.4
"""

from datetime import datetime

from meridianforge.acquisition.opportunity import (
    Opportunity,
)

from meridianforge.acquisition.property_adapter import (
    AcquisitionPropertyAdapter,
)

from meridianforge.models.domain.property import (
    Property,
)


def test_property_adapter_creates_canonical_property() -> None:
    """
    Acquisition opportunity should convert into
    canonical underwriting Property.
    """

    opportunity = Opportunity(
        address="123 Main",
        city="Philadelphia",
        state="PA",
        zip_code="19143",
        purchase_price=200000,
        monthly_rent=2000,
        monthly_expenses=800,
        market="Philadelphia",
        source="test",
        created_at=datetime.now(),
    )

    adapter = AcquisitionPropertyAdapter()

    result = adapter.convert(
        opportunity,
    )

    assert isinstance(
        result,
        Property,
    )

    assert result.acquisition.purchase_price == 200000

    assert result.income.monthly_rent == 2000

    assert result.address.city == "Philadelphia"


def test_property_adapter_creates_financing_defaults() -> None:
    """
    Adapter should provide initial financing
    assumptions.
    """

    opportunity = Opportunity(
        address="456 Market",
        city="Philadelphia",
        state="PA",
        zip_code="19131",
        purchase_price=300000,
        monthly_rent=3000,
        monthly_expenses=1000,
        market="Philadelphia",
        source="test",
        created_at=datetime.now(),
    )

    result = AcquisitionPropertyAdapter().convert(
        opportunity,
    )

    assert result.financing.down_payment == 60000

    assert result.financing.loan_term_years == 30

    assert result.financing.interest_rate == 7.0
