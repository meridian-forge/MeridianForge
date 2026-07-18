from dataclasses import dataclass


@dataclass
class PropertyInput:

    address: str

    purchase_price: float
    monthly_rent: float

    noi: float
    annual_cash_flow: float
    cash_invested: float
    annual_debt: float
