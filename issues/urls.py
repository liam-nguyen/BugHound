from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path("dbmaintenance/", views.dbMaintenance, name='dbmaintenance'),

    # Issue
    path('issues/', views.searchIssue, name='issues'),
    path('addIssue', views.addIssue, name='addIssue'),
    path("<int:issueID>/", views.issue, name='issue'),

    # Area
    path('areas/', views.searchAreas, name='searchAreas'),
    path('areas/<int:areaID>/', views.editAreas, name='editAreas'),

    # Program
    path('programs/', views.searchPrograms, name='programs'),

    # Employee
    path('employees/', views.searchEmployees, name='employees'),
    path('employees/<int:employeeID>/', views.editEmployee, name='editEmployee')
]