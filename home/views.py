from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
        {
            "name": "django-allauth",
            "url": "https://pypi.org/project/django-allauth/0.38.0/",
        },
        {
            "name": "django-bootstrap4",
            "url": "https://pypi.org/project/django-bootstrap4/0.0.7/",
        },
        {
            "name": "djangorestframework",
            "url": "https://pypi.org/project/djangorestframework/3.9.0/",
        },
    ]
    context = {
        "customtext": CustomText.objects.first(),
        "homepage": HomePage.objects.first(),
        "packages": packages,
    }
    return render(request, "home/index.html", context)


def test_email(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'borhan@crowdbotics.com',
        ['tipu.but@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('ok')