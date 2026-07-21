#!/bin/bash

set -e

echo "======================================"
echo "MeridianForge Quality Gate"
echo "======================================"

echo ""
echo "Running Ruff..."
ruff check src tests

echo ""
echo "Running Black..."
black --check src tests

echo ""
echo "Running MyPy..."
mypy src

echo ""
echo "Running Pytest..."
pytest

echo ""
echo "======================================"
echo "QUALITY GATE PASSED"
echo "======================================"
