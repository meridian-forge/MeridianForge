from dataclasses import dataclass


@dataclass
class InvestorBrief:
    """
    Summary of analyzed investment opportunities.
    """

    total_analyzed: int
    buy_candidates: list[object]
    watch_candidates: list[object]
    rejected_candidates: list[object]

    @property
    def action_count(self) -> int:
        return len(self.buy_candidates) + len(self.watch_candidates)


class InvestorBriefGenerator:
    """
    Converts analysis results into
    an investor decision summary.
    """

    def generate(
        self,
        results: list[object],
    ) -> InvestorBrief:

        buy = []
        watch = []
        rejected = []

        for result in results:

            decision = getattr(
                result,
                "decision",
                None,
            )

            if decision == "BUY":
                buy.append(result)

            elif decision == "WATCH":
                watch.append(result)

            else:
                rejected.append(result)

        return InvestorBrief(
            total_analyzed=len(results),
            buy_candidates=buy,
            watch_candidates=watch,
            rejected_candidates=rejected,
        )
