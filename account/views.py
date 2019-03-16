from django.shortcuts import render
from django.views.generic import CreateView #import CreateView
from account.models import CreateAccount

class UserCreateView(CreateView):
    
    fields = ('surname', 'name', 'email', 'phone', 'password')

"""def v_account(request):

    return render(request, 'account.html')"""
