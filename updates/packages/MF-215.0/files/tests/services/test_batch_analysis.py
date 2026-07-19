from meridianforge.services.batch_analysis import (
    BatchAnalysisEngine,
)


class FakeRepository:

    def get_all(self):
        return [
            "Property A",
            "Property B",
        ]


class FakePipeline:

    def analyze(
        self,
        opportunity,
    ):
        return f"Analyzed {opportunity}"


def test_batch_analysis_runs_all_opportunities() -> None:

    engine = BatchAnalysisEngine(
        FakeRepository(),
        FakePipeline(),
    )

    results = engine.analyze_all()

    assert results == [
        "Analyzed Property A",
        "Analyzed Property B",
    ]
