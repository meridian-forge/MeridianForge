#!/bin/bash

set -e

echo "Building MF-208.0 Integrated Analysis Workflow"

mkdir -p src/meridianforge/workflow
mkdir -p tests/workflow

mkdir -p updates/packages/MF-208.0/files/src/meridianforge/workflow
mkdir -p updates/packages/MF-208.0/files/tests/workflow

touch src/meridianforge/workflow/__init__.py
touch src/meridianforge/workflow/analysis_pipeline.py
touch src/meridianforge/workflow/result.py

touch tests/workflow/test_analysis_pipeline.py

cp src/meridianforge/workflow/* \
updates/packages/MF-208.0/files/src/meridianforge/workflow/

cp tests/workflow/test_analysis_pipeline.py \
updates/packages/MF-208.0/files/tests/workflow/

echo "MF-208.0 structure created"