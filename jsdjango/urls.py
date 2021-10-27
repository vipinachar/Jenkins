"""jsdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api.views import AppUserApi,listAPIView,UpdateUserAPIView


urlpatterns = [
    path('adminsss/', admin.site.urls),
    path('api/v1/users/',AppUserApi.as_view()),
    path('api/v1/users/<str:email>/',AppUserApi.as_view()),
    path('list/',listAPIView.as_view()),
    path('register/',AppUserApi.as_view()),
    path('update/',UpdateUserAPIView.as_view()),
    path('update/<str:email>/',UpdateUserAPIView.as_view()),
    
   
  
    
]
