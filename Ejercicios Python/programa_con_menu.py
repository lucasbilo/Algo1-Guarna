#Escribir un programa modular, dividiendo en funciones, que cumpla con los siguientes requerimientos.
#Al iniciar al programa, se debe mostrar al usuario un menú que contenga 3 opciones:
#-Realizar operaciones con numeros.
#-Realizar operaciones con cadenas de caracteres.
#-Salir del programa.
#Si el usuario decide realizar operaciones con numeros, debemos mostrar un submenú que contenga las siguientes
#opciones:
#-Calcular el factorial de un numero (pedir el valor por pantalla).
#-Calcular la multiplicacion entre dos numeros por sumas sucesivas.
#-Calcular la potencia entre dos numeros (n ^ m).
#-Calcular la división por restas (se debe imprimir el resto).
#-Volver al menú principal.
#Si el usuario decide realizar operaciones con cadenas de caracteres, debemos mostrar un submenú que contenga
#las siguientes opciones:
#-Calcular la longitud de una frase que ingrese el usuario (asumir que las palabras vienen separadas por espacio).
#-Imprimir la palabra que ingrese el usuario, sin vocales.
#-Volver al menú principal.
#Al final del programa, se debe imprimir ordenadamente la cantidad de operaciones de cada tipo que realizó el usuario.

OPCION_MENU_NUMEROS = 1
OPCION_MENU_STRINGS = 2
OPCION_CALCULAR_FACTORIAL = 1
OPCION_CALCULAR_MULTIPLICACION = 2
OPCION_CALCULAR_POTENCIA = 3
OPCION_CALCULAR_DIVISION = 4
OPCION_CALCULAR_LONGITUD = 1
OPCION_PALABRA_SIN_VOCALES = 2

def mostrar_menu_principal():
    print("1- Realizar operaciones con numeros.")
    print("2- Realizar operaciones con cadenas de caracteres.")
    print("3- Salir del programa.")

def mostrar_menu_numeros():
    print("1- Calcular el factorial de un numero.")
    print("2- Calcular la multiplicacion entre dos numeros por sumas sucesivas.")
    print("3- Calcular la potencia entre dos numeros.")
    print("4- Calcular la division por restas.")
    print("5- Volver al menu principal")

def mostrar_menu_caracteres():
    print("1- Calcular la longitud de una frase. (se tienen en cuenta los espacios)")
    print("2- Imprimir la palabra que ingrese sin vocales.")
    print("3- Volver al menu principal.")

def pedir_opcion(mayor_restriccion):
    opcion = int(input("Ingrese una opcion: "))
    while opcion < 0 or mayor_restriccion < opcion:
        opcion = int(input("Por favor ingrese una opcion valida: "))
    return opcion

def pedir_numero_positivo(mensaje):
    print(mensaje)
    numero = int(input("Por favor ingrese un numero positivo: "))
    while numero < 0:
        numero = int(input("Numero negativo. Por favor ingrese un numero positivo: "))
    return numero

def calcular_factorial():
    numero = pedir_numero_positivo("Ingrese numero a calcular factorial.")
    resultado_factorial = 1
    for i in range(1, numero + 1):
        resultado_factorial *= i
    print("El factorial del numero ingresado es: ", resultado_factorial)

def multiplicacion_por_sumas():
    resultado_multiplicacion = 0
    numero_uno = pedir_numero_positivo("Ingrese el primer numero.")
    numero_dos = pedir_numero_positivo("Ingrese el segundo numero.")
    for i in range(1, numero_dos + 1):
        resultado_multiplicacion += numero_uno
    print("El resultado de la multiplicacion por sumas sucesivas entre los numeros ingresados es ", resultado_multiplicacion)

def calcular_potencia():
    base = pedir_numero_positivo("Ingrese el numero base.")
    exponente = pedir_numero_positivo("Ingrese el numero exponente.")
    resultado_potencia = base

    for i in range(1, exponente):
        resultado_potencia *= base
    print("El resultado de elevar ", base, "a ", exponente, "es de ", resultado_potencia)

def division_por_restas():
    dividiendo = pedir_numero_positivo("Ingrese el dividiendo.")
    divisor = pedir_numero_positivo("Ingrese el divisor.")
    resultado_division = 0
    while dividiendo >= divisor:
        resultado_division += 1
        dividiendo -= divisor
    print("El resultado de la division por restas sucesivas es de ", resultado_division, "y el resto es ", dividiendo)

def calcular_longitud_frase():
    frase = str(input("Por favor ingrese su frase: "))
    longitud_frase = len(frase)
    print("La longitud de la frase ingresada es de ", longitud_frase)

def palabra_sin_vocales():
    pass

def menu_operaciones_con_numeros():
    opcion_ingresada = 0
    while opcion_ingresada != 5:
        mostrar_menu_numeros()
        opcion_ingresada = pedir_opcion(5)
        if opcion_ingresada == OPCION_CALCULAR_FACTORIAL:
            calcular_factorial()
        elif opcion_ingresada == OPCION_CALCULAR_MULTIPLICACION:
            multiplicacion_por_sumas()
        elif opcion_ingresada == OPCION_CALCULAR_POTENCIA:
            calcular_potencia()
        elif opcion_ingresada == OPCION_CALCULAR_DIVISION:
            division_por_restas()

def menu_operaciones_con_caracteres():
    opcion_ingresada = 0
    while opcion_ingresada != 3:
        mostrar_menu_caracteres()
        opcion_ingresada = pedir_opcion(3)
        if opcion_ingresada == OPCION_CALCULAR_LONGITUD:
            calcular_longitud_frase()
        elif opcion_ingresada == OPCION_PALABRA_SIN_VOCALES:
            palabra_sin_vocales()

def main():
    opcion_ingresada = 0
    while opcion_ingresada != 3:
        mostrar_menu_principal()
        opcion_ingresada = pedir_opcion(3)
        if opcion_ingresada == OPCION_MENU_NUMEROS:
            menu_operaciones_con_numeros()
        elif opcion_ingresada == OPCION_MENU_STRINGS:
            menu_operaciones_con_caracteres()
    print("Gracias por utilizar mi programa.")

main()