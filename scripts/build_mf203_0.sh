#!/bin/bash

set -e

PACKAGE="updates/packages/MF-203.0"

echo "======================================"
echo "BUILD MF-203.0 REAL DEAL VALIDATION"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/validation" \
"$PACKAGE/files/tests/validation"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-203.0

Real Deal Validation Framework

Adds:
- Validation models
- Deal review workflow
- Missing field detection
- Validation tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-203.0

Creates the real-world validation framework.

Purpose:

Compare Meridian Forge analysis against actual investment opportunities.
EOF


cat > "$PACKAGE/files/src/meridianforge/validation/models.py" <<'EOF'
from dataclasses import dataclass, field


@dataclass
class ValidationResult:

    opportunity_file: str

    missing_fields: list[str] = field(
        default_factory=list
    )

    notes: list[str] = field(
        default_factory=list
    )
EOF


cat > "$PACKAGE/files/src/meridianforge/validation/checker.py" <<'EOF'
from meridianforge.opportunity.models import Opportunity
from meridianforge.validation.models import ValidationResult


REQUIRED_RENTAL_FIELDS = [
    "purchase_price",
    "rent",
]


def validate_opportunity(
    opportunity: Opportunity,
) -> ValidationResult:

    missing: list[str] = []

    for field in REQUIRED_RENTAL_FIELDS:

        if field not in opportunity.fields:

            missing.append(field)


    notes: list[str] = []


    if missing:

        notes.append(
            "Additional data required for underwriting"
        )


    return ValidationResult(
        opportunity_file=opportunity.source_file,
        missing_fields=missing,
        notes=notes,
    )
EOF


cat > "$PACKAGE/files/tests/validation/test_checker.py" <<'EOF'
from meridianforge.opportunity.models import Opportunity
from meridianforge.validation.checker import (
    validate_opportunity,
)


def test_missing_fields_detection() -> None:

    opportunity = Opportunity(
        source_file="deal.xlsx",
        fields={
            "purchase_price": "250000",
        },
    )


    result = validate_opportunity(
        opportunity
    )


    assert (
        "rent"
        in result.missing_fields
    )
EOF


echo
echo "MF-203.0 PACKAGE CREATED"