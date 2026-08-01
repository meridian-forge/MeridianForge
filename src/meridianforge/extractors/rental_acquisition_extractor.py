"""
Rental acquisition metadata extractor.

MF-512.1.2

Extracts structured acquisition metadata from rental property
marketing documents before underwriting and dashboard rendering.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RentalAcquisitionRecord:
    city: str
    state: str
    price: int
    rent: int
    cash_flow: int | None
    roi: float | None
    source_file: Path


class RentalAcquisitionExtractor:
    """
    Extracts structured metadata from rental acquisition documents.
    """

    LOCATION_RE = re.compile(
        r"Location:\s*([^,\n]+),\s*([A-Z]{2})",
        re.IGNORECASE,
    )

    PRICE_RE = re.compile(
        r"Price:\s*\$([0-9,]+)",
        re.IGNORECASE,
    )

    RENT_RE = re.compile(
        r"Rent:\s*\$([0-9,]+)",
        re.IGNORECASE,
    )

    CASHFLOW_RE = re.compile(
        r"Cashflow:\s*\$([0-9,]+)",
        re.IGNORECASE,
    )

    ROI_RE = re.compile(
        r"ROI:\s*([0-9]+(?:\.[0-9]+)?)%",
        re.IGNORECASE,
    )

    @classmethod
    def extract(
        cls,
        text: str,
        source_file: Path,
    ) -> RentalAcquisitionRecord | None:
        location = cls.LOCATION_RE.search(text)
        price = cls.PRICE_RE.search(text)
        rent = cls.RENT_RE.search(text)

        if not (location and price and rent):
            return None

        cashflow = cls.CASHFLOW_RE.search(text)
        roi = cls.ROI_RE.search(text)

        return RentalAcquisitionRecord(
            city=location.group(1).strip(),
            state=location.group(2).strip().upper(),
            price=int(price.group(1).replace(",", "")),
            rent=int(rent.group(1).replace(",", "")),
            cash_flow=(int(cashflow.group(1).replace(",", "")) if cashflow else None),
            roi=float(roi.group(1)) if roi else None,
            source_file=source_file,
        )
