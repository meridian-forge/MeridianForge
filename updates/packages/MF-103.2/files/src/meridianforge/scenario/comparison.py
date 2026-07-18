class ScenarioComparison:

    def compare(
        self,
        results: dict[str, float],
    ) -> dict[str, float]:

        return dict(
            sorted(
                results.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
