from django.urls import path
from account import views

urlpatterns = [
    path('', views.v_account),
]