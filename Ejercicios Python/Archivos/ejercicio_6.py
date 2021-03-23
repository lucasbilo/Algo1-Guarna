#6. Rehacer el ejercicio 1 pero con un archivo binario: “pruebas.dat”
# Dado un archivo “prueba.txt” de formato CSV (valores separados por coma), en donde hay 3 campos: número de legajo,
# nombre y apellido, nota (de tipo entero), se pide: leerlo e imprimirlo por pantalla con el mismo formato que está
# en el archivo.

"""def size(f):
    f.seek(0, 2)
    tamanio = f.tell()
    f.seek(0)
    return tamanio"""

import pickle
#Primero creo el archivo, le paso los datos como listas.
archivo = open("pruebas.dat", 'wb')
registros = [[132, "Lucas Bilo", 9], [212, "Simon Ponce", 10], [215, "Fede Recepter", 4], [331, "Nacho Dabove", 7], [340, "Guille Re", 2]]
for reg in registros:
    pickle.dump(reg, archivo)
archivo.close()

"""archivo = open("pruebas.dat", 'rb')
MAX = size(archivo)
posicion = 0
while posicion < MAX:
    registro = pickle.load(archivo)
    print(registro)
    posicion = archivo.tell()

archivo.close()"""

archivo = open("pruebas.dat", 'rb')
seguir_leyendo = True
while seguir_leyendo:
    try:
        dato = pickle.load(archivo)
        print(dato)
    except EOFError:
        seguir_leyendo = False

archivo.close()