from pathlib import Path

from openpyxl import load_workbook

from meridianforge.ranking.models import RankingResult
from meridianforge.reporting.excel_report import (
    export_excel_report,
)


def test_excel_export(
    tmp_path: Path,
) -> None:

    output = tmp_path / "results.xlsx"

    rankings = [
        RankingResult(
            opportunity_file="deal.xlsx",
            score=90,
            rank=1,
        )
    ]

    export_excel_report(
        rankings,
        output,
    )

    workbook = load_workbook(output)

    sheet = workbook["Rankings"]

    assert sheet["B2"].value == "deal.xlsx"
