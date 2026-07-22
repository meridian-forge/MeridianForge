#!/bin/bash

echo "====================================="
echo " MeridianForge Pre-Sprint Check"
echo "====================================="

echo ""
echo "1. Repository Structure"
echo "-------------------------------------"

find src/meridianforge -maxdepth 2 -type d | sort


echo ""
echo "2. Duplicate Domain Candidates"
echo "-------------------------------------"

find src/meridianforge \
\( -iname "*opportunity*" \
-o -iname "*property*" \
-o -iname "*asset*" \
\) | sort


echo ""
echo "3. Existing Services"
echo "-------------------------------------"

find src/meridianforge/services \
-type f | sort


echo ""
echo "4. Existing Models"
echo "-------------------------------------"

find src/meridianforge/models \
-type f | sort


echo ""
echo "5. Test Coverage Areas"
echo "-------------------------------------"

find tests \
-type f | grep -E "acquisition|investment|property|pipeline|workflow" | sort


echo ""
echo "6. Current Git Status"
echo "-------------------------------------"

git status


echo ""
echo "====================================="
echo " Pre-Sprint Check Complete"
echo "====================================="
