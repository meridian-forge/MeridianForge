from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)


def rank(
    decisions: list[AcquisitionDecision],
) -> list[AcquisitionDecision]:

    return sorted(
        decisions,
        key=lambda item: item.score,
        reverse=True,
    )
