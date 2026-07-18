def build_rationale(score: float, risk_level: str) -> str:
    reasons = []

    if score >= 75:
        reasons.append("Strong investment score")
    else:
        reasons.append("Investment score requires review")

    reasons.append(f"Risk profile: {risk_level}")

    return "; ".join(reasons)
