from pathlib import Path

from meridianforge.connectors.filesystem_connector import (
    FilesystemConnector,
)


def test_filesystem_connector_syncs_files(
    tmp_path: Path,
) -> None:
    source = tmp_path / "source"
    destination = tmp_path / "destination"

    source.mkdir()

    (source / "portfolio.xlsx").write_text("portfolio")
    (source / "offering.pdf").write_text("pdf")

    connector = FilesystemConnector(
        source,
    )

    files = connector.sync(
        destination,
    )

    assert len(files) == 2
    assert (destination / "portfolio.xlsx").exists()
    assert (destination / "offering.pdf").exists()
