#!/bin/bash

set -e

PACKAGE="updates/packages/MF-201.2"

echo "======================================"
echo "BUILD MF-201.2 OPPORTUNITY NORMALIZATION ENGINE"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/opportunity" \
"$PACKAGE/files/tests/opportunity"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-201.2

Opportunity Normalization Engine

Adds:
- Opportunity domain model
- Asset classification
- Field mapping
- Normalization service
- Tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-201.2

Creates the internal Meridian Forge Opportunity model.

Purpose:

Convert extracted source fields into standardized investment opportunities.
EOF


cat > "$PACKAGE/files/src/meridianforge/opportunity/models.py" <<'EOF'
from dataclasses import dataclass, field
from enum import StrEnum


class OpportunityType(StrEnum):
    UNKNOWN = "UNKNOWN"
    RENTAL_PROPERTY = "RENTAL_PROPERTY"
    SYNDICATION = "SYNDICATION"


@dataclass
class Opportunity:
    source_file: str
    opportunity_type: OpportunityType = OpportunityType.UNKNOWN
    fields: dict[str, str] = field(default_factory=dict)
    confidence: float = 0.0
EOF


cat > "$PACKAGE/files/src/meridianforge/opportunity/field_mapper.py" <<'EOF'
from typing import Mapping


FIELD_ALIASES: Mapping[str, list[str]] = {
    "purchase_price": [
        "purchase price",
        "price",
        "list price",
    ],
    "rent": [
        "rent",
        "monthly rent",
        "estimated rent",
    ],
    "taxes": [
        "taxes",
        "property tax",
    ],
    "insurance": [
        "insurance",
    ],
}


def normalize_field_name(field_name: str) -> str:

    normalized = field_name.strip().lower()

    for standard, aliases in FIELD_ALIASES.items():

        if normalized in aliases:
            return standard

    return normalized
EOF


cat > "$PACKAGE/files/src/meridianforge/opportunity/normalizer.py" <<'EOF'
from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.opportunity.field_mapper import normalize_field_name
from meridianforge.opportunity.models import (
    Opportunity,
    OpportunityType,
)


def normalize(
    extracted: ExtractedData,
) -> Opportunity:

    fields: dict[str, str] = {}

    for key, value in extracted.fields.items():
        fields[
            normalize_field_name(key)
        ] = value


    opportunity_type = OpportunityType.UNKNOWN

    if "purchase_price" in fields or "rent" in fields:
        opportunity_type = OpportunityType.RENTAL_PROPERTY

    if "irr" in fields or "preferred_return" in fields:
        opportunity_type = OpportunityType.SYNDICATION


    return Opportunity(
        source_file=extracted.source_file,
        opportunity_type=opportunity_type,
        fields=fields,
        confidence=0.80,
    )
EOF


cat > "$PACKAGE/files/tests/opportunity/test_normalizer.py" <<'EOF'
from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.opportunity.models import OpportunityType
from meridianforge.opportunity.normalizer import normalize


def test_normalize_rental_property() -> None:

    extracted = ExtractedData(
        source_file="property.xlsx",
        fields={
            "Purchase Price": "250000",
            "Monthly Rent": "2200",
        },
    )

    result = normalize(extracted)

    assert result.opportunity_type == OpportunityType.RENTAL_PROPERTY
    assert result.fields["purchase_price"] == "250000"
EOF


echo
echo "MF-201.2 PACKAGE CREATED"