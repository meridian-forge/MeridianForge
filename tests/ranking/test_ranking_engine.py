from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)
from meridianforge.ranking.ranking_engine import (
    RankingEngine,
)


def test_best():

    result = RankingEngine().best(
        [
            AcquisitionDecision(
                "BUY",
                80,
                [],
            ),
            AcquisitionDecision(
                "BUY",
                95,
                [],
            ),
        ]
    )

    assert result.score == 95
