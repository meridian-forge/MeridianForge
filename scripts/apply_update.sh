#!/bin/bash

set -e

PACKAGE="$1"

if [ -z "$PACKAGE" ]; then
    echo "Usage:"
    echo "./scripts/apply_update.sh <package_name>"
    exit 1
fi

UPDATE_DIR="updates/packages/$PACKAGE"

if [ ! -d "$UPDATE_DIR" ]; then
    echo "Update package not found:"
    echo "$UPDATE_DIR"
    exit 1
fi

echo "Applying:"
echo "$UPDATE_DIR"

bash "$UPDATE_DIR/apply.sh"

echo
echo "Running quality gate..."

./scripts/quality_gate.sh

echo
echo "Update completed successfully."
