#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D020.4.2"
echo "Email Content Extractor Foundation"
echo "======================================"

PACKAGE="updates/packages/D020.4.2"

mkdir -p "$PACKAGE/files/src/meridianforge/extractors"
mkdir -p "$PACKAGE/files/src/meridianforge/services"
mkdir -p "$PACKAGE/files/tests"


echo
echo "Creating email extractor..."


cat > "$PACKAGE/files/src/meridianforge/extractors/email_extractor.py" <<'PY'
"""
Email extractor.

Converts email content into
Meridian Forge source documents.
"""

from meridianforge.models.domain.source_document import (
    SourceDocument,
)


class EmailExtractor:
    """
    Extracts information from emails.
    """

    @staticmethod
    def extract(
        sender: str,
        subject: str,
        body: str,
        attachments: list[str] | None = None,
    ) -> SourceDocument:
        """
        Create SourceDocument from email.
        """

        return SourceDocument(
            source_type="EMAIL",
            provider=sender,
            content=body,
            attachments=attachments or [],
            metadata={
                "sender": sender,
                "subject": subject,
            },
        )
PY


echo
echo "Creating email intake service..."


cat > "$PACKAGE/files/src/meridianforge/services/email_intake_service.py" <<'PY'
"""
Email intake service.

Application layer wrapper for email extraction.
"""

from meridianforge.extractors.email_extractor import (
    EmailExtractor,
)
from meridianforge.models.domain.source_document import (
    SourceDocument,
)


class EmailIntakeService:
    """
    Handles email ingestion.
    """

    @staticmethod
    def ingest(
        sender: str,
        subject: str,
        body: str,
        attachments: list[str] | None = None,
    ) -> SourceDocument:
        """
        Convert email into source document.
        """

        return EmailExtractor.extract(
            sender,
            subject,
            body,
            attachments,
        )
PY


echo
echo "Creating tests..."


cat > "$PACKAGE/files/tests/test_email_extractor.py" <<'PY'
from meridianforge.extractors.email_extractor import (
    EmailExtractor,
)


def test_email_extractor() -> None:

    document = EmailExtractor.extract(
        sender="JWB Capital",
        subject="Featured Property",
        body="<html>Rental $1850</html>",
    )

    assert document.source_type == "EMAIL"
    assert document.provider == "JWB Capital"
    assert "Rental" in document.content
PY


cat > "$PACKAGE/files/tests/test_email_intake_service.py" <<'PY'
from meridianforge.services.email_intake_service import (
    EmailIntakeService,
)


def test_email_intake_service() -> None:

    document = EmailIntakeService.ingest(
        sender="Rent To Retirement",
        subject="New Deal",
        body="Property details",
        attachments=["deal.pdf"],
    )

    assert document.provider == "Rent To Retirement"
    assert document.attachments == ["deal.pdf"]
PY


echo
echo "Creating manifest..."


cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D020.4.2

Purpose:
Email Content Extractor Foundation

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D020.4.2 deployment handled by update engine"
EOF


chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

