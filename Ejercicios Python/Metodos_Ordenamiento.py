def pedir_vector():
    vector = []
    seguir = 's'
    while seguir == 's':
        numero = int(input("Ingrese un numero: "))
        vector.append(numero)
        seguir = input("Desea seguir? (s/n): ")
    return vector

#SELECCION
"""def intercambiar(vec, i, j):
    aux = vec[i]
    vec[i] = vec[j]
    vec[j] = aux

def calcular_minimo(vector, i):
    minimo = i
    for j in range(i + 1, len(vector)):
        if (vector[j] < vector[minimo]):
            minimo = j
    return minimo

def seleccion(vector):
    for i in range(len(vector) - 1):
        minimo = calcular_minimo(vector, i)
        intercambiar(vector, i, minimo)
    print(vector)"""

#BURBUJEO
"""def intercambiar(vec, i, j):
    aux = vec[i]
    vec[i] = vec[j]
    vec[j] = aux

def burbujeo(vector):
    for i in range(len(vector) - 1, 0,  -1):
        for j in range(i):
            if (vector[j] > vector[j + 1]):
                intercambiar(vector, j, j + 1)
    print(vector)"""

#INSERCION
"""def corrimiento(vector, i, clave):
    while (i >= 0) and (vector[i] > clave):
        vector[i + 1] = vector[i]
        i -= 1
    return i

def insercion(vector):
    for j in range(1, len(vector)):
        clave = vector[j]
        i = corrimiento(vector, j - 1, clave)
        vector[i + 1] = clave
    print(vector)"""


