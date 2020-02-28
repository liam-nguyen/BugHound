from django import forms
from .models import Program, Version, Department

class AreaForm(forms.Form):
    program = forms.ModelChoiceField(queryset=Program.objects.all())
    name = forms.CharField()

class ProgramForm(forms.Form):
    version = forms.ModelChoiceField(queryset=Version.objects.all())
    release = forms.IntegerField()
    name = forms.CharField()

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