def confidence_from_score(score: float) -> str:
    if score >= 90:
        return "VERY_HIGH"

    if score >= 75:
        return "HIGH"

    if score >= 60:
        return "MODERATE"

    return "LOW"
