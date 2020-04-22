from django.contrib.auth.models import User

def level_1_required(function):
    def wrap(request, *args, **kwargs): 
        # user = User.objects.get(pk=)
        pass
