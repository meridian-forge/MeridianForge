#!/bin/bash

set -e

echo "Creating B001.2 Criteria Engine structure..."

mkdir -p src/meridianforge/engine
mkdir -p src/meridianforge/models/results
mkdir -p tests

touch src/meridianforge/engine/criteria_engine.py
touch src/meridianforge/models/results/deal_evaluation.py
touch tests/test_criteria_engine.py

echo "B001.2 structure ready."
