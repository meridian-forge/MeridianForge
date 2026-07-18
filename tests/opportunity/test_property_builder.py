import pytest

from meridianforge.opportunity.property_builder import (
    build_property,
)


def test_property_builder_placeholder():

    with pytest.raises(NotImplementedError):
        build_property({})
