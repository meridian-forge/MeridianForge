#!/bin/bash

set -e

echo "================================"
echo "Meridian Forge Repository View"
echo "================================"

echo ""
echo "INTELLIGENCE"
echo "------------"
find src/meridianforge/intelligence \
    -maxdepth 1 \
    -type f \
    -name "*.py" \
    | sort

echo ""
echo "NORMALIZATION"
echo "-------------"
find src/meridianforge/normalization \
    -maxdepth 1 \
    -type f \
    -name "*.py" \
    | sort

echo ""
echo "DOMAIN MODELS"
echo "-------------"
find src/meridianforge/models/domain \
    -maxdepth 1 \
    -type f \
    -name "*.py" \
    | sort

echo ""
echo "RESULT MODELS"
echo "-------------"
find src/meridianforge/models/results \
    -maxdepth 1 \
    -type f \
    -name "*.py" \
    | sort

echo ""
echo "SERVICES"
echo "--------"
find src/meridianforge/services \
    -maxdepth 1 \
    -type f \
    -name "*.py" \
    | sort

echo ""
echo "TESTS"
echo "-----"
find tests \
    -maxdepth 1 \
    -type f \
    -name "test_*.py" \
    | sort
