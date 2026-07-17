from meridianforge.models.domain.attachment_document import (
    AttachmentDocument,
)


def test_attachment_document() -> None:

    document = AttachmentDocument(
        filename="deal.pdf",
        attachment_type="PDF",
    )

    assert document.attachment_type == "PDF"
