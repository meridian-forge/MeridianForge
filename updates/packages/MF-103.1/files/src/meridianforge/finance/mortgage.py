def monthly_payment(
    loan_amount: float,
    annual_rate: float,
    years: int,
) -> float:

    if loan_amount <= 0:
        raise ValueError(
            "Loan amount must be positive"
        )

    monthly_rate = annual_rate / 12
    payments = years * 12

    if monthly_rate == 0:
        return loan_amount / payments

    return (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** payments
        /
        ((1 + monthly_rate) ** payments - 1)
    )
