from django.contrib import admin

# Register your models here.\
from .models import Issue, Status, BugType, Resolution, Priority, FunctionalArea, Severity

admin.site.register(Issue)
admin.site.register(Status)
admin.site.register(BugType)
admin.site.register(Resolution)
admin.site.register(Severity)
admin.site.register(Priority)

