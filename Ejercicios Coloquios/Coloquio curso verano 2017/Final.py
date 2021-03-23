def esta_en_diccionario(clave, diccionario):
    for claves in diccionario:
        if clave == claves:
            return True
    return False

def esta_en_lista(elemento, lista):
    for i in range(len(lista)):
        if elemento == lista[i][0]:
            return i
    return None

def cargar_vendedor_ranking(id, importe, ranking):
    if esta_en_diccionario(id, ranking):
        ranking[id] += int(importe)
    else:
        ranking[id] = int(importe)


def imprimir_lista_en_dicc(diccionario):
    print("ID - CANTIDAD - IMPORTE ")
    for listas in diccionario:
        print("{} - {} - {}".format(listas[0], listas[1], listas[2]))

def leer_linea(archivo):
    linea = archivo.readline()
    linea = linea.rstrip("\n")
    if not linea:
        return None
    return linea

def agregar_a_archivo(archivo, codigo, sucursal, id, cantidad, importe):
    archivo.write("{},{},{},{},{}\n".format(codigo, sucursal, id, cantidad, importe))

s1 = open("sucursal1.csv.txt")
s2 = open("sucursal2.csv.txt")
s = open("sucursal.csv", 'w')

suc_1 = leer_linea(s1)
suc_2 = leer_linea(s2)
ranking = {}
while (suc_1 != None) and (suc_2 != None):
    cod_s1, id_s1, cant_s1, imp_s1 = suc_1.split(',')
    cod_s2, id_s2, cant_s2, imp_s2 = suc_2.split(',')
    if cod_s1 > cod_s2:
        agregar_a_archivo(s, cod_s2, 'S2', id_s2, cant_s2, imp_s2)
        cargar_vendedor_ranking(id_s2, imp_s2, ranking)
        suc_2 = leer_linea(s2)
    else:
        agregar_a_archivo(s, cod_s1, 'S1', id_s1, cant_s1, imp_s1)
        cargar_vendedor_ranking(id_s1, imp_s1, ranking)
        suc_1 = leer_linea(s1)

while suc_1 != None:
    cod_s1, id_s1, cant_s1, imp_s1 = suc_1.split(',')
    agregar_a_archivo(s, cod_s1, 'S1', id_s1, cant_s1, imp_s1)
    cargar_vendedor_ranking(id_s1, imp_s1, ranking)
    suc_1 = leer_linea(s1)

while suc_2 != None:
    cod_s2, id_s2, cant_s2, imp_s2 = suc_2.split(',')
    agregar_a_archivo(s, cod_s2, 'S2', id_s2, cant_s2, imp_s2)
    cargar_vendedor_ranking(id_s2, imp_s2, ranking)
    suc_2 = leer_linea(s2)

s1.close()
s2.close()
s.close()

sucursales = open("sucursal.csv")
productos = open("productos.csv.txt")
totales = {}
linea = leer_linea(sucursales)
while linea != None:
    cod, suc, id, cant, imp = linea.split(',')
    if not esta_en_diccionario(cod, totales):
        totales[cod] = {'S1': [], 'S2': []}
    i = esta_en_lista(id, totales[cod][suc])
    if i != None:
        totales[cod][suc][i][1] += int(cant)
        totales[cod][suc][i][2] += int(imp)
    else:
        totales[cod][suc].append([id, int(cant), int(imp)])
    linea = leer_linea(sucursales)

linea_producto = leer_linea(productos)
while linea_producto != None:
    codigo, descripcion = linea_producto.split(',')
    if esta_en_diccionario(codigo, totales):
        print("*** {} - {} ***".format(codigo, descripcion))
        for claves in totales[codigo]:
            if totales[codigo][claves]:
                print("*** {} *** ".format(claves))
                imprimir_lista_en_dicc(totales[codigo][claves])
    linea_producto = leer_linea(productos)

sucursales.close()
productos.close()

ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
print("\n\n*** RANKING POR COMISION ***")
print("VENDEDOR - IMPORTE - COMISION")
total_comision = 0
total_importe = 0
for tuplas in ranking_ordenado:
    comision = tuplas[1] * 0.03
    total_comision += comision
    total_importe += tuplas[1]
    print("{} - {} - {}".format(tuplas[0], tuplas[1], comision))
print("TOTAL IMPORTE - TOTAL COMISIONES\n   {}           {}".format(total_importe, total_comision))