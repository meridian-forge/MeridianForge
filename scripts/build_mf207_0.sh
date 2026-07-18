#!/bin/bash

set -e

echo "======================================"
echo "Building Meridian Forge MF-207.0"
echo "Investment Decision Intelligence Layer"
echo "======================================"

PACKAGE="updates/packages/MF-207.0"

echo "Creating directories..."

mkdir -p src/meridianforge/intelligence/decision
mkdir -p tests/intelligence

mkdir -p "$PACKAGE/files/src/meridianforge/intelligence/decision"
mkdir -p "$PACKAGE/files/tests/intelligence"


echo "Creating package files..."

cp src/meridianforge/intelligence/decision/*.py \
"$PACKAGE/files/src/meridianforge/intelligence/decision/"

cp tests/intelligence/test_decision.py \
"$PACKAGE/files/tests/intelligence/"


echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Version:
MF-207.0

Feature:
Investment Decision Intelligence Layer

Purpose:
Convert recommendation and scoring outputs
into investor decision guidance.

Files:
$(find "$PACKAGE/files" -type f | sort)

EOF


echo "Creating release notes..."

cat > "$PACKAGE/release_notes.md" <<EOF
# MF-207.0 Release Notes

## Investment Decision Intelligence Layer

### Added

- Investment decision models
- Decision engine
- Confidence assessment
- Decision rationale generation
- Recommended investor actions

### Validation

Quality Gate:
- Ruff
- Black
- MyPy
- PyTest

EOF


echo "MF-207.0 package build complete"

find "$PACKAGE" -maxdepth 10 -type f | sort