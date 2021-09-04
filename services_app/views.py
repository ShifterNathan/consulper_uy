from django.shortcuts import render, get_object_or_404
from .models import Services
from home_app.models import Category

'''    def services(request):
        services = Services.objects.all()
        categories = Category.objects.all()
        return render(request, "services_app/services.html", {"services": services, "categories": categories})
'''

def service_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    services = Services.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        services = services.filter(category=category)
    return render(request, 'services_app/services.html', {'categories':categories, 'category':category, 'services':services,})
