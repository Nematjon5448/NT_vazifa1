"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from .views import (asosiy, index_1, index_2, index_3, index_4, index_5,
                    index_6, index_7, index_8, index_9, index_10, index_11,
                    index_12, index_13, index_14, index_15)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asosiy),
    path('index_1.html', index_1),
    path('index_2.html', index_2),
    path('index_3.html', index_3),
    path('index_4.html', index_4),
    path('index_5.html', index_5),
    path('index_6.html', index_6),
    path('index_7.html', index_7),
    path('index_8.html', index_8),
    path('index_9.html', index_9),
    path('index_10.html', index_10),
    path('index_11.html', index_11),
    path('index_12.html', index_12),
    path('index_13.html', index_13),
    path('index_14.html', index_14),
    path('index_15.html', index_15)
]
