#!/bin/bash
set -eo pipefail

sed -i -r "s;r'\^', include\('apps.urls'\);r'^${APP_PREFIX}', include('apps.urls');g" /app/versioning_service/urls.py

if [ ! $DATABASE_PATH ]; then
	DATABASE_PATH="{0}/dev.sqlite"
fi

sed -i -r "s;\{0\}/dev.sqlite;${DATABASE_PATH};g" /app/versioning_service/settings.py

python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'test@localhost.com', 'root123')" | python manage.py shell

exec "$@"
