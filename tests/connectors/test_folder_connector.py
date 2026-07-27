from pathlib import Path

from meridianforge.connectors.folder_connector import FolderConnector


def test_folder_connector_imports_supported_files(
    tmp_path: Path,
) -> None:
    (tmp_path / "deal.xlsx").touch()
    (tmp_path / "offering.pdf").touch()
    (tmp_path / "notes.docx").touch()

    connector = FolderConnector()

    records = connector.import_folder(tmp_path)

    assert len(records) == 3

    assert all(record.status == "READY" for record in records)
