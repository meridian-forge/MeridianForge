from pathlib import Path

from openpyxl import Workbook

from meridianforge.ranking.models import RankingResult


def export_excel_report(
    rankings: list[RankingResult],
    output_path: Path,
) -> None:

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Rankings"


    sheet.append(
        [
            "Rank",
            "Opportunity",
            "Score",
        ]
    )


    for item in rankings:

        sheet.append(
            [
                item.rank,
                item.opportunity_file,
                item.score,
            ]
        )


    workbook.save(
        output_path
    )
