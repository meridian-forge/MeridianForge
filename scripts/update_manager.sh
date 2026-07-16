#!/bin/bash

echo "Meridian Forge Update Manager"

echo
echo "Available update packages:"

find updates/packages -maxdepth 1 -mindepth 1 -type d 2>/dev/null \
    | sed 's#updates/packages/##' \
    || echo "No update packages found."
