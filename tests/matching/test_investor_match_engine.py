"""
Tests for investor matching engine.
"""

from datetime import datetime

from meridianforge.acquisition.opportunity import (
    Opportunity,
)
from meridianforge.intelligence.investor_profile import (
    InvestorProfile,
)
from meridianforge.matching.investor_match_engine import (
    InvestorMatchEngine,
)


def test_investor_match_engine_matches_property_to_investor() -> None:
    """
    Validate opportunity investor matching.
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

    investor = InvestorProfile(
        name="Cash Flow Investor",
        strategy="CASH_FLOW",
        risk_tolerance="MODERATE",
        target_cash_flow=0.50,
        appreciation_priority=0.20,
        tax_focus=0.20,
    )

    match = InvestorMatchEngine().match(
        opportunity,
        investor,
    )

    assert match.investor_name == "Cash Flow Investor"
    assert match.property_address == "123 Main Street"
    assert match.fit_score.overall_score > 0.70
