from meridianforge.services.web_intake_service import (
    WebIntakeService,
)


def test_web_intake_service() -> None:

    document = WebIntakeService.ingest(
        "https://example.com/listing",
        "Property details",
    )

    assert document.metadata["url"] == (
        "https://example.com/listing"
    )
