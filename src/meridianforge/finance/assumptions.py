from dataclasses import dataclass


@dataclass
class FinancialAssumptions:

    purchase_price: float

    down_payment_percent: float
    interest_rate: float
    loan_years: int

    monthly_rent: float

    vacancy_percent: float
    repairs_percent: float
    management_percent: float

    insurance_monthly: float
    taxes_monthly: float
