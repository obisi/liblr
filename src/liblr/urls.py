"""liblr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from app.views import *

urlpatterns = [
    # Admin urls
    path('admin/', admin.site.urls),

    # App urls
    path('', IndexView.as_view(), name='index'),
    path('tips/', ReadingTipListView.as_view(), name='tips'),
    path('tips/<int:tip_id>/', ReadingTipListView.as_view(), name='tips_detail'),
    path('tips/create/', ReadingTipCreateView.as_view(), name='tips_create'),
    path('tips/delete/<pk>/', ReadingTipDeleteView.as_view(), name='tips_delete'),

    # Authentication
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
