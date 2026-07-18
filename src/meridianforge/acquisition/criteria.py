from dataclasses import dataclass


@dataclass
class AcquisitionCriteria:

    minimum_dscr: float = 1.20
    minimum_cap_rate: float = 0.05
    minimum_cash_return: float = 0.08
