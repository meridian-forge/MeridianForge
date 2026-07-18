def monthly_expenses(
    rent: float,
    vacancy: float,
    repairs: float,
    management: float,
    insurance: float,
    taxes: float,
) -> float:

    return rent * vacancy + rent * repairs + rent * management + insurance + taxes
