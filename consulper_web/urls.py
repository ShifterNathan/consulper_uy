from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', include('djoser.urls')),
    path('api/v1', include('djoser.urls.authtoken')),
    path('', include('home_app.urls')),
    path('services/', include('services_app.urls')),
    path('contact/', include('contact_app.urls')),
]
