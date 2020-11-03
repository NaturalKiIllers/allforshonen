import unittest
from django.test import TestCase
from tienda.models import Figura

class testFigura(unittest.TestCase):
    def test_crear_objeto_Ok(self):
            figura = Figura.objects.create( 
                                    codigof          = 'Op15',
                                    nombre           = 'Luffy',
                                    anime            = 'One Piece',
                                    descripcion      = 'Luffy Gears 4',
                                    precio           = 100000,
                                    altura           = 10,
                                    material         = 'Pvc',
                                    tipo             = 'Estatua',
                                    foto             = '',
                                    activo           = 1)
            figura.save()
            self.assertTrue(figura, True)
    def test_BusarFigura(self):
        figura = Figura.objects.get(codigof='Op15')
        self.assertEquals(figura.codigof, 'Op15')

    def test_Eliminar(self):
        figura = Figura.objects.get(codigof='Op15')
        figura.delete()
        self.assertTrue(figura, True)
        



   

    
    