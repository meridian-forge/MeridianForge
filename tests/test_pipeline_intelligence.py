from meridianforge.knowledge.mapping_learning import (
    MappingLearning,
)
from meridianforge.services.mapping_reuse_service import (
    MappingReuseService,
)


def test_mapping_reuse_service() -> None:

    learning = MappingLearning()

    learning.learn(
        "Property Price",
        "purchase_price",
    )

    service = MappingReuseService(
        learning,
    )

    result = service.reuse(
        ["Property Price"],
    )

    assert result["Property Price"] == "purchase_price"
