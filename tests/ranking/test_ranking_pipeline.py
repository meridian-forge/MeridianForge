from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)
from meridianforge.ranking.pipeline import (
    AcquisitionPipeline,
)
from meridianforge.ranking.ranking_engine import (
    RankingEngine,
)


def test_pipeline():

    result = AcquisitionPipeline(RankingEngine()).execute(
        [
            AcquisitionDecision(
                "WATCH",
                99,
                [],
            ),
            AcquisitionDecision(
                "BUY",
                80,
                [],
            ),
        ]
    )

    assert len(result) == 1
    assert result[0].status == "BUY"
