from django import forms
from .models import Program

class AreaForm(forms.Form):
    program = forms.ModelChoiceField(queryset=Program.objects.all())
    name = forms.CharField()