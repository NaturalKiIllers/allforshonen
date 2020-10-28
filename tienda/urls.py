
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
    path('agregar_figura', views.agregar_figura, name='administrador'),
    path('eliminar_figura', views.eliminar_figura, name='eliminar_figura'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('MangaAg', views.MangaAg, name='MangaAg'),
    path('MangaEl', views.MangaEl, name='MangaEl'),
    path('MangaBu', views.MangaBu, name='MangaBu'),
    path('MangaL', views.MangaL, name='MangaL'),

    path('FiguraAg', views.FiguraAg, name='FiguraAg'),
    path('FiguraEl', views.FiguraEl, name='FiguraEl'),
    path('FiguraBu', views.FiguraBu, name='FiguraBu'),
    path('FiguraL', views.FiguraL, name='FiguraL'),

    path('ArtAg', views.ArtAg, name='ArtAg'),
    path('ArtEl', views.ArtEl, name='ArtEl'),
    path('ArtBu', views.ArtBu, name='ArtBu'),
    path('ArtL', views.ArtL, name='ArtL'),
    
    
  
]
