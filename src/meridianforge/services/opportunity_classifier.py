"""
Opportunity classification service.

MF-512.1.1

Classifies incoming investment artifacts into the Family Office
OS opportunity taxonomy before extraction occurs.
"""

from __future__ import annotations

from pathlib import Path

from meridianforge.models.opportunity import (
    OpportunityClassification,
    OpportunityType,
)


class OpportunityClassifier:
    """
    Lightweight heuristic classifier for incoming investment artifacts.
    """

    @staticmethod
    def classify(
        path: Path,
        text: str = "",
    ) -> OpportunityClassification:
        name = path.name.lower()
        ext = path.suffix.lower()
        content = text.lower()

        # ---------------------------------------------------------
        # Private lending / secured notes (highest priority)
        # ---------------------------------------------------------
        lending_signals = (
            "interest rate",
            "interest-only",
            "lien",
            "ltv",
            "note",
            "maturity",
            "quarterly",
            "secured",
        )

        if any(signal in content for signal in lending_signals):
            return OpportunityClassification(
                opportunity_type=OpportunityType.PRIVATE_LENDING,
                confidence=0.97,
                reason="Private lending terms detected",
            )

        # ---------------------------------------------------------
        # Rental acquisition
        # Property-level investment metrics should win over generic
        # inventory marketing language inside PDFs.
        # ---------------------------------------------------------
        rental_signals = (
            "rent:",
            "cashflow",
            "cash flow",
            "roi",
            "property",
            "price:",
            "bed",
            "bath",
            "turnkey",
            "rosharon",
        )

        rental_score = sum(signal in content for signal in rental_signals)

        if rental_score >= 2:
            return OpportunityClassification(
                opportunity_type=OpportunityType.RENTAL_ACQUISITION,
                confidence=0.96,
                reason="Property-level rental acquisition metrics detected",
            )

        # ---------------------------------------------------------
        # Inventory workbook
        # Reserve this primarily for workbook-style inventory files.
        # ---------------------------------------------------------
        if ext in {".xlsx", ".xls", ".csv"} and (
            "inventory" in name or "available inventory" in content
        ):
            return OpportunityClassification(
                opportunity_type=OpportunityType.INVENTORY_WORKBOOK,
                confidence=0.98,
                reason="Inventory workbook detected from workbook filename/content",
            )

        # ---------------------------------------------------------
        # Syndication / fund
        # ---------------------------------------------------------
        syndication_signals = (
            "sponsor",
            "fund",
            "hold period",
            "minimum investment",
            "preferred return",
            "limited partner",
        )

        if any(signal in content for signal in syndication_signals):
            return OpportunityClassification(
                opportunity_type=OpportunityType.SYNDICATION,
                confidence=0.95,
                reason="Syndication indicators detected",
            )

        return OpportunityClassification(
            opportunity_type=OpportunityType.UNKNOWN,
            confidence=0.10,
            reason="No opportunity classification signals detected",
        )
