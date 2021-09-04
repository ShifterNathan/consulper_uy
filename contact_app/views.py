from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

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
    
    return render(request, "contact_app/contact.html", {})
