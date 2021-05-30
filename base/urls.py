from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('', include('core.api.urls')),
    path('', include('users.api.urls')),
    
]
