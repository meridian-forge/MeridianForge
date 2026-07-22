# MeridianForge Test Health Report

## Summary


Production modules:
297

Test modules:
198

Test functions:
230


## Test Distribution

- intake: 11
- analysis: 2
- ranking: 5
- scoring: 1
- reporting: 14
- services: 11
- workflows: 6
- e2e: 4
- cli: 8


## Duplicate Production Files

- __init__.py
- models.py
- normalizer.py
- acquisition_report.py
- engine.py
- pipeline.py
- metrics.py
- underwriting_engine.py
- analyzer.py
- result.py
- file_reader.py
- investor_profile.py
- opportunity.py
- expenses.py
- scenario.py
- acquisition.py
- assumptions.py
- investor_package.py
- workflow.py
- mortgage.py
- import_pipeline.py


## Duplicate Test Files

- test_version.py
- test_normalizer.py
- test_mortgage.py
- test_metrics.py
- __init__.py
- test_import_pipeline.py
- test_acquisition_report.py
- test_investor_profile.py
- test_cli.py
- test_engine.py
- test_pipeline.py
- test_opportunity.py
- test_workflow.py


## Core Architecture Targets


### InvestmentPipeline

Referenced in:


- src/meridianforge/models/results/investment_pipeline_result.py
- src/meridianforge/models/results/investment_workflow_result.py
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