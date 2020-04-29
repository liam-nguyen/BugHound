#!/bin/bash

    PYTHON_REF=$(which python | grep "/python")

    # Remove database
    rm -rf db.sqlite3

    # Remove all migrations
    rm -rf issues/migrations/*

    # Recreate __init__.py
    touch issues/migrations/__init__.py

    # Remigrate database
    # Create first migration
    $PYTHON_REF manage.py makemigrations 
    
    # Create migrations for super users and employees
    cat issues/helpers/create_superuser_and_1_employees.py >> issues/migrations/0002_create_superuser_and_employees.py

    $PYTHON_REF manage.py migrate

    $PYTHON_REF manage.py runserver


