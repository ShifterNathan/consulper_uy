from django.shortcuts import render, HttpResponse
from .models import Category, Specialty

# Create your views here.

def home(request):
    categories = Category.objects.all()
    return render(request, "home_app/home.html", {"categories": categories})


'''
def home(request):
    specialties = Specialty.objects.all()
    return render(request, "home_app/home.html", {"specialties": specialties})
'''