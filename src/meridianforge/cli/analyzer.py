"""
CLI analysis orchestration.
"""

from dataclasses import dataclass

from meridianforge.engine.risk import RiskEngine
from meridianforge.engine.stress_test import StressTestEngine
from meridianforge.engine.underwriting_engine import UnderwritingEngine
from meridianforge.imports.property_json import PropertyJsonImporter
from meridianforge.models.domain.property import Property
from meridianforge.models.domain.scenario import Scenario
from meridianforge.models.results.analysis_result import AnalysisResult
from meridianforge.models.results.risk_rating import RiskRating


@dataclass(frozen=True)
class CLIAnalysis:
    """
    Complete CLI analysis result.
    """

    property: Property
    analysis: AnalysisResult
    risk: RiskRating


class CLIAnalyzer:
    """
    Coordinates property analysis for CLI usage.
    """

    @staticmethod
    def analyze_file(
        file_path: str,
    ) -> CLIAnalysis:
        """
        Analyze a property JSON file.
        """

        property_data = PropertyJsonImporter.load(file_path)

        analysis = UnderwritingEngine.analyze(property_data)

        stress_result = StressTestEngine.analyze(
            property_data,
            Scenario(
                name="Default Stress Test",
                expense_change_percent=0.25,
                vacancy_change_percent=0.10,
                interest_rate_change_percent=0.01,
            ),
        )

        risk = RiskEngine.evaluate(stress_result)

        return CLIAnalysis(
            property=property_data,
            analysis=analysis,
            risk=risk,
        )
