#!/bin/bash

set -e

SOURCE="updates/packages/MF-104.1/files/tests/ranking/test_engine.py"
TARGET="updates/packages/MF-104.1/files/tests/ranking/test_ranking_engine.py"

echo "======================================"
echo "MF-104.1 TEST MODULE FIX"
echo "======================================"

mv "$SOURCE" "$TARGET"

echo "Renamed:"
echo "$SOURCE"
echo "to:"
echo "$TARGET"