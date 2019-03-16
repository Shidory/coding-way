from django.shortcuts import render
from django.views.generic import CreateView #import CreateView
from .models import CreateAccount

class AccountCreateView(CreateView):
    pass

def v_account(request):
    return render(request, 'account.html')
