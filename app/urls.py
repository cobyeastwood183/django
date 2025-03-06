"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def trigger_error(request):
    division_by_zero = 1 / 0
    return HttpResponse("Testing Sentry Error")

def trigger_transaction(request):
    return HttpResponse("Testing Sentry Transaction")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

urlpatterns = [
    path('', index),
    path('sentry-debug/', trigger_error),
    path('sentry-transaction/', trigger_transaction),
    path('admin/', admin.site.urls),
]
