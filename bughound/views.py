# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login as auth_login
# from django.http import HttpResponse

# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid(): 
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect("index")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'bughound/index.html', {'form' : form})
