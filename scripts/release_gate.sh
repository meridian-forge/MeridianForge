#!/bin/bash

set -e

if [ -z "$1" ]; then
    echo "Usage:"
    echo "./scripts/release_gate.sh <version-tag>"
    exit 1
fi

TAG=$1

echo "======================================"
echo "MeridianForge Release Gate"
echo "======================================"

echo ""
echo "Checking working tree..."

if [ -n "$(git status --porcelain)" ]; then
    echo "ERROR: Working tree is not clean"
    git status
    exit 1
fi

echo ""
echo "Creating tag:"
echo "$TAG"

git tag -a "$TAG" -m "$TAG"

echo ""
echo "Latest checkpoint:"
git log --oneline -3

echo ""
echo "Available tag:"
git tag --list "$TAG"

echo ""
echo "======================================"
echo "RELEASE GATE PASSED"
echo "======================================"
