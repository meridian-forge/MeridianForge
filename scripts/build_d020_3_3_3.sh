#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D020.3.3.3"
echo "Knowledge Layer Foundation"
echo "======================================"

PACKAGE="updates/packages/D020.3.3.3"

echo
echo "Creating package structure..."

mkdir -p "$PACKAGE/files/src/meridianforge/knowledge"
mkdir -p "$PACKAGE/files/src/meridianforge/models/results"
mkdir -p "$PACKAGE/files/src/meridianforge/services"
mkdir -p "$PACKAGE/files/tests"


echo
echo "Creating knowledge modules..."

cat > "$PACKAGE/files/src/meridianforge/knowledge/__init__.py" <<'PY'
"""
Meridian Forge Knowledge Layer.

Stores reusable intelligence gathered
from previous imports.
"""
PY


cat > "$PACKAGE/files/src/meridianforge/knowledge/provider_profile.py" <<'PY'
"""
Provider profile model.

Represents known data sources.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class ProviderProfile:
    """
    Represents a known external provider.
    """

    name: str

    category: str = "UNKNOWN"

    mappings: dict[str, str] = field(
        default_factory=dict,
    )

    confidence: float = 0.0
PY


cat > "$PACKAGE/files/src/meridianforge/knowledge/source_memory.py" <<'PY'
"""
Source memory.

Stores recognized providers.
"""

from meridianforge.knowledge.provider_profile import (
    ProviderProfile,
)


class SourceMemory:
    """
    Learns and retrieves known sources.
    """

    def __init__(self) -> None:
        self._providers: dict[str, ProviderProfile] = {}

    def remember(
        self,
        profile: ProviderProfile,
    ) -> None:
        """
        Store provider knowledge.
        """

        self._providers[
            profile.name.lower()
        ] = profile

    def find(
        self,
        name: str,
    ) -> ProviderProfile | None:
        """
        Retrieve provider knowledge.
        """

        return self._providers.get(
            name.lower()
        )

    def count(self) -> int:
        """
        Return known provider count.
        """

        return len(self._providers)
PY


cat > "$PACKAGE/files/src/meridianforge/knowledge/mapping_learning.py" <<'PY'
"""
Mapping learning engine.

Learns field relationships.
"""


class MappingLearning:
    """
    Learns source to canonical mappings.
    """

    def __init__(self) -> None:
        self._mappings: dict[str, str] = {}

    def learn(
        self,
        source_field: str,
        target_field: str,
    ) -> None:
        """
        Store a mapping.
        """

        self._mappings[
            source_field.lower()
        ] = target_field

    def lookup(
        self,
        source_field: str,
    ) -> str | None:
        """
        Retrieve learned mapping.
        """

        return self._mappings.get(
            source_field.lower()
        )

    def count(self) -> int:
        """
        Return mapping count.
        """

        return len(self._mappings)
PY


echo
echo "Creating import decision model..."

cat > "$PACKAGE/files/src/meridianforge/models/results/import_decision.py" <<'PY'
"""
Import decision result model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ImportDecision:
    """
    Represents import intelligence outcome.
    """

    source: str

    asset_type: str

    confidence: float

    mappings_used: int

    warnings: int = 0
PY


echo
echo "Creating learning service..."

cat > "$PACKAGE/files/src/meridianforge/services/import_learning_service.py" <<'PY'
"""
Import learning service.

Coordinates knowledge capture.
"""

from meridianforge.knowledge.mapping_learning import (
    MappingLearning,
)
from meridianforge.knowledge.source_memory import (
    SourceMemory,
)
from meridianforge.models.results.import_decision import (
    ImportDecision,
)


class ImportLearningService:
    """
    Provides import learning operations.
    """

    def __init__(self) -> None:

        self.sources = SourceMemory()

        self.mappings = MappingLearning()

    def record_mapping(
        self,
        source_field: str,
        target_field: str,
    ) -> None:
        """
        Learn a mapping.
        """

        self.mappings.learn(
            source_field,
            target_field,
        )

    def create_decision(
        self,
        source: str,
        asset_type: str,
        confidence: float,
        mappings_used: int,
        warnings: int = 0,
    ) -> ImportDecision:
        """
        Create import decision.
        """

        return ImportDecision(
            source=source,
            asset_type=asset_type,
            confidence=confidence,
            mappings_used=mappings_used,
            warnings=warnings,
        )
PY


echo
echo "Creating tests..."

cat > "$PACKAGE/files/tests/test_knowledge_layer.py" <<'PY'
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
PY


echo
echo "Creating manifest..."

cat > "$PACKAGE/manifest.txt" <<EOF
Meridian Forge Update Package

Name:
D020.3.3.3

Purpose:
Knowledge Layer Foundation

Created:
$(date)

EOF


cat > "$PACKAGE/apply.sh" <<'EOF'
#!/bin/bash

echo "D020.3.3.3 deployment handled by update engine"
EOF


chmod +x "$PACKAGE/apply.sh"


echo
echo "Package created:"
echo "$PACKAGE"

