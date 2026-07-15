"""
Aggregate property model.
"""

from dataclasses import dataclass

from .acquisition import Acquisition
from .address import Address
from .assumptions import Assumptions
from .expenses import Expenses
from .financing import Financing
from .income import Income
from .metadata import Metadata


@dataclass(slots=True)
class Property:
    address: Address
    acquisition: Acquisition
    financing: Financing
    income: Income
    expenses: Expenses
    assumptions: Assumptions
    metadata: Metadata
