from dataclasses import dataclass
from typing import Protocol


class InvestorBriefProtocol(Protocol):
    """
    Interface required by the report builder.
    """

    total_analyzed: int
    buy_candidates: list[object]
    watch_candidates: list[object]
    rejected_candidates: list[object]


@dataclass
class InvestorReport:
    """
    Human-readable investment summary.
    """

    title: str
    summary_lines: list[str]

    def render(self) -> str:
        return "\n".join(self.summary_lines)


class InvestorReportBuilder:
    """
    Converts an InvestorBrief into a readable report.
    """

    def build(
        self,
        brief: InvestorBriefProtocol,
    ) -> InvestorReport:

        lines: list[str] = []

        lines.append("Meridian Forge Weekly Opportunity Brief")
        lines.append("=" * 40)

        lines.append(f"Opportunities Analyzed: " f"{brief.total_analyzed}")

        lines.append("")
        lines.append("BUY")
        lines.append("---")

        for item in brief.buy_candidates:
            lines.append(str(item))

        lines.append("")
        lines.append("WATCH")
        lines.append("---")

        for item in brief.watch_candidates:
            lines.append(str(item))

        lines.append("")
        lines.append("PASS")
        lines.append("---")

        lines.append(f"{len(brief.rejected_candidates)} opportunities")

        return InvestorReport(
            title="Meridian Forge Weekly Brief",
            summary_lines=lines,
        )
