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
