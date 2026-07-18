from pathlib import Path


PACKAGE = Path("updates/packages/MF-102.1.2")


FILES = {
    "manifest.txt": """
MF-102.1.2
File Intake Adapters

Adds:
- PDF adapter
- CSV adapter
- XLSX adapter
- Email adapter foundation
""",

    "release_notes.md": """
# MF-102.1.2 File Intake Adapters

Adds file-based ingestion support.

Supported:
- PDF
- CSV
- XLSX
- Email
""",

    "files/src/meridianforge/intake/file_adapter.py": """
from abc import ABC, abstractmethod

from meridianforge.domain.source import Source


class FileAdapter(ABC):

    @abstractmethod
    def ingest(self, location: str) -> Source:
        raise NotImplementedError
""",

    "files/src/meridianforge/intake/pdf_adapter.py": """
from pathlib import Path

from meridianforge.domain.source import Source, SourceType

from meridianforge.intake.file_adapter import FileAdapter


class PDFAdapter(FileAdapter):

    def ingest(self, location: str) -> Source:

        if not Path(location).exists():
            raise FileNotFoundError(location)

        return Source(
            source_type=SourceType.PDF,
            location=location,
        )
""",

    "files/src/meridianforge/intake/csv_adapter.py": """
from pathlib import Path

from meridianforge.domain.source import Source, SourceType

from meridianforge.intake.file_adapter import FileAdapter


class CSVAdapter(FileAdapter):

    def ingest(self, location: str) -> Source:

        if not Path(location).exists():
            raise FileNotFoundError(location)

        return Source(
            source_type=SourceType.CSV,
            location=location,
        )
""",

    "files/src/meridianforge/intake/xlsx_adapter.py": """
from pathlib import Path

from meridianforge.domain.source import Source, SourceType

from meridianforge.intake.file_adapter import FileAdapter


class XLSXAdapter(FileAdapter):

    def ingest(self, location: str) -> Source:

        if not Path(location).exists():
            raise FileNotFoundError(location)

        return Source(
            source_type=SourceType.XLSX,
            location=location,
        )
""",

    "files/src/meridianforge/intake/email_adapter.py": """
from meridianforge.domain.source import Source, SourceType

from meridianforge.intake.file_adapter import FileAdapter


class EmailAdapter(FileAdapter):

    def ingest(self, location: str) -> Source:

        return Source(
            source_type=SourceType.EMAIL,
            location=location,
        )
""",

    "files/tests/intake/test_file_adapters.py": """
from pathlib import Path

from meridianforge.domain.source import SourceType
from meridianforge.intake.pdf_adapter import PDFAdapter
from meridianforge.intake.csv_adapter import CSVAdapter
from meridianforge.intake.xlsx_adapter import XLSXAdapter


def test_pdf_adapter(tmp_path):

    file = tmp_path / "property.pdf"
    file.write_text("test")

    source = PDFAdapter().ingest(str(file))

    assert source.source_type == SourceType.PDF


def test_csv_adapter(tmp_path):

    file = tmp_path / "property.csv"
    file.write_text("test")

    source = CSVAdapter().ingest(str(file))

    assert source.source_type == SourceType.CSV


def test_xlsx_adapter(tmp_path):

    file = tmp_path / "property.xlsx"
    file.write_text("test")

    source = XLSXAdapter().ingest(str(file))

    assert source.source_type == SourceType.XLSX
"""
}


def main():

    if PACKAGE.exists():
        for item in PACKAGE.rglob("*"):
            if item.is_file():
                item.unlink()

    PACKAGE.mkdir(parents=True, exist_ok=True)

    for name, content in FILES.items():

        target = PACKAGE / name

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
    print("MF-102.1.2 PACKAGE CREATED")


if __name__ == "__main__":
    main()