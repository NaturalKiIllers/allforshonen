from django.db import models
from django.contrib.auth.models import User


class Figura(models.Model):
    id_figura        = models.AutoField(db_column='id_figura', primary_key=True)
    codigof          = models.CharField(max_length=10, unique=True,null=True)
    nombre           = models.CharField(max_length=20, blank=True, null=True)
    anime            = models.CharField(max_length=20, blank=True, null=True)
    descripcion      = models.CharField(max_length=50, blank=True, null=True)
    precio           = models.IntegerField(blank=True, null=True)
    altura           = models.IntegerField(blank=True, null=True)
    material         = models.CharField(max_length=20, blank=True, null=True)
    tipo             = models.CharField(max_length=20, blank=True, null=True)
    foto             = models.ImageField(upload_to='fotos', blank=True, null=True)
    activo           = models.IntegerField(blank=True, null=True)
    


class Manga(models.Model):
    id_manga         = models.AutoField(db_column='id_manga', primary_key=True)
    codigoM         = models.CharField(max_length=10, unique=True,null=True)
    nombre           = models.CharField(max_length=30, blank=True, null=True)
    editorial        = models.CharField(max_length=20, blank=True, null=True)
    tipo             = models.CharField(max_length=20, blank=True, null=True)
    precio           = models.IntegerField(blank=True, null=True)
    nombre_desc      = models.CharField(max_length=50, blank=True, null=True)
    descripcion      = models.CharField(max_length=100, blank=True, null=True)
    fotoManga        = models.ImageField(upload_to='fotos', blank=True, null=True)
    activo           = models.IntegerField(blank=True, null=True)

class Artbook(models.Model):
    id_artbook       = models.AutoField(db_column='id_artbook', primary_key=True)
    codigoA         = models.CharField(max_length=10, unique=True,null=True)
    nombre           = models.CharField(max_length=30, blank=True, null=True)
    precio           = models.IntegerField(blank=True, null=True)
    nombre_desc      = models.CharField(max_length=50, blank=True, null=True)
    descripcion      = models.CharField(max_length=100, blank=True, null=True)
    fotoArtbook      = models.ImageField(upload_to='fotos', blank=True, null=True)
    activo           = models.IntegerField(blank=True, null=True)

class Contacto(models.Model):
    id_contacto       = models.AutoField(db_column='id_contacto', primary_key=True)
    nombres           = models.CharField(max_length=50, blank=True, null=True)
    correo            = models.CharField(max_length=50, blank=True, null=True)
    asunto            = models.CharField(max_length=10, blank=True, null=True)
    mensaje           = models.CharField(max_length=120, blank=True, null=True)
    
