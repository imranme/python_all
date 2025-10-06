"""
URL configuration for off_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views as v
from .views import HomeView
from django.urls import path, include


def home_view(request):
    view = HomeView()
    return view.get1(request)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', demo_view)
    path('', v.demo),
    path('home/', home_view, name='home'),
    path('myapp/', include('demoapp1.urls')),
]
