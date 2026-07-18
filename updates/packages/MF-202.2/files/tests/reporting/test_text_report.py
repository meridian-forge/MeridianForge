from meridianforge.ranking.models import RankingResult
from meridianforge.reporting.text_report import (
    generate_text_report,
)


def test_generate_report() -> None:

    rankings = [
        RankingResult(
            opportunity_file="property.xlsx",
            score=85,
            rank=1,
        )
    ]


    report = generate_text_report(
        rankings
    )


    assert (
        "property.xlsx"
        in report.content
    )
