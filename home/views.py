from django.shortcuts import render

# Create your views here.
def home_controller():
    
    return render(request, 'index.html')