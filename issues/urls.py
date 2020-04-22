from django.urls import path

from . import views
from .views import AreaListView, area_create, AreaUpdateView, AreaDeleteView
from .views import ProgramListView, program_create, ProgramUpdateView, ProgramDeleteView
from .views import IssueListView, IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView
from .views import login_view, logout_view, index, register_view, database_view, export

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register_view, name='register_view'),

    # Export
    path('export/', views.export, name='export'),
    
    # Issue
    path('issues/', IssueListView.as_view(), name='IssueListView'),
    path('issues/<int:pk>', IssueDetailView.as_view(), name='IssueDetailView'),
    path('issues/create', IssueCreateView.as_view(), name='IssueCreateView'),
    path('issues/update/<int:pk>',
         IssueUpdateView.as_view(), name='IssueUpdateView'),
    path('issues/delete/<int:pk>',
         IssueDeleteView.as_view(), name='IssueDeleteView'),

    # Area
    # path('areas/', views.searchAreas, name='searchAreas'),
    path('areas/create', area_create, name='area_create'),
    path('areas/update/<int:pk>/', AreaUpdateView.as_view(), name='AreaUpdateView'),
    path('areas/delete/<int:pk>/', AreaDeleteView.as_view(), name='AreaDeleteView'),
    path('areas/', AreaListView.as_view(), name='AreaListView'),

    # Program
    # path('programs/', views.searchPrograms, name='programs'),
    # path('programs/<int:programID>', views.editPrograms, name='editPrograms'),
    path('programs/create', program_create, name='program_create'),
    path('programs/update/<int:pk>/',
         ProgramUpdateView.as_view(), name='ProgramUpdateView'),
    path('programs/delete/<int:pk>/',
         ProgramDeleteView.as_view(), name='ProgramDeleteView'),
    path('programs/', ProgramListView.as_view(), name='ProgramListView'),

     # Database
     path('database/', database_view, name='database_view'),
     
     # Export 
     path('export/', export, name="export"),
#     # Employee
# #     path('employees/', views.searchEmployees, name='employees'),
#     path('employees/<int:employeeID>/', views.editEmployee, name='editEmployee')
]
