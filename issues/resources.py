from import_export import resources
from .models import Employee, FunctionalArea, Program, Issue

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee

class FunctionalAreaResource(resources.ModelResource):
    class Meta:
        model = FunctionalArea

class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program

class IssueResource(resources.ModelResource):
    class Meta:
        model = Issue