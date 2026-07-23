"""
Portfolio domain model.

MF-341.1

Represents an investor portfolio
containing acquisition assets.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Portfolio:
    """
    Investor portfolio aggregate.

    Owns portfolio identity and asset collection.
    """

    name: str

    strategy: str

    assets: list[Any] = field(
        default_factory=list,
    )

    created_at: datetime = field(
        default_factory=datetime.now,
    )

    def add_asset(
        self,
        asset: Any,
    ) -> None:
        """
        Add an acquisition asset.
        """

        self.assets.append(asset)

    @property
    def asset_count(self) -> int:
        """
        Number of assets in portfolio.
        """

        return len(self.assets)
