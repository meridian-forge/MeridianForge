"""
Tests for acquisition opportunity model.
"""

from datetime import datetime

from meridianforge.acquisition.opportunity import (
    Opportunity,
)


def test_opportunity_calculates_cash_flow_and_cap_rate() -> None:
    """
    Validate acquisition metrics.
    """

    opportunity = Opportunity(
        address="123 Main Street",
        city="Jacksonville",
        state="FL",
        zip_code="32210",
        purchase_price=200000,
        monthly_rent=1800,
        monthly_expenses=700,
        market="Jacksonville",
        source="CSV",
        created_at=datetime(2026, 7, 21),
    )

    assert opportunity.monthly_cash_flow == 1100
    assert opportunity.annual_cash_flow == 13200
    assert opportunity.cap_rate == 0.066
