# Generated by Django 3.0.3 on 2020-04-22 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0014_auto_20200422_0900'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='program',
            unique_together={('name', 'release', 'version')},
        ),
    ]