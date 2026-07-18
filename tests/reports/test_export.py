from meridianforge.reports.export import (
    ReportExporter,
)


def test_json_export():

    result = ReportExporter().to_json({"decision": "BUY"})

    assert "BUY" in result
