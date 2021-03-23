#Ejercicio 1: Se pide un programa que registre el resultado de una votación. Para esto, se le debe pedir a un usuario
# que ingrese votos (únicamente el nombre del partido político) hasta que decida finalizar. Una vez que finalice,
# se debe imprimir ordenadamente (de mayor a menor) el resultado de la votación (es decir, cada partido político con
# la cantidad de votos correspondientes)

"""def resultado_votaciones():
    resultado = {}
    partido = input("Ingrese el nombre del partido o 0 para salir: ")
    while partido != '0':
        if partido in resultado:
            resultado[partido] += 1
        else:
            resultado[partido] = 1
        partido = input("Ingrese el nombre del partido o 0 para salir: ")
    return sorted(resultado.items(), key=lambda x: x[1], reverse=True)

def main():
    resultado_final = resultado_votaciones()
    print("Resultado finales: ")
    for x in resultado_final:
        print("Partido : ", x[0], "\nVotos: ", x[1])

main()"""

#Ejercicio 2: Se pide un programa que analice promedios de alumnos universitarios. Para esto, se debe pedir al usuario
# que ingrese un alumno con 3 notas hasta que este decida finalizar. Una vez que termina, se debe obtener el promedio
# de cada uno de ellos, para finalmente imprimir a por pantalla los 3 alumnos cuyo promedio sea el más alto.

"""def calcular_promedios(datos):
    promedios = {}
    for alumnos in datos:
        suma = 0
        for notas in datos[alumnos]:
            suma += notas
        promedios[alumnos] = suma / 3
    return sorted(promedios.items(), key=lambda x: x[1], reverse=True)

def pedir_y_guardar_datos_alumno():
    nombre = input("Por favor ingrese el nombre del alumno o 0 para salir: ")
    alumnos = {}
    while nombre != '0':
        nota_uno = int(input("Por favor ingrese la primer nota: "))
        nota_dos = int(input("Por favor ingrese la segunda nota: "))
        nota_tres = int(input("Por favor ingrese la tercer nota: "))
        alumnos[nombre] = [nota_uno, nota_dos, nota_tres]
        nombre = input("Por favor ingrese el nombre del alumno o 0 para salir: ")
    return alumnos

def main():
    alumnos = pedir_y_guardar_datos_alumno()
    promedios = calcular_promedios(alumnos)
    print("Alumnos con promedios mas altos: ")
    for i in range(3):
        print('Nombre: ', promedios[i][0], '\nPromedio: ', promedios[i][1])

main()"""

# Ejercicio 3: Optimizar el programa del ej 2 de forma tal que no esté limitado únicamente a que se ingresen 3 notas
# por alumnos, sino que se puedan ingresar n notas y que el usuario decida cuando parar.

#MAS O MENOS
"""def pedir_y_guardar_datos_alumno():
    alumnos = {}
    seguir = 's'
    contador = 1
    while seguir == 's':
        nombre = input("Por favor ingrese el nombre del alumno: ")
        nota = int(input("Por favor ingrese una nota: "))
        alumnos[nombre] = nota
        seguir_notas = input("Desea seguir ingresando notas? (s/n)")
        while seguir_notas == 's':
            nota = int(input("Por favor ingrese una nota: "))
            contador += 1
            alumnos[nombre] += nota
            seguir_notas = input("Desea seguir ingresando notas? (s/n)")
        alumnos[nombre] /= contador
        contador = 1
        seguir = input("Desea seguir ingresando datos de alumnos? (s/n)")
    return sorted(alumnos.items(), key=lambda x: x[1], reverse=True)

def main():
    alumnos = pedir_y_guardar_datos_alumno()
    print("Alumnos con promedios mas altos: ")
    for i in range(3):
        print('Nombre: ', alumnos[i][0], '\nPromedio: ', alumnos[i][1])

main()"""