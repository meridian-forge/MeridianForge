from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)


class RankingEngine:

    def rank(
        self,
        decisions: list[AcquisitionDecision],
    ) -> list[AcquisitionDecision]:

        return sorted(
            decisions,
            key=lambda item: item.score,
            reverse=True,
        )

    def best(
        self,
        decisions: list[AcquisitionDecision],
    ) -> AcquisitionDecision | None:

        ranked = self.rank(decisions)

        if not ranked:
            return None

        return ranked[0]
