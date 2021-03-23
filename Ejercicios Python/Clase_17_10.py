"""import unittest

class TestMisFuncs(unittest.TestCase):
    def test_en_may(self):
        en_may = "Hola!"
        esperado = "Hola!"
        self.assertEqual(en_may, esperado, "Error! esperado {0} recibido {1}".format(esperado, en_may))

if __name__ == "__main__":
    unittest.main()"""

"""import pickle
with open("ejemplo.bin", "wb") as arch: #wb es para escritura en modo binario
    pkl = pickle.Pickler(arch)
    alumno = {"nombre": "Juan", "apellido": "Pérez", "edad": 22, "promedio": 7.58}
    l = [0, 0, 1, 3]
    n = 7
    pkl.dump(alumno)
    pkl.dump(l)
    pkl.dump(n)"""

import pickle

with open("ejemplo.bin", "rb") as arch:
    seguir_leyendo = True
    while seguir_leyendo:
        try:
            dato = pickle.load(arch)
        except EOFError:
            seguir_leyendo = False
        else:
            print(dato)