from meridianforge.ranking.models import RankingResult
from meridianforge.reporting.models import Report


def generate_text_report(
    rankings: list[RankingResult],
) -> Report:

    lines: list[str] = []

    lines.append(
        "Meridian Forge Investment Review"
    )

    lines.append(
        "================================"
    )


    for item in rankings:

        lines.append(
            (
                f"#{item.rank} "
                f"{item.opportunity_file} "
                f"- Score: {item.score:.1f}"
            )
        )


    return Report(
        title="Investment Review",
        content="\n".join(lines),
    )
