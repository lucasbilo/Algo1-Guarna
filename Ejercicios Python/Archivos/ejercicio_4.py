# Dados dos archivos de ventas de SUCURSAL_1.txt y SUCURSAL_2.txt como los del ejemplo del video:
# Fecha (año-mes-dia),Sucursal (1 o 2),monto
# Ambos ordenados por fecha de menor a mayor.
# Se pide hacer un merge, teniendo en cuenta que la cantidad de campos (en cualquiera de los archivos) puede no ser la
# correcta (más o menos campos). En ese caso enviar esa línea al archivo ERRORES.txt

FIN = "9999-99-99"
MAX = "9999-99-99,9,9"

def leer_linea(archivo):
    linea = archivo.readline()
    if not linea:
        linea = MAX
    linea = linea.rstrip("\n")
    return linea.split(',')

def grabar(archivo, fecha, sucursal, monto):
    archivo.write("{},{},{}\n".format(fecha, sucursal, monto))

def grabar_error(archivo, lista):
    archivo.write("{]\n".format(lista))

sucursal_1 = open("SUCURSAL_1.txt", 'r')
sucursal_2 = open("SUCURSAL_2.txt", 'r')
sucursal_1_y_2 = open("SUCURSAL_1_Y_2.txt", 'w')
errores = open("ERRORES_MERGE.txt", 'w')

lista_uno = leer_linea(sucursal_1)
lista_dos = leer_linea(sucursal_2)

while (lista_uno[0] != FIN) and (lista_dos[0] != FIN):
    if (len(lista_uno) == 3) and (len(lista_dos) == 3):
        if lista_uno[0] == lista_dos[0]:
            grabar(sucursal_1_y_2, lista_uno[0], lista_uno[1], lista_uno[2])
            grabar(sucursal_1_y_2, lista_dos[0], lista_dos[1], lista_dos[2])
            lista_uno = leer_linea(sucursal_1)
            lista_dos = leer_linea(sucursal_2)
        elif lista_uno[0] < lista_dos[0]:
            grabar(sucursal_1_y_2, lista_uno[0], lista_uno[1], lista_uno[2])
            lista_uno = leer_linea(sucursal_1)
        else: #fecha_1 > fecha_2
            grabar(sucursal_1_y_2, lista_dos[0], lista_dos[1], lista_dos[2])
            lista_dos = leer_linea(sucursal_2)
    elif len(lista_uno) != 3:
        grabar_error(errores, lista_uno)
        lista_uno = leer_linea(sucursal_1)
    else:
        grabar_error(errores, lista_dos)
        lista_dos = leer_linea(sucursal_2)

while lista_uno[0] != FIN:
    if len(lista_uno) == 3:
        grabar(sucursal_1_y_2, lista_uno[0], lista_uno[1], lista_uno[2])
        lista_uno = leer_linea(sucursal_1)
    else:
        grabar_error(errores, lista_uno)
        lista_uno = leer_linea(sucursal_1)

while lista_dos[0] != FIN:
    if len(lista_dos) == 3:
        grabar(sucursal_1_y_2, lista_dos[0], lista_dos[1], lista_dos[2])
        lista_dos = leer_linea(sucursal_2)
    else:
        grabar_error(errores, lista_dos)
        lista_dos = leer_linea(sucursal_2)


sucursal_1.close()
sucursal_2.close()
sucursal_1_y_2.close()
errores.close()



