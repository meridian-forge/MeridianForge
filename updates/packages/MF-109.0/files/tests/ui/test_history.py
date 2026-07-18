from meridianforge.ui.history import (
    AnalysisHistory,
    HistoryStore,
)


def test_history():

    store = HistoryStore()

    store.add(
        AnalysisHistory(
            "123 Main",
            "BUY",
            90,
        )
    )

    assert len(store.all()) == 1
