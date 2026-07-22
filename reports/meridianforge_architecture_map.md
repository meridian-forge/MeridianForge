# MeridianForge Architecture Map

Generated: 2026-07-22T10:50:19.577104


## Architecture Direction

MeridianForge follows this dependency direction:

Domain Models
        ↓
Engines
        ↓
Services
        ↓
Workflows
        ↓
Presentation / CLI

Lower layers should not depend on higher layers.


## Domain Models

- `models/__init__.py`
- `models/domain/__init__.py`
- `models/domain/acquisition.py`
- `models/domain/address.py`
- `models/domain/assumptions.py`
- `models/domain/attachment_document.py`
- `models/domain/expenses.py`
- `models/domain/financing.py`
- `models/domain/income.py`
- `models/domain/investment_strategy.py`
- `models/domain/investor_profile.py`
- `models/domain/metadata.py`
- `models/domain/normalized_asset.py`
- `models/domain/property.py`
- `models/domain/property_candidate.py`
- `models/domain/scenario.py`
- `models/domain/source_document.py`
- `models/results/__init__.py`
- `models/results/acquisition_assessment.py`
- `models/results/acquisition_orchestration_result.py`
- `models/results/acquisition_result.py`
- `models/results/analysis_result.py`
- `models/results/analysis_workflow_result.py`
- `models/results/batch_analysis_result.py`
- `models/results/batch_import_result.py`
- `models/results/deal_evaluation.py`
- `models/results/field_mapping.py`
- `models/results/import_decision.py`
- `models/results/import_error.py`
- `models/results/import_execution_result.py`
- `models/results/import_mapping_result.py`
- `models/results/import_quality_report.py`
- `models/results/import_result.py`
- `models/results/import_warning.py`
- `models/results/investment_assessment_result.py`
- `models/results/investment_pipeline_result.py`
- `models/results/investment_report.py`
- `models/results/investment_workflow_result.py`
- `models/results/mapping_history.py`
- `models/results/pipeline_result.py`
- `models/results/ranked_deal.py`
- `models/results/ranked_opportunity.py`
- `models/results/recommendation.py`
- `models/results/report.py`
- `models/results/risk_rating.py`
- `models/results/stress_result.py`
- `models/results/suggested_mapping.py`
- `models/results/unknown_field.py`
- `domain/__init__.py`
- `domain/investor_profile.py`
- `domain/opportunity.py`
- `domain/opportunity_status.py`
- `domain/provider.py`
- `domain/source.py`

## Engines

- `engine/__init__.py`
- `engine/criteria_engine.py`
- `engine/deal_ranking.py`
- `engine/deal_scoring.py`
- `engine/investment_assessment.py`
- `engine/metrics.py`
- `engine/mortgage.py`
- `engine/risk.py`
- `engine/stress_test.py`
- `engine/underwriting_engine.py`
- `analysis/__init__.py`
- `analysis/analyzer.py`
- `analysis/metrics.py`
- `analysis/models.py`
- `analysis/result.py`
- `analysis/underwriting_engine.py`
- `scoring/__init__.py`
- `scoring/deal_score_engine.py`
- `ranking/__init__.py`
- `ranking/engine.py`
- `ranking/filters.py`
- `ranking/models.py`
- `ranking/opportunity_ranker.py`
- `ranking/pipeline.py`
- `ranking/ranking_engine.py`

## Services

- `services/__init__.py`
- `services/acquisition_execution_service.py`
- `services/acquisition_file_service.py`
- `services/acquisition_intake_service.py`
- `services/acquisition_intelligence.py`
- `services/acquisition_orchestrator.py`
- `services/acquisition_pipeline.py`
- `services/analysis_workflow.py`
- `services/attachment_intake_service.py`
- `services/batch_analysis.py`
- `services/batch_analyzer.py`
- `services/batch_import_processor.py`
- `services/email_intake_service.py`
- `services/import_confidence_service.py`
- `services/import_execution_service.py`
- `services/import_learning_service.py`
- `services/import_pipeline.py`
- `services/import_quality_service.py`
- `services/investment_pipeline.py`
- `services/investment_thesis_builder.py`
- `services/investment_workflow.py`
- `services/investor_package_builder.py`
- `services/mapping_reuse_service.py`
- `services/monday_analyzer.py`
- `services/monday_artifact_service.py`
- `services/monday_execution.py`
- `services/personalized_thesis_builder.py`
- `services/property_extraction_service.py`
- `services/provider_detection_service.py`
- `services/recommendation_engine.py`
- `services/report_generation_service.py`
- `services/source_intake_service.py`
- `services/web_intake_service.py`

## Workflows

- `workflow/__init__.py`
- `workflow/analysis_pipeline.py`
- `workflow/monday_pipeline.py`
- `workflow/result.py`
- `workflows/__init__.py`
- `workflows/acquisition_context.py`
- `workflows/acquisition_decision_workflow.py`
- `workflows/acquisition_input.py`
- `workflows/acquisition_package_workflow.py`
- `workflows/acquisition_run.py`
- `workflows/investor_package_workflow.py`

## Intake / Import

- `intake/__init__.py`
- `intake/adapter.py`
- `intake/csv_adapter.py`
- `intake/csv_property_adapter.py`
- `intake/detector.py`
- `intake/email_adapter.py`
- `intake/excel_property_adapter.py`
- `intake/extracted_data.py`
- `intake/extractors/base.py`
- `intake/extractors/excel.py`
- `intake/extractors/registry.py`
- `intake/file_adapter.py`
- `intake/file_scanner.py`
- `intake/manual_adapter.py`
- `intake/models.py`
- `intake/pdf_adapter.py`
- `intake/pipeline.py`
- `intake/property_import_service.py`
- `intake/router.py`
- `intake/source_classifier.py`
- `intake/url_adapter.py`
- `intake/workflow.py`
- `intake/xlsx_adapter.py`
- `imports/__init__.py`
- `imports/file_reader.py`
- `imports/property_json.py`
- `importers/__init__.py`
- `importers/excel_template.py`
- `importers/file_reader.py`
- `importers/real_estate_template.py`
- `data/__init__.py`
- `data/import_pipeline.py`
- `data/loader.py`
- `data/normalizer.py`
- `data/validator.py`

## Reporting / Presentation

- `reporting/__init__.py`
- `reporting/acquisition_report.py`
- `reporting/builder.py`
- `reporting/dashboard_models.py`
- `reporting/decision_brief.py`
- `reporting/excel_report.py`
- `reporting/executive_summary.py`
- `reporting/exporter.py`
- `reporting/formatter.py`
- `reporting/investment_thesis_exporter.py`
- `reporting/investor_report.py`
- `reporting/models.py`
- `reporting/monday_dashboard.py`
- `reporting/monday_dashboard_builder.py`
- `reporting/monday_dashboard_formatter.py`
- `reporting/monday_dashboard_json.py`
- `reporting/monday_dashboard_model.py`
- `reporting/monday_dashboard_renderer.py`
- `reporting/package_exporter.py`
- `reporting/portfolio_summary.py`
- `reporting/text_report.py`
- `presentation/__init__.py`
- `presentation/excel_renderer.py`
- `presentation/export_service.py`
- `presentation/investor_report_renderer.py`
- `presentation/markdown_renderer.py`
- `reports/__init__.py`
- `reports/acquisition_report.py`
- `reports/export.py`
- `reports/generator.py`
- `reports/models.py`

## Application / CLI

- `application/__init__.py`
- `application/models.py`
- `application/service.py`
- `application/workflow.py`
- `cli/__init__.py`
- `cli/acquisition.py`
- `cli/analyzer.py`
- `cli/commands.py`
- `cli/investor_package.py`
- `cli/main.py`
- `cli/monday.py`
- `cli/monday_command.py`
- `cli/parser.py`


## Canonical Ownership Decisions

| Capability | Owner |
|---|---|
| Underwriting | engine |
| Deal Ranking | engine |
| Deal Scoring | engine |
| Investment Pipeline | services |
| Acquisition Flow | workflows/services |
| Reporting | reporting |
| File Intake | intake |
