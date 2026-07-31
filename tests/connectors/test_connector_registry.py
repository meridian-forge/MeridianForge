from pathlib import Path

from meridianforge.connectors.filesystem_connector import (
    FilesystemConnector,
)
from meridianforge.connectors.registry import (
    ConnectorRegistry,
)


def test_registry_returns_filesystem_connector(
    tmp_path: Path,
) -> None:
    registry = ConnectorRegistry()

    connector = registry.filesystem(
        tmp_path,
    )

    assert isinstance(
        connector,
        FilesystemConnector,
    )
