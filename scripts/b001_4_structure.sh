#!/bin/bash

set -e

echo "Creating B001.4 Deal Ranking Engine structure..."

mkdir -p src/meridianforge/engine
mkdir -p src/meridianforge/models/results
mkdir -p tests

touch src/meridianforge/engine/deal_ranking.py
touch src/meridianforge/models/results/ranked_deal.py
touch tests/test_deal_ranking.py

echo "B001.4 structure ready."
