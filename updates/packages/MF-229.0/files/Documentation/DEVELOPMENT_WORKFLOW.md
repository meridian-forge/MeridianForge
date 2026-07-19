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
