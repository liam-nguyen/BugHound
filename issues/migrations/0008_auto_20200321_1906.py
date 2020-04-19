# Generated by Django 3.0.3 on 2020-03-21 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_auto_20200321_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignedTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_assignedToID', to='issues.Employee'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='testedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_testedByID', to='issues.Employee'),
        ),
    ]