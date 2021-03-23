# 8. Rehacer el ejercicio 3 pero con archivos binarios: MAESTRO.DAT y NOVEDAD.DAT.
# # Dado un archivo MAESTRO.txt y uno NOVEDAD.txt con el formato que se encuentra en el video de ejemplo:
# # MAESTRO: Legajo, nombre, sueldo
# # NOVEDAD : Legajo, nombre, sueldo, tipo de novedad
# # Ambos ordenados por número de legajo de menor a mayor.
# # Se pide hacer un apareo, teniendo en cuenta que, la cantidad de campos del archivo NOVEDAD puede no ser correcta
# # (más o menos campos), en estos casos, la línea irá al archivo de ERRORES.

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

#Creo los archivos NOVEDAD y MAESTRO.
maestro = open("MAESTRO.dat", 'wb')
novedad = open("NOVEDAD.dat", 'wb')
lista_1 = [[132, "Lucas Bilo", 9123], [212, "Simon Ponce", 10322], [215, "Fede Recepter", 451], [331, "Nacho Dabove", 731], [340, "Guille Re", 211], [355, "Chita", 321]]
for elem in lista_1:
    pickle.dump(elem, maestro)
lista_2 = [[132, "Lucas Bilo", 10000, 'M'], [212, "Simon Ponce", 10312, 'A'], [215, 4511, 'M'],
           [300, "Cholo Simeone", 1032, 'A'], [331, "Nacho Dabove", 391, 'B'], [340, "Guille Re", 25111, 'M'], [3]]
for elem in lista_2:
    pickle.dump(elem, novedad)

maestro.close()
novedad.close()

maestro = open("MAESTRO.dat", 'rb')
novedad = open("NOVEDAD.dat", 'rb')
errores = open("ERRORES.dat", 'wb')
actualizado = open("MAESTRO_ACT.dat", 'wb')

l_maestro = leer_binario(maestro)
l_novedad = leer_binario(novedad)

while (l_maestro != None) and (l_novedad != None):
    if len(l_novedad) == 4:
        if l_maestro[0] < l_novedad[0]:
            pickle.dump(l_maestro, actualizado)
            l_maestro = leer_binario(maestro)
        elif l_maestro[0] > l_novedad[0]:
            if l_novedad[3] == 'A':
                pickle.dump(l_novedad[:3], actualizado)
            else:
                pickle.dump(l_novedad, errores)
            l_novedad = leer_binario(novedad)
        else: #legajos iguales
            if l_novedad[3] == 'M':
                pickle.dump(l_novedad[:3], actualizado)
            elif l_novedad[3] == 'A':
                pickle.dump(l_novedad, errores)
                pickle.dump(l_maestro, actualizado)
            l_maestro = leer_binario(maestro)
            l_novedad = leer_binario(novedad)
    else: #novedad con menos campos
        pickle.dump(l_novedad, errores)
        l_novedad = leer_binario(novedad)

while l_maestro != None:
    pickle.dump(l_maestro, actualizado)
    l_maestro = leer_binario(maestro)

while l_novedad != None:
    if len(l_novedad) == 4:
        if l_novedad[3] == 'A':
            pickle.dump(l_novedad[:3], actualizado)
        else:
            pickle.dump(l_novedad, errores)
    else:
        pickle.dump(l_novedad, errores)
    l_novedad = leer_binario(novedad)

maestro.close()
novedad.close()
errores.close()
actualizado.close()

print("ACTUALIZADO")
archivo = open("MAESTRO_ACT.dat", 'rb')
imprimir_binario(archivo)
archivo.close()

print("ERRORES:")
archivo = open("ERRORES.dat", 'rb')
imprimir_binario(archivo)
archivo.close()



"""
max_maestro = size(r_maestro)
max_novedad = size(r_novedad)
maestro = pickle.load(r_maestro)
novedad = pickle.load(r_novedad)
pos_maestro = r_maestro.tell()
pos_novedad = r_novedad.tell()

while (pos_maestro < max_maestro) and (pos_novedad < max_novedad):
    if len(novedad) == 4:
        if maestro[0] < novedad[0]:
            pickle.dump(maestro, actualizado)
            maestro = pickle.load(r_maestro)
        elif maestro[0] > novedad[0]:
            if novedad[3] == 'A':
                pickle.dump(novedad[0:3], actualizado)
            else: 
                pickle.dump(novedad, errores)
            novedad = pickle.load(r_novedad)
        else:  # legajos iguales
            if novedad[3] == 'M':
                pickle.dump(novedad[0:3], actualizado)
            elif novedad[3] == 'A':
                pickle.dump(novedad, errores)
                pickle.dump(maestro, actualizado)
            maestro = pickle.load(r_maestro)
            novedad = pickle.load(r_novedad)
    else:  # novedad vino con menos campos
        pickle.dump(novedad, errores)
        novedad = pickle.load(r_novedad)
    pos_novedad = r_novedad.tell()
    pos_maestro = r_maestro.tell()

if pos_maestro < max_maestro:
    pickle.dump(maestro, actualizado)
    pos_maestro = r_maestro.tell()
    while pos_maestro < max_maestro:
        maestro = pickle.load(r_maestro)
        pickle.dump(maestro, actualizado)
        pos_maestro = r_maestro.tell()

while pos_novedad < max_novedad:
    if len(novedad) == 4:
        if novedad[3] == 'A':
            pickle.dump(novedad, actualizado)
        else:
            pickle.dump(novedad, errores)
    else:
        pickle.dump(novedad, errores)
    pos_novedad = r_novedad.tell()
    novedad = pickle.load(r_novedad)


r_maestro.close()
r_novedad.close()
errores.close()
actualizado.close()

archivo_nuevo = open("MAESTRO_ACT.dat", 'rb')
MAX = size(archivo_nuevo)
posicion = 0
print("ARCHIVO ACTUALIZADO:")
while posicion < MAX:
    registro = pickle.load(archivo_nuevo)
    print(registro)
    posicion = archivo_nuevo.tell()

archivo_nuevo.close()

errores = open("ERRORES.dat", 'rb')
MAX = size(errores)
posicion = 0
print("ERRORES:")
while posicion < MAX:
    registro = pickle.load(errores)
    print(registro)
    posicion = errores.tell()

errores.close()"""





