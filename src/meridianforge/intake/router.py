from meridianforge.intake.csv_adapter import CSVAdapter
from meridianforge.intake.email_adapter import EmailAdapter
from meridianforge.intake.manual_adapter import ManualAdapter
from meridianforge.intake.pdf_adapter import PDFAdapter
from meridianforge.intake.url_adapter import URLAdapter
from meridianforge.intake.xlsx_adapter import XLSXAdapter

AdapterType = (
    CSVAdapter | EmailAdapter | ManualAdapter | PDFAdapter | URLAdapter | XLSXAdapter
)


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
