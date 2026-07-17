#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D022.1"
echo "Real Opportunity Validation"
echo "======================================"

PACKAGE="updates/packages/D022.1"

mkdir -p "$PACKAGE/files/tests/fixtures"
mkdir -p "$PACKAGE/files/tests"


echo "Creating sample opportunity fixture..."

cat > "$PACKAGE/files/tests/fixtures/sample_property_opportunity.py" <<'PY'
"""
Sample real estate opportunity fixture.
"""


def sample_property() -> dict[str, object]:
    return {
        "address": "123 Example Street",
        "purchase_price": 215000,
        "monthly_rent": 1850,
        "property_management": 185,
        "insurance": 120,
        "taxes": 220,
        "maintenance": 100,
        "vacancy": 90,
    }
PY


echo "Creating workflow test..."

cat > "$PACKAGE/files/tests/test_real_opportunity_workflow.py" <<'PY'
from tests.fixtures.sample_property_opportunity import (
    sample_property,
)

from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)

from meridianforge.services.acquisition_pipeline import (
    AcquisitionPipeline,
)

from meridianforge.services.recommendation_engine import (
    RecommendationEngine,
)


def test_real_opportunity_workflow() -> None:

    property_data = sample_property()

    assessment = AcquisitionAssessment(
        purchase_price=float(
            property_data["purchase_price"]
        ),
        monthly_cash_flow=350,
        dscr=1.30,
        cap_rate=0.07,
    )

    pipeline = AcquisitionPipeline()

    result = pipeline.process(
        assets=[property_data],
        confidence=0.90,
        assessment=assessment,
    )

    recommendation = RecommendationEngine.evaluate(
        assessment
    )

    assert result.assets_analyzed == 1
    assert recommendation.decision == "BUY"
PY


echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D022.1

Purpose:
Real Opportunity Validation

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D022.1 deployment handled by update engine"
EOF

chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

