#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D020.4.5"
echo "Attachment Intelligence Layer"
echo "======================================"

PACKAGE="updates/packages/D020.4.5"

mkdir -p "$PACKAGE/files/src/meridianforge/models/domain"
mkdir -p "$PACKAGE/files/src/meridianforge/extractors"
mkdir -p "$PACKAGE/files/src/meridianforge/services"
mkdir -p "$PACKAGE/files/tests"


echo "Creating AttachmentDocument model..."

cat > "$PACKAGE/files/src/meridianforge/models/domain/attachment_document.py" <<'PY'
"""
Attachment document model.

Represents incoming files attached
to external sources.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class AttachmentDocument:
    """
    Attachment representation.
    """

    filename: str

    attachment_type: str

    size_bytes: int = 0
PY


echo "Creating attachment detector..."

cat > "$PACKAGE/files/src/meridianforge/extractors/attachment_type_detector.py" <<'PY'
"""
Attachment type detector.

Identifies common investment document formats.
"""


class AttachmentTypeDetector:
    """
    Detects attachment category.
    """

    @staticmethod
    def detect(
        filename: str,
    ) -> str:
        """
        Determine attachment type.
        """

        name = filename.lower()

        if name.endswith(
            ".xlsx"
        ):
            return "EXCEL"

        if name.endswith(
            ".pdf"
        ):
            return "PDF"

        if name.endswith(
            ".docx"
        ):
            return "DOCUMENT"

        return "UNKNOWN"
PY


echo "Creating attachment intake service..."

cat > "$PACKAGE/files/src/meridianforge/services/attachment_intake_service.py" <<'PY'
"""
Attachment intake service.

Creates attachment documents.
"""

from meridianforge.extractors.attachment_type_detector import (
    AttachmentTypeDetector,
)
from meridianforge.models.domain.attachment_document import (
    AttachmentDocument,
)


class AttachmentIntakeService:
    """
    Handles attachment ingestion.
    """

    @staticmethod
    def ingest(
        filename: str,
        size_bytes: int = 0,
    ) -> AttachmentDocument:
        """
        Create attachment document.
        """

        return AttachmentDocument(
            filename=filename,
            attachment_type=AttachmentTypeDetector.detect(
                filename,
            ),
            size_bytes=size_bytes,
        )
PY


echo "Creating tests..."

cat > "$PACKAGE/files/tests/test_attachment_document.py" <<'PY'
from meridianforge.models.domain.attachment_document import (
    AttachmentDocument,
)


def test_attachment_document() -> None:

    document = AttachmentDocument(
        filename="deal.pdf",
        attachment_type="PDF",
    )

    assert document.attachment_type == "PDF"
PY


cat > "$PACKAGE/files/tests/test_attachment_detector.py" <<'PY'
from meridianforge.extractors.attachment_type_detector import (
    AttachmentTypeDetector,
)


def test_attachment_detector() -> None:

    assert (
        AttachmentTypeDetector.detect(
            "proforma.xlsx",
        )
        == "EXCEL"
    )
PY


cat > "$PACKAGE/files/tests/test_attachment_intake_service.py" <<'PY'
from meridianforge.services.attachment_intake_service import (
    AttachmentIntakeService,
)


def test_attachment_intake_service() -> None:

    result = AttachmentIntakeService.ingest(
        "brochure.pdf",
    )

    assert result.attachment_type == "PDF"
PY


echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D020.4.5

Purpose:
Attachment Intelligence Layer

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D020.4.5 deployment handled by update engine"
EOF


chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

