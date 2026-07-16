#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D020.3.3.4"
echo "Pipeline Intelligence Integration"
echo "======================================"

PACKAGE="updates/packages/D020.3.3.4"

mkdir -p "$PACKAGE/files/src/meridianforge/services"
mkdir -p "$PACKAGE/files/tests"


echo "Creating provider detection service..."

cat > "$PACKAGE/files/src/meridianforge/services/provider_detection_service.py" <<'PY'
"""
Provider detection service.

Identifies known external data sources.
"""

from meridianforge.knowledge.provider_profile import (
    ProviderProfile,
)
from meridianforge.knowledge.source_memory import (
    SourceMemory,
)


class ProviderDetectionService:
    """
    Detects provider identity from imported data.
    """

    def __init__(
        self,
        memory: SourceMemory | None = None,
    ) -> None:

        self.memory = memory or SourceMemory()

    def detect(
        self,
        record: dict[str, object],
    ) -> ProviderProfile | None:
        """
        Identify provider from record metadata.
        """

        provider = record.get("provider")

        if provider is None:
            return None

        return self.memory.find(
            str(provider),
        )
PY


echo "Creating mapping reuse service..."

cat > "$PACKAGE/files/src/meridianforge/services/mapping_reuse_service.py" <<'PY'
"""
Mapping reuse service.

Retrieves previously learned field mappings.
"""

from meridianforge.knowledge.mapping_learning import (
    MappingLearning,
)


class MappingReuseService:
    """
    Reuses learned mappings.
    """

    def __init__(
        self,
        learning: MappingLearning | None = None,
    ) -> None:

        self.learning = learning or MappingLearning()

    def reuse(
        self,
        fields: list[str],
    ) -> dict[str, str]:
        """
        Return known mappings.
        """

        results: dict[str, str] = {}

        for field in fields:

            target = self.learning.lookup(
                field,
            )

            if target:
                results[field] = target

        return results
PY


echo "Creating tests..."

cat > "$PACKAGE/files/tests/test_pipeline_intelligence.py" <<'PY'
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

    assert (
        result["Property Price"]
        == "purchase_price"
    )
PY


echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D020.3.3.4

Purpose:
Pipeline Intelligence Integration

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D020.3.3.4 deployment handled by update engine"
EOF


chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

