from meridianforge.reports.models import (
    InvestmentReport,
)


class ReportGenerator:

    def create_summary(
        self,
        report: InvestmentReport,
    ) -> dict[str, object]:

        return {
            "property": report.address,
            "decision": report.decision,
            "score": report.score,
            "metrics": {
                "cap_rate": report.cap_rate,
                "dscr": report.dscr,
                "cash_flow": report.cash_flow,
            },
        }
