def calculate_cash_on_cash(
    annual_cash_flow: float,
    cash_invested: float,
) -> float:

    if cash_invested == 0:
        return 0.0

    return annual_cash_flow / cash_invested


def cash_on_cash_return(
    annual_cash_flow: float,
    cash_invested: float,
) -> float:

    return calculate_cash_on_cash(
        annual_cash_flow,
        cash_invested,
    )


def roi(
    profit: float,
    investment: float,
) -> float:

    if investment == 0:
        return 0.0

    return profit / investment


def calculate_cap_rate(
    annual_noi: float,
    property_value: float,
) -> float:

    if property_value == 0:
        return 0.0

    return annual_noi / property_value


def calculate_dscr(
    annual_noi: float,
    annual_debt_service: float,
) -> float:

    if annual_debt_service == 0:
        return 0.0

    return annual_noi / annual_debt_service
