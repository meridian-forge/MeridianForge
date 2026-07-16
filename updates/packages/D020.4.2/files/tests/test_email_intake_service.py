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
