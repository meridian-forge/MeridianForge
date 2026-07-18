#!/bin/bash

set -e

echo "Fixing MF-110.0 MVP version..."

echo "1.0.0-MVP" > updates/packages/MF-110.0/files/VERSION

echo "Version updated:"
cat updates/packages/MF-110.0/files/VERSION

