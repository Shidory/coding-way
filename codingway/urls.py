from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/', include('account.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]
