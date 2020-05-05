from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import loader
from django.core.files import File
from django.forms.models import model_to_dict
from django.shortcuts import redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .resources import FunctionalAreaResource, EmployeeResource, ProgramResource, IssueResource
from .models import Issue, FunctionalArea, Program, Employee, Department, Status
from .forms import ProgramForm, EmployeeForm, LoginForm, AreaForm, IssueForm, IssueSearchForm
from .helpers.decorators import at_least_level_1_employee_required, at_least_level_2_employee_required, at_least_level_3_employee_required, AtLeastLevel1RequiredMixin, AtLeastLevel2RequiredMixin, AtLeastLevel3RequiredMixin
from .helpers.utils import getAllFields, XMLExport

## Home view ##
def index(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('IssueListView'))
    else:
        return redirect(reverse_lazy('login_view'))

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect(reverse_lazy('IssueListView'))
            messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    
    current_user = request.user.username
    try:
        current_user = User.objects.get(username=request.user)
    except User.DoesNotExist as e:
        current_user = request.user.username
    context = {
        'form': form, 
        'user': current_user
    }
    return render(request, 'issues/pages/login.html', context)

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('login_view'))
    # return render(request, 'issues/pages/logout.html')

@at_least_level_3_employee_required
def register_view(request):
    form = EmployeeForm()
    context = {'form': form}

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                newUser = User.objects.create_user(username=data['username'],
                                                   password=data['password'])
                if data['level'] == 3:
                    newUser.is_staff = True
                newUser.save()
                employee = form.save(commit=False)
                employee.user = newUser
                employee.save()
                messages.success(
                    request, "Registered, please log in.")
                return redirect(reverse_lazy('login_view'))
            except Exception as e:
                messages.error(request, e)
                return render(request, 'issues/pages/register.html', context)
        return render(request, 'issues/pages/register.html', context)
    return render(request, 'issues/pages/register.html', context)

@at_least_level_1_employee_required
def issue_search_view(request):
    issues = Issue.objects.all()
    form = IssueSearchForm()

    if request.method == 'POST':
        form = IssueSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            query = {}
            if data['program']:
                query['program_id'] = data['program']
            if data['bugType']:
                query['bugtype_id'] = data['bugType']
            if data['severity']:
                query['severity_id'] = data['severity']
            if data['area']:
                query['functionalArea_id'] = data['area']
            if data['assigned_to']:
                query['assignedTo_id'] = data['assigned_to']
            if data['reported_by']:
                query['reportedBy_id'] = data['reported_by']
            if data['status']:
                query['status_id'] = data['status']
            if data['priority']:
                query['priority_id'] = data['priority']
            if data['resolution']:
                query['resolution_id'] = data['resolution']
            issues = Issue.objects.filter(**query)

    processed_issues = list(map(getAllFields, issues))
    context = {
        'issues': issues,
        'form' : form
    }
    return render(request, 'issues/pages/issues/issues_search.html', context)


class IssueListView(AtLeastLevel1RequiredMixin, ListView):
    template_name = 'issues/pages/issues/issues.html'
    model = Issue
    paginate_by = 10
    ordering= ['id']

    def get_queryset(self):
        return super().get_queryset().filter(status__name__contains="Open")

class IssueDetailView(AtLeastLevel1RequiredMixin, DetailView):
    template_name = 'issues/pages/issues/issues_detail.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        fields = [field.name for field in Issue._meta.get_fields()]
        context['fields'] = fields
        return context

class IssueAttachmentView(AtLeastLevel1RequiredMixin, DetailView):
    template_nae = "issues/pages/issues/issues_attachment.html"
    model = Issue
    fields = ['attachment', 'attachment2', 'attachment3', 'attachment4', 'attachment5']

class IssueCreateView(AtLeastLevel1RequiredMixin, CreateView):
    model = Issue
    fields = '__all__'
    form_class = IssueForm
    template_name = 'issues/pages/issues/issues_create.html'
    success_url = reverse_lazy('IssueListView')

class IssueUpdateView(AtLeastLevel2RequiredMixin, UpdateView):
    model = Issue
    template_name = 'issues/pages/issues/issues_update.html'
    success_url = reverse_lazy('IssueListView')
    fields = '__all__'
    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if (form.is_valid()):
    #         cleaned_data = form.cleaned_data
    #         print(cleaned_data['status'] == Status.objects.filter(name__contains="Open"))
    #         print(dir(cleaned_data))
    #         print(cleaned_data)

    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

class IssueDeleteView(AtLeastLevel2RequiredMixin, DeleteView):
    model = Issue
    template_name = 'issues/pages/issues/issues_delete.html'
    success_url = reverse_lazy('IssueListView')


########## Areas #############
@at_least_level_3_employee_required
def area_create(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AreaListView')
    else:
        form = AreaForm()
    context = {'form': form}
    return render(request, 'issues/pages/areas/areas_create.html', context)

class AreaListView(AtLeastLevel2RequiredMixin, ListView):
    template_name = 'issues/pages/areas/areas.html'
    model = FunctionalArea
    context_object_name = 'areas'
    ordering = ['name']
    paginate_by = 10


class AreaUpdateView(AtLeastLevel2RequiredMixin, UpdateView):
    template_name = 'issues/pages/areas/areas_update.html'
    model = FunctionalArea
    fields = ['name']
    success_url = reverse_lazy('AreaListView')


class AreaDeleteView(AtLeastLevel3RequiredMixin, DeleteView):
    template_name = 'issues/pages/areas/areas_delete.html'
    model = FunctionalArea
    success_url = reverse_lazy('AreaListView')

########## Programs #############
@at_least_level_3_employee_required
def program_create(request):
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ProgramListView')
    else:
        form = ProgramForm()
    context = {'form': form}
    return render(request, 'issues/pages/programs/programs_create.html', context)


class ProgramListView(AtLeastLevel2RequiredMixin, ListView):
    template_name = 'issues/pages/programs/programs.html'
    model = Program
    context_object_name = 'programs'
    ordering = ['name']
    paginate_by = 10
    login_url = reverse_lazy('login_view')


class ProgramUpdateView(AtLeastLevel2RequiredMixin, UpdateView):
    template_name = 'issues/pages/programs/programs_update.html'
    model = Program
    form_class = ProgramForm
    success_url = reverse_lazy('ProgramListView')

class ProgramDeleteView(AtLeastLevel3RequiredMixin, DeleteView):
    template_name = 'issues/pages/programs/programs_delete.html'
    model = Program
    success_url = reverse_lazy('ProgramListView')


### Employees ###
@at_least_level_3_employee_required
def employee_view(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            newUser = User.objects.create_user(username=data['username'],
                            password=data['password'])
            if data['level'] > 2:
                newUser.is_superuser = True
            newUser.is_staff = True
            employee = Employee(name=data['name'],
                                username=data['username'],
                                level=data['level'],
                                password=data['password'],
                                departmentID=data['departmentID'])
            employee.save()
            newUser.save()
    else:
        form = EmployeeForm()
    context = {
        'employees' : employees,
        'form' : form
        }
    return render(request, 'issues/pages/employees/employees.html', context)

class EmployeeUpdateView(AtLeastLevel3RequiredMixin, UpdateView):
    model = Employee
    template_name = 'issues/pages/employees/employees_update.html'
    success_url = reverse_lazy('employee_view')
    fields = '__all__'

########## Export #############
@at_least_level_1_employee_required
def export(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        resource_name = request.POST['resource-name']
        if (file_format != 'XML'):
            resource_mapping = {
                'Issue': IssueResource,
                'Area': FunctionalAreaResource,
                'Program': ProgramResource,
                'Employee': EmployeeResource
            }
            file_format_mapping = {
                'CSV': 'get_csv',
                'JSON': 'get_json',
                'YAML': 'get_yaml',
                'HTML': 'get_html'}
            resource = resource_mapping[resource_name]()
            dataset = resource.export()
            data = getattr(dataset, file_format_mapping[file_format])()
        else:
            data = XMLExport(resource_name)

        response = HttpResponse(
            data, content_type='application/x-download')
        file_name = resource_name.lower() + "." + file_format.lower()
        response['Content-Disposition'] = f"attachment; filename={file_name}"
        return response
    
    return render(request, 'issues/pages/export.html')

