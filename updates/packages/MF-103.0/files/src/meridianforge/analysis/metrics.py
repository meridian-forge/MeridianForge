def calculate_cap_rate(
    annual_noi: float,
    purchase_price: float,
) -> float:

    if purchase_price <= 0:
        raise ValueError(
            "Purchase price must be positive"
        )

    return annual_noi / purchase_price



def calculate_cash_on_cash(
    annual_cash_flow: float,
    cash_invested: float,
) -> float:

    if cash_invested <= 0:
        raise ValueError(
            "Cash invested must be positive"
        )

    return annual_cash_flow / cash_invested



def calculate_dscr(
    noi: float,
    annual_debt: float,
) -> float:

    if annual_debt <= 0:
        raise ValueError(
            "Debt service must be positive"
        )

    return noi / annual_debt
