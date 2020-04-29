# Generated by Django 3.0.3 on 2020-04-29 04:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BugType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('level', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='issues.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FunctionalArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Severity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('release', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(max_length=200)),
                ('areas', models.ManyToManyField(to='issues.FunctionalArea')),
            ],
            options={
                'unique_together': {('name', 'release', 'version')},
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='issue_images/')),
                ('summary', models.CharField(blank=True, max_length=500, null=True)),
                ('problem', models.CharField(blank=True, max_length=500, null=True)),
                ('suggestedFix', models.CharField(blank=True, max_length=500, null=True)),
                ('issueDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('isAssignedToGroup', models.BooleanField(null=True)),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('resolveByDate', models.DateTimeField(blank=True, null=True)),
                ('testByDate', models.DateTimeField(blank=True, null=True)),
                ('treatedAsDeferred', models.BooleanField(default=False)),
                ('reproducible', models.BooleanField(null=True)),
                ('assignedTo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_assignedToID', to='issues.Employee')),
                ('bugtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.BugType')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Priority')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Program')),
                ('reportedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_reportedByID', to='issues.Employee')),
                ('resolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Resolution')),
                ('severity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Severity')),
                ('status', models.ForeignKey(default='OPEN', on_delete=django.db.models.deletion.CASCADE, to='issues.Status')),
                ('testedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_testedByID', to='issues.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to='issues.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=500)),
                ('typeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.AttachmentType')),
            ],
        ),
    ]
