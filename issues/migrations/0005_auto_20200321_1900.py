# Generated by Django 3.0.3 on 2020-03-21 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0004_auto_20200321_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignedTo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_assignedToID', to='issues.Employee'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='attachment',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='comments',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='isAssignedToGroup',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='reproducible',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='resolveByDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='suggestedFix',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='summary',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='testByDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='testedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_testedByID', to='issues.Employee'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='treatedAsDeferred',
            field=models.BooleanField(default=False),
        ),
    ]
