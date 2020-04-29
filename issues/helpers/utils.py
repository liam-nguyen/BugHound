from issues.models import Issue, FunctionalArea, Program, Employee, Department
from django.core import serializers

def getAllFields(issue):
    fields = {
        'status': 'name',
        'program': 'name',
    }

    issue_dict = dict()
    for field in fields:
        issue_dict['id'] = issue.id
        issue_dict[field] = getattr(getattr(issue, field), fields[field])
    return issue_dict


def XMLExport(resource_name):
    mapping = {
        'Issue': Issue,
        'Area': FunctionalArea,
        'Program': Program,
        'Employee': Employee
    }

    model = mapping[resource_name]
    return serializers.serialize('xml', model.objects.all())
