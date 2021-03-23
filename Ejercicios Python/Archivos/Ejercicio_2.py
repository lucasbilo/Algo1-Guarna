#Dado el mismo archivo del punto anterior, leerlo por completo e ir generando, a medida que se lo lee, un nuevo archivo
# “prueba2.txt” con el mismo formato, pero, en lugar de nota irá: R (recursa) si la nota es menor a 4, A (aprobado) si
# está entre 4 y 7, D (distinguido) si es 8 o 9, y S (sobresaliente) si es 10.

def tipo_de_nota(nota):
    if nota < 4:
        return 'R'
    elif 4 <= nota <= 7:
        return 'A'
    elif 8 <= nota <= 9:
        return 'D'
    return 'S'

archivo_anterior = open("prueba.txt", 'r')
nuevo_archivo = open("prueba2.txt", 'w')

linea = archivo_anterior.readline()
while linea:
    lista = linea.split(',')
    nota_nueva = tipo_de_nota(int(lista[2]))
    print(lista)
    nuevo_archivo.write("{},{},{}{}".format(lista[0], lista[1], nota_nueva, "\n"))
    linea = archivo_anterior.readline()

archivo_anterior.close()
nuevo_archivo.close()