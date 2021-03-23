def leer_linea(archivo):
    linea = archivo.readline()
    linea = linea.rstrip("\n")
    if not linea:
        linea = ' , , , , ,'
    return linea.split(',')

def cargar_exceso(archivo, legajo, cod_reintegro, descripcion_codigo, cantidad_excedida):
    archivo.write("{},{},{},{}\n".format(legajo, cod_reintegro, descripcion_codigo, cantidad_excedida))

def ordenar_diccionario(diccionario):
    return sorted(diccionario.items(), key= lambda x: x[1], reverse=True)

def generar_archivo_ranking(archivo, diccionario):
    for claves in diccionario:
        archivo.write("{},{}\n".format(claves, diccionario[claves]))


# from herramientas import cargar_topes

rendicion = open("rendicion_gastos.cvs")
excedidos = open("excedidos.txt", 'w')
ranking = open("ranking_devoluciones.csv", 'w')

legajo, fecha, id, cod_reintegro, monto = leer_linea(rendicion)

dic = cargar_topes()

empleados = {}

while legajo != ' ':
    print("Legajo: ", legajo)
    total_a_reintegrar = 0
    leg_anterior = legajo
    while legajo == leg_anterior:
        cod_anterior = cod_reintegro
        sum_codigo = 0
        while legajo == leg_anterior and cod_reintegro == cod_anterior:
            total_a_reintegrar += monto
            sum_codigo += monto
            legajo, fecha, id, cod_reintegro, monto = leer_linea(rendicion)
        if dic[cod_anterior][1] < sum_codigo:
            cantidad_excedida = sum_codigo - dic[cod_anterior][1]
            total_a_reintegrar -= cantidad_excedida
            print("Por codigo {} debe pagar {}".format(cod_anterior, cantidad_excedida))
            cargar_exceso(excedidos, legajo, cod_anterior, dic[cod_anterior][0], cantidad_excedida)
    empleados[legajo] = total_a_reintegrar

empleados = ordenar_diccionario(empleados)
generar_archivo_ranking(ranking, empleados)

ranking.close()
rendicion.close()
excedidos.close()



