#!/bin/bash

# ======================================
# Meridian Forge MF-210.0
# Monday Morning Analyzer Foundation
# ======================================

set -e

echo "Building Meridian Forge MF-210.0"

mkdir -p src/meridianforge/workspace
mkdir -p tests/workspace

mkdir -p updates/packages/MF-210.0/files/src/meridianforge/workspace
mkdir -p updates/packages/MF-210.0/files/tests/workspace

touch updates/packages/MF-210.0/manifest.txt
touch updates/packages/MF-210.0/release_notes.md

echo "MF-210.0 structure created"