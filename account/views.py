from django.shortcuts import render
from django.views.generic import CreateView #import CreateView
from .models import CreateAccount
from django.http.response import HttpResponse

"""class UserCreateView(CreateView):
    
    model = CreateAccount
    template_name = 'login.html'
    fields = ('surname', 'name', 'email', 'phone', 'password')

def account_controller(request):

    return render(request, 'account.html')"""

def contact(request):
    return HttpResponse('contact view')
