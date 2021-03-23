# 1. Desarrollar una función que devuelva en un vector (una lista) los números primos
# entre 2 y 200. Reutilizar lo que ya se escribió y probó.

"""def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if (numero % i) == 0:
            contador += 1
    if contador == 2:
        return True
    return False

def main():
    primos_2_al_200 = []
    for i in range(2, 201):
        primo = es_primo(i)
        if primo == True:
            primos_2_al_200.append(i)
    print("Lista de numeros primos del 2 al 200: ", primos_2_al_200)

main()"""

# 2. Dados dos vectores A y B, de N elementos cada uno, se desean calcular:
# a. el vector suma.
# b. el producto escalar.

"""def pedir_numeros(cantidad_max):
    lista_numeros = []
    while cantidad_max != 0:
        numero = int(input("Por favor ingrese un numero: "))
        lista_numeros += [numero]
        cantidad_max -= 1
    return lista_numeros

def sumar_listas(a, b, cantidad_max):
    vector_suma = []
    for i in range(len(a)):
        vector_suma.append(a[i] + b[i])
    return vector_suma

def producto_escalar_listas(a, b):
    vector_producto = []
    for i in range(len(b)):
        vector_producto.append(a[i] * b[i])
    return vector_producto

def main():
    cantidad_elementos = int(input("Ingrese la cantidad de elementos que tendran los vectores: "))
    print("Ingrese el primer vector: ")
    vector_a = pedir_numeros(cantidad_elementos)
    print("El primer vector es: ", vector_a)
    print("Ingrese el segundo vector: ")
    vector_b = pedir_numeros(cantidad_elementos)
    print("El segundo vector es: ", vector_b)
    suma = sumar_listas(vector_a, vector_b)
    producto = producto_escalar_listas(vector_a, vector_b)
    print("El vector suma es: ", suma)
    print("El producto escalar es: ", producto)

main() """

# 3. Por cada alumno que rindió un examen de una materia se lee el número de legajo  y la nota obtenida. Se desea saber
# la cantidad de alumnos que rindieron el  examen, el porcentaje de alumnos que obtuvieron cada nota, y el (o los)
# legajos de la nota más alta.

"""def pedir_datos():
    datos = []
    seguir = 's'
    while seguir == 's':
        legajo = int(input("Ingrese numero de legajo: "))
        nota = float(input("Ingrese nota: "))
        datos += [[legajo, nota]]
        seguir = input("Desea seguir ingresando? (s/n): ")
    return datos

def nota_mas_alta(datos):
    nota_mas_alta = 0
    alumnos = []
    for i in range(len(datos)):
        if nota_mas_alta <= datos[i][1]:
            nota_mas_alta = datos[i][1]
            alumnos.append(datos[i][0])
    print("Nota mas alta: ", nota_mas_alta)
    print("Legajos de alumnos con dicha nota: ", alumnos)


def main():
    datos = pedir_datos()
    print("Cantidad de alumnos que rindieron el examen:", len(datos))
    nota_mas_alta(datos)

main()"""

# 4. Escribir una función que reciba una lista y un valor y devuelva verdadero (True)
#si el valor está en la lista, falso (False) en caso contrario. Hacerlo sin usar in ni count.

"""def valor_en_lista(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return True
    return False

def main():
    cantidad_max = int(input("Cantidad max; "))
    lista_numeros = []
    while cantidad_max != 0:
        numero = int(input("Por favor ingrese un numero: "))
        lista_numeros += [numero]
        cantidad_max = cantidad_max - 1
    valor = int(input("Ingrese el valor: "))
    valor_en_lista(lista_numeros, valor)
    
main()"""

# 5. Escribir la misma función del punto anterior usando count.

"""def valor_en_lista(lista, valor):
    contador = lista.count(valor)
    if contador != 0:
        return True
    else:
        return False"""

# 6. Escribir la misma función del punto anterior usando in.

"""def valor_en_lista(lista, valor):
    if valor in lista:
        return True
    else:
        return False"""

# 7. Escribir una función que reciba una lista y un valor y devuelva la posición en que
#encuentra al valor en la lista, si el valor estuviera repetido devolver la primera
#aparición, si no estuviera devolver –1. Escribirla sin utilizar funciones como in, count, index, etc.

"""def posicion_valor_en_lista(lista, valor):
    for pos in range(len(lista)):
        if lista[pos] == valor:
            return pos + 1
    return -1

def main():
    cantidad_max = int(input("Cantidad max: "))
    lista_numeros = []
    while cantidad_max != 0:
        numero = int(input("Por favor ingrese un numero: "))
        lista_numeros.append(numero)
        cantidad_max -= 1
    valor = int(input("Ingrese el valor: "))
    posicion = posicion_valor_en_lista(lista_numeros, valor)
    print(posicion)

main()"""

#8. Escribir la misma función del punto anterior usando funciones específicas de Python.

"""def main():
    seguir = 's'
    lista_numeros = []
    while seguir == 's':
        numero = int(input("Por favor ingrese un numero: "))
        lista_numeros.append(numero)
        seguir = input("Desea seguir ingresando numeros a la lista? (s/n): ")
    valor = int(input("Ingrese el valor: "))
    print("La posicion en la lista del valor ingresado es:", lista_numeros.index(valor) + 1)

main()"""

# 9. Se lee un vector X de N elementos (enteros). Escribir un algoritmo que devuelva
# un vector que tenga todos los elementos de X, pero sin elementos repetidos.

"""def pedir_numeros(cantidad_max):
    lista_numeros = []
    while len(lista_numeros) < cantidad_max:
        numero = int(input("Por favor ingrese un numero: "))
        lista_numeros.append(numero)
    return lista_numeros

def lista_sin_repetir(lista):
    lista_nueva = []
    for elem in lista:
        if not(elem in lista_nueva):
            lista_nueva.append(elem)
    return lista_nueva

def main():
    cantidad_elementos = int(input("Ingrese la cantidad de elementos que tendra el vector: "))
    lista_x = pedir_numeros(cantidad_elementos)
    lista_nueva = lista_sin_repetir(lista_x)
    print("Lista nueva sin repetir elementos: ", lista_nueva)

main()"""

# 11. Si los números de un vector representan los coeficientes de un polinomio (de grado no mayor a 10), escribir un
# algoritmo que calcule la especialización de ese polinomio con un número que elige el usuario.

"""def pedir_coeficientes():
    coeficientes = []
    coeficiente = int(input("Por favor ingrese el primer coeficiente del polinomio (menor a mayor) o 0 para salir: "))
    while (len(coeficientes) < 10) and (coeficiente != 0):
        coeficientes += [coeficiente]
        coeficiente = int(input("Por favor ingrese el coeficiente del polinomio (menor a mayor) o 0 para salir: "))
    return coeficientes

def calcular_especializacion(coeficientes, numero):
    especializacion = 0
    for x in range(len(coeficientes)):
        especializacion += (coeficientes[x] * (numero ** (x + 1)))
    return especializacion


def main():
    coeficientes = pedir_coeficientes()
    numero = int(input("Por favor ingrese el numero para calcular la especializacion del polinomio: "))
    especializacion = calcular_especializacion(coeficientes, numero)
    print("La especializacion del numero ", numero, "en el polinomio es de ", especializacion)

main()"""

# 12. Escribir un algoritmo que halle una matriz C como suma de dos matrices A y B.
# La dimensión de las matrices de M × N se lee como dato (suponer un MAX para fila y columna).

"""def pedir_dimension():
    dimension = int(input("Por favor ingrese la dimension (max 5): "))
    while (dimension > 5) or (dimension < 0):
        dimension = int(input("Por favor ingrese la dimension (max 5): "))
    return dimension

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            print("Por favor ingrese el numero correspondiente a la fila", i+1, "y columna", j+1)
            numero = int(input(""))
            matriz[i].append(numero)
    return matriz

def sumar_matrices(matriz_a, matriz_b):
    matriz_suma = matriz_a
    for x in range(len(matriz_a)):
        for y in range(len(matriz_a[x])):
            matriz_suma[x][y] += matriz_b[x][y]
    return matriz_suma

def imprimir_matriz(matriz):
    for elem in matriz:
        print(elem)

def main():
    print("Filas")
    filas = pedir_dimension()
    print("Columnas")
    columnas = pedir_dimension()
    print("Datos de la matriz A")
    matriz_a = crear_matriz(filas, columnas)
    print("Datos de la matriz B")
    matriz_b = crear_matriz(filas, columnas)
    print("Matriz A: ")
    imprimir_matriz(matriz_a)
    print("Matriz B: ")
    imprimir_matriz(matriz_b)
    matriz_c = sumar_matrices(matriz_a, matriz_b)
    print("Matriz C: ")
    imprimir_matriz(matriz_c)

main()"""

#13. Escribir un algoritmo que halle un vector cuyos elementos son la suma de los
# elementos de cada fila de una matriz previamente ingresada.

"""def pedir_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            print("Fila", i+1, "y columna", j+1)
            numero = int(input("Ingrese numero para dicha columna y fila: "))
            matriz[i].append(numero)
    return matriz

def main():
    filas = int(input("Ingrese dimension de filas que tendra la matriz: "))
    columnas = int(input("Ingrese dimension de columnas que tendra la matriz: "))
    matriz = pedir_matriz(filas, columnas)
    vector = []
    for i in range(filas):
        suma = 0
        for j in range(columnas):
            suma += matriz[i][j]
        vector.append(suma)
    print(vector)

main()"""

#14. Escribir un programa que calcule la traza de una matriz cuadrada. Recordar que
# la traza de una matriz es la suma de los elementos de su diagonal principal.

"""def traza_matriz(matriz):
    traza = 0
    for i in range(len(matriz)):
            traza += matriz[i][i]
    print("Traza: ", traza)

def crear_matriz_cuadrada(dimension):
    matriz = []
    for i in range(dimension):
        matriz.append([])
        for j in range(dimension):
            print("Fila", i+1, "y columna", j+1)
            numero = int(input("Ingrese numero para dicha columna y fila: "))
            matriz[i].append(numero)
    return matriz

def main():
    dimension = int(input("Por favor ingrese la dimension de la matriz(cuadrada): "))
    matriz = crear_matriz_cuadrada(dimension)
    traza_matriz(matriz)

main()"""

# 16. Escribir un algoritmo que construya un vector con los valores mínimos de cada una de las filas de una matriz.

"""def pedir_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            print("Fila", i+1, "y columna", j+1,)
            numero = int(input("Ingrese numero para dicha columna y fila: "))
            matriz[i].append(numero)
    return matriz

def construir_vector(matriz):
    vector = []
    for i in range(len(matriz)):
        vector.append(min(matriz[i]))
    print(vector)

def main():
    filas = int(input("Ingrese dimension de filas que tendra la matriz: "))
    columnas = int(input("Ingrese dimension de columnas que tendra la matriz: "))
    matriz = pedir_matriz(filas, columnas)
    construir_vector(matriz)

main()"""

# 17. Definir una función que dada una fecha en formato DD/MM/AA, verifique si es correcta o errónea.
# Ejemplo: El 31/02/18 es una fecha errónea. Investigar cómo se calcula si un año es bisiesto o no.

"""def cantidad_maxima_por_mes(mes, anio):
    if mes in (4, 6, 9, 11):
        return 30
    elif mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes == 2:
        if (anio % 4) == 0:
            if (anio % 100 != 0) or (anio % 100 == 0 and anio % 400 == 0):
                return 29
            else:
                return 28
        else:
            return 28

def verificar_fecha(dia, mes, anio):
    cantidad_max_dias_por_mes = cantidad_maxima_por_mes(mes, anio)
    if (dia < 0) or (dia > cantidad_max_dias_por_mes) or (mes < 0) or (mes > 12):
        print("La fecha ingresada es incorrecta.")
    else:
        print("La fecha ingresada es correcta.")

def main():
    dia = int(input("Ingrese dia: "))
    mes = int(input("Ingrese mes: "))
    anio = int(input("Ingrese anio: "))
    verificar_fecha(dia, mes, anio)

main()"""

#19. Escribir una función que ordene alfabéticamente una lista de N nombres.
# Escribirlo sin utilizar sort ni sorted.

"""def ordenar_nombres(nombres):
    nombres_ordenados = []
    

def main():
    nombres = []
    nombre = input("Ingrese un nombre o 0 para salir: ")
    while nombre != 0:
        nombres += nombre
        nombre = input("Ingrese un nombre o 0 para salir: ")
    print("Lista de nombres: ", nombres)
    ordenar_nombres(nombres)
main() """

# 20. Hacer el mismo punto anterior usando la función sorted.

"""def pedir_nombres():
    nombres = []
    nombre = input("Ingrese un nombre o 0 para salir: ")
    while nombre != '0':
        nombres += [nombre]
        nombre = input("Ingrese un nombre o 0 para salir: ")
    return nombres"""

"""def main():
    nombres = pedir_nombres()
    print("Lista de nombres: ", nombres)
    nombres_ordenados = sorted(nombres)
    print("Lista de nombres ordenados alfabeticamente: ", nombres_ordenados)

main()"""

# 21. Hacer el mismo punto anterior usando el método sort.

"""def main():
    nombres = pedir_nombres()
    print("Lista de nombres: ", nombres)
    nombres.sort()
    print("Lista de nombres ordenados alfabeticamente: ", nombres)

main()"""

#22. Escribir una función que, dado dos vectores (uno contiene nombres y el otro número de legajos), ordene el primero
# y el segundo en paralelo. ¿Se puede utilizar sort o sorted en este ejercicio?

"""def pedir_nombres():
    nombres = []
    nombre = input("Ingrese un nombre o 0 para salir: ")
    while nombre != '0':
        nombres += [nombre]
        nombre = input("Ingrese un nombre o 0 para salir: ")
    return nombres

def pedir_legajos():
    legajos = []
    numero = int(input("Ingrese un nombre o 0 para salir: "))
    while numero != 0:
        legajos += [numero]
        numero = input("Ingrese un nombre o 0 para salir: ")
    return legajos

def ordenar_vectores(vector):


def main():
    nombres = pedir_nombres()
    legajos = pedir_legajos()
    ordenar_vectores()

main()"""
