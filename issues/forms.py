from django import forms
from .models import Program, Version, Department, BugType, Severity, FunctionalArea, Employee, Status, Priority, Resolution

# Issue Forms
class IssueForm(forms.Form):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), required=False)
    bugType = forms.ModelChoiceField(queryset=BugType.objects.all(), required=False)
    severirty = forms.ModelChoiceField(queryset=Severity.objects.all(), required=False)
    functionalArea = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(), required=False)
    assignedTo = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
    reportedBY = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False)
    priroty = forms.ModelChoiceField(queryset=Priority.objects.all(), required=False)
    resolution = forms.ModelChoiceField(queryset=Resolution.objects.all(), required=False)


# Area Forms
class AreaForm(forms.Form):
    program = forms.ModelChoiceField(queryset=Program.objects.all())
    name = forms.CharField()

# Program Forms
class ProgramForm(forms.Form):
    version = forms.ModelChoiceField(queryset=Version.objects.all())
    release = forms.IntegerField()
    name = forms.CharField()

# Employee Forms
class EmployeeForm(forms.Form):
    levelChoices = (
        (1, '1'),
        (2, '2'),
        (3, '3')
    )
    departmentID = forms.ModelChoiceField(queryset=Department.objects.all())
    name = forms.CharField()
    userName = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    level = forms.ChoiceField(choices=levelChoices)
    widgets = {
        'password': forms.PasswordInput(),
    }

class EmployeeEditForm(forms.Form):
    levelChoices = (
        (1, '1'),
        (2, '2'),
        (3, '3')
    )
    departmentID = forms.ModelChoiceField(queryset=Department.objects.all())
    name = forms.CharField()
    level = forms.ChoiceField(choices=levelChoices)