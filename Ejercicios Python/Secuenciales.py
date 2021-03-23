# 1. Leer un número por teclado e imprimirlo en pantalla con el siguiente cartel:
# “Número ingresado = ” número.

'''numero = int(input('Ingrese un numero: '))
print('Numero ingresado = ', numero)'''

'''2. Pedir al usuario que ingrese dos números por teclado e imprimir
- La suma de ambos
- La resta (el primero menos el segundo)
- La multiplicación
- La división entera (suponer que el segundo número no es cero).
- La división con decimales.'''

'''num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

print('La suma de ambos numeros es: ', num1 + num2)
print('La resta entre ellos es: ', num1 - num2)
print('La multiplicacion entre ellos es: ', num1 * num2)
print('La division entera entre ellos es: ', int(num1/num2))
print('La division con decimales entre ellos es: ', float(num1/num2))'''

# 3. Escribir un programa que lea el nombre de una persona y, luego, lo salude.

'''nombre = input('Ingrese un nombre: ')
print('Hola ', nombre) '''


#  4. Dado el radio R de una esfera, calcular e imprimir su superficie y su volumen.

'''radio = int(input('Ingrese el radio de la esfera: '))
print('El volumen de la esfera es: ', int((4/3)*(radio**3)*3.1415), 'y la superficie es: ', int(4*3.1415*(radio**2)))'''

#5. Leer la base y la altura de un rectángulo, calcular el perímetro y la superficie.

'''base = int(input('Ingrese la medida de la base del rectangulo: '))
altura = int(input('Ingrese la medida de la altura del rectangulo: '))
print('El perimetro del rectangulo es: ', (base*2 + altura*2), 'y la superficie es: ', base*altura)'''

#6. Leer dos números A y B e intercambiar el valor de sus variables.

"""a = int(input("Ingrese numero A: "))
b = int(input("Ingrese numero B: "))
aux = a
a = b
b = aux
print("Ahora el numero A es:", a, "y el numero B es:", b)"""
