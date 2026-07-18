from dataclasses import dataclass


@dataclass
class Scenario:

    name: str

    rent_multiplier: float = 1.0
    vacancy_multiplier: float = 1.0
    expense_multiplier: float = 1.0
    interest_rate_multiplier: float = 1.0
