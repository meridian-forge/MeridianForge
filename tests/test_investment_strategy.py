"""
Investment strategy tests.
"""

from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)


def test_strategy_values() -> None:
    """
    Verify strategy definitions.
    """

    assert InvestmentStrategy.GROWTH.value == "GROWTH"

    assert InvestmentStrategy.CASH_FLOW.value == "CASH_FLOW"
