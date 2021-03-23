import random

intentos = 1
num_a_adivinar = int(random.randint(0, 1000))
numero = int(input("Ingrese un numero entre 0 y 1000, tiene 7 intentos!: "))

while intentos < 7:
    if num_a_adivinar > numero:
        numero = int(input("El numero es mayor! Vuelva a intentarlo: "))
        intentos += 1
    elif num_a_adivinar < numero:
        numero = int(input("El numero es menor! Vuelva a intentarlo: "))
        intentos += 1
    else:
        print("Ganaste!")
        intentos += 8

if intentos == 7:
    print("No adivino el numero en 7 intentos, perdio!")