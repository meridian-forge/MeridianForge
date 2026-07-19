#!/bin/bash

set -e

echo "MF-229 Release Governance Documentation"

mkdir -p Documentation

cat > Documentation/RELEASE_PROCESS.md <<'DOC'
# MeridianForge Release Process

## Purpose

Define the controlled process for MeridianForge releases.

## Release Flow

1. Complete sprint scope
2. Run quality checks
3. Update documentation
4. Create release package
5. Commit changes
6. Create git tag

## Required Checks

Before release:

- ruff
- black
- mypy
- pytest

## Release Package

Every sprint package must contain:

- manifest.txt
- release_notes.md
- files/
- scripts/

## Versioning

Version must remain aligned across:

- VERSION
- pyproject.toml
- git tags
DOC


cat > Documentation/ARCHITECTURE_FREEZE.md <<'DOC'
# MeridianForge Architecture Freeze

## Purpose

Prevent unnecessary architecture changes during productization.

## Current Stable Architecture

Core layers:

- Intake
- Normalization
- Analysis
- Ranking
- Reporting
- Workflow

## Rules

Architecture changes require:

1. Documented reason
2. Impact assessment
3. Migration plan

## Principle

Prefer improving user capability over creating new technical layers.
DOC


cat > Documentation/DEVELOPMENT_WORKFLOW.md <<'DOC'
# MeridianForge Development Workflow

## Sprint Model

Each sprint follows:

1. Define objective
2. Create package
3. Implement changes
4. Test
5. Document
6. Release

## Developer Loop

Before commit:

ruff check src tests
black src tests
mypy src
pytest

## Repository Hygiene

Do not commit:

- __pycache__
- runtime outputs
- generated artifacts
- virtual environments

## Product Principle

Build only capabilities that increase MeridianForge usefulness.
DOC


echo "MF-229 governance documentation created."
