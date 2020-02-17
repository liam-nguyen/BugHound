from django.db import models
from model_utils import Choices
import datetime

# Create your models here.


# Priority
class Priority(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



# Status
class Status(models.Model):
    STATUS = Choices("Open", "Closed or Open", "Closed", "Resolved")
    name = models.CharField(choices=STATUS, default=STATUS.Open, max_length=50, unique=True)

    def __str__(self):
        return self.name

# FunctionalArea
class FunctionalArea(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

# IssueType
class BugType(models.Model):
    STATUS = Choices("Coding Error", "Design Issue", "Suggestion", "Documentation", 
                    "Hardware", "Query")
    name = models.CharField(choices=STATUS,  max_length=50, unique=True)
    def __str__(self):
        return self.name

# Severity
class Severity(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

# Resolution
class Resolution(models.Model):
    STATUS = Choices("Pending", "Fixed", "Irreproducible", "Deferred", "As designed", 
                    "Withdrawn by reporter", "Need more info", "Disagree with suggestion", "Duplicate")
    name = models.CharField(choices=STATUS, default=STATUS.Pending ,max_length=50, unique=True)
    def __str__(self):
        return self.name

# AttachmentType
class AttachmentType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

# Attachment
class Attachment(models.Model):
    typeID = models.ForeignKey(AttachmentType, on_delete=models.CASCADE)
    location = models.CharField(max_length=500)
    def __str__(self):
        return self.typeID + self.location

# Version
class Version(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

# Program
class Program(models.Model):
    versionID = models.ForeignKey(Version, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.versionID + self.name

# # ProgramIssue
# class ProgramIssue(models.Model):
#     programID = models.ForeignKey(Program, on_delete=models.CASCADE)
#     issueID = models.ForeignKey(IssueType, on_delete=models.CASCADE)
    

# Department
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Employee
class Employee(models.Model):
    name = models.CharField(max_length=100, unique=True)
    departmentID = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Group
class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

# GroupEmployee
class GroupEmployee(models.Model):
    groupID = models.ForeignKey(Group, on_delete=models.CASCADE)
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.groupID + ' ' +self.employeeID

# Issue
class Issue(models.Model):
    programID = models.ForeignKey(Program, on_delete=models.CASCADE)
    bugtypeID = models.ForeignKey(BugType, on_delete=models.CASCADE)
    severityID = models.ForeignKey(Severity, on_delete=models.CASCADE)
    reportedByID = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_reportedByID')
    functionalAreaID = models.ForeignKey(FunctionalArea, on_delete=models.CASCADE)
    assignedToID = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_assignedToID')
    statusID = models.ForeignKey(Status, on_delete=models.CASCADE)
    priorityID = models.ForeignKey(Priority, on_delete=models.CASCADE)
    resolutionID = models.ForeignKey(Resolution, on_delete=models.CASCADE)
    testedByID = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_testedByID')
    attachmentID = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    
    summary = models.CharField(max_length=500)
    suggestedFix = models.CharField(max_length=500)
    issueDate = models.DateTimeField()
    isAssignedToGroup = models.BooleanField()
    comments = models.CharField(max_length=500)
    resolveByDate = models.DateTimeField()
    testByDate = models.DateTimeField()
    treatedAsDeferred = models.BooleanField()
    reproducible = models.BooleanField()

    def __str__(self):
        return f"[programID: {self.programID}, summary: {self.summary}]"


