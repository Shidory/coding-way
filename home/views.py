from django.shortcuts import render

# Create your views here.
def home_controller(request):
    
    return render(request, 'home/index.html')