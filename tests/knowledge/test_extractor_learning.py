from meridianforge.knowledge.mapping_learning import (
    MappingLearning,
)
from meridianforge.knowledge.provider_profile import (
    ProviderProfile,
)
from meridianforge.knowledge.source_memory import (
    SourceMemory,
)


def test_mapping_learning_remembers_field_relationships():
    learning = MappingLearning()

    learning.learn(
        "Monthly Rent",
        "monthly_rent",
    )

    assert (
        learning.lookup(
            "monthly rent",
        )
        == "monthly_rent"
    )

    assert learning.count() == 1


def test_source_memory_remembers_provider_profile():
    memory = SourceMemory()

    profile = ProviderProfile(
        name="JWB Capital",
        category="TURNKEY_PROVIDER",
        confidence=0.85,
        mappings={
            "rent": "monthly_rent",
        },
    )

    memory.remember(profile)

    result = memory.find(
        "jwb capital",
    )

    assert result is not None
    assert result.category == "TURNKEY_PROVIDER"
    assert result.mappings["rent"] == "monthly_rent"
    assert memory.count() == 1
