from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .models import Category, Services

# Create your views here.

def home(request):
    categories = Category.objects.all()
    return render(request, "home_app/home.html", {"categories": categories})


def services(request):
    services = Services.objects.all()
    return render(request, "home_app/services.html", {"services": services})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject=request.POST.get("subject")
        email=request.POST.get("email")
        message=request.POST.get("message")

        email=EmailMessage("Mensaje de Consulper Uruguay web",
            "Usuario: {} Asunto: {} Dirección: {} Mensaje:\n\n {}".format(name,subject,email,message),
            "",["alternplayer00@gmail.com"],reply_to=[email])
        
        try: 
            email.send()
            return redirect("/contact/?valid")

        except:
            return redirect("/contact/?notvalid")
    
    return render(request, "home_app/contact.html", {})



