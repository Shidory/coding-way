from django.shortcuts import render
from django.views.generic import CreateView #import CreateView
from .models import User

class UserCreateView(CreateView):
    
    model = User
    fields = ('surname', 'name', 'email', 'phone', 'password')

"""def v_account(request):

    return render(request, 'account.html')"""
