from __future__ import annotations

import os
from pathlib import Path


class RuntimeLocator:
    """Resolve MeridianForge workspace and runtime paths."""

    def __init__(self, workspace_root: Path | None = None) -> None:
        if workspace_root is not None:
            self._workspace_root = workspace_root.expanduser().resolve()
        else:
            home = os.environ.get("MERIDIANFORGE_HOME")
            if home:
                self._workspace_root = Path(home).expanduser().resolve()
            else:
                self._workspace_root = Path.home() / "Documents" / "MeridianForge"

    @property
    def workspace_root(self) -> Path:
        return self._workspace_root

    @property
    def runtime_root(self) -> Path:
        return self.workspace_root / "10_Runtime"

    @property
    def reports_dir(self) -> Path:
        return self.runtime_root / "reports"

    @property
    def dashboard_dir(self) -> Path:
        return self.runtime_root / "dashboard"

    @property
    def credentials_dir(self) -> Path:
        return self.runtime_root / "credentials"

    @property
    def logs_dir(self) -> Path:
        return self.runtime_root / "logs"

    @property
    def incoming_dir(self) -> Path:
        return self.runtime_root / "incoming"

    @property
    def archive_dir(self) -> Path:
        return self.runtime_root / "archive"
