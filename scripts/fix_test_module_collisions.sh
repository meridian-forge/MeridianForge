#!/bin/bash

set -e

echo "======================================"
echo "MERIDIAN FORGE TEST MODULE CLEANUP"
echo "======================================"

echo "Renaming duplicate test modules..."

# Ranking pipeline
if [ -f tests/ranking/test_pipeline.py ]; then
    mv \
    tests/ranking/test_pipeline.py \
    tests/ranking/test_ranking_pipeline.py
fi

# Data pipeline
if [ -f tests/data/test_pipeline.py ]; then
    mv \
    tests/data/test_pipeline.py \
    tests/data/test_import_pipeline.py
fi


# Package copies

if [ -f updates/packages/MF-105.0/files/tests/data/test_pipeline.py ]; then
    mv \
    updates/packages/MF-105.0/files/tests/data/test_pipeline.py \
    updates/packages/MF-105.0/files/tests/data/test_import_pipeline.py
fi


find . -type d -name "__pycache__" -exec rm -rf {} +

find . -name "*.pyc" -delete


echo
echo "TEST MODULE CLEANUP COMPLETE"