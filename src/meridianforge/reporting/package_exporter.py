"""
Investor package export service.

Writes investor package artifacts to disk.
"""

import json
from pathlib import Path

from meridianforge.product.investor_package import (
    InvestorPackage,
)
from meridianforge.reporting.executive_summary import (
    ExecutiveSummaryBuilder,
)


class PackageExporter:
    """
    Export investor packages into files.
    """

    def export(
        self,
        package: InvestorPackage,
        output_directory: Path,
    ) -> list[Path]:
        """
        Export package artifacts.
        """

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        files: list[Path] = []

        summary = ExecutiveSummaryBuilder().build(
            package,
        )

        content = "# Decision Brief\n\n" f"{summary}\n"

        if package.personalized_thesis:

            thesis = package.personalized_thesis

            content += (
                "\n## Personalized Investor Thesis\n\n"
                f"Investor Fit: {thesis.investor_fit}\n\n"
                "### Rationale\n\n"
                f"{thesis.rationale}\n\n"
                "### Strengths\n\n"
            )

            for strength in thesis.strengths:
                content += f"- {strength}\n"

            content += "\n### Risks\n\n"

            for risk in thesis.risks:
                content += f"- {risk}\n"

        decision_brief = output_directory / "Decision_Brief.md"

        decision_brief.write_text(
            content,
            encoding="utf-8",
        )

        files.append(
            decision_brief,
        )

        metadata = output_directory / "Archive_Metadata.json"

        metadata.write_text(
            json.dumps(
                {
                    "package_id": package.package_id,
                    "property_name": package.property_name,
                    "artifact_count": len(
                        package.artifacts,
                    ),
                    "has_personalized_thesis": (
                        package.personalized_thesis is not None
                    ),
                },
                indent=2,
            ),
            encoding="utf-8",
        )

        files.append(
            metadata,
        )

        return files
