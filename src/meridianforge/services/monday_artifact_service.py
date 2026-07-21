"""
Monday artifact generation service.

Creates investor-facing outputs:
- Dashboard
- JSON
- Decision briefs
"""

from pathlib import Path

from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.reporting.decision_brief import (
    DecisionBriefBuilder,
)
from meridianforge.reporting.monday_dashboard_builder import (
    MondayDashboardBuilder,
)
from meridianforge.reporting.monday_dashboard_json import (
    MondayDashboardJSONExporter,
)
from meridianforge.reporting.monday_dashboard_renderer import (
    MondayDashboardRenderer,
)


class MondayArtifactService:
    """
    Generates Monday investor package.
    """

    def generate(
        self,
        review: WeeklyInvestorReview,
        output_directory: Path,
    ) -> Path:

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        buy_dir = output_directory / "BUY"
        watch_dir = output_directory / "WATCH"
        pass_dir = output_directory / "PASS"

        buy_dir.mkdir(exist_ok=True)
        watch_dir.mkdir(exist_ok=True)
        pass_dir.mkdir(exist_ok=True)

        dashboard = MondayDashboardBuilder.build(review)

        # Dashboard.txt

        dashboard_text = MondayDashboardRenderer.render(dashboard)

        (output_directory / "Dashboard.txt").write_text(dashboard_text)

        # Dashboard.json

        MondayDashboardJSONExporter.export(
            dashboard,
            output_directory / "Dashboard.json",
        )

        # Decision briefs

        for card in review.cards:

            brief = DecisionBriefBuilder.build(card)

            folder = (
                buy_dir
                if card.recommendation.upper() == "BUY"
                else watch_dir if card.recommendation.upper() == "WATCH" else pass_dir
            )

            filename = card.property_address.replace(" ", "_") + ".txt"

            content = f"""
MERIDIAN FORGE INVESTMENT DECISION

Recommendation:
{brief.recommendation}

Property:
{brief.property_address}

Confidence:
{brief.confidence:.0%}


STRENGTHS
---------
"""

            for item in brief.strengths:
                content += f"- {item}\n"

            content += """

RISKS
-----
"""

            for item in brief.risks:
                content += f"- {item}\n"

            content += """

INVESTOR NOTES
--------------
"""

            for item in brief.investor_notes:
                content += f"- {item}\n"

            (folder / filename).write_text(content)

        return output_directory
