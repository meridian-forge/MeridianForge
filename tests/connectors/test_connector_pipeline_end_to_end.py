from pathlib import Path

from meridianforge.connectors.filesystem_connector import (
    FilesystemConnector,
)
from meridianforge.services.operations_service import (
    OperationsService,
)
from meridianforge.workflows.monday_execution_pipeline import (
    MondayExecutionPipeline,
)


def test_connector_pipeline_end_to_end(
    tmp_path: Path,
) -> None:
    source = tmp_path / "source"
    working = tmp_path / "working"

    source.mkdir()

    workbook = source / "portfolio.xlsx"
    workbook.write_bytes(b"not-a-real-xlsx")

    connector = FilesystemConnector(
        source,
    )

    operations = OperationsService(
        deals_directory=working,
        connector=connector,
    )

    operations_result = operations.execute()

    assert (working / "portfolio.xlsx").exists()
    assert len(operations_result.files_discovered) == 1

    pipeline = MondayExecutionPipeline(
        deals_directory=working,
    )

    pipeline_result = pipeline.execute()

    assert pipeline_result.operations is not None
    assert pipeline_result.analysis is not None

    # Invalid workbook input should not break the canonical pipeline.
    assert pipeline_result.intelligence is None
