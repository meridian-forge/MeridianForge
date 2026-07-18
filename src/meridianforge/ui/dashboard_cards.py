from typing import Any


def decision_card(
    result: dict[str, Any],
) -> dict[str, Any]:

    decision = result.get(
        "decision",
        "UNKNOWN",
    )

    score = result.get(
        "score",
        0,
    )

    return {
        "decision": decision,
        "score": score,
        "rating": ("GREEN" if score >= 80 else "YELLOW"),
    }
