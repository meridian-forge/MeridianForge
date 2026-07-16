#!/bin/bash

set -e

echo "Creating B002.4.1 pipeline result model..."

mkdir -p src/meridianforge/models/results

touch src/meridianforge/models/results/pipeline_result.py
touch src/meridianforge/models/results/import_warning.py

echo "B002.4.1 structure ready."
