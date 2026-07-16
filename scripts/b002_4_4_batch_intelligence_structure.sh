#!/bin/bash

set -e

echo "Creating B002.4.4 Batch Intelligence structure..."

mkdir -p src/meridianforge/intelligence
mkdir -p src/meridianforge/services
mkdir -p src/meridianforge/models/results
mkdir -p tests

touch src/meridianforge/intelligence/batch_confidence.py
touch src/meridianforge/services/batch_import_processor.py
touch src/meridianforge/models/results/batch_import_result.py
touch tests/test_batch_import_processor.py

echo "B002.4.4 structure ready."
