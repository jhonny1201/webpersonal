from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)    
        if form.is_valid():
            name = request.POST['name'] + " " + request.POST['last_name']
            subject = request.POST['subject']
            message = "Nombre:" + name + " " + " Correo electrónico:" + request.POST['email'] + " Mensaje:" + request.POST["content"]
            email_from = settings.EMAIL_HOST_USER
            recipient_liv = ['jhonnyrivas1999@gmail.com']
            send_mail(subject, message, email_from, recipient_liv)
            context = {
                'name': name
            }
            return render(request, 'contact/thanks.html', context)

    else:
        form = ContactForm()
        context = {
        'form':form
        }   
        return render(request, 'contact/contact.html', context)


