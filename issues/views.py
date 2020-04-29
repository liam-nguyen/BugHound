from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import loader
from django.core.files import File
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .resources import FunctionalAreaResource, EmployeeResource, ProgramResource, IssueResource
from .models import Issue, FunctionalArea, Program, Employee, Department
from .forms import ProgramForm, EmployeeForm, LoginForm
from .forms import AreaForm, IssueForm, IssueSearchForm
# from .serializers import IssueSerializer

from .decorators import at_least_level_1_employee_required, at_least_level_2_employee_required, at_least_level_3_employee_required
from .decorators import AtLeastLevel1RequiredMixin, AtLeastLevel2RequiredMixin, AtLeastLevel3RequiredMixin

from .helpers import getAllFields, XMLExport

# def index(request):
#     form = LoginForm()
#     context = {'form' : form}
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         context['level'] = user.is_superuser
#         context['name'] = user.username
#         if user is not None:
#             login(request, user)
#             return render(request, 'issue_pages/index.html', context)
#     return render(request, 'issue_pages/login.html', context)
#     # return render(request, 'issue_pages/index.html')

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
    return render(request, 'issues/pages/logout.html')

# def logout_view(request):
#     logout(request)
#     return HttpResponse('Logged Out!')

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

# @login_required
# def dbMaintenance(request):
#     return render(request, 'issue_pages/databaseMaintenance.html')


########## Issues #############
# @login_required
# def issue(request, issueID):
#     # template = loader.get_template('templates/issue_pages/index.html')
#     try:
#         issue = Issue.objects.get(pk=issueID)
#         context = {'issue' : issue}
#     except Issue.DoesNotExist:
#         raise Http404("Issue does not exist")
#     return render(request, 'issue_pages/index.html', context)

# @login_required
# def addIssue(request):
#     if request.method == 'POST':
#         form = IssueEditForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             issue = Issue(
#                 programID = data['program'],
#                 bugtypeID = data['bugType'],
#                 severityID = data['severity'],
#                 reportedByID = data['reported_by'],
#                 functionalAreaID = data['area'],
#                 assignedToID = data['assigned_to'],
#                 statusID = data['status'],
#                 priorityID = data['priority'],
#                 resolutionID = data['resolution'],
#                 testedByID = data['tested_by_id'],
#                 attachmentID = data['attachment'],
#                 summary = data['summary'],
#                 suggestedFix = data['suggestedFix'],
#                 issueDate = data['issueDate'],
#                 isAssignedToGroup = data['isAssignedToGroup'],
#                 comments = data['comments'],
#                 resolveByDate = data['resolveByDate'],
#                 testByDate = data['testByDate'],
#                 treatedAsDeferred = data['treatedAsDeferred'],
#                 reproducible = data['reproducible']
#             )
#             issue.save()
#             print(f"Issue saved. ID = {issue.id}")
#         else:
#             issue = None
#     else:
#         form = IssueEditForm()
#         issue = None
#     context = {
#         'issue' : issue,
#         'form' : form
#     }
#     print("AddIssue - Form", form)
#     return render(request, 'issue_pages/addIssue.html', context)

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
    # return render(request, 'issue_pages/issues.html', context)
    return render(request, 'issues/pages/issues/issues_search.html', context)


# def editIssue(request, issueID):
#     issue = Issue.objects.get(pk=issueID)
#     IssueForm = IssueForm(model_to_dict(issue))
#     context = {
#         'form' : form
#     }
#     return render(request, 'issue_pages/issue-edit', context)

class IssueListView(AtLeastLevel1RequiredMixin, ListView):
    template_name = 'issues/pages/issues/issues.html'
    model = Issue
    paginate_by = 5


class IssueDetailView(AtLeastLevel1RequiredMixin, DetailView):
    template_name = 'issues/pages/issues/issues_detail.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        fields = [field.name for field in Issue._meta.get_fields()]
        context['fields'] = fields
        return context

class IssueCreateView(AtLeastLevel1RequiredMixin, CreateView):
    model = Issue
    fields = '__all__'
    template_name = 'issues/pages/issues/issues_create.html'
    success_url = reverse_lazy('IssueListView')

class IssueUpdateView(AtLeastLevel2RequiredMixin, UpdateView):
    model = Issue
    template_name = 'issues/pages/issues/issues_update.html'
    success_url = reverse_lazy('IssueListView')
    fields = '__all__'


class IssueDeleteView(AtLeastLevel2RequiredMixin, DeleteView):
    model = Issue
    template_name = 'issues/pages/issues/issues_delete.html'
    success_url = reverse_lazy('IssueListView')


# def issue_search_view(request):
#     if request.method == 'POST': 
#         pass

#     context = {}
#     return render(request, 'issues/pages/issues/issues_search.html', context)
    


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

class AreaListView(AtLeastLevel1RequiredMixin, ListView):
    template_name = 'issues/pages/areas/areas.html'
    model = FunctionalArea
    context_object_name = 'areas'
    ordering = ['name']
    paginate_by = 5

class AreaUpdateView(AtLeastLevel3RequiredMixin, UpdateView):
    template_name = 'issues/pages/areas/areas_update.html'
    model = FunctionalArea
    fields = ['name']
    success_url = reverse_lazy('AreaListView')

class AreaDeleteView(AtLeastLevel3RequiredMixin, DeleteView):
    template_name = 'issues/pages/areas/areas_delete.html'
    model = FunctionalArea
    success_url = reverse_lazy('AreaListView')

# @login_required
# @staff_member_required
# def searchAreas(request):
#     areas = FunctionalArea.objects.all()
#     if request.method == 'POST':
#         form = AreaForm(request.POST)
#         if form.is_valid():
#             print("valid")
#             print(form.cleaned_data)
#             data = form.cleaned_data
#             area = FunctionalArea(programID = data['program'], name=data['name'])
#             area.save()
#             print("Area saved!")
#     else:
#         form = AreaForm()
#     context = {'areas': areas,
#                 'form' : form}
#     return render(request, 'issues/pages/areas.html', context)

# @login_required
# @staff_member_required
# def editAreas(request, area_id):
#     area = FunctionalArea.objects.get(pk=area_id)
#     if request.method == 'POST':
#         form = AreaForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             area.name = data['name']
#             area.program = data['program']
#             area.save()
#             return redirect("AreaListView")
#     else:
#         form = AreaForm()
#     context = {'form' : form}
#     return render(request, AreaListView.as_view(), context)

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

class ProgramListView(AtLeastLevel1RequiredMixin, ListView):
    template_name = 'issues/pages/programs/programs.html'
    model = Program
    context_object_name = 'programs'
    ordering = ['name']
    paginate_by = 5


class ProgramUpdateView(AtLeastLevel3RequiredMixin, UpdateView):
    template_name = 'issues/pages/programs/programs_update.html'
    model = Program
    fields = '__all__'
    success_url = reverse_lazy('ProgramListView')


class ProgramDeleteView(AtLeastLevel3RequiredMixin, DeleteView):
    template_name = 'issues/pages/programs/programs_delete.html'
    model = Program
    success_url = reverse_lazy('ProgramListView')


# # Programs
# @login_required
# # @staff_member_required
# def searchPrograms(request):
#     programs = Program.objects.all()
#     if request.method == 'POST':
#         form = ProgramForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             program = Program(version = data['version'], release = data['release'],
#                                 name = data['name'])
#             program.save()
#     else:
#         form = ProgramForm()

#     context = {'programs' : programs,
#                 'form': form}
#     # return render(request, 'issue_pages/programs.html', context)
#     return render(request, 'issues/pages/programs/programs.html', context)

# @login_required
# # @staff_member_required
# def editPrograms(request, programID):
#     program = Program.objects.get(pk=programID)
#     if request.method == 'POST':
#         form = ProgramForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             program.name = data['name']
#             program.version = data['version']
#             program.release = data['release']
#             program.save()
#     else:
#         form = ProgramForm(model_to_dict(program))
#     context = {
#         'program' : program,
#         'form' : form
#     }
#     return render(request, 'issue_pages/program-edit.html', context)



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

# @login_required
# @staff_member_required
# def employee_update_view(request, pk):
#     employee = Employee.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             employee.first_name = data['first_name']
#             employee.last_name = data['last_name']
#             department = Department.objects.get(name__exact=data['department'])
#             print(employee)
#             # employee.level = data['level']
#             # user = User.objects.get(
#             #     username=Employee.objects.get(pk=pk).username)
#             # if int(data['level']) > 2:
#             #     user.is_superuser = True
#             # employee.save()
#             # user.save()
#     # print({
#     #         'name' : employee.name,
#     #         'departmentId' : employee.departmentID,
#     #         'level' : employee.level
#     #     })
#     form = EmployeeForm(model_to_dict(employee))
    
#     context = {
#         'employee': employee,
#         'form': form
#     }
#     print(context)          
#     return render(request, 'issues/pages/employees/employees_update.html', context)

########## Programs #############
# @login_required
# def database_view(request):
#     return render(request, 'issues/pages/database.html')

########## Export #############
@at_least_level_1_employee_required
def export(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        resource_name = request.POST['resource-name']
        # xml_mappings = {
        #     'Areas' : FunctionalArea,
        #     'Programs' : Program,
        #     'Employees' : Employee
        # }
        # csv_mappings = {
        #     'Areas' : FunctionalAreaResource,
        #     'Programs' : ProgramResource,
        #     'Employees' : EmployeeResource
        # }

        # if file_format == 'CSV':
        #     dataset = csv_mappings[data]()
        #     dataset = dataset.export()
        #     response = HttpResponse(dataset.csv, content_type='text/csv')
        #     response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
        #     return response
        # # elif file_format == 'JSON':
        #     # response = HttpResponse(dataset.json, content_type='application/json')
        #     # response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
        #     # return response
        # elif file_format == 'XML':
        #     dataset = xml_mappings[data]
        #     data = serializers.serialize('xml', dataset.objects.all())
        #     f = open('output.xml', 'w')
        #     myFile = File(f)
        #     myFile.write(data)
        #     myFile.close()
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

