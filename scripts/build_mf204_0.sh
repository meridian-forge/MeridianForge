#!/bin/bash

set -e

PACKAGE="updates/packages/MF-204.0"

echo "======================================"
echo "BUILD MF-204.0 INTELLIGENCE FOUNDATION"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/intelligence/scoring" \
"$PACKAGE/files/src/meridianforge/intelligence/recommendation" \
"$PACKAGE/files/tests/intelligence"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-204.0

Investment Intelligence Foundation

Adds:
- Investor intelligence domain models
- Scoring framework foundation
- Recommendation layer foundation
- Intelligence module tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-204.0

Investment Intelligence Foundation

Meridian Forge evolves from property analysis
into investor-aware acquisition intelligence.

This release introduces:
- Investor strategy modeling
- Intelligence scoring foundation
- Recommendation architecture
EOF


cat > "$PACKAGE/files/src/meridianforge/intelligence/__init__.py" <<'EOF'
"""
Investment intelligence layer.
"""
EOF


cat > "$PACKAGE/files/src/meridianforge/intelligence/models.py" <<'EOF'
"""
Investment intelligence domain models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class InvestorProfile:
    """
    Defines investor priorities.
    """

    goal: str

    cashflow_weight: float = 0.40
    appreciation_weight: float = 0.30
    tax_weight: float = 0.20
    risk_weight: float = 0.10

    def __post_init__(self) -> None:

        weights = [
            self.cashflow_weight,
            self.appreciation_weight,
            self.tax_weight,
            self.risk_weight,
        ]

        if any(
            weight < 0
            for weight in weights
        ):
            raise ValueError(
                "Weights cannot be negative."
            )

        if round(sum(weights), 5) != 1:
            raise ValueError(
                "Investor weights must total 1.0."
            )
EOF


cat > "$PACKAGE/files/src/meridianforge/intelligence/scoring/__init__.py" <<'EOF'
"""
Intelligence scoring engines.
"""
EOF


cat > "$PACKAGE/files/src/meridianforge/intelligence/recommendation/__init__.py" <<'EOF'
"""
Investment recommendation engines.
"""
EOF


cat > "$PACKAGE/files/tests/intelligence/test_models.py" <<'EOF'
import pytest

from meridianforge.intelligence.models import (
    InvestorProfile,
)


def test_valid_profile() -> None:

    profile = InvestorProfile(
        goal="cash_flow"
    )

    assert profile.goal == "cash_flow"


def test_invalid_weights() -> None:

    with pytest.raises(ValueError):

        InvestorProfile(
            goal="growth",
            cashflow_weight=2.0,
        )
EOF


echo
echo "MF-204.0 PACKAGE CREATED"