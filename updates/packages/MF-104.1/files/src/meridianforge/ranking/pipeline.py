from dataclasses import dataclass

from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)

from meridianforge.ranking.filters import (
    filter_buy_candidates,
)

from meridianforge.ranking.ranking_engine import (
    RankingEngine,
)


@dataclass
class AcquisitionPipeline:

    engine: RankingEngine

    def execute(
        self,
        decisions: list[AcquisitionDecision],
    ) -> list[AcquisitionDecision]:

        candidates = filter_buy_candidates(
            decisions
        )

        return self.engine.rank(
            candidates
        )
