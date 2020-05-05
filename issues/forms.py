from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, widgets
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from .models import Program, Department, BugType, Severity, FunctionalArea, Employee, Status, Priority, Resolution
from .models import Issue

# from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)

class IssueSearchForm(forms.Form):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), required=False)
    bugType = forms.ModelChoiceField(queryset=BugType.objects.all(), required=False)
    severity = forms.ModelChoiceField(queryset=Severity.objects.all(), required=False)
    area = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(), required=False)
    assigned_to = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
    reported_by = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False)
    priority = forms.ModelChoiceField(queryset=Priority.objects.all(), required=False)
    resolution = forms.ModelChoiceField(queryset=Resolution.objects.all(), required=False)

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'

    # files = MultiFileField(min_num=1, max_num=5, max_file_size=1024*1024*5)

    # # def save(self, commit=True):
    #     instance = super(IssueForm, self).save(commit)
    #     for each in self.cleaned_data['files']:
    #         Attachment.objects.create(file=each, message=instance)

    #     return instance
        
class AreaForm(ModelForm):
    class Meta:
        model = FunctionalArea
        fields = '__all__'

class ProgramForm(ModelForm):
    class Meta: 
        model = Program
        fields = ['name', 'version', 'release', 'areas']
    
    def __init__(self, *args, **kwargs):
       super(ProgramForm, self).__init__(*args, **kwargs)
       print(self)
       self.fields['areas'].widget = widgets.CheckboxSelectMultiple()
       self.fields["areas"].queryset = FunctionalArea.objects.all()

class EmployeeForm(ModelForm):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Employee
        fields = ['level', 'department', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super(EmployeeForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")
