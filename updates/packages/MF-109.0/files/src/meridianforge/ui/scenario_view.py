from typing import Any


def summarize_scenarios(
    scenarios: list[dict[str, Any]],
) -> dict[str, int]:

    summary = {
        "PASS": 0,
        "WATCH": 0,
        "FAIL": 0,
    }

    for item in scenarios:

        status = item.get(
            "status",
            "WATCH",
        )

        if status in summary:
            summary[status] += 1

    return summary
