from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
from django.urls import reverse_lazy

from .models import Employee

##### For function-based view #####
LOGIN_URL = 'login_view'

def at_least_level_1_employee_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL):
    actual_decorator = user_passes_test(
        lambda user: user.is_authenticated and user.employee.level >= 1,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def at_least_level_2_employee_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL):
    actual_decorator = user_passes_test(
        lambda user: user.is_authenticated and user.employee.level >= 2,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def at_least_level_3_employee_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL):
    actual_decorator = user_passes_test(
        lambda user: user.is_authenticated and user.employee.level >= 3,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

##### For Class-based View #####
class AtLeastLevel1RequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.employee.level >= 1:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AtLeastLevel2RequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.employee.level >= 2:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AtLeastLevel3RequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.employee.level >= 3:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
