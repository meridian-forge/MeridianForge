#!/bin/bash

set -e

PACKAGE="updates/packages/D024.1"

echo "Creating Meridian Forge D024.1 package..."

rm -rf "$PACKAGE"

mkdir -p "$PACKAGE/files/src/meridianforge/domain"
mkdir -p "$PACKAGE/tests"

cat > "$PACKAGE/files/src/meridianforge/domain/investor_profile.py" <<'PY'
from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class InvestorProfile:
    """
    Defines investor-specific objectives and assumptions.
    """

    name: str
    strategy: str
    primary_goal: str
    risk_level: str

    financing_type: str
    interest_rate: float
    down_payment_percent: float

    hold_period_years: int
    target_number_of_properties: int

    tax_strategy: str

    def to_dict(self) -> Dict:
        return asdict(self)

    def validate(self) -> bool:
        if not self.name:
            raise ValueError("Investor name is required")

        if not 0 < self.interest_rate < 1:
            raise ValueError(
                "Interest rate must be between 0 and 1"
            )

        if not 0 < self.down_payment_percent < 1:
            raise ValueError(
                "Down payment percent must be between 0 and 1"
            )

        if self.hold_period_years <= 0:
            raise ValueError(
                "Hold period must be positive"
            )

        if self.target_number_of_properties <= 0:
            raise ValueError(
                "Target number of properties must be positive"
            )

        return True
PY


cat > "$PACKAGE/tests/test_investor_profile.py" <<'PY'
from meridianforge.domain.investor_profile import InvestorProfile


def test_investor_profile_creation():

    profile = InvestorProfile(
        name="Mahi",
        strategy="Long Term Portfolio Growth",
        primary_goal="Capital Velocity",
        risk_level="Aggressive",
        financing_type="DSCR",
        interest_rate=0.075,
        down_payment_percent=0.20,
        hold_period_years=10,
        target_number_of_properties=5,
        tax_strategy="Depreciation + CPA Reviewed 1031",
    )

    assert profile.validate() is True


def test_investor_profile_serialization():

    profile = InvestorProfile(
        name="Test Investor",
        strategy="Growth",
        primary_goal="Cash Flow",
        risk_level="Moderate",
        financing_type="Conventional",
        interest_rate=0.055,
        down_payment_percent=0.25,
        hold_period_years=10,
        target_number_of_properties=3,
        tax_strategy="CPA Review",
    )

    data = profile.to_dict()

    assert data["financing_type"] == "Conventional"
    assert data["target_number_of_properties"] == 3
PY


cat > "$PACKAGE/manifest.txt" <<EOF
Package: D024.1

Purpose:
Investor Profile Engine Foundation

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D024.1 deployment handled by update engine"
EOF

chmod +x "$PACKAGE/apply.sh"

echo
echo "======================================"
echo "D024.1 PACKAGE CREATED"
echo "======================================"
echo "$PACKAGE"
