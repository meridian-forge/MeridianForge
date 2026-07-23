"""
Ranking category classification.

MF-337.1
"""


def classify_rank_score(
    score: float,
) -> str:
    """
    Convert score into investor category.
    """

    if score >= 90:
        return "A+"

    if score >= 80:
        return "A"

    if score >= 70:
        return "B"

    if score >= 60:
        return "C"

    return "D"
