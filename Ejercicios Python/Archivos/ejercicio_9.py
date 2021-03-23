#9. Rehacer el ejercicio 4 pero con archivos binarios SUCURSAL_1.DAT y SUCURSAL_2.DAT.
# Dados dos archivos de ventas de SUCURSAL_1.txt y SUCURSAL_2.txt como los del ejemplo del video:
# Fecha (año-mes-dia),Sucursal (1 o 2),monto
# Ambos ordenados por fecha de menor a mayor.
# Se pide hacer un merge, teniendo en cuenta que la cantidad de campos (en cualquiera de los archivos) puede no ser la
# correcta (más o menos campos). En ese caso enviar esa línea al archivo ERRORES.txt

import pickle

def leer_binario(archivo):
    try:
        dato = pickle.load(archivo)
        return dato
    except EOFError:
        return None

def imprimir_binario(archivo):
    seguir_leyendo = True
    while seguir_leyendo:
        try:
            dato = pickle.load(archivo)
            print(dato)
        except EOFError:
            seguir_leyendo = False

def convertir_fechas(fecha):
    numero = ''
    lista = fecha.split('-')
    for elem in lista:
        numero += elem
    return int(numero)

#CREO LOS ARCHIVOS:
s1 = open("SUCURSAL_1.dat", 'wb')
s2 = open("SUCURSAL_2.dat", 'wb')
l1 = [['2018-01-15', "Sucursal 1", 31012], ['2018-03-15', "Sucursal 1", 3129], ['2018-05-19', "Sucursal 1", 5783], ['2018-05-19', "Sucursal 1"],
    ['2018-10-09', "Sucursal 1", 3819], ['2018-10-30', "Sucursal 1", 3819], ['2019-10-30', "Sucursal 1", 3813], ['2019-10-31', "Sucursal 1", 313]]
for elem in l1:
    pickle.dump(elem, s1)
l2 = [['2018-02-15', "Sucursal 2", 61012], ['2018-03-15', "Sucursal 2", 1129], ['2018-05-20', "Sucursal 2", 9783],
      ['2018-09-09', "Sucursal 2", 319], ["Sucursal 2", 5783], ['2018-10-19', 3129]]
for elem in l2:
    pickle.dump(elem, s2)

s1.close()
s2.close()

s1 = open("SUCURSAL_1.dat", 'rb')
s2 = open("SUCURSAL_2.dat", 'rb')
s1y2 = open("SUCURSAL_1_2.DAT", 'wb')
errores = open("ERROR.DAT", 'wb')

suc1 = leer_binario(s1)
suc2 = leer_binario(s2)

while (suc1 != None) and (suc2 != None):
    if (len(suc1) == 3) and (len(suc2) == 3):
        fechasuc1 = convertir_fechas(suc1[0])
        fechasuc2 = convertir_fechas(suc2[0])
        if fechasuc1 < fechasuc2:
            pickle.dump(suc1, s1y2)
            suc1 = leer_binario(s1)
        elif fechasuc1 > fechasuc2:
            pickle.dump(suc2, s1y2)
            suc2 = leer_binario(s2)
        else: # igual fecha
            pickle.dump(suc1, s1y2)
            pickle.dump(suc2, s1y2)
            suc1 = leer_binario(s1)
            suc2 = leer_binario(s2)
    elif len(suc1) != 3:
        pickle.dump(suc1, errores)
        suc1 = leer_binario(s1)
    elif len(suc2) != 3:
        pickle.dump(suc2, errores)
        suc2 = leer_binario(s2)

while suc1 != None:
    if len(suc1) == 3:
        pickle.dump(suc1, s1y2)
    else:
        pickle.dump(suc1, errores)
    suc1 = leer_binario(s1)

while suc2 != None:
    if len(suc2) == 3:
        pickle.dump(suc2, s1y2)
    else:
        pickle.dump(suc2, errores)
    suc2 = leer_binario(s2)

s1.close()
s2.close()
s1y2.close()
errores.close()

s1y2 = open("SUCURSAL_1_2.DAT", 'rb')
errores = open("ERROR.DAT", 'rb')

print("1 Y 2")
imprimir_binario(s1y2)

print("ERRORES:")
imprimir_binario(errores)

errores.close()
s1y2.close()
