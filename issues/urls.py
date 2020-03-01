from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:issueID>", views.issue, name='issue'),
    path("dbmaintenance", views.dbMaintenance, name='dbmaintenance'),
    # Area
    path('area-search', views.searchAreas, name='searchAreas'),
    # Program
    path('programs', views.searchPrograms, name='programs'),
    # Employee
    path('employees', views.searchEmployees, name='employees'),
    path('employees/<int:employeeID>', views.editEmplyee, name='editEmployee')
]