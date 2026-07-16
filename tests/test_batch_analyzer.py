"""
Batch analyzer service tests.
"""

from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.services.batch_analyzer import (
    BatchAnalyzerService,
)
from tests.test_criteria_engine import create_sample_property


def test_batch_analysis_returns_ranked_deals() -> None:
    """
    Verify batch analyzer returns ranked results.
    """

    properties = [
        create_sample_property(),
        create_sample_property(),
        create_sample_property(),
    ]

    profile = InvestorProfile(
        name="Balanced Investor",
        strategy=InvestmentStrategy.BALANCED,
        minimum_dscr=1.20,
        minimum_cap_rate=6.0,
        minimum_cash_on_cash=8.0,
        maximum_purchase_price=300000,
    )

    ranked = BatchAnalyzerService.analyze(
        properties,
        profile,
    )

    assert len(ranked.ranked_deals) == 3
    assert ranked.ranked_deals[0].rank == 1
    assert ranked.ranked_deals[-1].rank == 3
