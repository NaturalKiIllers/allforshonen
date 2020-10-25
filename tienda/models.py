from django.db import models


class Figura(models.Model):
    id_figura        = models.AutoField(db_column='id_figura', primary_key=True)
    nombre           = models.CharField(max_length=20, blank=True, null=True)
    anime            = models.CharField(max_length=20, blank=True, null=True)
    descripcion      = models.CharField(max_length=50, blank=True, null=True)
    precio           = models.IntegerField(blank=True, null=True)
    altura           = models.IntegerField(blank=True, null=True)
    material         = models.CharField(max_length=20, blank=True, null=True)
    tipo             = models.CharField(max_length=20, blank=True, null=True)
    foto             = models.ImageField(upload_to='fotos', blank=True, null=True)

