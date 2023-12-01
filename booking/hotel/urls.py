from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotel_app/', include('hotel_app.urls')),
    path('', include('hotel_app.urls')),
    path("auth/", include("django.contrib.auth.urls"))

]