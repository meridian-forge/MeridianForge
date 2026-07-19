from meridianforge.workspace.runner import AnalysisRunner


class MockPipeline:

    def analyze(self, opportunity):

        return {"address": opportunity.address}


def test_analysis_runner_processes_queue():

    runner = AnalysisRunner(pipeline=MockPipeline())

    opportunities = [
        type(
            "Opportunity",
            (),
            {"address": "123 Main"},
        )()
    ]

    results = runner.run(opportunities)

    assert len(results) == 1
    assert results[0]["address"] == "123 Main"
