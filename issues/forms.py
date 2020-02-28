from django import forms
from .models import Program, Version

class AreaForm(forms.Form):
    program = forms.ModelChoiceField(queryset=Program.objects.all())
    name = forms.CharField()

class ProgramForm(forms.Form):
    version = forms.ModelChoiceField(queryset=Version.objects.all())
    release = forms.IntegerField()
    name = forms.CharField()