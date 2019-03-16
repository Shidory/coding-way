from django.shortcuts import render
from .models import CreateAccount

def v_account(request):
    return render(request, 'account.html')
