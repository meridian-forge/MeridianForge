"""
Tests for investor fit engine.
"""

from meridianforge.intelligence.investor_fit_engine import (
    InvestorFitEngine,
)
from meridianforge.intelligence.investor_profile import (
    InvestorProfile,
)


def test_investor_fit_engine_scores_alignment() -> None:
    """
    Validate weighted investor fit calculation.
    """

    profile = InvestorProfile(
        name="Cash Flow Investor",
        strategy="CASH_FLOW",
        risk_tolerance="MODERATE",
        target_cash_flow=0.50,
        appreciation_priority=0.20,
        tax_focus=0.20,
    )

    result = InvestorFitEngine().evaluate(
        profile=profile,
        cash_flow_score=1.00,
        appreciation_score=0.50,
        tax_score=0.75,
        risk_score=0.80,
    )

    assert result.cash_flow_fit == 1.00
    assert result.tax_fit == 0.75
    assert result.overall_score == 0.83
