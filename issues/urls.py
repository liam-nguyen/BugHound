from django.urls import path

from . import views
from .views import AreaListView, area_create, AreaUpdateView, AreaDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),

    
    path("dbmaintenance/", views.dbMaintenance, name='dbmaintenance'),


    # Export
    path('export/', views.export, name='export'),
    # Issue
    path('issues/', views.searchIssue, name='issues'),
    path('addIssue/', views.addIssue, name='addIssue'),
    # path("<int:issueID>/", views.issue, name='issue'),
    path('issues/<int:issueID>', views.editIssue, name='editIssue'),

    # Area
    # path('areas/', views.searchAreas, name='searchAreas'),
    path('areas/create', area_create, name='area_create'),
    path('areas/update/<int:pk>/', AreaUpdateView.as_view(), name='AreaUpdateView'),
    path('areas/delete/<int:pk>/', AreaDeleteView.as_view(), name='AreaDeleteView'),
    path('areas/', AreaListView.as_view(), name='AreaListView'),

    # Program
    path('programs/', views.searchPrograms, name='programs'),
    path('programs/<int:programID>', views.editPrograms, name='editPrograms'),

    # Employee
    path('employees/', views.searchEmployees, name='employees'),
    path('employees/<int:employeeID>/', views.editEmployee, name='editEmployee')
]
