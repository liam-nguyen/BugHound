# This script will remove database and load all dummy data
### BE AWARE: this will remove all users

#!/bin/bash
echo  BE AWARE: this will remove entire database and reload load all dummy data.
read -p "Are you sure? (Y/y) " -n 1 -r

if [[ $REPLY =~ ^[Yy]$ ]]
then
    rm -rf db.sqlite3

    PYTHON_REF=$(which python | grep "/python")
    $PYTHON_REF manage.py migrate

    $PYTHON_REF manage.py shell < create_superuser.py

    $PYTHON_REF manage.py loaddata issues/fixtures/*.yaml
fi


printf "Complete...\n\nDon\'t forget to create a superuser: python manage.py createsuperuser.\n\n"
