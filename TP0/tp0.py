
#Pre: Recibe dos palabras previamente inicializadas.
#Post: Devuelve la cantidad de letras que suman ambas palabras.
def sumarLetras (palabra1, palabra2):
    return len(palabra1) + len(palabra2)


#Pre: Recibe dos palabras previamente inicializadas.
#Post: Devuelve true en caso de que la palabra uno sea mas larga que la dos, false en caso contrario.
#Si las palabras tienen la misma longitud, devuelve un 1.
def determinarPalabraMasLarga(palabra1, palabra2):
    if len(palabra1) > len(palabra2):
        return True
    elif len(palabra1) < len(palabra2):
        return False
    else:
        return 1

#Pre: Recibe tres valores previamente inicializados: horas, minutos y segundos.
#Post: Devuelve la duracion en segundos del intervalo de tiempo que surge de la suma de la duracion
#en segundos de los tres parametros. EJ: horas: 1, minutos: 3, segundos: 117 devuelve: 3897
def cantidadDeSegundos(horas, minutos, segundos):
    return ((horas*3600) + (minutos*60) + segundos)
    

#Pre: Recibe un numero previamente inicializado.
#Post: Devuelve 1 si el numero es par, 0 en caso contrario.
def esPar(numero):
    if numero % 2 == 0:
        return 1
    else:
        return 0
    
#Pre: Recibe tres numeros previamente inicializados.
#Post: Devuelve el mayor producto entre dos de ellos
#EJ: Si recibe (5,3,8), debe devolver 40.
def mayorProducto(numeroUno, numeroDos, numeroTres):
   return ((numeroUno*numeroDos*numeroTres) / min(numeroUno, numeroDos, numeroTres))
