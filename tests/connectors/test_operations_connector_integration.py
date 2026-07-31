from pathlib import Path

from meridianforge.connectors.filesystem_connector import (
    FilesystemConnector,
)
from meridianforge.services.operations_service import (
    OperationsService,
)


def test_operations_service_runs_connector_before_discovery(
    tmp_path: Path,
) -> None:
    source = tmp_path / "source"
    working = tmp_path / "working"

    source.mkdir()

    (source / "portfolio.xlsx").write_text("portfolio")

    connector = FilesystemConnector(
        source,
    )

    service = OperationsService(
        deals_directory=working,
        connector=connector,
    )

    result = service.execute()

    assert (working / "portfolio.xlsx").exists()
    assert len(result.files_discovered) == 1
