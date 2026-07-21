"""
Tests for investment thesis model.
"""

from meridianforge.intelligence.investment_thesis import (
    InvestmentThesis,
)


def test_investment_thesis_creation() -> None:
    """
    Validate investment thesis structure.
    """

    thesis = InvestmentThesis(
        recommendation="BUY",
        confidence=0.90,
        rationale="Strong cash flow opportunity",
        investor_fit="Cash flow investor",
    )

    thesis.add_strength(
        "Positive rental yield",
    )

    thesis.add_risk(
        "Market vacancy risk",
    )

    assert thesis.recommendation == "BUY"
    assert thesis.confidence == 0.90
    assert len(thesis.strengths) == 1
    assert len(thesis.risks) == 1
