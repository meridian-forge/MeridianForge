from dataclasses import asdict, dataclass


@dataclass
class InvestorProfile:
    """
    Defines investor-specific objectives and assumptions.
    """

    name: str
    strategy: str
    primary_goal: str
    risk_level: str

    financing_type: str
    interest_rate: float
    down_payment_percent: float

    hold_period_years: int
    target_number_of_properties: int

    tax_strategy: str

    def to_dict(self) -> dict:
        return asdict(self)

    def validate(self) -> bool:
        if not self.name:
            raise ValueError("Investor name is required")

        if not 0 < self.interest_rate < 1:
            raise ValueError("Interest rate must be between 0 and 1")

        if not 0 < self.down_payment_percent < 1:
            raise ValueError("Down payment percent must be between 0 and 1")

        if self.hold_period_years <= 0:
            raise ValueError("Hold period must be positive")

        if self.target_number_of_properties <= 0:
            raise ValueError("Target number of properties must be positive")

        return True
