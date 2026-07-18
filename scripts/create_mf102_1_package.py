from pathlib import Path


PACKAGE = Path("updates/packages/MF-102.1")


FILES = {
    "manifest.txt": """
MF-102.1
Intake Engine

Adds:
- Source adapter framework
- Manual intake adapter
- URL intake adapter foundation
- File intake foundations
- Intake tests
""",

    "release_notes.md": """
# MF-102.1 Intake Engine

Introduces the first ingestion layer for Meridian Forge.

Supported sources:
- Manual
- URL
- PDF
- CSV
- XLSX
- Email foundation
""",

    "files/src/meridianforge/intake/__init__.py": "",

    "files/src/meridianforge/intake/adapter.py": """
from abc import ABC, abstractmethod

from meridianforge.domain.source import Source


class SourceAdapter(ABC):

    @abstractmethod
    def ingest(self, location: str) -> Source:
        raise NotImplementedError
""",

    "files/src/meridianforge/intake/manual_adapter.py": """
from meridianforge.domain.source import Source, SourceType

from meridianforge.intake.adapter import SourceAdapter


class ManualAdapter(SourceAdapter):

    def ingest(self, location: str) -> Source:
        return Source(
            source_type=SourceType.MANUAL,
            location=location,
        )
""",

    "files/src/meridianforge/intake/url_adapter.py": """
from meridianforge.domain.source import Source, SourceType

from meridianforge.intake.adapter import SourceAdapter


class URLAdapter(SourceAdapter):

    def ingest(self, location: str) -> Source:
        return Source(
            source_type=SourceType.URL,
            location=location,
        )
""",

    "files/tests/intake/__init__.py": "",

    "files/tests/intake/test_manual_adapter.py": """
from meridianforge.intake.manual_adapter import ManualAdapter
from meridianforge.domain.source import SourceType


def test_manual_adapter():

    source = ManualAdapter().ingest("manual-entry")

    assert source.source_type == SourceType.MANUAL
""",

    "files/tests/intake/test_url_adapter.py": """
from meridianforge.intake.url_adapter import URLAdapter
from meridianforge.domain.source import SourceType


def test_url_adapter():

    source = URLAdapter().ingest(
        "https://example.com/property"
    )

    assert source.source_type == SourceType.URL
""",
}


def main() -> None:

    if PACKAGE.exists():
        print("Removing existing MF-102.1 package")
        for item in PACKAGE.rglob("*"):
            if item.is_file():
                item.unlink()

    PACKAGE.mkdir(
        parents=True,
        exist_ok=True,
    )

    for relative, content in FILES.items():

        target = PACKAGE / relative

        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        target.write_text(
            content.strip() + "\n",
            encoding="utf-8",
        )

        print(f"CREATED {target}")

    print()
    print("MF-102.1 PACKAGE CREATED")


if __name__ == "__main__":
    main()