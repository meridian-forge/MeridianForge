from meridianforge.domain.source import SourceType
from meridianforge.intake.csv_adapter import CSVAdapter
from meridianforge.intake.pdf_adapter import PDFAdapter
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
