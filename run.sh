#!/bin/bash
set -eo pipefail

sed -i -r "s;r'\^', include\('apps.urls'\);r'^${APP_PREFIX}', include('apps.urls');g" /app/versioning_service/urls.py

exec "$@"
