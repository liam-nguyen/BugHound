from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Issue, FunctionalArea, Program, Employee
from django.template import loader
from .serializers import IssueSerializer
from django.core import serializers
from .forms import AreaForm, ProgramForm, EmployeeForm, EmployeeEditForm, IssueSearchForm
from django.forms.models import model_to_dict
from django.shortcuts import redirect



# Issue
def issue(request, issueID):
    # template = loader.get_template('templates/issue_pages/index.html')
    try:
        issue = Issue.objects.get(pk=issueID)
        context = {'issue' : issue}
    except Issue.DoesNotExist:
        raise Http404("Issue does not exist")
    return render(request, 'issue_pages/index.html', context)

def searchIssue(request):    
    if request.method == 'POST':
        form = IssueSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            query = {}
            if data['program']:
                query['programID'] = data['program']
            if data['bugType']:
                query['bugtypeID'] = data['bugType']
            if data['severity']:
                query['severity'] = data['severity']
            if data['area']:
                query['areaID'] = data['area']
            if data['assigned_to']:
                query['assignedToID'] = data['assigned_to']
            if data['reported_by']:
                query['reportedBy'] = data['reported_by']
            if data['status']:
                query['status'] = data['status']
            if data['priority']:
                query['priority'] = data['priority']
            if data['resolution']:
                query['resolution'] = data['resolution']
            issue = Issue.objects.filter(**query)
            print(issue)
    else:
        form = IssueSearchForm()
        issue = Issue.objects.all()
    context = {
        'issues': issue,
        'form' : form
    }
    return render(request, 'issue_pages/issues.html', context)


def index(request):
    return HttpResponse("Welcome to BugHound!")

def dbMaintenance(request):
    return render(request, 'issue_pages/databaseMaintenance.html')

# Areas
def searchAreas(request):
    areas = FunctionalArea.objects.all()
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            print("valid")
            print(form.cleaned_data)
            data = form.cleaned_data
            area = FunctionalArea(programID = data['program'], name=data['name'])
            area.save()
            print("Area saved!")
    else:
        form = AreaForm()
    context = {'areas': areas,
                'form' : form}
    return render(request, 'issue_pages/areas.html', context)

def editAreas(request, areaID):
    area = FunctionalArea.objects.get(pk=areaID)
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            area.name = data['name']
            area.program = data['program']
            area.save()
            return redirect(searchAreas)
    else:
        form = AreaForm({
            'program' : area.programID,
            'name' : area.name
        })
    context = {
        'area' : area,
        'form' : form
    }
    return render(request, 'issue_pages/areas-edit.html', context)



# Programs
def searchPrograms(request):
    programs = Program.objects.all()
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            program = Program(versionID = data['version'], release = data['release'],
                                name = data['name'])
            program.save()
    else:
        form = ProgramForm()

    context = {'programs' : programs,
                'form': form}
    return render(request, 'issue_pages/programs.html', context)


# Employees
def searchEmployees(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            employee = Employee(name=data['name'],
                                userName=data['userName'],
                                level=data['level'],
                                password=data['password'],
                                departmentID=data['departmentID'])
            employee.save()
    else:
        form = EmployeeForm()
    context = {'employees' : employees,
            'form' : form}
    return render(request, 'issue_pages/employees.html', context)

def editEmployee(request, employeeID):
    employee = Employee.objects.get(pk=employeeID)
    if request.method == 'POST':
        form = EmployeeEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            employee.name = data['name']
            employee.departmentID = data['departmentID']
            employee.leve = data['level']
            employee.save()
    else:
        print({
            'name' : employee.name,
            'departmentId' : employee.departmentID,
            'level' : employee.level
        })
        form = EmployeeEditForm(model_to_dict(employee))
    context = {
        'employee': employee,
        'form': form
    }
    return render(request, 'issue_pages/employee-edit.html', context)

# TODO Make admin account for professor
#   show professor admin CRUD

# TODO page that returns all issues and routes to issue to update/ add