
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('mangas', views.mangas, name='mangas'),
    path('index', views.index, name='index'),
    path('artbooks', views.artbooks, name='artbooks'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('figuras', views.figuras, name='figuras'),
    path('contacto', views.contacto, name='contacto'),
    path('login', views.login, name='login'),
    path('agregar_contacto', views.agregar_contacto, name='agregar_contacto'),
    path('administrador', views.administrador, name='administrador'),
]
