import pytest

from meridianforge.intelligence.models import (
    InvestorProfile,
)


def test_valid_profile() -> None:

    profile = InvestorProfile(goal="cash_flow")

    assert profile.goal == "cash_flow"


def test_invalid_weights() -> None:

    with pytest.raises(ValueError):

        InvestorProfile(
            goal="growth",
            cashflow_weight=2.0,
        )
