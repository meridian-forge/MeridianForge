"""
Investment workflow integration tests.

Validates the complete Meridian Forge
user-facing investment analysis flow.
"""

from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.services.investment_workflow import (
    InvestmentWorkflow,
)


def test_investment_workflow_generates_report() -> None:
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

    workflow = InvestmentWorkflow()

    result = workflow.analyze(
        records,
        investor,
    )

    assert result.pipeline_result is not None

    assert len(result.pipeline_result.ranked_deals) == 3

    assert result.report.total_opportunities == 3

    assert result.report.title == "Meridian Forge Investment Report"

    assert len(result.report.recommendations) > 0
