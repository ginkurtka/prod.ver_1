from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel_app.urls')),
    path('', include('users.urls')),
] +  static(STATIC_URL, document_root=STATIC_URL)  + static('hotel_photos', document_root='hotel_photos')