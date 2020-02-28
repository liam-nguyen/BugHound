from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Issue, FunctionalArea
from django.template import loader
from .serializers import IssueSerializer
from django.core import serializers

def index(request):
    return HttpResponse("Welcome to BugHound!")

def dbMaintenance(request):
    return render(request, 'issue_pages/databaseMaintenance.html')

def editAreas(request):
    areas = FunctionalArea.objects.all()
    context = {'areas': areas}
    print(areas)
    return render(request, 'issue_pages/areas.html', context)



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