#!/bin/bash

set -e

echo "Creating B001.3 Deal Scoring Engine structure..."

mkdir -p src/meridianforge/engine
mkdir -p src/meridianforge/models/results
mkdir -p tests

touch src/meridianforge/engine/deal_scoring.py
touch src/meridianforge/models/results/deal_score.py
touch tests/test_deal_scoring.py

echo "B001.3 structure ready."
