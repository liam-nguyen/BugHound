from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

import datetime
from .models import Program, Department, BugType, Severity, FunctionalArea, Employee, Status, Priority, Resolution
from .models import Issue

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

# Issue Forms
# class IssueSearchForm(forms.Form):
#     program = forms.ModelChoiceField(queryset=Program.objects.all(), required=False)
#     bugType = forms.ModelChoiceField(queryset=BugType.objects.all(), required=False)
#     severity = forms.ModelChoiceField(queryset=Severity.objects.all(), required=False)
#     area = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(), required=False)
#     assigned_to = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
#     reported_by = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False)
#     priority = forms.ModelChoiceField(queryset=Priority.objects.all(), required=False)
#     resolution = forms.ModelChoiceField(queryset=Resolution.objects.all(), required=False)

# class IssueEditForm(forms.Form):
#     class Meta:
#         model = Issue
class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'

# Area Forms
# class AreaForm(forms.Form):
#     program = forms.ModelChoiceField(queryset=Program.objects.all())
#     name = forms.CharField()
class AreaForm(ModelForm):
    class Meta:
        model = FunctionalArea
        fields = ['name']

# Program Forms
class ProgramForm(forms.Form):
    version = forms.IntegerField()
    release = forms.IntegerField()
    name = forms.CharField()

# Employee Forms
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeEditForm(forms.Form):
    levelChoices = (
        (1, '1'),
        (2, '2'),
        (3, '3')
    )
    name = forms.CharField(max_length=100)
    departmentID = forms.ModelChoiceField(queryset=Department.objects.all())
    level = forms.ChoiceField(choices = levelChoices)
