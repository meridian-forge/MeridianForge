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
