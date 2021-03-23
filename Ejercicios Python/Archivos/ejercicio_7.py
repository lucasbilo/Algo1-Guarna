# 7. Rehacer el ejercicio 2 pero con archivos binarios: “pruebas2.dat”
# #Dado el mismo archivo del punto anterior, leerlo por completo e ir generando, a medida que se lo lee, un nuevo archivo
# “prueba2.txt” con el mismo formato, pero, en lugar de nota irá: R (recursa) si la nota es menor a 4, A (aprobado) si
# está entre 4 y 7, D (distinguido) si es 8 o 9, y S (sobresaliente) si es 10.

import pickle

def tipo_de_nota(nota):
    if nota < 4:
        return 'R'
    elif 4 <= nota <= 7:
        return 'A'
    elif 8 <= nota <= 9:
        return 'D'
    return 'S'

archivo = open("pruebas.dat", 'rb')
archivo_nuevo = open("pruebas2.dat", 'wb')

seguir_leyendo = True
while seguir_leyendo:
    try:
        dato = pickle.load(archivo)
        tipo_nota = tipo_de_nota(dato[2])
        dato[2] = tipo_nota
        print(dato)
        pickle.dump(dato, archivo_nuevo)
    except EOFError:
        seguir_leyendo = False

archivo.close()
archivo_nuevo.close()


"""def size(f):
    f.seek(0, 2)
    tamanio = f.tell()
    f.seek(0)
    return tamanio
MAX = size(archivo)
posicion = 0
while posicion < MAX:
    registro = pickle.load(archivo)
    nota_nueva = tipo_de_nota(int(registro[2]))
    pickle.dump([registro[0], registro[1], nota_nueva], archivo_nuevo)
    posicion = archivo.tell()


archivo.close()
archivo_nuevo.close()

archivo_nuevo = open("pruebas2.dat", 'rb')
MAX = size(archivo_nuevo)
posicion = 0
while posicion < MAX:
    registro = pickle.load(archivo_nuevo)
    print(registro)
    posicion = archivo_nuevo.tell()

archivo_nuevo.close()"""