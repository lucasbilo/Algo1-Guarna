# 1. Hacer una función que, dado los coeficientes de un polinomio de segundo grado
# (3 números reales), indique si tiene o no raíces reales (devuelve verdadero o falso).

"""def tiene_raices_reales(a, b , c):
    num_adentro_raiz = ((b ** 2) - (4 * a * c))
    if num_adentro_raiz >= 0:
        return True
    else:
        return False """

"""x = int(input("Ingrese numero cuadratico: "))
y = int(input("Ingrese numero lineal: "))
z = int(input("Ingrese numero independiente: "))

tiene_raices_reales(x, y, z) """

# 2. Hacer una función que invocada como expo(x,n) devuelva el valor de x a la n,
# donde x es un número real y n entero (puede ser negativo). Resolverla con
# multiplicaciones sucesivas.

"""def expo(numero, potencia):
    resultado = 1
    if potencia > 0:
        for i in range (1, potencia + 1):
            resultado *= numero
    elif potencia < 0:
        for i in range(1, 1 - potencia):
            resultado *= (1 / numero)
    else:
        resultado = 0
    return print(resultado) """

"""x = int(input("Ingrese numero a elevar: "))
n = int(input("Ingrese potencia: "))

expo(x, n) """

#3. Hacer una función que devuelva las raíces reales de un polinomio de segundo
# grado y, además, indique si tiene o no raíces reales (una booleana).

"""def raices_polinomio_segundo_grado(a, b , c):
    if tiene_raices_reales(x, y, z) == True:
        raiz_uno = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        raiz_dos = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        print("Las raices son: ", raiz_dos, raiz_uno)
    else:
        print("No tiene raices reales!") """

"""x = int(input("Ingrese numero cuadratico: "))
y = int(input("Ingrese numero lineal: "))
z = int(input("Ingrese numero independiente: "))

raices_polinomio_segundo_grado(x, y, z)"""

# 4. Hacer una función que indique si un número grande es primo o no. Utilizar lo
# realizado en el ejercicio 8 de la práctica anterior.

"""def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if (numero % i) == 0:
            contador += 1
    if contador == 2:
        print("El numero es primo")
    else:
        print("El numero no es primo")"""

# 5. Hacer un programa que liste todos los números primos desde 2 hasta un número
# ingresado por el usuario utilizando la función realizada en el ejercicio anterior.

"""def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if (numero % i) == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False

def main():
    numero = int(input("Ingrese un numero: "))
    print("Numeros primos desde 2 al", numero, ":")
    for i in range(2, numero + 1):
        primo = es_primo(i)
        if primo == True:
            print(i) 
            
main()"""

#6. Escribir un programa, utilizando funciones, que descomponga un número en sus
#factores primos. Agregale comentarios al programa donde lo creas necesario.

"""def descomponer_en_factores_primos(numero):
    x = int(2)
    while numero != 1:
        if (numero % x == 0):
            print("Factor primo: ", x)
            numero = (numero // x )
        else:
            x += 1

numero_a_descomponer = int(input("Ingrese numero a descomponer: "))
descomponer_en_factores_primos(numero_a_descomponer) """

# 7. Realizar un algoritmo que lea una serie de números reales y verifique si están
# ordenados en forma ascendente, descendente o si no están ordenados,
# informando por pantalla.

"""def pedir_numeros():
    lista_numeros = []
    numero = int(input("Por favor ingrese un numero o 0 para salir: "))
    while numero != 0:
        lista_numeros += [numero]
        numero = int(input("Por favor ingrese un numero o 0 para salir: "))
    return lista_numeros

def verificar_orden(lista_numeros):
    if (lista_numeros == sorted(lista_numeros)):
        print("La lista es ascendente")
    elif (lista_numeros == sorted(lista_numeros, reverse = True)):
        print("La lista es descendente")
    else:
        print("Estan desordenados")

def main():
    lista_numeros = pedir_numeros()
    verificar_orden(lista_numeros)

main()"""

# 8. Dada una serie de datos de la forma mes (1 a 12, no vienen ordenados), cantidad
# recaudada (en pesos) y costo total (en pesos), hacer un algoritmo que calcule e
# imprima cuál fue el mes que arrojó mayor ganancia. La serie termina con mes
# igual a cero. No se deben guardar los datos.

"""def calcular_mejor_mes(mes, recaudado, costo_final):
    mes_mayor_ganancia = 0
    recaudado_mejor_mes = 0
    costo_mejor_mes = 0
    if ((recaudado - costo_final) > (recaudado_mejor_mes - costo_mejor_mes)):
        mes_mayor_ganancia = mes
        recaudado_mejor_mes = recaudado
        costo_mejor_mes = costo_final
    return mes_mayor_ganancia

def mostrar_datos_a_pedir():
    mes = int(input("Ingrese el numero del mes o 0 para salir: "))
    recaudado = int(input("Ingrese las ganancias recaudadas en el mes: "))
    costo_final = int(input("Ingrese el costo total en el mes: "))
    return mes, recaudado, costo_final

def menu_principal():
    mejor_mes = 0
    mes = int(input("Ingrese el numero del mes o 0 para salir: "))
    while mes != 0:
        recaudado = int(input("Ingrese las ganancias recaudadas en el mes: "))
        costo_final = int(input("Ingrese el costo total en el mes: "))
        mejor_mes = calcular_mejor_mes(mes, recaudado, costo_final)
        mes = int(input("Ingrese el numero del mes o 0 para salir: "))
    print("El mejor mes fue: ", mejor_mes)
menu_principal() """

#9. Se leen 300 datos (usar constantes para poder achicar esta cantidad) que
#representan el peso de la misma cantidad de niños que hay internados en un
#hospital. Se desea confeccionar la siguiente tabla:
#- Entre 0,000 y 10,000 kg. hay ............... niños.
#- Entre 10,001 y 20,000 kg. hay ............. niños.
#- Entre 20,001 y 30,000 kg. hay ............. niños.
#- Más de 30,000 kg. hay .................... niños.

"""def pedir_datos(cantidad_ninios):
    ninios_entre_0_y_10 = 0
    ninios_entre_10_y_20 = 0
    ninios_entre_20_y_30 = 0
    ninios_mas_30 = 0
    while cantidad_ninios != 0:
        peso_por_ninio = int(input("Ingrese el peso del ninio: "))
        if 0 <= peso_por_ninio <= 10:
            ninios_entre_0_y_10 += 1
        elif 10 < peso_por_ninio <= 20:
            ninios_entre_10_y_20 += 1
        elif 20 < peso_por_ninio < 30:
            ninios_entre_20_y_30 += 1
        else:
            ninios_mas_30 += 1
        cantidad_ninios -= 1
    print("Entre 0,000 y 10,000 kg. hay ", ninios_entre_0_y_10, "ninios.")
    print("Entre 10,001 y 20,000 kg. hay ", ninios_entre_10_y_20, "ninios.")
    print("Entre 20,001 y 30,000 kg. hay ", ninios_entre_20_y_30, "ninios.")
    print("Mas de 30,000 kg. hay ", ninios_mas_30, "ninios.")

def main():
    cantidad_de_ninios = int(input("Ingrese la cantidad de ninios: "))
    pedir_datos(cantidad_de_ninios)

main() """

# 11. Contar la cantidad de letras de un telegrama que termina en punto sin utilizar
# funciones de string, salvo la que indica la longitud

"""def cantidad_letras(texto):
    cantidad = 0
    for letra in texto:
        if letra in "abcdefghijklmnopqerstuvwxyzABCDEFGHIJKLMNOPGERSTUVWXYZ":
            cantidad += 1
    return cantidad

def main():
    texto = input("Ingrese texto: ")
    cantidad = cantidad_letras(texto)
    print("Cantidad de letras del texto ingresado:", cantidad)

main()"""

#13. Dado un texto terminado en punto, determinar cuál es la vocal que aparece con mayor frecuencia.

"""def calcular_vocal_mas_aparece(a, e, i, o, u):
    if max(a, e, i, o, u) == a:
        print("La vocal que mas aparece es la A")
    elif max(a, e, i, o, u) == e:
        print("La vocal que mas aparece es la E")
    elif max(a, e, i, o, u) == i:
        print("La vocal que mas aparece es la I")
    elif max(a, e, i, o, u) == o:
        print("La vocal que mas aparece es la O")
    else:
        print("La vocal que mas aparece es la U")


def convertir_vocales(texto):
    todo_mayuscula = texto.upper()
    vocal_a = todo_mayuscula.count('A')
    vocal_e = todo_mayuscula.count('E')
    vocal_i = todo_mayuscula.count('I')
    vocal_o = todo_mayuscula.count('O')
    vocal_u = todo_mayuscula.count('U')
    calcular_vocal_mas_aparece(vocal_a, vocal_e, vocal_i, vocal_o, vocal_u)

def main():
    texto = input("Por favor ingrese el texto: ")
    convertir_vocales(texto)
main()"""

# 14. Dado un texto terminado en “.” se pide determinar cuántas veces aparece
# determinada letra que se indica por teclado. Sin utilizar funciones de string, salvo len.

"""def cantidad_aparicion_letra(texto, letra):
    cantidad = 0
    for letras in texto:
        if letras == letra:
            cantidad += 1
    return cantidad

def main():
    texto = input("Ingrese el texto: ")
    letra = input("Ingrese letra: ")
    cantidad = cantidad_aparicion_letra(texto, letra)
    print("La letra", letra, "aparece", cantidad, "de veces en el texto.")

main()"""

# 15. Dado un texto terminado en “.” averiguar qué cantidad de letras tiene la palabra más larga.

"""def palabra_mas_larga(texto):
    cantidad_letras = 0
    palabras = texto.split()
    for palabra in palabras:
        if len(palabra) > cantidad_letras:
            cantidad_letras = len(palabra)
    return cantidad_letras

def main():
    texto = input("Ingrese texto: ")
    cantidad = palabra_mas_larga(texto)
    print("La palabra mas larga tiene", cantidad, "letras.")

main()"""

# 16. Leer dos letras de teclado y luego un texto terminado en “.”. Se pide determinar la cantidad de veces que la
# primera letra precede a la segunda en el texto. No utilizar funciones de string salvo la que indica la longitud.

"""def primera_precede_segunda(a, b, texto):
    cantidad = 0
    letra_anterior = ''
    for letras in texto:
        if (letras == b) and (letra_anterior == a):
            cantidad += 1
        letra_anterior = letras
    return cantidad

def main():
    letra_uno = input("Ingrese primer letra: ")
    letra_dos = input("Ingrese segunda letra: ")
    texto = input("Ingrese texto: ")
    cantidad = primera_precede_segunda(letra_uno, letra_dos, texto)
    print("En el texto la letra", letra_uno, "precede a la letra", letra_dos, "una cantidad de", cantidad, "veces.")

main()"""

# 18. Escribir un algoritmo que lea un número real cualquiera y lo redondee con dos
# decimales. Verificar con distintas entradas.

"""def redondear_dos_decimales(numero):
    print("{: < 4.2f}".format(numero))

def main():
    numero = float(input("Por favor ingrese el numero a redondear: "))
    redondear_dos_decimales(numero)

main()"""

# 19. Hacer una función que devuelva el máximo común divisor y el mínimo común múltiplo entre dos enteros.

"""import math
def mcm(num1, num2):
    menor = min(num1, num2)
    for i in range(1, menor):
        if ((num1 % i == 0) and (num2 % i == 0)):
            mcd = i
            mcm = (num1 * num2) // mcd
    return mcm, mcd

def main():
    numero_uno = int(input("Ingrese un numero entero: "))
    numero_dos = int(input("Ingrese un numero entero: "))
    mcm, mcd = mcm(numero_uno, numero_dos)
    print("El maximo comun divisor entre ", numero_uno, "y ", numero_dos, "es de ", mcd)
    print("El minimo comun multiplo entre ", numero_uno, "y ", numero_dos, "es de ", mcm)

main()"""

# 20. Escribir un programa principal, con un menú de opciones, para que invoque a las funciones de los puntos 3, 4 y 19.
# Escribir en el programa del punto anterior comentarios al principio de cada función indicando qué es lo que hace,
# qué recibe y qué devuelve. Agregar comentarios en el programa principal.
# Verificar que los nombres de las variables y las funciones sean correctos.

"""RAICES = 1
ES_PRIMO = 2
MCD_MCM = 3

def mostrar_menu():
    print("1- Función que devuelva las raíces reales de un polinomio de segundo grado.")
    print("2- Función que indique si un número grande es primo o no.")
    print("3- Función que devuelva el máximo común divisor y el mínimo común múltiplo entre dos enteros.")
    print("4- Salir.")

def main():
    mostrar_menu()
    opcion = input("Por favor ingrese una opcion: ")
    if opcion == RAICES:
        x = int(input("Ingrese numero cuadratico: "))
        y = int(input("Ingrese numero lineal: "))
        z = int(input("Ingrese numero independiente: "))
        raices_polinomio_segundo_grado(x, y, z)
    elif opcion == ES_PRIMO:
        numero = int(input("Ingrese numero para ver si es primo o no: "))
        es_primo(numero)
    elif opcion == MCD_MCM:
        numero_uno = int(input("Ingrese un numero entero: "))
        numero_dos = int(input("Ingrese un numero entero: "))
        mcm, mcd = mcm(numero_uno, numero_dos)

main()"""


