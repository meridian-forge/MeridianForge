#!/bin/bash

set -e

PACKAGE_NAME="$1"

if [ -z "$PACKAGE_NAME" ]; then
    echo "Usage:"
    echo "./scripts/create_update_package.sh <package>"
    exit 1
fi


PACKAGE="updates/packages/$PACKAGE_NAME"

mkdir -p "$PACKAGE/files"


cat > "$PACKAGE/manifest.txt" <<MANIFEST
Meridian Forge Update Package

Name:
$PACKAGE_NAME

Created:
$(date)

MANIFEST


cat > "$PACKAGE/apply.sh" <<EOF2
#!/bin/bash

echo "Package: $PACKAGE_NAME"
echo "Deployment handled by apply_update.sh"
EOF2


chmod +x "$PACKAGE/apply.sh"


echo
echo "Created:"
echo "$PACKAGE"

