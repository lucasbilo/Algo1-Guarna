import unittest
from tp0 import *

class TestTP0(unittest.TestCase):

    def test_sumarLetrasDeDistintasPalabras(self):
        palabra1 = '    '
        palabra2 = '    '
        self.assertEquals(sumarLetras(palabra1, palabra2), 8)
        palabra3 = '     '
        palabra4 = '      '
        self.assertEquals(sumarLetras(palabra3, palabra4), 11)
        palabra5 = '     '
        palabra6 = ' '
        self.assertEquals(sumarLetras(palabra5, palabra6), 6)

    def test_determinarPalabraMasLarga(self):
        palabra1 = '    '
        palabra2 = '    '
        self.assertEquals(determinarPalabraMasLarga(palabra1, palabra2), 1)
        palabra3 = '     '
        palabra4 = '      '
        self.assertFalse(determinarPalabraMasLarga(palabra3, palabra4))
        palabra5 = '     '
        palabra6 = ' '
        self.assertTrue(determinarPalabraMasLarga(palabra5, palabra6))

    def test_cantidadDeSegundos(self):
        self.assertEquals(cantidadDeSegundos(1,3,117), 3897)
        self.assertEquals(cantidadDeSegundos(24, 50, 4500), 93900)

    def test_numeroEsPar(self):
        self.assertTrue(esPar(2))
        self.assertFalse(esPar(25))
        self.assertTrue(esPar(0))
        self.assertFalse(esPar(7))

    def test_mayorProducto(self):
        self.assertEquals(mayorProducto(1,2,3), 6)
        self.assertEquals(mayorProducto(3,2,1), 6)
        self.assertEquals(mayorProducto(3,1,2), 6)
        self.assertEquals(mayorProducto(1,3,2), 6)
        self.assertEquals(mayorProducto(2,3,1), 6)
        self.assertEquals(mayorProducto(2,1,3), 6)

if __name__ == '__main__':
    unittest.main()
