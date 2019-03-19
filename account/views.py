from django.shortcuts import render
from django.views.generic import CreateView #import CreateView
from .models import CreateAccount
from django.http.response import HttpResponse

from .forms import ContactForm

"""class UserCreateView(CreateView):
    
    model = CreateAccount
    template_name = 'login.html'
    fields = ('surname', 'name', 'email', 'phone', 'password')

def account_controller(request):

    return render(request, 'account.html')"""

def contact(request):
    
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
    form = ContactForm()
    return render(request, 'account/form.html', {'form': form})
