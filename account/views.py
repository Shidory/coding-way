from django.shortcuts import render
from django.views.generic import CreateView #import CreateView
from .models import CreateAccount

class AccountCreateView(CreateView):
    
    fields = ('surname', 'name', 'email', 'phone', 'password')

def v_account(request):
    
    return render(request, 'account.html')
