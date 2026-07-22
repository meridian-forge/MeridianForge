#!/bin/bash

echo "====================================="
echo " MeridianForge Test Architecture Check"
echo "====================================="

ROOT="src/meridianforge"
TESTS="tests"

echo ""
echo "1. TEST INVENTORY"
echo "-------------------------------------"

TEST_COUNT=$(find "$TESTS" \
-type f \
-name "test_*.py" \
-not -path "*/__pycache__*" \
| wc -l)

echo "Test files found: $TEST_COUNT"


FUNCTION_COUNT=$(grep -R "def test_" "$TESTS" \
--include="*.py" \
--exclude-dir="__pycache__" \
| wc -l)

echo "Test functions found: $FUNCTION_COUNT"


echo ""
echo "2. DOMAIN DUPLICATE CHECK"
echo "-------------------------------------"

for TERM in Opportunity Property Pipeline Import Report Workflow; do

    COUNT=$(grep -R "$TERM" "$ROOT" "$TESTS" \
    --include="*.py" \
    --exclude-dir="__pycache__" \
    | wc -l)

    echo "$TERM references: $COUNT"

done


echo ""
echo "3. CORE PRODUCTION MODULE CHECK"
echo "-------------------------------------"

echo "Production modules:"
find "$ROOT" \
-type f \
-name "*.py" \
-not -path "*/__pycache__*" \
| wc -l


echo ""
echo "Test modules:"
find "$TESTS" \
-type f \
-name "test_*.py" \
-not -path "*/__pycache__*" \
| wc -l


echo ""
echo "4. HIGH-RISK DUPLICATE FILE NAMES"
echo "-------------------------------------"

find "$ROOT" \
-type f \
-name "*.py" \
-not -path "*/__pycache__*" \
| sed 's#.*/##' \
| sort \
| uniq -d


echo ""
echo "5. KEY ARCHITECTURE TARGETS"
echo "-------------------------------------"

for TARGET in \
"InvestmentPipeline" \
"AcquisitionOrchestrator" \
"RealEstateAdapter" \
"UnderwritingEngine" \
"DealRankingEngine" \
"DealScoringEngine"; do

    echo ""
    echo "$TARGET"

    grep -R "$TARGET" "$ROOT" \
    --include="*.py" \
    --exclude-dir="__pycache__" \
    | head -10

done


echo ""
echo "6. TEST COVERAGE AREAS"
echo "-------------------------------------"

for AREA in \
intake \
analysis \
ranking \
scoring \
reporting \
services \
workflows \
e2e \
cli; do

    if [ -d "$TESTS/$AREA" ]; then
        COUNT=$(find "$TESTS/$AREA" \
        -name "test_*.py" \
        | wc -l)

        echo "$AREA tests: $COUNT"
    else
        echo "$AREA tests: root level"
    fi

done


echo ""
echo "====================================="
echo " Test Architecture Check Complete"
echo "====================================="
