from django.urls import path
from account import views

urlpatterns = [
    #path('', views.v_account, name='v_account'),
    path('', 'templates/login.html'),
]