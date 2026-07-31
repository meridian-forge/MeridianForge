from __future__ import annotations

from pathlib import Path

from meridianforge.connectors.connector import (
    Connector,
)
from meridianforge.connectors.filesystem_connector import (
    FilesystemConnector,
)
from meridianforge.connectors.gmail_connector import (
    GmailConnector,
)


class ConnectorRegistry:
    """
    Registry of available MeridianForge connectors.

    The registry provides a stable lookup layer between configuration
    and connector implementations.
    """

    def filesystem(
        self,
        source_directory: Path,
    ) -> Connector:
        return FilesystemConnector(
            source_directory,
        )

    def gmail(
        self,
        label: str = "MeridianForge",
    ) -> Connector:
        return GmailConnector(
            label=label,
        )
