from .models import DecisionType


def recommended_action(decision: DecisionType) -> str:
    actions = {
        DecisionType.BUY: "Proceed to financing and due diligence",
        DecisionType.WATCH: "Monitor opportunity and reassess",
        DecisionType.PASS: "Archive opportunity",
    }

    return actions[decision]
