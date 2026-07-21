"""
Investment thesis exporter.

Writes investor thesis artifacts to disk.
"""

from pathlib import Path

from meridianforge.intelligence.investment_thesis import (
    InvestmentThesis,
)


class InvestmentThesisExporter:
    """
    Export investment thesis into investor-readable format.
    """

    def export(
        self,
        thesis: InvestmentThesis,
        output_directory: Path,
    ) -> Path:
        """
        Write investment thesis markdown artifact.
        """

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = output_directory / "Investment_Thesis.md"

        content = (
            "# Investment Thesis\n\n"
            f"Recommendation: {thesis.recommendation}\n\n"
            f"Confidence: {thesis.confidence:.1%}\n\n"
            "## Rationale\n\n"
            f"{thesis.rationale}\n\n"
            "## Investor Fit\n\n"
            f"{thesis.investor_fit}\n\n"
            "## Strengths\n\n"
        )

        for strength in thesis.strengths:
            content += f"- {strength}\n"

        content += "\n## Risks\n\n"

        for risk in thesis.risks:
            content += f"- {risk}\n"

        file_path.write_text(
            content,
            encoding="utf-8",
        )

        return file_path
