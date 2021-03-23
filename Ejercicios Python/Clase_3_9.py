# NOTA: Los siguientes ejercicios fueron realizados el dia 03-09. Prestar atencion a su resolucion
# (de aquellos que estan resueltos), analizando las instrucciones utilizadas y comprendiendo el por que de cada cosa.
# En caso de no entender, utilizar el foro para realizar consultas. Todo tipo de sugerencia es bienvenida.
# Se recomienda volver a realizar todos los ejercicios a modo de practica, especialmente aquellos que 
# quedaron sin resolver. 

# Escribir un programa que solicite el ingreso de notas a su usuario. Utilizar s/n para indicar si seguir ingresando o no.
# Una vez que el usuario decide terminar el ingreso, imprimir el promedio de las notas ingresadas.
'''contador_notas = 0
acumulador_notas = 0
seguir_ingresando = 's'
while seguir_ingresando == 's':
    nota = int(input('Ingrese una nota: '))
    acumulador_notas += nota
    contador_notas += 1
    seguir_ingresando = input('Desea seguir ingresando notas? s/n ')

print('El promedio de notas es:', acumulador_notas/contador_notas)'''

# Escribir un programa que solicite el ingreso de notas y nombres a un usuario
# (se ingresa una de cada una por ciclo).
# Una vez que el usuario decide terminar el ingreso, imprimir al alumno con mayor
# nota y al de menor nota
# con las respectivas notas.
# Podemos asumir que se ingresan por lo menos dos alumnos con notas distintas.
'''nota_max = 0
nota_min = 11
alumno_max = ''
alumno_min = ''
seguir = 's'
while seguir == 's':
    nombre = input('Ingrese el nombre del alumno: ')
    nota = int(input('Ingrese su nota: '))
    if nota > nota_max:
        alumno_max = nombre
        nota_max = nota
    if nota < nota_min:
        alumno_min = nombre
        nota_min = nota
    seguir = input('Desea ingresar otro alumno? (s/n): ')
print('El alumno', alumno_max, 'obtuvo la nota mas alta con: ', nota_max)
print('El alumno', alumno_min, 'obtuvo la nota mas baja con: ', nota_min)'''

# Escribir un programa que solicite al usuario un numero por pantalla.
# Imprimir, por pantalla, todos los numeros pares elevados al cuadrado
# en el intervalo de 1 hasta el numero ingresado (1, n) (n inclusive).

'''numero = int(input('Ingrese un numero '))
for x in range (2, numero + 1, 2):
    print(x**2)'''

# Escribir un programa que solicite al usuario un numero por pantalla.
# Validar que el numero sea mayor a 0.
# Para todo n entre 0 y el numero ingresado, imprimir la suma de todos los numeros anteriores (es decir, la suma de
#  todos los intervalos entre 0 y n).
# Se debe proveer al usuario una forma tal que pueda efectuar el flujo anterior la cantidad de veces que desee.

'''seguir = "s"
while seguir == "s":
    n = int(input("Ingrese un numero mayor a 1: "))
    while n <= 0:
        n = int(input("Se equivoco. Ingrese un numero mayor a 0: "))
    
    suma = 0

    for i in range (1, n):
        suma += i
    print("La suma da como resultado:", suma)
    seguir = input("Desea volver a ingresar? s/n")'''


# Escribir un programa que solicite al usuario un numero positivo por pantalla.
# Si no es positivo, pedirle que vuelva a reingresar el numero.
# Para el numero ingresado, calcular e imprimir su factorial.
# f(n) = 1 x 2 x 3 x .. x (n-1) x n

'''numero_ingresado = int(input("Ingrese un numero positivo: "))

while numero_ingresado <= 0:
    numero_ingresado = int(input("Ingrese un numero positivo: "))

resultado = 1

for i in range(2, numero_ingresado + 1):
    resultado *= i

print("El resultado de f es ", resultado)'''

#Ejercicio de finanzas personales.
#Escribir un programa que permita al usuario ingresar un numero, que representa los ahorros del usuario.
#Luego, pedirle que ingrese otro numero, que respresenta una cantidad de años.
#Una vez que se tengan los ahorros y los años, imprimir cual es el monto obtenido por el usuario
#al final de cada año, teniendo en cuenta una tasa anual efectiva del 5%.

ahorros = float(input('Ingrese sus ahorros: '))
anios = int(input('Ingrese cantidad de anios: '))
for x in range(1, anios + 1):
    ahorros += (ahorros * 0.05)
    print('Sus ahorros al anio ', x, ' son de', ahorros)

