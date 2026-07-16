#!/bin/bash

set -e

PACKAGE_NAME="$1"

if [ -z "$PACKAGE_NAME" ]; then
    echo "Usage:"
    echo "./scripts/create_update_package.sh <package_name>"
    exit 1
fi

mkdir -p "updates/packages/$PACKAGE_NAME/files"

cat > "updates/packages/$PACKAGE_NAME/manifest.txt" <<MANIFEST
Meridian Forge Update Package

Name:
$PACKAGE_NAME

Created:
$(date)

Files:
MANIFEST

cat > "updates/packages/$PACKAGE_NAME/apply.sh" <<'APPLY'
#!/bin/bash

echo "Applying Meridian Forge update..."
echo "Package execution placeholder."
APPLY

chmod +x "updates/packages/$PACKAGE_NAME/apply.sh"

echo
echo "Created update package:"
echo "updates/packages/$PACKAGE_NAME"
