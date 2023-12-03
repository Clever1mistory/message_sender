from django.contrib import admin
from django.urls import path, include
from swagger import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
] + swagger_urls
