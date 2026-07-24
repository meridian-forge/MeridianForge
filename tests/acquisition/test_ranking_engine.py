from datetime import datetime

from meridianforge.acquisition.opportunity import (
    Opportunity,
)
from meridianforge.acquisition.pipeline import (
    AcquisitionPipeline,
)
from meridianforge.acquisition.ranking_engine import (
    AcquisitionRankingEngine,
)


def build_opportunity(
    address: str,
    rent: float,
) -> Opportunity:

    return Opportunity(
        address=address,
        city="Philadelphia",
        state="PA",
        zip_code="19143",
        purchase_price=200000,
        monthly_rent=rent,
        monthly_expenses=600,
        market="Philadelphia",
        source="test",
        created_at=datetime.now(),
    )


def test_ranking_engine_orders_results():

    pipeline = AcquisitionPipeline()

    results = [
        pipeline.run(
            build_opportunity(
                "Property A",
                1500,
            )
        ),
        pipeline.run(
            build_opportunity(
                "Property B",
                2500,
            )
        ),
    ]

    ranked = AcquisitionRankingEngine.rank(results)

    assert len(ranked) == 2

    assert ranked[0].rank == 1

    assert ranked[1].rank == 2

    assert ranked[0].score >= ranked[1].score
