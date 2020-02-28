from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:issueID>", views.issue, name='issue'),
    path("dbmaintenance", views.dbMaintenance, name='dbmaintenance'),
    path('area-search', views.searchAreas, name='searchAreas')
]