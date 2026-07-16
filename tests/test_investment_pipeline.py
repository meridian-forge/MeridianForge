"""
Investment pipeline integration tests.
"""

from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.services.investment_pipeline import (
    InvestmentPipeline,
)


def test_investment_pipeline_ranks_properties() -> None:
    investor = InvestorProfile(
        name="MVP Investor",
        strategy=InvestmentStrategy.CASH_FLOW,
        minimum_dscr=1.10,
        minimum_cap_rate=5.0,
        minimum_cash_on_cash=5.0,
        maximum_purchase_price=500000,
    )

    records = [
        {
            "purchase_price": 200000,
            "monthly_rent": 2200,
            "property_tax": 2400,
            "insurance": 1200,
            "state": "FL",
        },
        {
            "purchase_price": 250000,
            "monthly_rent": 2300,
            "property_tax": 3000,
            "insurance": 1400,
            "state": "FL",
        },
        {
            "purchase_price": 180000,
            "monthly_rent": 1700,
            "property_tax": 2200,
            "insurance": 1100,
            "state": "TN",
        },
    ]

    pipeline = InvestmentPipeline()

    result = pipeline.analyze(
        records,
        investor,
    )

    assert len(result.ranked_deals) == 3

    assert (
        result.ranked_deals[0].evaluation.score
        >= result.ranked_deals[1].evaluation.score
    )

    assert (
        result.ranked_deals[1].evaluation.score
        >= result.ranked_deals[2].evaluation.score
    )
