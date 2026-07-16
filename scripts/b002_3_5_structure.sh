#!/bin/bash

set -e

echo "Creating B002.3.5 Real Estate Normalizer Adapter structure..."

mkdir -p src/meridianforge/normalization
mkdir -p tests

touch src/meridianforge/normalization/real_estate_adapter.py
touch tests/test_real_estate_adapter.py

echo "B002.3.5 structure ready."
