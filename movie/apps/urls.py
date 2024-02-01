"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from apps import views
app_name = 'apps'
urlpatterns = [
    path('',views.viewmovies,name="viewmovies"),
    path('add/',views.add,name="add"),
    path('add1/',views.add1,name="add1"),
    path('viewbyid/<int:p>',views.viewmoviebyid,name="viewmoviebyid"),
    path('deletebyid/<int:p>',views.deletemoviebyid,name="deletemoviebyid"),
    path('editbyid<int:p>',views.editmoviebyid,name="editmoviebyid"),
]
