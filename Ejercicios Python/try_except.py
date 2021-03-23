"""def lee_entero(entrada):
    try:
        entrada = int(entrada)
        return entrada
    except ValueError:
        entrada = input("La entrada es incorrecta: escribe un numero entero")"""

def lee_entero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero")

print(type(lee_entero('ingrese numerooooo')))