from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)
from meridianforge.acquisition.ranking import (
    rank,
)


def test_ranking():

    result = rank(
        [
            AcquisitionDecision(
                "WATCH",
                50,
                [],
            ),
            AcquisitionDecision(
                "BUY",
                90,
                [],
            ),
        ]
    )

    assert result[0].status == "BUY"
