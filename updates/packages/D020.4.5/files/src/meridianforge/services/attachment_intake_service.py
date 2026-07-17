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
