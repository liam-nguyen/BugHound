from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("/issues/<int:issueID>", views.issue, name='issue')
]