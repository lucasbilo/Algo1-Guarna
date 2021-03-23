# Dado un archivo “prueba.txt” de formato CSV (valores separados por coma), en donde hay 3 campos: número de legajo,
# nombre y apellido, nota (de tipo entero), se pide: leerlo e imprimirlo por pantalla con el mismo formato que está
# en el archivo. Nota: escribir un archivo para probar el programa.

archivo = open("prueba.txt", 'r')

"""dato = archivo.read()
print(dato)"""

linea = archivo.readline()
while linea:
    print(linea, end='')
    linea = archivo.readline()

archivo.close()