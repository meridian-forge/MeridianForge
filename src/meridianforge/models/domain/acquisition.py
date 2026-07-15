"""
Acquisition information.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Acquisition:
    purchase_price: float
    closing_costs: float
    rehab_cost: float = 0.0

    def __post_init__(self) -> None:
        if self.purchase_price <= 0:
            raise ValueError("Purchase price must be positive.")

        if self.closing_costs < 0:
            raise ValueError("Closing costs cannot be negative.")

        if self.rehab_cost < 0:
            raise ValueError("Rehab cost cannot be negative.")

    @property
    def total_project_cost(self) -> float:
        return self.purchase_price + self.closing_costs + self.rehab_cost
