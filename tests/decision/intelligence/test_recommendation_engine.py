"""
Tests for recommendation engine.
"""

from meridianforge.decision.intelligence.decision_context import (
    DecisionContext,
)
from meridianforge.decision.intelligence.decision_recommendation import (
    RecommendationAction,
)
from meridianforge.decision.intelligence.recommendation_engine import (
    RecommendationEngine,
)


def test_recommendation_engine_returns_buy_for_strong_property() -> None:
    """
    Positive cash flow and strong yield should produce BUY.
    """

    context = DecisionContext(
        property_address="123 Main St",
        market="Jacksonville",
        purchase_price=250000,
        monthly_rent=2500,
        monthly_expenses=1000,
        noi=18000,
        cap_rate=0.072,
        monthly_cash_flow=1500,
        investor_strategy="CASH_FLOW",
    )

    result = RecommendationEngine().evaluate(
        context,
    )

    assert result.action == RecommendationAction.BUY
    assert result.confidence >= 0.85
    assert len(result.reasons) > 0


def test_recommendation_engine_returns_pass_for_negative_cash_flow() -> None:
    """
    Negative cash flow should produce PASS.
    """

    context = DecisionContext(
        property_address="456 Oak Ave",
        market="Memphis",
        purchase_price=200000,
        monthly_rent=1200,
        monthly_expenses=1500,
        noi=-3600,
        cap_rate=0.02,
        monthly_cash_flow=-300,
        investor_strategy="CASH_FLOW",
    )

    result = RecommendationEngine().evaluate(
        context,
    )

    assert result.action == RecommendationAction.PASS
    assert result.confidence >= 0.80
    assert len(result.risks) > 0
