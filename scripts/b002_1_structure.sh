#!/bin/bash

set -e

echo "Creating B002.1 Batch Analyzer Service..."

mkdir -p src/meridianforge/services
mkdir -p tests

touch src/meridianforge/services/batch_analyzer.py
touch tests/test_batch_analyzer.py

echo "B002.1 structure ready."
