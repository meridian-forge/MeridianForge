def evaluate_rules(
    cash_flow: float,
    dscr: float,
    appreciation_score: float,
) -> str:
    """
    Basic investment decision rules.
    """

    if cash_flow > 0 and dscr >= 1.20 and appreciation_score >= 70:
        return "BUY"

    if cash_flow > 0 and dscr >= 1.0:
        return "HOLD"

    return "PASS"
