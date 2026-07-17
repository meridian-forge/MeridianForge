#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D022.3"
echo "Excel Proforma Validation"
echo "======================================"

PACKAGE="updates/packages/D022.3"

mkdir -p "$PACKAGE/files/tests/fixtures"
mkdir -p "$PACKAGE/files/tests"


echo "Creating proforma fixture..."

cat > "$PACKAGE/files/tests/fixtures/sample_proforma.py" <<'PY'
"""
Sample Excel proforma fixture.

Represents normalized values extracted
from a provider investment spreadsheet.
"""


def sample_proforma_property() -> dict[str, object]:

    return {
        "source": "EXCEL",
        "provider": "JWB",
        "address": "789 Rental Drive",
        "purchase_price": 210000,
        "monthly_rent": 1850,
        "annual_taxes": 2400,
        "annual_insurance": 1500,
        "management_percent": 0.10,
        "vacancy_percent": 0.05,
        "loan_to_value": 0.75,
        "loan_term_years": 30,
    }
PY


echo "Creating Excel workflow test..."

cat > "$PACKAGE/files/tests/test_excel_proforma_workflow.py" <<'PY'
from tests.fixtures.sample_proforma import (
    sample_proforma_property,
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


def test_excel_proforma_workflow() -> None:

    property_data = sample_proforma_property()

    assessment = AcquisitionAssessment(
        purchase_price=float(
            property_data["purchase_price"]
        ),
        monthly_cash_flow=275,
        dscr=1.22,
        cap_rate=0.065,
    )

    pipeline = AcquisitionPipeline()

    result = pipeline.process(
        assets=[property_data],
        confidence=0.92,
        assessment=assessment,
    )

    recommendation = RecommendationEngine.evaluate(
        assessment
    )

    assert result.assets_analyzed == 1
    assert result.confidence == 0.92
    assert recommendation.decision in (
        "BUY",
        "WATCH",
    )
PY


echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D022.3

Purpose:
Excel Proforma Validation

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D022.3 deployment handled by update engine"
EOF

chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

