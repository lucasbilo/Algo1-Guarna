#1. Solicitar al usuario el ingreso de un texto. A continuación:
#a. Mostrar el texto, pero ordenado por palabra y todo en mayusculas.
#b. Informar cuantos caracteres tiene la palabra más larga.
#c. Generar una nueva lista sin palabras repetidas.
#d. Armar un ranking de palabras, informando palabra y cantidad de ocurrencias, ordenado por la cantidad de ocurrencias.

"""def texto_ordenado_todo_mayusculas(palabras):
    palabras_mayuscula = []
    for palabra in palabras:
        palabras_mayuscula.append(palabra.upper())
    palabras_mayuscula.sort()
    texto_ordenado = ''
    for palabras in palabras_mayuscula:
        texto_ordenado += palabras + ' '
    print(texto_ordenado)

def palabra_mas_larga(palabras):
    mayor_cantidad_caracteres = 0
    for palabra in palabras:
        if len(palabra) > mayor_cantidad_caracteres:
            mayor_cantidad_caracteres = len(palabra)
    print("La palabra mas larga tiene", mayor_cantidad_caracteres, "de caracteres.")

def palabras_sin_repetir(palabras):
    palabras_sin_repetir = []
    for palabra in palabras:
        if palabra.lower() not in palabras_sin_repetir:
            palabras_sin_repetir.append(palabra.lower())
    print("Lista de palabras (sin repetir):", palabras_sin_repetir)

def ranking_ocurrencias(palabras):
    ranking = {}
    for palabra in palabras:
        if palabra.lower() in ranking:
            ranking[palabra.lower()] += 1
        else:
            ranking[palabra.lower()] = 1
    print("Ranking de las ocurrencias de las palabras:", sorted(ranking.items(), key=lambda x: x[1], reverse=True))

def main():
    texto = input("Ingrese un texto: ")
    palabras = texto.split()
    texto_ordenado_todo_mayusculas(palabras)
    palabra_mas_larga(palabras)
    palabras_sin_repetir(palabras)
    ranking_ocurrencias(palabras)

main()"""

#2. Escribir una función que, dado un texto que se pasa por parámetro, lo imprima al revés y sin ninguna vocal.
# Las vocales pueden estar en minúsculas o mayúsculas.

"""def imprimir_texto_invertido(texto):
    texto_cambiado = ''
    for caracter in texto:
        if caracter not in "AEIOUaeiou":
            texto_cambiado += caracter
    print(texto_cambiado[::-1])"""

#3. Solicitar al usuario el ingreso de un texto. El mismo debe contener al menos 100 palabras, de lo contrario deberá
# exigirle que ingrese más palabras y adicionarlas a las ya ingresadas hasta superar el mínimo establecido. Considere
# que el usuario solo ingresa palabras separadas por blancos sin ningún otro tipo de caracteres.
# Muestre una lista de las palabras ingresadas, ordenada alfabéticamente, sin repetir palabras.

"""def solicitar_texto():
    texto = input("Por favor ingrese el texto: ")
    while (len(texto.split()) < 100):
        texto += '' + input("Texto demasiado corto, siga ingresando: ")
    return texto

def palabras_sin_repetir(palabras):
    palabras.sort()
    palabra_anterior = ''
    for palabra in palabras:
        if palabra != palabra_anterior:
            print(palabra)
            palabra_anterior = palabra


def main():
    texto = solicitar_texto()
    palabras_sin_repetir(texto.split())

main()"""

#4. Ingresar, en un diccionario, pares de datos con una clave que será el nombre de un partido político y un valor que
# será la cantidad de votos obtenidos en una provincia, una misma clave se puede ingresar varias veces. Se pide:
# a. Calcular el total de votos para cada partido e imprimirlo sin ningún orden.
# b. Imprimir el listado anterior ordenado de mayor a menor por cantidad de votos.

"""def pedir_datos():
    datos = {}
    partido = input("Ingrese el nombre del partido o 0 para salir: ")
    while partido != '0':
        votos = int(input("Ingrese cantidad de votos:"))
        if partido in datos:
            datos[partido] += votos
        else:
            datos[partido] = votos
        partido = input("Ingrese el nombre del partido o 0 para salir: ")
    return datos

def main():
    datos = pedir_datos()
    print("Votos sin orden:")
    for partidos in datos:
        print("Partido:", partidos, "|| Votos:", datos[partidos])
    print("Votos ordenados de mayor a menor:")
    votos_ordenados = sorted(datos.items(), key=lambda x: x[1], reverse=True)
    for partidos in votos_ordenados:
        print("Partido:", partidos[0], "|| Votos:", partidos[1])

main()"""


# 5. Escribir una función que, dado un texto que se pasa por parámetro, lo devuelva
# cambiando la letra “m” por “eme”, y “M” por “EME”.

"""def cambiar_letra_m(texto):
    texto_cambiado = ''
    for caracter in texto:
        if caracter == 'm':
            texto_cambiado += 'eme'
        elif caracter == 'M':
            texto_cambiado += 'EME'
        else:
            texto_cambiado += caracter
    return texto_cambiado"""

# 6. Solicitar al usuario el ingreso de un texto. Considerar que el usuario solo ingresa palabras separadas por blancos,
# sin ningún otro tipo de caracteres. Mostrar una lista de las palabras capicúas ingresadas, ordenadas alfabéticamente,
# sin repetirlas. Una palabra capicúa es la que es exactamente igual al invertirla.

"""def palabras_capicuas(palabras):
    capicuas = []
    for palabra in palabras:
        if palabra == palabra[::-1]:
            capicuas += [palabra]
    print("Palabras capicuas:", sorted(capicuas))

def main():
    texto = input("Ingrese un texto: ")
    palabras_capicuas(texto.split())

main()"""

# 7. Ingresar en un diccionario pares de datos con una clave que será el nombre de una ONG (Organización No
# Gubernamental) y el monto que será una donación. Una misma clave se puede ingresar varias veces. Se pide:
# a. Calcular el total recaudado para cada ONG e imprimirlo sin importar un orden.
# b. Imprimir el listado anterior ordenado de mayor a menor por cantidad recaudado, indicando: cantidad – ONG

"""def solicitar_datos():
    datos = {}
    ong = input("Ingrese el nombre de la ONG o 0 para salir: ")
    while ong != '0':
        donacion = float(input("Ingrese donacion: "))
        if ong in datos:
            datos[ong] += donacion
        else:
            datos[ong] = donacion
        ong = input("Ingrese el nombre de la ONG o 0 para salir: ")
    return datos

def main():
    datos = solicitar_datos()
    print("Recaudacion final, sin importar el orden:")
    for claves in datos:
        print("ONG:", claves, "|| Recaudacion:", datos[claves])
    print("Por orden de mayor recaudacion:")
    datos_finales_ordenados = sorted(datos.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(datos_finales_ordenados)):
        print("Recaudado:", datos_finales_ordenados[i][1], "|| ONG:", datos_finales_ordenados[i][0])

main()"""