# This script will remove database and load dummy data

#!/bin/bash

rm -rf db.sqlite3

PYTHON_REF=$(which python | grep "/python")
$PYTHON_REF manage.py migrate

./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'root@example.com', 'root')"

$PYTHON_REF manage.py loaddata issues/fixtures/*.yaml

