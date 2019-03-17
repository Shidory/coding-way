from django.shortcuts import render
from django.views.generic import CreateView #import CreateView
from .models import CreateAccount

class UserCreateView(CreateView):
    
    model = CreateAccount
    template_name = 'login.html'
    fields = ('surname', 'name', 'email', 'phone', 'password')

def account_controller(request):

    return render(request, 'account.html')
