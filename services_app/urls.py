from django.urls import path
from services_app import views

urlpatterns = [

    path('', views.service_list, name='Services'),
    path('<slug:category_slug>', views.service_list, name='services_by_category'),

]
