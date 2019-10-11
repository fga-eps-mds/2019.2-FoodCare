from django.shortcuts import render,redirect
from django.core.mail import send_mail

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Create your views here.
def mensagem(nome,email,mensagem):
    msg = """

    Olá, {}
    {}    
    {}
    """.format(nome,mensagem,email)
    return msg

def index(n,e,m):
    subject = "FoodCare: Mensagem de {}".format(n)
    message = mensagem(n,e,m)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER,]
    send_mail( subject, message, email_from, recipient_list )

@csrf_exempt
def email(request):
    if request.method == "POST":
        print(request.POST)
        index(request.POST.get('nome'),request.POST.get('email'),request.POST.get('msg'))
        return redirect('/admin/')
    return redirect('/admin/')