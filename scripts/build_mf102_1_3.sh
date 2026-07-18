#!/bin/bash

set -e

PACKAGE="updates/packages/MF-102.1.3"

echo "======================================"
echo "BUILD MF-102.1.3 INTAKE WORKFLOW"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/intake" \
"$PACKAGE/files/tests/intake"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-102.1.3
Intake Workflow Orchestrator

Adds:
- Intake Router
- Intake Workflow
- Adapter selection
- Opportunity creation flow
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-102.1.3 Intake Workflow

Introduces orchestration between incoming sources,
adapters, and opportunity creation.
EOF


cat > "$PACKAGE/files/src/meridianforge/intake/router.py" <<'PY'
from meridianforge.intake.csv_adapter import CSVAdapter
from meridianforge.intake.email_adapter import EmailAdapter
from meridianforge.intake.manual_adapter import ManualAdapter
from meridianforge.intake.pdf_adapter import PDFAdapter
from meridianforge.intake.url_adapter import URLAdapter
from meridianforge.intake.xlsx_adapter import XLSXAdapter


class IntakeRouter:

    def select(self, location: str):

        suffix = location.lower()

        if suffix.startswith("http"):
            return URLAdapter()

        if suffix.endswith(".pdf"):
            return PDFAdapter()

        if suffix.endswith(".csv"):
            return CSVAdapter()

        if suffix.endswith(".xlsx"):
            return XLSXAdapter()

        if suffix.endswith(".eml"):
            return EmailAdapter()

        return ManualAdapter()
PY


cat > "$PACKAGE/files/src/meridianforge/intake/workflow.py" <<'PY'
from meridianforge.domain.opportunity import Opportunity
from meridianforge.intake.router import IntakeRouter


class IntakeWorkflow:

    def __init__(self):
        self.router = IntakeRouter()

    def create_opportunity(self, name: str, location: str) -> Opportunity:

        adapter = self.router.select(location)

        source = adapter.ingest(location)

        return Opportunity(
            name=name,
            source=source,
        )
PY


cat > "$PACKAGE/files/tests/intake/test_router.py" <<'PY'
from meridianforge.intake.router import IntakeRouter
from meridianforge.intake.pdf_adapter import PDFAdapter
from meridianforge.intake.url_adapter import URLAdapter


def test_router_url():

    assert isinstance(
        IntakeRouter().select(
            "https://example.com"
        ),
        URLAdapter,
    )


def test_router_pdf():

    assert isinstance(
        IntakeRouter().select(
            "property.pdf"
        ),
        PDFAdapter,
    )
PY


cat > "$PACKAGE/files/tests/intake/test_workflow.py" <<'PY'
from meridianforge.intake.workflow import IntakeWorkflow
from meridianforge.domain.source import SourceType


def test_workflow():

    opportunity = IntakeWorkflow().create_opportunity(
        "Test Property",
        "manual-entry",
    )

    assert opportunity.source.source_type == SourceType.MANUAL
PY


echo
echo "MF-102.1.3 PACKAGE CREATED"