#!/bin/bash

set -e

PACKAGE="updates/packages/MF-104.1"

echo "======================================"
echo "BUILD MF-104.1 DEAL RANKING ENGINE"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/ranking" \
"$PACKAGE/files/tests/ranking"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-104.1
Deal Ranking Engine

Adds:
- Opportunity filtering
- Ranking engine
- Pipeline selection
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-104.1 Deal Ranking Engine

Enables multi-property comparison.

Supports:
- Filtering
- Ranking
- Best opportunity selection
EOF


cat > "$PACKAGE/files/src/meridianforge/ranking/__init__.py" <<'PY'
PY


cat > "$PACKAGE/files/src/meridianforge/ranking/filters.py" <<'PY'
from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)


def filter_buy_candidates(
    decisions: list[AcquisitionDecision],
) -> list[AcquisitionDecision]:

    return [
        item
        for item in decisions
        if item.status == "BUY"
    ]
PY


cat > "$PACKAGE/files/src/meridianforge/ranking/ranking_engine.py" <<'PY'
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
PY


cat > "$PACKAGE/files/src/meridianforge/ranking/pipeline.py" <<'PY'
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
PY


cat > "$PACKAGE/files/tests/ranking/test_engine.py" <<'PY'
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
PY


cat > "$PACKAGE/files/tests/ranking/test_pipeline.py" <<'PY'
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

    result = AcquisitionPipeline(
        RankingEngine()
    ).execute(
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
PY


echo
echo "MF-104.1 PACKAGE CREATED"