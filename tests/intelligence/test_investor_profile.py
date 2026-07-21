"""
Tests for investor profile model.
"""

from meridianforge.intelligence.investor_profile import (
    InvestorProfile,
)


def test_investor_profile_creation() -> None:
    """
    Validate investor profile structure.
    """

    profile = InvestorProfile(
        name="Cash Flow Investor",
        strategy="CASH_FLOW",
        risk_tolerance="AGGRESSIVE",
        target_cash_flow=0.08,
        appreciation_priority=0.40,
        tax_focus=0.70,
    )

    assert profile.name == "Cash Flow Investor"
    assert profile.strategy == "CASH_FLOW"
    assert profile.risk_tolerance == "AGGRESSIVE"
    assert profile.target_cash_flow == 0.08
    assert profile.tax_focus == 0.70
