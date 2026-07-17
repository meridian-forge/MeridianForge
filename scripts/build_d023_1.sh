#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D023.1"
echo "Real Deal Test Run"
echo "======================================"

PACKAGE="updates/packages/D023.1"

mkdir -p "$PACKAGE/files/tests/fixtures"
mkdir -p "$PACKAGE/files/tests"


echo "Creating real deal fixture..."

cat > "$PACKAGE/files/tests/fixtures/real_deal_case.py" <<'PY'
"""
Representative turnkey rental opportunity.
"""


def real_deal_property() -> dict[str, object]:

    return {
        "source": "PROVIDER",
        "market": "Jacksonville FL",
        "purchase_price": 215000,
        "monthly_rent": 1850,
        "down_payment_percent": 0.20,
        "interest_rate": 0.07,
        "loan_term_years": 30,
        "annual_taxes": 2400,
        "annual_insurance": 1500,
        "management_percent": 0.10,
        "vacancy_percent": 0.05,
        "maintenance_percent": 0.05,
    }
PY


echo "Creating real deal workflow test..."

cat > "$PACKAGE/files/tests/test_real_deal_analysis.py" <<'PY'
from tests.fixtures.real_deal_case import (
    real_deal_property,
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

from meridianforge.reports.acquisition_report import (
    AcquisitionReport,
)


def test_real_deal_analysis() -> None:

    property_data = real_deal_property()

    assessment = AcquisitionAssessment(
        purchase_price=float(
            property_data["purchase_price"]
        ),
        monthly_cash_flow=250,
        dscr=1.25,
        cap_rate=0.065,
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

    report = AcquisitionReport.generate(
        result
    )

    assert result.assets_analyzed == 1
    assert recommendation.decision in (
        "BUY",
        "WATCH",
        "PASS",
    )
    assert "MERIDIAN FORGE" in report
PY


echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D023.1

Purpose:
Real Deal Test Run

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D023.1 deployment handled by update engine"
EOF

chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

