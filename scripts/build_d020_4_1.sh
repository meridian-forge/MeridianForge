#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D020.4.1"
echo "Source Document Foundation"
echo "======================================"

PACKAGE="updates/packages/D020.4.1"

mkdir -p "$PACKAGE/files/src/meridianforge/models/domain"
mkdir -p "$PACKAGE/files/src/meridianforge/services"
mkdir -p "$PACKAGE/files/tests"


echo
echo "Creating SourceDocument model..."


cat > "$PACKAGE/files/src/meridianforge/models/domain/source_document.py" <<'PY'
"""
Source document domain model.

Represents external information entering
Meridian Forge.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class SourceDocument:
    """
    Universal external source representation.
    """

    source_type: str

    content: str

    provider: str | None = None

    attachments: list[str] = field(
        default_factory=list,
    )

    metadata: dict[str, str] = field(
        default_factory=dict,
    )
PY


echo
echo "Creating Source Intake Service..."


cat > "$PACKAGE/files/src/meridianforge/services/source_intake_service.py" <<'PY'
"""
Source intake service.

Creates normalized source documents
from external inputs.
"""

from meridianforge.models.domain.source_document import (
    SourceDocument,
)


class SourceIntakeService:
    """
    Handles external source ingestion.
    """

    @staticmethod
    def create(
        source_type: str,
        content: str,
        provider: str | None = None,
        attachments: list[str] | None = None,
    ) -> SourceDocument:
        """
        Create a source document.
        """

        return SourceDocument(
            source_type=source_type,
            content=content,
            provider=provider,
            attachments=attachments or [],
        )
PY


echo
echo "Creating tests..."


cat > "$PACKAGE/files/tests/test_source_document.py" <<'PY'
from meridianforge.models.domain.source_document import (
    SourceDocument,
)


def test_source_document_creation() -> None:

    document = SourceDocument(
        source_type="EMAIL",
        provider="JWB Capital",
        content="Property opportunity",
    )

    assert document.source_type == "EMAIL"
    assert document.provider == "JWB Capital"
PY


cat > "$PACKAGE/files/tests/test_source_intake_service.py" <<'PY'
from meridianforge.services.source_intake_service import (
    SourceIntakeService,
)


def test_source_intake_service() -> None:

    document = SourceIntakeService.create(
        source_type="EMAIL",
        provider="Rent To Retirement",
        content="Rental opportunity",
    )

    assert document.provider == "Rent To Retirement"
    assert document.content == "Rental opportunity"
PY


echo
echo "Creating manifest..."


cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D020.4.1

Purpose:
Source Document Foundation

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D020.4.1 deployment handled by update engine"
EOF


chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

