from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['kdragondev@gmail.com',]

    send_mail(subject=subject, message=message, from_email=email_from, recipient_list=recipient_list)

    return render('redirect to a new page')