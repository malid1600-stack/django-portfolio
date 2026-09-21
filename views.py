from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.

def home(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        send_mail(
            subject=f"Portfolio Contact: {subject}",
            message=f"""
Name: {name}
Email: {email}

Message:
{message}
""",
             from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        )

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

    return render(request, "home.html")