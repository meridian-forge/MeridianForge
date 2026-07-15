"""
CLI integration tests.
"""

from meridianforge.cli.commands import analyze_command


def test_analyze_command() -> None:
    """
    Verify the CLI returns a formatted analysis report.
    """

    output = analyze_command(
        "examples/sample_property.json",
    )

    assert "Meridian Forge Property Analyzer" in output
    assert "Purchase Price" in output
    assert "Monthly Rent" in output
    assert "Cap Rate" in output
    assert "DSCR" in output
    assert "Risk Rating" in output
    assert "Recommendation" in output
