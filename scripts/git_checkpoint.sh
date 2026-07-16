#!/bin/bash

set -e

MESSAGE="$1"

if [ -z "$MESSAGE" ]; then
    echo "Error: commit message required"
    echo "Usage:"
    echo "./scripts/git_checkpoint.sh \"Commit message\""
    exit 1
fi

echo "======================================"
echo "Meridian Forge Git Checkpoint"
echo "======================================"

echo ""
echo "Current status:"
git status

echo ""
echo "Adding changes..."
git add src tests scripts Documentation

echo ""
echo "Creating commit:"
echo "$MESSAGE"

git commit -m "$MESSAGE"

echo ""
echo "Latest commits:"
git log --oneline --decorate -5

echo ""
echo "======================================"
echo "CHECKPOINT COMPLETE"
echo "======================================"
