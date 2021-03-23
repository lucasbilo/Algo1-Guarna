# 1. El Servicio Meteorológico Nacional tiene registrado, mes por mes, la cantidad de lluvia caída por provincia, en mm
# (entero) y el promedio de humedad relativa (real).
# Estos datos los guarda en una matriz de 24 (23 provincias más CABA) x 12 (meses).
# Se pide, hacer una aplicación en Python que realice lo siguiente:
# a. Indicar en qué mes llovió más y la cantidad.
# b. Indicar si la provincia donde más llovió es la que tiene mayor humedad relativa.
# c. Hacer un listado de las 10 provincias donde más llovió, ordenado de mayor a menor por cantidad de agua caída.
# Indicando: nombre de provincia y cantidad de agua caída
# Nota: simular la carga de forma aleatoria (utilizando la función random).

"""import random

LLUVIA = 0
HUMEDAD = 1

def simulacion_carga():
    datos = {"CABA": [], "Buenos Aires": [], "Formosa": [], "Entre Rios": [], "Cordoba": [], "Santa Fe": [],
             "Corrientes": [], "San Juan": [], "San Luis": [], "Jujuy": [], "Salta": [], "La Pampa": [],
             "Santa Cruz": [], "Catamarca": [], "Santiago del Estero": [], "Neuquen": [], "Rio Negro": [], "Chaco": [],
             "Tucuman": [],  "Mendoza": [], "La Rioja": [], "Misiones": [], "Chubut": [], "Tierra del Fuego": []}
    for provincias in datos:
        for i in range(12):
            datos[provincias] += [[random.randint(0, 100), random.randint(50, 80)]]
    return datos

def mes_mas_llovio(datos):
    total_lluvia = 0
    nro_mes = 0
    for i in range(12):
        sumatoria = 0
        for provincias in datos:
            sumatoria += datos[provincias][i][LLUVIA]
        if sumatoria > total_lluvia:
            total_lluvia = sumatoria
            nro_mes = i + 1
    return total_lluvia, nro_mes

def calcular_mayor_humedad(datos):
    mayor_humedad = 0
    provincia = ''
    for provincias in datos:
        sumatoria = 0
        for meses in datos[provincias]:
            sumatoria += meses[HUMEDAD]
        if sumatoria > mayor_humedad:
            mayor_humedad = sumatoria
            provincia = provincias
    return provincia

def lluvia_total_por_provincia(datos):
    lluvias_totales = []
    for provincias in datos:
        sumatoria = 0
        for meses in datos[provincias]:
            sumatoria += meses[LLUVIA]
        lluvias_totales += [[provincias, sumatoria]]
    return sorted(lluvias_totales, key=lambda x: x[1], reverse=True)

def main():
    datos = simulacion_carga()
    total_lluvia, mes_mas_lluvia = mes_mas_llovio(datos)
    print("El mes que mas llovio fue el numero", mes_mas_lluvia, "con una cantidad de", total_lluvia, "en mm.")
    lluvia_total = lluvia_total_por_provincia(datos)
    provincia_mas_lluvia = lluvia_total[0]
    provincia_mas_humedad = calcular_mayor_humedad(datos)
    if provincia_mas_humedad == provincia_mas_lluvia:
        print("El mes que tuvo mayor humedad fue el mismo que tuvo mas cantidad de lluvia.")
    else:
        print("El mes que tuvo mayor humedad NO fue el mismo que tuvo mas cantidad de lluvia.")
    print("Las 10 provincias en las que mas llovio:")
    for i in range(10):
        print("Provincia:", lluvia_total[i][0], "- Cantidad de agua:", lluvia_total[i][1])

main()"""

#2. Un artículo se comercializa en 5 sucursales. Se leen N (N lo carga el usuario) datos, con el siguiente formato:
# sucursal: Número de sucursal (de 1 a 5)
# mes: Número de mes (de 1 a 12)
# cantidad: Cantidad del producto vendida.
# monto_total: Monto recaudado (los precios del producto difieren por cada sucursal y por cada mes).
# Se pide hacer un programa en Python que:
# a. Vuelque los datos en una matriz de 5 (sucursales) x 12 (meses). Cada celda contendrá un registro con la
# información cantidad – monto_total.
# b. A partir de la matriz armar un listado, ordenado de mayor a menor por monto, indicando sucursal, mes y cantidad
# vendida.
# c. Indicar si la mayor cantidad vendida corresponde al precio unitario más bajo.
# Nota: generar los datos de forma aleatoria.

"""from random import randint

def crear_matriz():
    datos = {}
    for i in range(5):
        datos[i + 1] = []
        for j in range(12):
            datos[i + 1].append([])
    return datos

def generar_datos(n):
    datos = crear_matriz()
    for i in range(n):
        sucursal = randint(1, 5)
        mes = randint(1, 12)
        cantidad = randint(1, 100)
        monto = randint(1, 1000)
        datos[sucursal][mes - 1] = [cantidad, monto]
    return datos

def main():
    n = int(input("Ingrese el numero de la cantidad de datos que quiere ver: "))
    datos = generar_datos(n)
    for sucursales in datos:
        print("Sucursal nro.", sucursales, datos[sucursales])

main()"""

# 3. Escribir un programa que recorra una lista de números, que puede ser cargada
# por teclado o en forma aleatoria, calculando:
# a. Para cada uno el cuadrado ( x ** 2) y genere otra lista con dichos números.
# b. Unir las 2 listas y ordenarlas por valor. Imprimir la misma sin duplicados.

"""def pedir_numeros():
    numeros = []
    numero = int(input("Por favor ingrese un numero o 0 para salir: "))
    while numero != 0:
        numeros += [numero]
        numero = int(input("Por favor ingrese un numero o 0 para salir: "))
    return numeros

def numeros_al_cuadrado(numeros):
    numeros_cuadrado = []
    for elem in numeros:
        numeros_cuadrado += [(elem ** 2)]
    return numeros_cuadrado

def unir_listas(num, num_cuadrado):
    numeros_por_valor = {}
    for i in range(len(num)):
        if not(num[i] in numeros_por_valor):
            numeros_por_valor[num[i]] = num_cuadrado[i]
    return sorted(numeros_por_valor.items(), key=lambda x: x[1], reverse=True)

def main():
    numeros = pedir_numeros()
    print("Lista de numeros: ", numeros)
    numeros_cuadrado = numeros_al_cuadrado(numeros)
    print("Lista de numeros elevados al cuadrado : ", numeros_cuadrado)
    num_por_valor = unir_listas(numeros, numeros_cuadrado)
    for x in num_por_valor:
        print("Numero:", x[0], "elevado al cuadrado:", x[1])

main()"""

# 4. Armar una lista con las primeras 7 letras del alfabeto, pasar c d y e a mayúsculas.
# Borrar las ultimas 2 letras, e imprimir el resultado y la cantidad de elementos de la misma.

"""def main():
    letras_abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letras_abc)
    for i in range(2, 5):
        letras_abc[i] = letras_abc[i].upper()
    print(letras_abc)
    print("Borro ultimas 2 letras: ")
    del(letras_abc[5:])
    print(letras_abc)
    print("La cantidad de elementos es: ", len(letras_abc))

main()"""

# 5. Imprimir los elementos de una lista con su posición:
# a. Sin usar la función enumerate.
# b. Usando la función enumerate.

"""def pedir_lista():
    lista = []
    elemento = input("Por favor ingrese un elemento o 0 para salir: ")
    while elemento != '0':
        lista += [elemento]
        elemento = input("Por favor ingrese un elemento o 0 para salir: ")
    return lista

def main():
    lista = pedir_lista()
    print("Sin funcion enumerate: ")
    for i in range(len(lista)):
        print("En la posicion", (i + 1), "se ingreso:", lista[i])
    print("Con funcion enumerate: ")
    for i, lista in enumerate(lista):
        print("En la posicion:", i + 1, "se ingreso:", lista)

main() """

# 6. Procesar una lista de números enteros, e imprimir para cada uno de ellos: el número que está procesando y la suma
# parcial de los mismos. Además, indicar True si el número es mayor al número anterior y False de lo contrario. Terminar
# cuando se hayan procesado todos los  números o cuando la suma parcial haya alcanzado un valor mayor o igual a 100.

"""def pedir_lista():
    lista = []
    elemento = int(input("Por favor ingrese un numero o 0 para salir: "))
    while elemento != '0':
        lista += [elemento]
        elemento = input("Por favor ingrese un numero o 0 para salir: ")
    return lista

def main():
    sumatoria = 0
    numeros = pedir_lista()
    for i in range(len(numeros)):
        while (sumatoria <= 100):
            print("Numero a sumar: ", numeros[i])
            sumatoria += int(numeros[i])
            print("Sumatoria parcial: ", sumatoria)
    print("Sumatoria total: ", sumatoria)

main()"""

#7. Suponiendo que cuenta con una lista en la que en cada posición tiene la información de un alumno en un registro:
# [{'nombre': 'XX', 'legajo': 1, 'nota': 4, 'grupo': 1}, ...]
# Se desea imprimir el nombre y legajo de todos los alumnos aprobados.
# Asumiendo que la lista se encuentra ordenada por número de grupo, se pide indicar aquellos grupos para los cuales
# todos sus integrantes hayan aprobado el parcial recorriendo sólo una vez la lista.

"""def pedir_datos():
    datos = []
    nombre = input("Por favor ingrese el nombre del alumno o 0 para salir: ")
    while nombre != '0':
        legajo = int(input("Ingrese el legajo del alumno: "))
        nota = int(input("Ingrese la nota del alumno: "))
        grupo = int(input("Ingrese el grupo del alumno: "))
        datos += [{'Nombre': nombre, 'Legajo': legajo, 'Nota': nota, 'Grupo': grupo}]
        nombre = input("Por favor ingrese el nombre del alumno o 0 para salir: ")
    return datos

def alumnos_aprobados(datos):
    lista_aprobados = []
    print("Alumnos aprobados:")
    for i in range(len(datos)):
        if datos[i]['Nota'] >= 4:
            print("Nombre:", datos[i]['Nombre'], "y su legajo es:", datos[i]['Legajo'])
            
def main():
    datos = pedir_datos()
    alumnos_aprobados(datos)

main()"""

#####METODO DE INSERCION #####
#8. Se cuenta con dos listas de números ordenadas de forma creciente y se desea obtener una nueva lista ordenada que
# contenga todos los números, pero sin ordenarla nuevamente.

"""def pedir_lista():
    lista = []
    numero = int(input("Por favor ingrese un numero o 0 para salir: "))
    while numero != 0:
        lista += [numero]
        numero = int(input("Por favor ingrese un numero o 0 para salir: "))
    return sorted(lista)

def reubicar(lista, posicion):
    valor_a_reubicar = lista[posicion]
    j = posicion
    while (j > 0) and (valor_a_reubicar < lista[j - 1]):
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = valor_a_reubicar


def ordenar_por_insercion(lista):
    for i in range(len(lista) - 1):
        if lista[i+1] < lista[i]:
            reubicar(lista, i+1)
    return lista

def main():
    print("Lista uno: ")
    lista_uno = pedir_lista()
    print("Lista dos: ")
    lista_dos = pedir_lista()
    print("Lista uno:", lista_uno)
    print("Lista dos:", lista_dos)
    nueva_lista = ordenar_por_insercion(lista_uno + lista_dos)
    print("Lista uno + lista dos ordenadas:", nueva_lista)

main() """

#9. Procesar una lista de números y generar un diccionario con dos claves llamadas "par" e "impar". Al terminar de
# procesar la lista el diccionario debe tener todos los números que procesó agrupados en pares e impares.
# Por ejemplo, si contamos con la lista [1, 5, 2, 6, 9, 3, 8], el diccionario que se obtenga debería ser:
# {"par": [2, 6, 8], "impar": [1, 5, 9, 3]}

"""def pedir_lista():
    lista = []
    numero = int(input("Por favor ingrese un numero o 0 para salir: "))
    while numero != 0:
        lista += [numero]
        numero = int(input("Por favor ingrese un numero o 0 para salir: "))
    return lista

def main():
    diccionario = {'Pares': [], 'Impares': []}
    numeros = pedir_lista()
    for num in numeros:
        if (num % 2) == 0:
            diccionario['Pares'] += [num]
        else:
            diccionario['Impares'] += [num]
    print(diccionario)

main()"""

# 10. Procesar una lista de strings e ir guardando en un diccionario la cantidad de ocurrencias de cada palabra
# (distinguir mayúsculas y minúsculas).

"""def pedir_lista():
    lista = []
    elemento = input("Por favor ingrese un numero o 0 para salir: ")
    while elemento != '0':
        lista += [elemento]
        elemento = input("Por favor ingrese un numero o 0 para salir: ")
    return lista

def main():
    ocurrencias = {}
    strings = pedir_lista()
    for elementos in strings:
        if elementos in ocurrencias:
            ocurrencias[elementos] += 1
        else:
            ocurrencias[elementos] = 1
    print("Ocurrencias de las palabras: ", ocurrencias)

main()"""

# 11. Se tienen dos diccionarios, uno de precios de productos y otro de stock de productos. Ambos tienen las mismas
# claves. Se pide:
# a. acceder a los dos diccionarios simultáneamente calculando la multiplicación del precio por la cantidad de
# artículos para cada producto, e imprimir los casos en que dicho monto supere los $100.000.
# b. Calcular el monto total para el total del stock.

"""def pedir_datos():
    precios = {}
    stocks = {}
    productos = []
    producto = input("Ingrese el nombre del producto o 0 para salir:")
    while producto != '0':
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        precios[producto] = precio
        stocks[producto] = stock
        productos += [producto]
        producto = input("Ingrese el nombre del producto o 0 para salir:")
    return productos, precios, stocks

def main():
    productos, precios, stocks = pedir_datos()
    monto_total = 0
    for elem in productos:
        monto_total += (precios[elem] * stocks[elem])
        if ((precios[elem] * stocks[elem]) > 100000):
            print("El producto", elem, "con un stock de", stocks[elem], "supera los $100.000")
    print("Monto total para el total del stock:", monto_total)
    
main()"""

# 12. Se pide que ingresen por teclado pares de equipo – puntos ganados, el mismo par se puede ingresar varias veces.
# Se pide:
# a. generar una tabla de puntos acumulados para cada equipo.
# b. Mostrar la tabla de posiciones (equipo – total de puntos) ordenada por el total de puntos en forma descendente.

"""def pedir_datos():
    datos = []
    equipo = input("Ingrese el nombre del equipo o 0 para salir: ")
    while equipo != '0':
        puntos = int(input("Ingrese puntos ganados del equipo: "))
        datos += [[equipo, puntos]]
        equipo = input("Ingrese el nombre del equipo o 0 para salir: ")
    return datos

def tabla_puntos(datos):
    datos_finales = {}
    for i in range(len(datos)):
        if datos[i][0] in datos_finales.keys():
            datos_finales[datos[i][0]] += datos[i][1]
        else:
            datos_finales[datos[i][0]] = datos[i][1]
    print(datos_finales)
    return datos_finales

def main():
    datos = pedir_datos()
    tabla = tabla_puntos(datos)
    tabla_ordenada = sorted(tabla.items(), key=lambda x: x[1], reverse=True)
    print("Tabla ordenada por puntos, de forma descendente:")
    for elem in tabla_ordenada:
        print(elem)

main()"""

#13. Dada una lista de empleados, donde cada elemento es, a su vez, una lista que contiene: legajo, nombre, sexo,
# sueldo. Nota: un empleado puede tener más de un registro ya que puede cobrar adicionales. Se pide:
# a. Armar un diccionario con clave legajo y el resto de los datos como valor, unificando los datos:
# se deben sumar los sueldos para un mismo empleado.
# b. Listar legajo – nombre – sueldo, ordenado por legajo.
# c. Listar legajo – nombre – sueldo, ordenado por sueldo, de mayor a menor.
# d. Indicar el mayor sueldo y a quién corresponde.
# e. Indicar si el promedio de sueldos de las mujeres es menor que el promedio de sueldos de los hombres.

"""LEGAJO = 0
NOMBRE = 1
SUELDO = 2
SEXO = 3

def pedir_datos():
    #En cada posicion de la lista se guarda otra lista, que contiene datos en el siguiente orden:
    #Legajo(0) - Nombre(1) - Sueldo(2) - Sexo(3)
    datos = []
    legajo = int(input("Ingrese el legajo del empleado o 0 para salir: "))
    while legajo != 0:
        nombre = input("Ingrese el nombre del empleado: ")
        sexo = input("Ingrese el sexo del empleado (F/M): ")
        sueldo = int(input("Ingrese el sueldo del empleado: "))
        datos += [[legajo, nombre, sueldo, sexo]]
        legajo = int(input("Ingrese el legajo del empleado o 0 para salir: "))
    return datos

def armar_diccionario(datos):
    #Como claves los legajos, y luego una lista con Nombre(0) - Sueldo(1) - Sexo(2)
    datos_empleados = {}
    for i in range(len(datos)):
        if datos[i][LEGAJO] in datos_empleados.keys():
            datos_empleados[datos[i][LEGAJO]][SUELDO] += datos[i][SUELDO]
        else:
            datos_empleados[datos[i][LEGAJO]] = [datos[i][NOMBRE], datos[i][SUELDO], datos[i][SEXO]]
    return datos_empleados

def listar_por_legajo(diccionario):
    lista_por_legajo = []
    ordenado_por_legajo = sorted(diccionario.items())
    print("Por orden de legajos:")
    for claves,valores in ordenado_por_legajo:
        print("Legajo:", claves, "// Nombre:", valores[NOMBRE-1], "// Sueldo:", valores[SUELDO-1])
        lista_por_legajo += [[claves, valores[NOMBRE-1], valores[SUELDO-1]]]
    return lista_por_legajo

def listar_por_sueldo(diccionario):
    lista_por_sueldo = []
    ordenado_por_sueldo = sorted(diccionario.items(), key=lambda x: x[1][1], reverse=True)
    print("Por orden de mayor sueldo:")
    for claves,valores in ordenado_por_sueldo:
        print("Legajo:", claves, "// Nombre:", valores[NOMBRE-1], "// Sueldo:", valores[SUELDO-1])
        lista_por_sueldo += [[claves, valores[NOMBRE-1], valores[SUELDO-1]]]
    return lista_por_sueldo

def promedio_sueldo_por_sexo(diccionario):
    cantidad_mujeres = 0
    cantidad_hombres = 0
    sueldos_mujeres = 0
    sueldos_hombres = 0
    for valores in diccionario.values():
        if valores[SEXO-1] == 'F':
            cantidad_mujeres += 1
            sueldos_mujeres += valores[SUELDO-1]
        else:
            cantidad_hombres += 1
            sueldos_hombres += valores[SUELDO-1]
    if (sueldos_mujeres // cantidad_mujeres) > (sueldos_hombres // cantidad_hombres):
        print("El promedio de sueldo de las mujeres es mas alto que el de hombres.")
    else:
        print("El promedio de sueldo de los hombres es mas alto.")


def main():
    lista_datos = pedir_datos()
    diccionario_datos = armar_diccionario(lista_datos)
    listado_por_legajo = listar_por_legajo(diccionario_datos)
    listado_por_sueldo = listar_por_sueldo(diccionario_datos)
    print("El mayor sueldo es de", listado_por_sueldo[0][SUELDO], "y corresponde a", listado_por_sueldo[0][NOMBRE])
    promedio_sueldo_por_sexo(diccionario_datos)

main()"""
