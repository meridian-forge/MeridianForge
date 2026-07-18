from meridianforge.analysis.models import AnalysisResult
from meridianforge.ranking.models import RankingResult


def calculate_score(
    analysis: AnalysisResult,
) -> float:

    score = 50.0


    if "cash_on_cash" in analysis.metrics:

        coc = analysis.metrics["cash_on_cash"]

        score += min(
            coc * 100,
            20,
        )


    if "dscr" in analysis.metrics:

        dscr = analysis.metrics["dscr"]

        if dscr >= 1.25:
            score += 15


    if analysis.warnings:

        score -= (
            len(analysis.warnings)
            * 5
        )


    return max(
        0,
        min(
            score,
            100,
        ),
    )


def rank(
    analyses: list[AnalysisResult],
) -> list[RankingResult]:

    ranked = [

        RankingResult(
            opportunity_file=result.opportunity_file,
            score=calculate_score(result),
        )

        for result in analyses
    ]


    ranked.sort(
        key=lambda item: item.score,
        reverse=True,
    )


    for index, item in enumerate(
        ranked,
        start=1,
    ):

        item.rank = index


    return ranked
