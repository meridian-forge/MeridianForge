from meridianforge.domain.provider import Provider


def test_provider():

    provider = Provider("JWB")

    assert provider.validate()
