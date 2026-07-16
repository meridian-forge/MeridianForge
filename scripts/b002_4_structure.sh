#!/bin/bash

set -e

echo "Creating B002.4 Intelligent Import Pipeline structure..."

mkdir -p src/meridianforge/services
mkdir -p src/meridianforge/models/results
mkdir -p tests

touch src/meridianforge/services/import_pipeline.py
touch src/meridianforge/models/results/import_warning.py
touch tests/test_import_pipeline.py

echo "B002.4 structure ready."
