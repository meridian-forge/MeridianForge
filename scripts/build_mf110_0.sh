#!/bin/bash

set -e

PACKAGE="updates/packages/MF-110.0"

echo "======================================"
echo "BUILD MF-110.0 MVP RELEASE"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/docs" \
"$PACKAGE/files/scripts" \
"$PACKAGE/files/examples" \
"$PACKAGE/files/tests/release"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-110.0
Meridian Forge MVP Release

Adds:
- Release documentation
- Startup workflow
- Version management
- Demo package
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# Meridian Forge MVP v0.1.0

## Included

- Property analysis workflow
- Underwriting engine
- Scenario analysis
- Acquisition scoring
- Ranking
- Streamlit interface
- Reporting

## Status

MVP Release
EOF


cat > "$PACKAGE/files/VERSION" <<'EOF'
0.1.0-MVP
EOF


cat > "$PACKAGE/files/docs/GETTING_STARTED.md" <<'EOF'
# Meridian Forge Getting Started

## Start Application

Run:

streamlit run src/meridianforge/ui/app.py


## Workflow

1. Enter property data
2. Analyze property
3. Review metrics
4. Review decision
5. Export report
EOF


cat > "$PACKAGE/files/docs/ARCHITECTURE.md" <<'EOF'
# Meridian Forge Architecture

Data
 |
Application Layer
 |
Underwriting
 |
Scenario Engine
 |
Acquisition Intelligence
 |
Reporting
 |
UI
EOF


cat > "$PACKAGE/files/examples/demo_property.json" <<'EOF'
{
  "address": "123 Main Street",
  "purchase_price": 250000,
  "monthly_rent": 2200,
  "decision": "BUY",
  "score": 87
}
EOF


cat > "$PACKAGE/files/scripts/start_meridianforge.sh" <<'EOF'
#!/bin/bash

set -e

echo "Starting Meridian Forge MVP..."

streamlit run src/meridianforge/ui/app.py
EOF


cat > "$PACKAGE/files/tests/release/test_version.py" <<'PY'
from pathlib import Path


def test_version_exists():

    version = Path(
        "VERSION"
    )

    assert version.exists()
PY


echo
echo "MF-110.0 PACKAGE CREATED"