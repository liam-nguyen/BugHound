from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Issue, FunctionalArea, Program, Employee
from django.template import loader
from .serializers import IssueSerializer
from django.core import serializers
from .forms import AreaForm, ProgramForm, EmployeeForm, EmployeeEditForm, IssueSearchForm, IssueEditForm, LoginForm
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



def index(request):
    print(request)
    form = LoginForm()
    context = {'form' : form}
    print(context)
    return render(request, 'issue_pages/login.html', context)

def dbMaintenance(request):
    return render(request, 'issue_pages/databaseMaintenance.html')


# Issue
def issue(request, issueID):
    # template = loader.get_template('templates/issue_pages/index.html')
    try:
        issue = Issue.objects.get(pk=issueID)
        context = {'issue' : issue}
    except Issue.DoesNotExist:
        raise Http404("Issue does not exist")
    return render(request, 'issue_pages/index.html', context)

def addIssue(request):
    if request.method == 'POST':
        form = IssueEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            issue = Issue(
                programID = data['program'],
                bugtypeID = data['bugType'],
                severityID = data['severity'],
                reportedByID = data['reported_by'],
                functionalAreaID = data['area'],
                assignedToID = data['assigned_to'],
                statusID = data['status'],
                priorityID = data['priority'],
                resolutionID = data['resolution'],
                testedByID = data['tested_by_id'],
                attachmentID = data['attachment'],
                summary = data['summary'],
                suggestedFix = data['suggestedFix'],
                issueDate = data['issueDate'],
                isAssignedToGroup = data['isAssignedToGroup'],
                comments = data['comments'],
                resolveByDate = data['resolveByDate'],
                testByDate = data['testByDate'],
                treatedAsDeferred = data['treatedAsDeferred'],
                reproducible = data['reproducible']
            )
            issue.save()
            print(f"Issue saved. ID = {issue.id}")
        else:
            issue = None
    else:
        form = IssueEditForm()
        issue = None
    context = {
        'issue' : issue,
        'form' : form
    }
    return render(request, 'issue_pages/addIssue.html', context)

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
                query['severityID'] = data['severity']
            if data['area']:
                query['functionalAreaID'] = data['area']
            if data['assigned_to']:
                query['assignedToID'] = data['assigned_to']
            if data['reported_by']:
                query['reportedByID'] = data['reported_by']
            if data['status']:
                query['statusID'] = data['status']
            if data['priority']:
                query['priorityID'] = data['priority']
            if data['resolution']:
                query['resolutionID'] = data['resolution']
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

def editIssue(request, issueID):
    pass


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

            newUser = User.objects.create_user(username=data['username'],
                            password=data['password'])
            print(newUser)
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
    context = {'employees' : employees,
            'form' : form}
    return render(request, 'issue_pages/employees.html', context)

def editEmployee(request, employeeID):
    employee = Employee.objects.get(pk=employeeID)
    if request.method == 'POST':
        print(1)
        form = EmployeeEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            employee.name = data['name']
            employee.departmentID = data['departmentID']
            employee.level = data['level']

            user = User.objects.get(username=Employee.objects.get(pk=employeeID).username)
            if int(data['level']) > 2:
                user.is_superuser = True
            employee.save()
            redirect(searchEmployees)
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