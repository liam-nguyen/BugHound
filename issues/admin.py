from django.contrib import admin

# Register your models here.\
from .models import Issue, Status, BugType, Resolution, Priority
from .models import  FunctionalArea, Severity,AttachmentType, Attachment
from .models import Program, Department, Employee, Group

admin.site.register(Issue)
admin.site.register(Status)
admin.site.register(BugType)
admin.site.register(Resolution)
admin.site.register(Priority)
admin.site.register(FunctionalArea)
admin.site.register(Severity)
admin.site.register(AttachmentType)
admin.site.register(Attachment)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Group)
admin.site.register(Program)

