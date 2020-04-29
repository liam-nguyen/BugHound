from django.contrib.auth.models import User

user = User.objects.create_user(username='john',
                                email='jlennon@beatles.com',
                                password='glass onion')
