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
