#Escribir un programa en Python que:
# 1) Solicitar el ingreso de un texto asegurando que tenga entre 150 y 500 palabras.
# 2) Imprimir sin repetir las palabras que tengan como minimo 5 caracteres y que comiencen con vocal.
# 3) Solicitar el ingreso de otro texto que contengan entre 10 y 50 palabras e indicar si el mismo esta ingresado en el
# primer texto ingresado o si al menos las palabras estan en el primer texto.
# 4) Genere un ranking de palabras por c/u de los textos, mostrando las palabras y la cantidad de veces que aparece la
# la misma ordenado descendentemente por la cantidad. Luego generar otro para la suma de ambos textos.


def solicitar_texto(min_palabras, max_palabras):
    texto = input("Por favor ingrese el texto: ")
    palabras = texto.split()
    while (len(palabras) < min_palabras):
        texto += " " + input("Texto demasiado corto, siga ingresando: ")
        palabras = texto.split()
    if (len(palabras) > max_palabras):
        palabras = palabras[0: max_palabras]
    return palabras

def imprimir_palabras_5_caracteres(palabras):
    print("Palabras con al menos 5 caracteres y que empiezan con vocal: ")
    palabras.sort()
    palabra_anterior = ''
    for palabra in palabras:
        while palabra != palabra_anterior:
            if (len(palabra) >= 5) and (palabra[0] in "AEIOUaeiou"):
                print(palabra)
                palabra_anterior = palabra

def comparar_textos(lista_uno, lista_dos):
    #SOLO COMPARA SI LAS PALABRAS DEL TEXTO2 ESTAN EN EL TEXTO1, SIN IMPORTAR EL ORDEN!
    contador = 0
    for palabras in lista_dos:
        if palabras in lista_uno:
            contador += 1
    if (len(lista_dos) == contador) or (len(lista_uno) < contador):
        print("Todas las palabras del texto dos están en el texto uno")
    else:
        print("Al menos una palabra del texto dos no se encuentran en el texto uno")


def ranking_palabras(palabras):
    ranking = {}
    for palabra in palabras:
        if palabra in ranking:
            ranking[palabra] += 1
        else:
            ranking[palabra] = 1
    return sorted(ranking.items(), key=lambda x: x[1], reverse=True)


# Principal:
def main():
    print("Texto que contengan entre 150 y 500 palabras.")
    palabras_uno = solicitar_texto(5, 500)
    imprimir_palabras_5_caracteres(palabras_uno)
    print("Texto que contengan entre 10 y 50 palabras.")
    palabras_dos = solicitar_texto(5, 50)
    comparar_textos(palabras_uno, palabras_dos)
    ranking_texto_uno = ranking_palabras(palabras_uno)
    ranking_texto_dos = ranking_palabras(palabras_dos)
    ranking_suma_textos = ranking_palabras(palabras_uno + palabras_dos)
    print("El ranking de palabras del primer texto es: ", ranking_texto_uno)
    print("El ranking de palabras del segundo texto es: ", ranking_texto_dos)
    print("El ranking de palabras de la suma de los textos es: ", ranking_suma_textos)

main()