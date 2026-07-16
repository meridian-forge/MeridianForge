#!/bin/bash

set -e

echo "Creating B002.3.4 Normalization Framework structure..."

mkdir -p src/meridianforge/normalization
mkdir -p src/meridianforge/models/domain
mkdir -p tests

touch src/meridianforge/normalization/normalizer.py
touch src/meridianforge/models/domain/normalized_asset.py
touch tests/test_normalizer.py

echo "B002.3.4 structure ready."
