#!/bin/bash

set -e

echo "======================================"
echo "MeridianForge Build Gate"
echo "======================================"

echo ""
echo "Cleaning previous build artifacts..."

rm -rf build/
rm -rf dist/
rm -rf *.egg-info


echo ""
echo "Building package..."

python -m build


echo ""
echo "Checking generated artifacts..."

ls -la dist/


echo ""
echo "======================================"
echo "BUILD GATE PASSED"
echo "======================================"
