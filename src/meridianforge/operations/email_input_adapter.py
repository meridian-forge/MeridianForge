from __future__ import annotations

from pathlib import Path

from meridianforge.connectors.gmail_connector import GmailConnector
from meridianforge.operations.input_adapter import InputAdapter


class EmailInputAdapter(InputAdapter):
    """
    Email-backed input adapter.

    Production mode:
        Synchronizes Gmail into the canonical workspace runtime directory.

    Test mode:
        When a runtime_root Path is provided, behaves as a simple directory
        adapter so existing unit tests remain valid.
    """

    def __init__(
        self,
        runtime_root: Path | None = None,
        label: str = "MeridianForge",
    ) -> None:
        workspace = Path.home() / "Documents" / "MeridianForge"

        # Test mode: use provided directory directly.
        if runtime_root is not None:
            self.runtime_root = runtime_root
            self.incoming_directory = runtime_root
            self.connector = None
            return

        # Production mode: Gmail sync into workspace runtime.
        self.runtime_root = workspace / "10_Runtime"
        self.incoming_directory = (
            self.runtime_root / "Incoming" / "Email"
        )
        self.connector = GmailConnector(
            label=label,
            destination=self.incoming_directory,
        )

    def discover(self) -> list[Path]:
        """
        Return newly available email artifacts.

        In production this synchronizes Gmail first.
        In tests it scans the provided directory.
        """

        if self.connector is None:
            if not self.incoming_directory.exists():
                return []

            return sorted(
                path
                for path in self.incoming_directory.iterdir()
                if path.is_file()
            )

        self.incoming_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        return self.connector.sync(
            self.incoming_directory,
        )
