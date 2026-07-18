#!/bin/bash

set -e

PACKAGE="updates/packages/MF-109.0"

echo "======================================"
echo "BUILD MF-109.0 UX ENHANCEMENT"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/ui" \
"$PACKAGE/files/examples" \
"$PACKAGE/files/tests/ui"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-109.0
User Experience Enhancement

Adds:
- Decision dashboard components
- Scenario display
- Analysis history foundation
- Demo dataset
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-109.0 UX Enhancement

Improves MVP usability.

Features:
- Decision cards
- Risk summaries
- Demo property data
EOF


cat > "$PACKAGE/files/src/meridianforge/ui/dashboard_cards.py" <<'PY'
from typing import Any


def decision_card(
    result: dict[str, Any],
) -> dict[str, Any]:

    decision = result.get(
        "decision",
        "UNKNOWN",
    )

    score = result.get(
        "score",
        0,
    )

    return {
        "decision": decision,
        "score": score,
        "rating": (
            "GREEN"
            if score >= 80
            else "YELLOW"
        ),
    }
PY


cat > "$PACKAGE/files/src/meridianforge/ui/scenario_view.py" <<'PY'
from typing import Any


def summarize_scenarios(
    scenarios: list[dict[str, Any]],
) -> dict[str, int]:

    summary = {
        "PASS": 0,
        "WATCH": 0,
        "FAIL": 0,
    }

    for item in scenarios:

        status = item.get(
            "status",
            "WATCH",
        )

        if status in summary:
            summary[status] += 1

    return summary
PY


cat > "$PACKAGE/files/src/meridianforge/ui/history.py" <<'PY'
from dataclasses import dataclass


@dataclass
class AnalysisHistory:

    address: str
    decision: str
    score: float


class HistoryStore:

    def __init__(self) -> None:

        self.items: list[AnalysisHistory] = []


    def add(
        self,
        item: AnalysisHistory,
    ) -> None:

        self.items.append(
            item
        )


    def all(
        self,
    ) -> list[AnalysisHistory]:

        return self.items
PY


cat > "$PACKAGE/files/examples/sample_properties.csv" <<'EOF'
address,purchase_price,rent
123 Main Street,250000,2200
456 Oak Avenue,300000,2600
EOF


cat > "$PACKAGE/files/tests/ui/test_dashboard_cards.py" <<'PY'
from meridianforge.ui.dashboard_cards import (
    decision_card,
)


def test_decision_card():

    result = decision_card(
        {
            "decision": "BUY",
            "score": 90,
        }
    )

    assert result["rating"] == "GREEN"
PY


cat > "$PACKAGE/files/tests/ui/test_history.py" <<'PY'
from meridianforge.ui.history import (
    AnalysisHistory,
    HistoryStore,
)


def test_history():

    store = HistoryStore()

    store.add(
        AnalysisHistory(
            "123 Main",
            "BUY",
            90,
        )
    )

    assert len(store.all()) == 1
PY


echo
echo "MF-109.0 PACKAGE CREATED"