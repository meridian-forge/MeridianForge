"""
Monday dashboard text renderer.

Creates investor-readable dashboard output.
"""

from meridianforge.reporting.dashboard_models import (
    MondayDashboard,
)


class MondayDashboardRenderer:
    """
    Converts dashboard model into text output.
    """

    @staticmethod
    def render(
        dashboard: MondayDashboard,
    ) -> str:

        lines: list[str] = []

        lines.append("=" * 60)

        lines.append("MERIDIAN FORGE")

        lines.append("MONDAY ACQUISITION DASHBOARD")

        lines.append("=" * 60)

        lines.append("")

        lines.append(f"Properties Reviewed: " f"{dashboard.total_reviewed}")

        lines.append(f"BUY: {dashboard.buy_count}")

        lines.append(f"WATCH: {dashboard.watch_count}")

        lines.append(f"PASS: {dashboard.pass_count}")

        lines.append("")

        if dashboard.top_opportunity:

            card = dashboard.top_opportunity

            lines.append("TOP OPPORTUNITY")

            lines.append("-" * 40)

            lines.append(card.property_address)

            lines.append(f"Recommendation: " f"{card.recommendation}")

            lines.append(f"Confidence: " f"{card.confidence:.0%}")

        lines.append("")

        if dashboard.buy_cards:

            lines.append("BUY LIST")

            lines.append("-" * 40)

            for card in dashboard.buy_cards:

                lines.append(
                    f"{card.rank}. "
                    f"{card.property_address} "
                    f"({card.confidence:.0%})"
                )

        lines.append("")

        if dashboard.watch_cards:

            lines.append("WATCH LIST")

            lines.append("-" * 40)

            for card in dashboard.watch_cards:

                lines.append(
                    f"{card.rank}. "
                    f"{card.property_address} "
                    f"({card.confidence:.0%})"
                )

        lines.append("")

        if dashboard.pass_cards:

            lines.append("PASS LIST")

            lines.append("-" * 40)

            for card in dashboard.pass_cards:

                lines.append(f"{card.rank}. " f"{card.property_address}")

        return "\n".join(lines)
