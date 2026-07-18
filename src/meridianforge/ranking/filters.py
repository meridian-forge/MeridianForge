from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)


def filter_buy_candidates(
    decisions: list[AcquisitionDecision],
) -> list[AcquisitionDecision]:

    return [item for item in decisions if item.status == "BUY"]
