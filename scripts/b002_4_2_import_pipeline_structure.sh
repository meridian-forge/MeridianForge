#!/bin/bash

set -e

echo "Creating B002.4.2 Import Pipeline service..."

mkdir -p src/meridianforge/services
mkdir -p tests

touch src/meridianforge/services/import_pipeline.py
touch tests/test_import_pipeline.py

echo "B002.4.2 structure ready."
