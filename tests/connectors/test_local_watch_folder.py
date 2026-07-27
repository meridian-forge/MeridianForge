from pathlib import Path

from meridianforge.connectors.folder_connector import (
    FolderConnector,
)


def test_folder_connector_imports_supported_files(
    tmp_path: Path,
) -> None:
    deal_file = tmp_path / "deal.xlsx"

    deal_file.touch()

    connector = FolderConnector()

    records = connector.import_folder(
        tmp_path,
    )

    assert len(records) == 1

    assert records[0].source == "FOLDER"

    assert records[0].source_reference == str(
        deal_file
    )
