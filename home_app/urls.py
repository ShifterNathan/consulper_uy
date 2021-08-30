from django.urls import path
from home_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name="Home"),
    path('contact/', views.contact, name="Contact"),
    path('services/', views.services, name="Services")

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)