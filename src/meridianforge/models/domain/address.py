"""
Address domain model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Address:
    """
    Physical location of a property.
    """

    street: str
    city: str
    state: str
    zip_code: str

    def __post_init__(self) -> None:
        self.street = self.street.strip()
        self.city = self.city.strip()
        self.state = self.state.strip().upper()
        self.zip_code = self.zip_code.strip()

        if len(self.state) != 2:
            raise ValueError("State must be a two-letter abbreviation.")
