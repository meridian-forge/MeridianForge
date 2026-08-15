from __future__ import annotations

from pathlib import Path

from meridianforge.runtime.runtime_locator import RuntimeLocator

WORKSPACE_FOLDERS = [
    "00_Project_Management",
    "01_Documents",
    "02_Data",
    "03_Templates",
    "04_Automation",
    "05_Analytics",
    "06_Portfolio",
    "07_Operations",
    "08_Reports",
    "09_Archive",
    "10_Runtime",
    "11_Backups",
]

RUNTIME_FOLDERS = [
    "credentials",
    "incoming",
    "processed",
    "reports",
    "dashboard",
    "logs",
    "temp",
]


class WorkspaceBootstrap:
    """Create and maintain the MeridianForge workspace layout."""

    def __init__(self, locator: RuntimeLocator | None = None) -> None:
        self._locator = locator or RuntimeLocator()

    @property
    def workspace_root(self) -> Path:
        return self._locator.workspace_root

    @property
    def runtime_root(self) -> Path:
        return self._locator.runtime_root

    def ensure_workspace(self) -> Path:
        self.workspace_root.mkdir(parents=True, exist_ok=True)

        for folder in WORKSPACE_FOLDERS:
            (self.workspace_root / folder).mkdir(parents=True, exist_ok=True)

        for folder in RUNTIME_FOLDERS:
            (self.runtime_root / folder).mkdir(parents=True, exist_ok=True)

        return self.workspace_root
