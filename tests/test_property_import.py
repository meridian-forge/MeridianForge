from meridianforge.imports import PropertyJsonImporter


def test_property_json_import() -> None:
    property_data = PropertyJsonImporter.load("examples/sample_property.json")

    assert property_data.address.city == "Jacksonville"

    assert property_data.acquisition.purchase_price == 200000

    assert property_data.acquisition.closing_costs == 5000

    assert property_data.financing.down_payment == 40000

    assert property_data.financing.loan_term_years == 30

    assert property_data.income.monthly_rent == 2000
