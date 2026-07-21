"""
Tests for personalized thesis builder.
"""

from meridianforge.intelligence.investor_fit_engine import (
    InvestorFitScore,
)
from meridianforge.intelligence.investor_profile import (
    InvestorProfile,
)
from meridianforge.services.personalized_thesis_builder import (
    PersonalizedThesisBuilder,
)


def test_personalized_thesis_builder_creates_investor_specific_thesis() -> None:
    """
    Validate personalized thesis generation.
    """

    profile = InvestorProfile(
        name="Cash Flow Investor",
        strategy="CASH_FLOW",
        risk_tolerance="MODERATE",
        target_cash_flow=0.50,
        appreciation_priority=0.20,
        tax_focus=0.20,
    )

    fit_score = InvestorFitScore(
        cash_flow_fit=1.00,
        appreciation_fit=0.50,
        tax_fit=0.75,
        risk_fit=0.80,
        overall_score=0.83,
    )

    thesis = PersonalizedThesisBuilder().build(
        profile=profile,
        fit_score=fit_score,
        property_name="123 Main Street",
        recommendation="BUY",
    )

    assert "123 Main Street" in thesis.rationale
    assert thesis.recommendation == "BUY"
    assert thesis.confidence == 0.83
    assert "83%" in thesis.investor_fit
