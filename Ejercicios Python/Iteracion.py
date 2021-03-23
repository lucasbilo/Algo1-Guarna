# 1. Imprimir por pantalla una lista de 20 números consecutivos, los cuales
# comienzan con un número ingresado por teclado.

"""num = int(input('Ingrese un numero: '))
for i in range(num, num + 21):
    print(i)"""

# 2. Leer un número N y calcular su factorial.

"""n = int(input('Ingrese un numero: '))
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print('El factorial del numero elegido es: ', factorial)"""

# 3. Leer una serie de números enteros, terminando la serie con un cero. Imprimir
# los datos a medida que se los ingresa junto con la suma parcial de los mismos.

"""suma_parcial = 0
num = int(input('Ingrese un numero entero o 0 para salir: '))
while num != 0:
    suma_parcial += num
    print('Suma parcial de los numeros ingresados: ', suma_parcial)
    num = int(input('Ingrese un numero entero o 0 para salir: '))"""

# 4. Dada una serie de números enteros, determinar el valor máximo, mínimo y las
# posiciones en que éstos se encontraban en la serie. El programa deberá ir
# preguntando si hay más números para ingresar

"""num_max = 0
num_min = 1000000
contador = 0
pos_max = 0
pos_min = 0
seguir= 's'

while seguir == 's':
    num = int(input('Ingrese un numero entero, como maximo puede ser 1.000.000: '))
    contador +=1
    if num > num_max:
        num_max = num
        pos_max = contador
    if num < num_min:
        num_min = num
        pos_min = contador
    seguir = input('Desea seguir? (s/n): ')

print('Se ingresaron ', contador, 'numeros')
print('El numero maximo es: ', num_max, 'y se ubica en la posicion ', pos_max)
print('El numero minimo es: ', num_min, 'y se ubica en la posicion ', pos_min) """

# 5. Leer un valor N y, luego, N números enteros. Se pide imprimir el mayor, el menor
# y las veces que aparece cada uno.    (SIN TERMINAR!!!, falta ver como hacer los contadores)

"""n = int(input('Ingrese un valor: '))
num = int(input('Ingrese un numero: '))
num_max = num
num_min = num
cont_max = 0
cont_min = 0

for i in range(1, n):
    num = int(input('Ingrese un numero: '))
    if num > num_max:
        num_max = num
    if num < num_min:
        num_min = num

print('El numero maximo es: ', num_max, 'y aparece ', cont_max, 'veces')
print('El numero minimo es: ', num_min, 'y aparece ', cont_min, 'veces') """

# 6. Leer A y B, enteros. Calcular C = A x B mediante sumas sucesivas e imprimir el
# resultado

"""a = int(input('Ingrese un numero entero(A): '))
b = int(input('Ingrese un numero entero(B): '))
c = 0

for i in range(1, b+1):
    c += a

print(c)"""

#7. Leer A y B, enteros. Calcular C = A^B mediante multiplicaciones sucesivas e imprimir el resultado. Tener en cuenta
# que son números enteros, por lo tanto pueden tomar valores positivos, negativos o cero.

"""a = int(input('Ingrese un numero entero(A): '))
b = int(input('Ingrese un numero entero(B): '))
c = 1
for i in range(1, b + 1):
    c *= a
print("A^B  es: ", c)"""


# 8. Escribir un algoritmo que indique si un número entero, ingresado por un usuario, es primo.

"""def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if (numero % i) == 0:
            contador += 1
    if contador == 2:
        print("El numero es primo")
    else:
        print("El numero no es primo")"""

#9. Dada una serie de números enteros terminada en cero, imprimir los tres mayores.

"""numero = int(input('Ingrese un numero o 0 para salir: '))
num1_max = numero
num2_max = 0
num3_max = 0

while numero != 0:
    numero = int(input('Ingrese un numero o 0 para salir: '))
    if numero > num1_max:
        num3_max = num2_max
        num2_max = num1_max
        num1_max = numero
    elif numero > num2_max:
        num3_max = num2_max
        num2_max = numero
    elif numero > num3_max:
        num3_max = numero

print('Los 3 numeros maximos ingresados son: ', num1_max, num2_max, num3_max) """

#10. Dada una serie de nombres y salarios respectivos, determinar el salario máximo,
# el mínimo y la persona que percibe cada uno. No se deben guardar todos los datos.

"""nombre = input('Ingrese el nombre: ')
salario = int(input('Ingrese el salario: '))
salario_max = salario
salario_min = salario
nombre_max = nombre
nombre_min = nombre
seguir = input('Desea seguir ingresando datos? (s/n): ')

while seguir == 's':
    nombre = input('Ingrese el nombre: ')
    salario = int(input('Ingrese el salario: '))
    if salario > salario_max:
        salario_max = salario
        nombre_max = nombre
    if salario < salario_min:
        salario_min = salario
        nombre_min = nombre
    seguir = input('Desea seguir ingresando datos? (s/n): ')

print('El salario maximo es de ', salario_max, 'y corresponde a ', nombre_max)
print('El salario minimo es de ', salario_min, 'y corresponde a ', nombre_min)"""