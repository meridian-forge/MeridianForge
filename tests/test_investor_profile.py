"""
Investor profile tests.
"""

from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)


def test_investor_profile_creation() -> None:
    """
    Verify investor profile creation.
    """

    profile = InvestorProfile(
        name="Mahi Growth Income Strategy",
        strategy=InvestmentStrategy.BALANCED,
        preferred_states=[
            "fl",
            "tx",
        ],
    )

    assert profile.name == "Mahi Growth Income Strategy"

    assert profile.strategy == InvestmentStrategy.BALANCED

    assert profile.preferred_states == [
        "FL",
        "TX",
    ]
