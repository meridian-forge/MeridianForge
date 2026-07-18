#!/bin/bash

set -e

PACKAGE="updates/packages/MF-106.0"

echo "======================================"
echo "BUILD MF-106.0 APPLICATION LAYER"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/application" \
"$PACKAGE/files/tests/application"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-106.0
MVP Application Layer

Adds:
- Application workflow
- Service layer
- Unified property analysis entry point
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-106.0 Application Layer

Connects Meridian Forge modules into a single workflow.

Provides:
- Unified analysis service
- Application orchestration
- MVP entry point
EOF


cat > "$PACKAGE/files/src/meridianforge/application/__init__.py" <<'PY'
PY


cat > "$PACKAGE/files/src/meridianforge/application/models.py" <<'PY'
from dataclasses import dataclass


@dataclass
class PropertyInput:

    address: str

    purchase_price: float
    monthly_rent: float

    noi: float
    annual_cash_flow: float
    cash_invested: float
    annual_debt: float
PY


cat > "$PACKAGE/files/src/meridianforge/application/workflow.py" <<'PY'
from meridianforge.application.models import (
    PropertyInput,
)

from meridianforge.analysis.underwriting_engine import (
    UnderwritingEngine,
)

from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)

from meridianforge.acquisition.score import (
    calculate_score,
)


class AnalysisWorkflow:

    def __init__(self) -> None:

        self.engine = UnderwritingEngine()

        self.criteria = AcquisitionCriteria()


    def execute(
        self,
        property_input: PropertyInput,
    ) -> dict[str, float]:

        result = self.engine.analyze(
            purchase_price=property_input.purchase_price,
            noi=property_input.noi,
            annual_cash_flow=property_input.annual_cash_flow,
            cash_invested=property_input.cash_invested,
            annual_debt=property_input.annual_debt,
        )

        score = calculate_score(
            result,
            self.criteria,
        )

        return {
            "cap_rate": result.cap_rate,
            "cash_on_cash": result.cash_on_cash_return,
            "dscr": result.dscr,
            "score": score,
        }
PY


cat > "$PACKAGE/files/src/meridianforge/application/service.py" <<'PY'
from meridianforge.application.models import (
    PropertyInput,
)

from meridianforge.application.workflow import (
    AnalysisWorkflow,
)


class MeridianForgeService:

    def __init__(self) -> None:

        self.workflow = AnalysisWorkflow()


    def analyze_property(
        self,
        property_input: PropertyInput,
    ) -> dict[str, float]:

        return self.workflow.execute(
            property_input
        )
PY


cat > "$PACKAGE/files/tests/application/test_service.py" <<'PY'
from meridianforge.application.models import (
    PropertyInput,
)

from meridianforge.application.service import (
    MeridianForgeService,
)


def test_service():

    result = MeridianForgeService().analyze_property(
        PropertyInput(
            address="123 Main",
            purchase_price=200000,
            monthly_rent=2000,
            noi=12000,
            annual_cash_flow=6000,
            cash_invested=50000,
            annual_debt=8000,
        )
    )

    assert result["cap_rate"] == 0.06
    assert result["dscr"] == 1.5
PY


echo
echo "MF-106.0 PACKAGE CREATED"