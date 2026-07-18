#!/bin/bash

set -e

PACKAGE="updates/packages/MF-202.1-fix"

echo "======================================"
echo "BUILD MF-202.1 TEST PACKAGE FIX"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/tests" \
"$PACKAGE/files/tests/analysis" \
"$PACKAGE/files/tests/ranking"


touch "$PACKAGE/files/tests/__init__.py"
touch "$PACKAGE/files/tests/analysis/__init__.py"
touch "$PACKAGE/files/tests/ranking/__init__.py"


cat > "$PACKAGE/manifest.txt" <<EOF
MF-202.1-fix

Fix pytest namespace collisions

Adds package markers to test directories.
EOF


echo
echo "MF-202.1 FIX PACKAGE CREATED"