#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge Workspace Cleanup"
echo "======================================"

ROOT=$(git rev-parse --show-toplevel)

echo "Repository root:"
echo "$ROOT"

cd "$ROOT"

echo ""
echo "Removing Python cache files..."

find . \
    -type d \
    -name "__pycache__" \
    -prune \
    -exec rm -rf {} +

find . \
    -type f \
    -name "*.pyc" \
    -delete


echo ""
echo "Removing pytest cache..."

rm -rf .pytest_cache


echo ""
echo "Removing mypy cache..."

rm -rf .mypy_cache


echo ""
echo "Removing runtime generated outputs..."

if [ -d runtime/outputs ]; then
    find runtime/outputs \
        -type f \
        ! -name ".gitkeep" \
        -delete
fi


echo ""
echo "Removing build artifacts..."

rm -rf build/
rm -rf dist/


echo ""
echo "Cleanup complete."

echo ""
echo "Git status:"
git status --short
