from meridianforge.services.attachment_intake_service import (
    AttachmentIntakeService,
)


def test_attachment_intake_service() -> None:

    result = AttachmentIntakeService.ingest(
        "brochure.pdf",
    )

    assert result.attachment_type == "PDF"
