from meridianforge.workspace.brief import (
    InvestorBriefGenerator,
)


class Result:

    def __init__(self, decision):
        self.decision = decision


def test_investor_brief_generation():

    generator = InvestorBriefGenerator()

    results = [
        Result("BUY"),
        Result("WATCH"),
        Result("PASS"),
    ]

    brief = generator.generate(results)

    assert brief.total_analyzed == 3
    assert len(brief.buy_candidates) == 1
    assert len(brief.watch_candidates) == 1
    assert len(brief.rejected_candidates) == 1
