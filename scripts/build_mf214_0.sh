#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge MF-214.0"
echo "Opportunity Repository"
echo "======================================"

mkdir -p \
src/meridianforge/repositories \
tests/repositories \
updates/packages/MF-214.0/files/src/meridianforge/repositories \
updates/packages/MF-214.0/files/tests/repositories


cat > src/meridianforge/repositories/__init__.py <<'PY'
"""Meridian Forge repository layer."""
PY


cat > src/meridianforge/repositories/opportunity_repository.py <<'PY'
from typing import Any


class OpportunityRepository:
    """
    In-memory repository for investment opportunities.

    Initial implementation provides the repository
    abstraction that later storage engines can replace.
    """

    def __init__(
        self,
        opportunities: list[Any] | None = None,
    ) -> None:
        self._opportunities: list[Any] = (
            opportunities or []
        )

    def add(
        self,
        opportunity: Any,
    ) -> None:
        self._opportunities.append(
            opportunity
        )

    def get_all(self) -> list[Any]:
        return list(
            self._opportunities
        )

    def count(self) -> int:
        return len(
            self._opportunities
        )
PY


cat > tests/repositories/test_opportunity_repository.py <<'PY'
from meridianforge.repositories.opportunity_repository import (
    OpportunityRepository,
)


def test_repository_add_and_get() -> None:

    repository = OpportunityRepository()

    repository.add(
        "Property A"
    )

    opportunities = (
        repository.get_all()
    )

    assert opportunities == [
        "Property A"
    ]


def test_repository_count() -> None:

    repository = OpportunityRepository(
        [
            "Property A",
            "Property B",
        ]
    )

    assert repository.count() == 2
PY


cp src/meridianforge/repositories/opportunity_repository.py \
updates/packages/MF-214.0/files/src/meridianforge/repositories/


cp tests/repositories/test_opportunity_repository.py \
updates/packages/MF-214.0/files/tests/repositories/


cat > updates/packages/MF-214.0/manifest.txt <<'TXT'
MF-214.0
Opportunity Repository

Files:
src/meridianforge/repositories/__init__.py
src/meridianforge/repositories/opportunity_repository.py
tests/repositories/test_opportunity_repository.py
TXT


cat > updates/packages/MF-214.0/release_notes.md <<'MD'
# MF-214.0 Opportunity Repository

Introduces the repository abstraction used by
Monday Analyzer workflows.

Capabilities:
- store opportunities
- retrieve opportunities
- count available opportunities
- prepare future database integration
MD


chmod +x scripts/build_mf214_0.sh

echo ""
echo "MF-214.0 build complete"
echo "Run:"
echo "./scripts/quality_gate.sh"
