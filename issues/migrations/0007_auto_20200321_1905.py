# Generated by Django 3.0.3 on 2020-03-21 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0006_auto_20200321_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='attachment',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='comments',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='resolveByDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='suggestedFix',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='summary',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='testByDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
