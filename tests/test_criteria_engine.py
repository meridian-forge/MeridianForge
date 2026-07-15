"""
Criteria engine tests.
"""

from meridianforge.engine.criteria_engine import (
    CriteriaEngine,
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


def create_sample_property():
    """
    Create sample investment property.
    """

    from tests.test_underwriting_engine import (
        create_sample_property as sample_property,
    )

    return sample_property()


def test_property_meets_investor_criteria() -> None:
    """
    Verify qualified property.
    """

    property_data = create_sample_property()

    analysis = UnderwritingEngine.analyze(
        property_data,
    )

    profile = InvestorProfile(
        name="Growth Income Strategy",
        strategy=InvestmentStrategy.BALANCED,
        minimum_dscr=1.20,
        minimum_cap_rate=6.0,
        minimum_cash_on_cash=8.0,
        maximum_purchase_price=300000,
    )

    result = CriteriaEngine.evaluate(
        profile,
        analysis,
    )

    assert result.qualified is True

    assert result.score == 100


def test_property_fails_price_limit() -> None:
    """
    Verify failed criteria.
    """

    property_data = create_sample_property()

    analysis = UnderwritingEngine.analyze(
        property_data,
    )

    profile = InvestorProfile(
        name="Low Price Strategy",
        strategy=InvestmentStrategy.CASH_FLOW,
        maximum_purchase_price=100000,
    )

    result = CriteriaEngine.evaluate(
        profile,
        analysis,
    )

    assert result.qualified is False

    assert "Purchase price exceeds maximum" in result.failed_criteria
