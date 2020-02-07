from django.db import models

# Create your models here.


# Priority
class Priority(models.Model):
    name = models.CharField(max_length=50)

# Status
class Status(models.Model):
    name = models.CharField(max_length=50)

# FunctionalArea
class FunctionalArea(models.Model):
    name = models.CharField(max_length=50)

# IssueType
class IssueType(models.Model):
    name = models.CharField(max_length=50)

# Severity
class Severity(models.Model):
    name = models.CharField(max_length=50)

# Resolution
class Resolution(models.Model):
    name = models.CharField(max_length=50)

# AttachmentType
class AttachmentType(models.Model):
    name = models.CharField(max_length=50)

# Attachment
class Attachment(models.Model):
    typeID = models.ForeignKey(AttachmentType, on_delete=models.CASCADE)
    location = models.CharField(max_length=500)

