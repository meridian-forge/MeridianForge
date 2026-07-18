from meridianforge.data.import_pipeline import (
    ImportPipeline,
)


def test_import_pipeline():

    result = ImportPipeline().run(
        [
            {
                "address": "123 Main",
                "price": "250000",
                "rent": "2200",
            }
        ]
    )

    assert len(result) == 1
    assert result[0]["purchase_price"] == 250000
