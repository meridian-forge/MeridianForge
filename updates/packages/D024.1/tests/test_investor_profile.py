from meridianforge.domain.investor_profile import InvestorProfile


def test_investor_profile_creation():

    profile = InvestorProfile(
        name="Mahi",
        strategy="Long Term Portfolio Growth",
        primary_goal="Capital Velocity",
        risk_level="Aggressive",
        financing_type="DSCR",
        interest_rate=0.075,
        down_payment_percent=0.20,
        hold_period_years=10,
        target_number_of_properties=5,
        tax_strategy="Depreciation + CPA Reviewed 1031",
    )

    assert profile.validate() is True


def test_investor_profile_serialization():

    profile = InvestorProfile(
        name="Test Investor",
        strategy="Growth",
        primary_goal="Cash Flow",
        risk_level="Moderate",
        financing_type="Conventional",
        interest_rate=0.055,
        down_payment_percent=0.25,
        hold_period_years=10,
        target_number_of_properties=3,
        tax_strategy="CPA Review",
    )

    data = profile.to_dict()

    assert data["financing_type"] == "Conventional"
    assert data["target_number_of_properties"] == 3
