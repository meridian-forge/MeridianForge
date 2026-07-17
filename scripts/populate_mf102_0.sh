#!/bin/bash

set -e

PACKAGE="updates/packages/MF-102.0"

echo
echo "======================================"
echo "POPULATING MF-102.0 PACKAGE"
echo "======================================"

mkdir -p \
"$PACKAGE/files/src/meridianforge/domain" \
"$PACKAGE/files/src/meridianforge/repositories" \
"$PACKAGE/files/tests/domain"


cat > "$PACKAGE/files/src/meridianforge/domain/opportunity_status.py" <<'PY'
from enum import Enum


class OpportunityStatus(str, Enum):
    NEW = "NEW"
    ANALYZING = "ANALYZING"
    ANALYZED = "ANALYZED"
    WATCHLIST = "WATCHLIST"
    REJECTED = "REJECTED"
    CLOSED = "CLOSED"
PY


cat > "$PACKAGE/files/src/meridianforge/domain/source.py" <<'PY'
from dataclasses import asdict, dataclass
from enum import Enum


class SourceType(str, Enum):
    PDF = "PDF"
    URL = "URL"
    EMAIL = "EMAIL"
    XLSX = "XLSX"
    CSV = "CSV"
    MANUAL = "MANUAL"


@dataclass
class Source:
    source_type: SourceType
    location: str

    def validate(self):
        if not self.location:
            raise ValueError("Source location required")
        return True

    def to_dict(self):
        data = asdict(self)
        data["source_type"] = self.source_type.value
        return data
PY


cat > "$PACKAGE/files/src/meridianforge/domain/provider.py" <<'PY'
from dataclasses import dataclass


@dataclass
class Provider:
    name: str
    contact: str | None = None

    def validate(self):
        if not self.name:
            raise ValueError("Provider name required")
        return True
PY


cat > "$PACKAGE/files/src/meridianforge/domain/opportunity.py" <<'PY'
from dataclasses import dataclass

from meridianforge.domain.opportunity_status import OpportunityStatus
from meridianforge.domain.source import Source


@dataclass
class Opportunity:
    name: str
    source: Source
    status: OpportunityStatus = OpportunityStatus.NEW

    def validate(self):
        if not self.name:
            raise ValueError("Opportunity name required")

        self.source.validate()

        return True
PY


cat > "$PACKAGE/files/src/meridianforge/domain/__init__.py" <<'PY'
PY


cat > "$PACKAGE/files/src/meridianforge/repositories/__init__.py" <<'PY'
PY


cat > "$PACKAGE/files/src/meridianforge/repositories/opportunity_repository.py" <<'PY'
import json
from pathlib import Path


class OpportunityRepository:

    def __init__(self, path="data/opportunities.json"):
        self.path = Path(path)

    def save(self, opportunity):
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.path.write_text(
            json.dumps(
                opportunity,
                default=lambda x: x.__dict__,
                indent=2
            )
        )

        return True
PY


cat > "$PACKAGE/files/tests/domain/test_source.py" <<'PY'
from meridianforge.domain.source import Source, SourceType


def test_source():

    source = Source(
        SourceType.URL,
        "https://example.com"
    )

    assert source.validate()
PY


cat > "$PACKAGE/files/tests/domain/test_provider.py" <<'PY'
from meridianforge.domain.provider import Provider


def test_provider():

    provider = Provider("JWB")

    assert provider.validate()
PY


cat > "$PACKAGE/files/tests/domain/test_opportunity.py" <<'PY'
from meridianforge.domain.opportunity import Opportunity
from meridianforge.domain.source import Source, SourceType


def test_opportunity():

    opportunity = Opportunity(
        "Test Property",
        Source(
            SourceType.MANUAL,
            "manual"
        )
    )

    assert opportunity.validate()
PY


echo
echo "======================================"
echo "MF-102.0 PACKAGE POPULATED"
echo "======================================"