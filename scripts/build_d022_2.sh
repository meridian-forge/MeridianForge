#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D022.2"
echo "Email Embedded Content Validation"
echo "======================================"

PACKAGE="updates/packages/D022.2"

mkdir -p "$PACKAGE/files/tests/fixtures"
mkdir -p "$PACKAGE/files/tests"


echo "Creating email fixture..."

cat > "$PACKAGE/files/tests/fixtures/sample_property_email.py" <<'PY'
"""
Sample provider email fixture.

Represents property information embedded
directly inside an email body.
"""


def sample_email_property() -> dict[str, object]:

    return {
        "source": "EMAIL",
        "provider": "Rent To Retirement",
        "address": "456 Investment Avenue",
        "purchase_price": 225000,
        "monthly_rent": 1950,
        "property_type": "Single Family",
        "market": "Jacksonville FL",
    }
PY


echo "Creating email workflow test..."

cat > "$PACKAGE/files/tests/test_email_opportunity_import.py" <<'PY'
from tests.fixtures.sample_property_email import (
    sample_email_property,
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


def test_embedded_email_property_workflow() -> None:

    property_data = sample_email_property()

    assessment = AcquisitionAssessment(
        purchase_price=float(
            property_data["purchase_price"]
        ),
        monthly_cash_flow=300,
        dscr=1.25,
        cap_rate=0.065,
    )

    pipeline = AcquisitionPipeline()

    result = pipeline.process(
        assets=[property_data],
        confidence=0.88,
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
D022.2

Purpose:
Email Embedded Content Validation

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D022.2 deployment handled by update engine"
EOF

chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

