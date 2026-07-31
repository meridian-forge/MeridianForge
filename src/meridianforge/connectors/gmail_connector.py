from __future__ import annotations

from pathlib import Path

from meridianforge.connectors.connector import (
    Connector,
)


class GmailConnector(Connector):
    """
    Gmail connector skeleton.

    MF-509.3

    This connector currently acts as a local stub that satisfies the
    Connector protocol. Future sprints will add OAuth authentication,
    inbox filtering, attachment extraction, and synchronization.
    """

    def __init__(
        self,
        label: str = "MeridianForge",
    ) -> None:
        self.label = label

    def sync(
        self,
        destination: Path,
    ) -> list[Path]:
        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Skeleton implementation: no Gmail API interaction yet.
        return []
