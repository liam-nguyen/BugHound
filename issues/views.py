from django.shortcuts import render
from django.http import HttpResponse
from .models import Issue

def index(request):
    return HttpResponse("Welcome to BugHound!")

def issue(request, issueID):
    try:
        issue = Issue.objects.get(pk=issueID)
    except Issue.DoesNotExist:
        raise HTTP404("Issue does not exist")
    return issue
