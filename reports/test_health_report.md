# MeridianForge Test Health Report

## Summary


Production modules:
391

Test modules:
281

Test functions:
320


## Test Distribution

- intake: 11
- analysis: 2
- ranking: 5
- scoring: 1
- reporting: 20
- services: 11
- workflows: 6
- e2e: 4
- cli: 8


## Duplicate Production Files

- __init__.py
- models.py
- normalizer.py
- dashboard.py
- investor_package.py
- acquisition_report.py
- ranking_engine.py
- engine.py
- pipeline.py
- metrics.py
- underwriting_engine.py
- analyzer.py
- result.py
- file_reader.py
- investor_profile.py
- actions.py
- decision.py
- opportunity.py
- property_adapter.py
- ranking.py
- risk.py
- report.py
- queue.py
- recommendation.py
- expenses.py
- scenario.py
- acquisition.py
- assumptions.py
- workflow.py
- alerts.py
- command_center.py
- action.py
- mortgage.py
- recommendation_engine.py
- import_pipeline.py
- investor_package_builder.py


## Duplicate Test Files

- test_version.py
- test_normalizer.py
- test_mortgage.py
- test_metrics.py
- __init__.py
- test_risk.py
- test_recommendation_engine.py
- test_import_pipeline.py
- test_acquisition_report.py
- test_investor_profile.py
- test_cli.py
- test_engine.py
- test_pipeline.py
- test_ranking_engine.py
- test_decision.py
- test_recommendation.py
- test_dashboard.py
- test_property_adapter.py
- test_ranking.py
- test_opportunity.py
- test_workflow.py
- test_alerts.py
- test_action.py


## Core Architecture Targets


### InvestmentPipeline

Referenced in:


- src/meridianforge/models/results/investment_pipeline_result.py
- src/meridianforge/models/results/investment_workflow_result.py
- src/meridianforge/decision/intelligence/decision_context_builder.py
- src/meridianforge/services/investment_pipeline.py
- src/meridianforge/services/acquisition_orchestrator.py
- src/meridianforge/services/investment_workflow.py
- src/meridianforge/services/acquisition_intelligence.py

### AcquisitionOrchestrator

Referenced in:


- src/meridianforge/services/acquisition_orchestrator.py
- src/meridianforge/services/acquisition_execution_service.py

### RealEstateAdapter

Referenced in:


- src/meridianforge/normalization/real_estate_adapter.py
- src/meridianforge/services/investment_pipeline.py

### UnderwritingEngine

Referenced in:


- src/meridianforge/reporting/builder.py
- src/meridianforge/analysis/underwriting_engine.py
- src/meridianforge/analysis/__init__.py
- src/meridianforge/acquisition/pipeline.py
- src/meridianforge/decision/pipeline.py
- src/meridianforge/application/workflow.py
- src/meridianforge/engine/underwriting_engine.py
- src/meridianforge/engine/__init__.py
- src/meridianforge/engine/investment_assessment.py
- src/meridianforge/engine/stress_test.py
- src/meridianforge/services/investment_pipeline.py
- src/meridianforge/services/batch_analyzer.py

### DealRankingEngine

Referenced in:


- src/meridianforge/engine/deal_ranking.py
- src/meridianforge/services/investment_pipeline.py
- src/meridianforge/services/batch_analyzer.py

### DealScoringEngine

Referenced in:


- src/meridianforge/engine/investment_assessment.py
- src/meridianforge/engine/deal_scoring.py
- src/meridianforge/services/investment_pipeline.py
- src/meridianforge/services/batch_analyzer.py