from pathlib import Path


FILES = {
    "src/meridianforge/intake/router.py": """
from typing import Union

from meridianforge.intake.csv_adapter import CSVAdapter
from meridianforge.intake.email_adapter import EmailAdapter
from meridianforge.intake.manual_adapter import ManualAdapter
from meridianforge.intake.pdf_adapter import PDFAdapter
from meridianforge.intake.url_adapter import URLAdapter
from meridianforge.intake.xlsx_adapter import XLSXAdapter


AdapterType = Union[
    CSVAdapter,
    EmailAdapter,
    ManualAdapter,
    PDFAdapter,
    URLAdapter,
    XLSXAdapter,
]


class IntakeRouter:

    def select(self, location: str) -> AdapterType:

        suffix = location.lower()

        if suffix.startswith("http"):
            return URLAdapter()

        if suffix.endswith(".pdf"):
            return PDFAdapter()

        if suffix.endswith(".csv"):
            return CSVAdapter()

        if suffix.endswith(".xlsx"):
            return XLSXAdapter()

        if suffix.endswith(".eml"):
            return EmailAdapter()

        return ManualAdapter()
""",

    "src/meridianforge/intake/workflow.py": """
from meridianforge.domain.opportunity import Opportunity
from meridianforge.intake.router import IntakeRouter


class IntakeWorkflow:

    def __init__(self) -> None:
        self.router = IntakeRouter()

    def create_opportunity(
        self,
        name: str,
        location: str,
    ) -> Opportunity:

        adapter = self.router.select(location)

        source = adapter.ingest(location)

        return Opportunity(
            name=name,
            source=source,
        )
"""
}


def main() -> None:

    root = Path.cwd()

    for path, content in FILES.items():

        target = root / path

        target.write_text(
            content.strip() + "\n",
            encoding="utf-8",
        )

        print(f"UPDATED: {path}")

    print()
    print("MF-102.1.3.1 MYPY FIX COMPLETE")


if __name__ == "__main__":
    main()