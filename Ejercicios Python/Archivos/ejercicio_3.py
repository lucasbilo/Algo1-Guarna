# Dado un archivo MAESTRO.txt y uno NOVEDAD.txt con el formato que se encuentra en el video de ejemplo:
# MAESTRO: Legajo, nombre, sueldo
# NOVEDAD : Legajo, nombre, sueldo, tipo de novedad
# Ambos ordenados por número de legajo de menor a mayor.
# Se pide hacer un apareo, teniendo en cuenta que, la cantidad de campos del archivo NOVEDAD puede no ser correcta
# (más o menos campos), en estos casos, la línea irá al archivo de ERRORES.

FIN = "999"
MAX = "999,9,99"

def leer_linea(archivo, n):
    linea = archivo.readline()
    if not linea:
        if n == 'M':
            linea = MAX
        else:
            linea = MAX + ",9"
    linea = linea.rstrip("\n")
    return linea.split(',')

def grabar_actualizado(archivo, legajo, nombre, sueldo):
    archivo.write("{},{},{}{}".format(legajo, nombre, sueldo, "\n"))

def grabar_error(archivo, lista):
    archivo.write("{}{}".format(lista, "\n"))

maestro = open("MAESTRO.txt", 'r')
novedad = open("NOVEDAD.txt", 'r')
m_actualizado = open("MAESTRO_ACTUALIZADO.txt", 'w')
errores = open("ERRORES_MAESTRO.txt", 'w')

lista_m = leer_linea(maestro, 'M')
lista_n = leer_linea(novedad, 'N')

while (lista_m[0] != FIN) and (lista_n[0] != FIN):
    if len(lista_n) == 4:
        if lista_m[0] < lista_n[0]:
            grabar_actualizado(m_actualizado, lista_m[0], lista_m[1], lista_m[2])
            lista_m = leer_linea(maestro, 'M')
        elif lista_m[0] > lista_n[0]:
            if lista_n[3] == 'A':
                grabar_actualizado(m_actualizado, lista_n[0], lista_n[1], lista_n[2])
            else:
                grabar_error(errores, lista_n)
            lista_n = leer_linea(novedad, 'N')
        else: #SON IGUALES
            if lista_n[3] == 'M':
                grabar_actualizado(m_actualizado, lista_n[0], lista_n[1], lista_n[2])
            elif lista_n[3] == 'A':
                grabar_error(errores, lista_n)
                grabar_actualizado(m_actualizado, lista_m[0], lista_m[1], lista_m[2])
            lista_m = leer_linea(maestro, 'M')
            lista_n = leer_linea(novedad, 'N')
    else:
        grabar_error(errores, lista_n)
        lista_n = leer_linea(novedad, 'N')


while lista_m[0] != FIN:
    grabar_actualizado(m_actualizado, lista_m[0], lista_m[1], lista_m[2])
    lista_m = leer_linea(maestro, 'M')

while lista_n[0] != FIN:
    if len(lista_n) == 4:
        if lista_n[3] == 'A':
            grabar_actualizado(m_actualizado, lista_n[0], lista_n[1], lista_n[2])
        else:
            grabar_error(errores, lista_n)
    else:
        grabar_error(errores, lista_n)
    lista_n = leer_linea(novedad, 'N')



maestro.close()
novedad.close()
m_actualizado.close()
errores.close()