# Generated by Django 3.0.3 on 2020-04-29 01:50

from django.db import migrations
from django.contrib.auth.models import User
from issues.models import Employee


def create_superuser(apps, schema_editor):
    user = User.objects.create_superuser(
        username='root', password='root', email='root@gmail.com')

    employee = Employee(user=user, level=3,
                        first_name="root", last_name="root")
    employee.save()
    

people = [
    {
        'username': 'smithbob',
        'password': 'bob',
        'first_name': 'Bob',
        'last_name': '',
        'level': 3
    },
    {
        'username': 'jonessue',
        'password': 'sue',
        'first_name': 'Sue',
        'last_name': '',
        'level': 2
    },
    {
        'username': 'smithhabib',
        'password': 'habib',
        'first_name': 'Habib',
        'last_name': '',
        'level': 2
    },
    {
        'username': 'jonesyoshi',
        'password': 'yoshi',
        'first_name': 'Yoshi',
        'last_name': '',
        'level': 1
    },
    {
        'username': 'smithfrancois',
        'password': 'francois',
        'first_name': 'Francois',
        'last_name': '',
        'last_name': '',
        'level': 2
    },
    {
        'username': 'jonesbecky',
        'password': 'bekcy',
        'first_name': 'Becky',
        'last_name': '',
        'level': 1
    },
    {
        'username': 'smithfelix',
        'password': 'felix',
        'first_name': 'Felix',
        'last_name': '',
        'level': 2
    },
    {
        'username': 'liam',
        'password': 'liam',
        'first_name': 'Liam',
        'last_name': 'Nguyen',
        'level': 3
    },
    {
        'username': 'marco',
        'password': 'marco',
        'first_name': 'Marco',
        'last_name': 'Curci',
        'level': 2
    },
    {
        'username': 'dillion',
        'password': 'dillion',
        'first_name': 'Dillion',
        'last_name': 'Brown',
        'level': 3
    },

]


def create_other_users(apps, schema_editor):
    for person in people:
        user = User.objects.create_user(
            username=person['username'], password=person['password'])
        if person['level'] == 3:
            user.is_staff = True
        employee = Employee(
            user=user, first_name=person['first_name'], 
            last_name=person['last_name'], level=person['level'])
        employee.save()
        

def create_all(apps, schema_editor):
    create_superuser(apps, schema_editor)
    create_other_users(apps, schema_editor)

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [migrations.RunPython(
        create_all)]

