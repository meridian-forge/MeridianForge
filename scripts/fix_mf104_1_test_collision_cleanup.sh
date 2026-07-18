#!/bin/bash

set -e

echo "======================================"
echo "MF-104.1 TEST COLLISION CLEANUP"
echo "======================================"

PACKAGE_TEST="updates/packages/MF-104.1/files/tests/ranking/test_engine.py"
DEPLOYED_TEST="tests/ranking/test_engine.py"

NEW_PACKAGE_TEST="updates/packages/MF-104.1/files/tests/ranking/test_ranking_engine.py"

if [ -f "$PACKAGE_TEST" ]; then
    mv "$PACKAGE_TEST" "$NEW_PACKAGE_TEST"
    echo "Renamed package test"
fi

if [ -f "$DEPLOYED_TEST" ]; then
    mv "$DEPLOYED_TEST" "tests/ranking/test_ranking_engine.py"
    echo "Renamed deployed test"
fi

find . -type d -name "__pycache__" -exec rm -rf {} +

find . -name "*.pyc" -delete

echo "Cache cleanup complete"

echo "MF-104.1 TEST COLLISION FIX COMPLETE"