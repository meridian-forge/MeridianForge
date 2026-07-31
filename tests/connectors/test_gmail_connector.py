from pathlib import Path

from meridianforge.connectors.gmail_connector import (
    GmailConnector,
)
from meridianforge.connectors.registry import (
    ConnectorRegistry,
)


def test_gmail_connector_sync_returns_empty_list(
    tmp_path: Path,
) -> None:
    connector = GmailConnector()

    files = connector.sync(
        tmp_path,
    )

    assert files == []


def test_registry_returns_gmail_connector() -> None:
    registry = ConnectorRegistry()

    connector = registry.gmail()

    assert isinstance(
        connector,
        GmailConnector,
    )
