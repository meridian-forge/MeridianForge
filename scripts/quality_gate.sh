#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge Quality Gate"
echo "======================================"

echo ""
echo "Running Ruff..."
ruff check src tests --fix

echo ""
echo "Running Black..."
black src tests

echo ""
echo "Running MyPy..."
mypy src

echo ""
echo "Running PyTest..."
pytest

echo ""
echo "======================================"
echo "QUALITY GATE PASSED"
echo "======================================"
