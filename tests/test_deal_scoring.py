"""
Deal scoring tests.
"""

from meridianforge.engine.criteria_engine import (
    CriteriaEngine,
)
from meridianforge.engine.deal_scoring import (
    DealScoringEngine,
)
from meridianforge.engine.underwriting_engine import (
    UnderwritingEngine,
)
from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)


def test_deal_scoring_generates_score() -> None:
    """
    Verify scoring calculation.
    """

    from tests.test_criteria_engine import (
        create_sample_property,
    )

    property_data = create_sample_property()

    analysis = UnderwritingEngine.analyze(
        property_data,
    )

    profile = InvestorProfile(
        name="Balanced Investor",
        strategy=InvestmentStrategy.BALANCED,
        minimum_dscr=1.20,
        minimum_cap_rate=6.0,
        minimum_cash_on_cash=8.0,
        maximum_purchase_price=300000,
    )

    evaluation = CriteriaEngine.evaluate(
        profile,
        analysis,
    )

    result = DealScoringEngine.evaluate(
        analysis,
        evaluation,
    )

    assert result.score > 0

    assert result.score <= 100
