#!/bin/bash

set -e

echo "Creating MF-229 release package structure"

mkdir -p updates/packages/MF-229.0/files
mkdir -p updates/packages/MF-229.0/scripts

touch updates/packages/MF-229.0/manifest.txt
touch updates/packages/MF-229.0/release_notes.md

echo "MF-229 package structure created"
