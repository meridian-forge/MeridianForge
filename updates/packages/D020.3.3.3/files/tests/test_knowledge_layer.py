from meridianforge.knowledge.mapping_learning import (
    MappingLearning,
)
from meridianforge.knowledge.source_memory import (
    SourceMemory,
)
from meridianforge.knowledge.provider_profile import (
    ProviderProfile,
)


def test_source_memory() -> None:

    memory = SourceMemory()

    memory.remember(
        ProviderProfile(
            name="JWB",
            category="REAL_ESTATE",
        )
    )

    assert memory.find("jwb") is not None


def test_mapping_learning() -> None:

    learning = MappingLearning()

    learning.learn(
        "Purchase Price",
        "purchase_price",
    )

    assert (
        learning.lookup("purchase price")
        == "purchase_price"
    )
