from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Issue

def index(request):
    return HttpResponse("Welcome to BugHound!")

def issue(request, issueID):
    try:
        issue = Issue.objects.get(pk=issueID)
        issueObj = {
            'ProgramID': str(issue.programID),
            'BugTypeID': str(issue.bugtypeID)
        }
        print(issueObj)
    except Issue.DoesNotExist:
        raise Http404("Issue does not exist")
    return HttpResponse(issueObj)
