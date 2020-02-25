from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Issue
from django.core import serializers

def index(request):
    return HttpResponse("Welcome to BugHound!")

def issue(request, issueID):
    try:
        issue = Issue.objects.get(pk=issueID)
        # issueObj = {
        #     'ProgramID': str(issue.programID),
        #     'BugTypeID': str(issue.bugtypeID),
        #     'SeverityID': str(issue.severityID),
        #     'ReportedByID': str(issue.reportedByID)

        # }
        data = serializers.serialize("json", [issue])
        print(data)
    except Issue.DoesNotExist:
        raise Http404("Issue does not exist")
    return JsonResponse(data, safe=False)
