from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Issue, FunctionalArea, Program
from django.template import loader
from .serializers import IssueSerializer
from django.core import serializers
from .forms import AreaForm, ProgramForm

def index(request):
    return HttpResponse("Welcome to BugHound!")

def dbMaintenance(request):
    return render(request, 'issue_pages/databaseMaintenance.html')

def searchAreas(request):
    # TODO edit areas
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
    return render(request, 'issue_pages/area-search.html', context)

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

def issue(request, issueID):
    # template = loader.get_template('templates/issue_pages/index.html')
    try:
        issue = Issue.objects.get(pk=issueID)
        context = {'issue' : issue}
    except Issue.DoesNotExist:
        raise Http404("Issue does not exist")
    return render(request, 'issue_pages/index.html', context)


# TODO Make admin account for professor
#   show professor admin CRUD

# TODO page that returns all issues and routes to issue to update/ add