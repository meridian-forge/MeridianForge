#!/bin/bash

set -e

echo "Creating B002.2 Batch Analysis Result structure..."

mkdir -p src/meridianforge/models/results
mkdir -p tests

touch src/meridianforge/models/results/batch_analysis_result.py
touch tests/test_batch_analysis_result.py

echo "B002.2 structure ready."
