def generate_explanation(
    recommendation: str,
) -> list[str]:
    """
    Creates investor-readable reasoning.
    """

    explanations = {
        "BUY": [
            "Positive cash flow",
            "Healthy debt coverage",
            "Strong appreciation alignment",
        ],
        "HOLD": [
            "Acceptable fundamentals",
            "Additional review recommended",
        ],
        "PASS": [
            "Does not meet investment thresholds",
        ],
    }

    return explanations.get(
        recommendation,
        [],
    )
