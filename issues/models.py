from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils import timezone
from model_utils import Choices
import datetime
import os

class Priority(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(
        max_length=200, 
        unique=True, 
        null=False, 
        blank=False)

    def __str__(self):
        return self.name

class BugType(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        null=False,
        blank=False)
        
    def __str__(self):
        return f'{self.id} - {self.name}'

class Severity(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        null=False,
        blank=False)

    def __str__(self):
        return str(self.name)

class Resolution(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        null=False,
        blank=False)
    
    def __str__(self):
        return self.name

class AttachmentType(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        null=False,
        blank=False)

    def __str__(self):
        return self.name

class Attachment(models.Model):
    typeID = models.ForeignKey(AttachmentType, on_delete=models.CASCADE)
    location = models.CharField(max_length=500)
    
    def __str__(self):
        return f"[Type: {self.typeID} + Location: {self.location}]"

class FunctionalArea(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        null=False,
        blank=False)

    def __str__(self):
        return self.name

class Program(models.Model):
    version = models.IntegerField(validators=[MinValueValidator(1)])
    release = models.IntegerField(validators=[MinValueValidator(1)])
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False)
    areas = models.ManyToManyField(FunctionalArea)

    def __str__(self):
        return f"{self.name} V:{self.version} R:{self.release}"

    class Meta:
        unique_together = [['name', 'release', 'version']]
    
class Department(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        null=False,
        blank=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    levelChoices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    level = models.IntegerField(choices=levelChoices, default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Group
class Group(models.Model):
    members = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name

class Issue(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    bugtype = models.ForeignKey(BugType, on_delete=models.CASCADE)
    severity = models.ForeignKey(Severity, on_delete=models.CASCADE)
    reportedBy = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_reportedByID')
    functionalArea = models.ForeignKey(FunctionalArea, on_delete=models.CASCADE)
    assignedTo = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, related_name='employee_assignedToID',
        null=True,
        blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default="OPEN")
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE)
    testedBy = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, related_name='employee_testedByID',
        null=True,
        blank=True)
    attachment = models.FileField(
        upload_to = 'issue_images/',
        null=True, 
        blank=True)
    summary = models.CharField(
        max_length=500, 
        null=True, 
        blank=True)
    suggestedFix = models.CharField(
        max_length=500, 
        null=True, 
        blank=True)
    issueDate = models.DateTimeField(default=timezone.now)
    isAssignedToGroup = models.BooleanField(null=True)
    comments = models.CharField(
        max_length=500, 
        null=True, 
        blank=True)
    resolveByDate = models.DateTimeField(null=True, blank=True)
    testByDate = models.DateTimeField(null=True, blank=True)
    treatedAsDeferred = models.BooleanField(default=False)
    reproducible = models.BooleanField(null=True)

    def __str__(self):
        return f"[BugID: {self.id}]"

    @property
    def filename(self):
        return os.path.basename(self.attachment.name)


