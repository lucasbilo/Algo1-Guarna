# Escribir un programa modular que permita:
# 1) El ingreso de una secuencia de valores, que termine en 0.
# 2) Mostrar lo ingresado con la posicion en la cual fue ingresado
# 3) Listar los valores hasta el tercer valor impar.
# 4) Listar los valores que estan en la posiciones pares
# 5) Listar de menor a mayor, sin repetirlos.

def generar_lista():
    lista = []
    elemento = int(input("Por favor ingrese un valor: "))
    while (elemento != 0):
        lista.append(elemento)
        elemento = int(input("Por favor ingrese un valor o 0 para salir: "))
    return lista

def mostrar_todos(lista):
    for orden, elemento in enumerate(lista):
        print("En la posicion", orden + 1, "se ingreso", elemento)

def mostrar_hasta_tercer_impar(lista):
    cant_impar = 0
    posicion = 0
    print("Lista hasta el tercer impar (si es que lo hay): ")
    while ((cant_impar < 3) and (posicion < len(lista))):
        print(lista[posicion])
        if (lista[posicion] % 2 == 1):
            cant_impar += 1
        posicion += 1

def mostrar_posiciones_pares(lista):
    print("Lo ingresado en las posiciones pares son: ")
    for posicion in range(1, len(lista), 2):
        print(lista[posicion])

def mostrar_menor_a_mayor(lista):
    lista.sort()
    lista_nueva = []
    for elem in lista:
        if elem not in lista_nueva:
            lista_nueva.append(elem)
    print("Lista de menor a mayor, sin repetir: ", lista_nueva)

def main():
    lista = generar_lista()
    mostrar_todos(lista)
    mostrar_hasta_tercer_impar(lista)
    mostrar_posiciones_pares(lista)
    mostrar_menor_a_mayor(lista)

main()