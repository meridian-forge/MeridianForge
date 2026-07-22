#!/bin/bash

echo "====================================="
echo " MeridianForge Architecture Inventory"
echo "====================================="

echo ""
echo "INPUT / INTAKE"
echo "-------------------------------------"

find src/meridianforge \
-type f \
-not -path "*/__pycache__*" \
| grep -Ei "intake|import|reader|adapter|extract"


echo ""
echo "DOMAIN OBJECTS"
echo "-------------------------------------"

find src/meridianforge \
-type f \
-not -path "*/__pycache__*" \
| grep -Ei "models/domain|domain"


echo ""
echo "PIPELINES / WORKFLOWS"
echo "-------------------------------------"

find src/meridianforge \
-type f \
-not -path "*/__pycache__*" \
| grep -Ei "pipeline|workflow|orchestr"


echo ""
echo "ANALYSIS / UNDERWRITING"
echo "-------------------------------------"

find src/meridianforge \
-type f \
-not -path "*/__pycache__*" \
| grep -Ei "analysis|underwrite|score|rank"


echo ""
echo "REPORTING"
echo "-------------------------------------"

find src/meridianforge \
-type f \
-not -path "*/__pycache__*" \
| grep -Ei "report|render|export"


echo ""
echo "CLI ENTRY POINTS"
echo "-------------------------------------"

find src/meridianforge \
-type f \
-not -path "*/__pycache__*" \
| grep -Ei "cli"


echo ""
echo "====================================="
echo " Inventory Complete"
echo "====================================="
