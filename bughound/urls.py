from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views as bh_views

urlpatterns = [
    path('', bh_views.login, name='bh_index'),
    path('issues/', include('issues.urls')),
    path('admin/', admin.site.urls),
]