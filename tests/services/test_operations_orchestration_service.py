from pathlib import Path

from meridianforge.services.operations_service import OperationsService


def test_operations_service_discovers_files(tmp_path: Path) -> None:
    deals = tmp_path / "deals"
    deals.mkdir()

    first = deals / "property.xlsx"
    second = deals / "property.pdf"

    first.write_text("test")
    second.write_text("test")

    service = OperationsService(
        deals_directory=deals,
    )

    result = service.execute()

    assert result.total_files == 2
    assert first in result.files_discovered
    assert second in result.files_discovered


def test_operations_service_handles_missing_directory(
    tmp_path: Path,
) -> None:
    missing = tmp_path / "missing"

    service = OperationsService(
        deals_directory=missing,
    )

    result = service.execute()

    assert result.total_files == 0
    assert result.success
