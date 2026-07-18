from meridianforge.ui.dashboard_cards import (
    decision_card,
)


def test_decision_card():

    result = decision_card(
        {
            "decision": "BUY",
            "score": 90,
        }
    )

    assert result["rating"] == "GREEN"
