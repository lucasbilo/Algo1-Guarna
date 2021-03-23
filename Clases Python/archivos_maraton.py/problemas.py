'''La funcion debe considerar infinito al string pasado como parametro.
Por ejemplo, si se recibe 'abc', debe considerarse 'abcabcabcabcabc..' hasta el infinito.
Se debe devolver la cantidad de veces que aparece el caracter pasado como parametro
en las primeras n letras del string infinito.
Por ejemplo: Se recibe 'aba', 10, a.
El string es 'abaabaabaabaaba...' y vemos que en las primeras 10 letras el caracter a
aparece 7 veces.
'''
def repeated_string(string, n, character):
    contador = 0
    string_infinito = string * n
    for i in range(n):
        if string_infinito[i] == character:
            contador += 1
    return contador

'''Rota los elementos de una lista tantas posiciones como
las recibidas como parametro. Si la cantidad de posiciones
es mayor a la cantidad de elementos en la lista, se debe lanzar
la excepcion IndexError.
Ejemplo 1: [1,2,3,4] con 1 posicion es: [2,3,4,1].
Ejemplo 2: [1,2,3,4] con 2 posicioens es: [3,4,1,2]'''
def left_rotation(list_to_rotate, positions):
    if len(list_to_rotate) < positions:
        raise IndexError
    else:
        for i in range(positions):
            numero = list_to_rotate.pop(0)
            list_to_rotate.append(numero)
        return list_to_rotate

'''Devuelve una lista con todas las subcadenas que estan contenidas
en ambas cadenas. La subcadena de longitud minima es 1.
Ejemplo: vaca, vacaciones -> [v,a,c,va,ac,ca,vac,aca,vaca]
'''
def substring_share(first_string, second_string):
    lista = []
    num = 0
    variable = len(first_string) + 1
    for i in range(len(first_string)):
        for j in range(1, variable):
            if (first_string[i:j+num] in second_string) and (first_string[i:j+num] not in lista):
                lista.append(first_string[i:j+num])
        num += 1
        variable -= 1
    return lista

'''
Devuelve true si las cadenas que recibe son anagramas.
Dos cadenas son anagramas si reordenando los caracteres de una
puedo formar la otra.
'''
def anagrams(first_string, second_string):
    contador = 0
    for i in range(len(first_string)):
        if first_string[i] in second_string:
            contador += 1
    if (contador == len(first_string)) and (contador == len(second_string)):
        return True
    return False

'Recibe un numero y devuelve el binario asociado a ese numero'
def binary(number):
    binario = ''
    while number // 2 != 0:
        binario += str(number % 2)
        number = number // 2
    return str(number) + binario
