from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'', include('semglu.urls')),
    path(r'admin/', admin.site.urls),

]