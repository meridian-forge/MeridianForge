"""
Excel template generator tests.
"""

from pathlib import Path

from meridianforge.importers.excel_template import (
    ExcelTemplateGenerator,
)


def test_excel_template_creation(
    tmp_path: Path,
) -> None:

    output = tmp_path / "template.xlsx"

    result = ExcelTemplateGenerator.generate(str(output))

    assert result.exists()
