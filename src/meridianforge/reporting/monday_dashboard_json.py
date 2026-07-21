"""
Monday dashboard JSON exporter.

Creates machine-readable dashboard artifacts.
"""

import json
from pathlib import Path

from meridianforge.reporting.dashboard_models import (
    MondayDashboard,
)


class MondayDashboardJSONExporter:
    """
    Export dashboard into JSON format.
    """

    @staticmethod
    def to_dict(
        dashboard: MondayDashboard,
    ) -> dict[str, object]:

        return {
            "summary": {
                "total_reviewed": dashboard.total_reviewed,
                "buy_count": dashboard.buy_count,
                "watch_count": dashboard.watch_count,
                "pass_count": dashboard.pass_count,
            },
            "top_opportunity": (
                {
                    "address": (dashboard.top_opportunity.property_address),
                    "recommendation": (dashboard.top_opportunity.recommendation),
                    "confidence": (dashboard.top_opportunity.confidence),
                }
                if dashboard.top_opportunity
                else None
            ),
            "buy": [
                {
                    "rank": card.rank,
                    "address": card.property_address,
                    "confidence": card.confidence,
                }
                for card in dashboard.buy_cards
            ],
            "watch": [
                {
                    "rank": card.rank,
                    "address": card.property_address,
                    "confidence": card.confidence,
                }
                for card in dashboard.watch_cards
            ],
            "pass": [
                {
                    "rank": card.rank,
                    "address": card.property_address,
                    "confidence": card.confidence,
                }
                for card in dashboard.pass_cards
            ],
        }

    @staticmethod
    def export(
        dashboard: MondayDashboard,
        output_file: Path,
    ) -> None:

        output_file.write_text(
            json.dumps(
                MondayDashboardJSONExporter.to_dict(dashboard),
                indent=2,
            )
        )
