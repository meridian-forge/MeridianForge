#!/bin/bash

set -e

PACKAGE="updates/packages/MF-203.1"

echo "======================================"
echo "BUILD MF-203.1 PROPERTY BUILDER"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/opportunity" \
"$PACKAGE/files/tests/opportunity"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-203.1

Opportunity Property Builder

Adds:
- Conversion from normalized opportunity data
- Property domain object creation
- Property builder workflow tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-203.1

Adds the Opportunity Property Builder layer.

Pipeline progression:

Intake
 ↓
ExtractedData
 ↓
Opportunity
 ↓
Property Builder
 ↓
Property Domain Model
 ↓
Underwriting Engine
EOF


cat > "$PACKAGE/files/src/meridianforge/opportunity/property_builder.py" <<'EOF'
"""
Property builder.

Converts normalized opportunity data
into Meridian Forge Property domain objects.
"""


def build_property(
    opportunity_fields: dict[str, object],
):
    """
    Build Property object from opportunity data.

    Implementation follows after
    mapping rules are finalized.
    """

    raise NotImplementedError(
        "Property builder pending implementation."
    )
EOF


cat > "$PACKAGE/files/tests/opportunity/test_property_builder.py" <<'EOF'
import pytest

from meridianforge.opportunity.property_builder import (
    build_property,
)


def test_property_builder_placeholder():

    with pytest.raises(
        NotImplementedError
    ):
        build_property({})
EOF


echo
echo "MF-203.1 PACKAGE CREATED"

find "$PACKAGE" -maxdepth 5 -type f | sort