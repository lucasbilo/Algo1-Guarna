# Realizar un algoritmo que simule el sistema de un estacionamiento, el garage cuenta como minimo de un piso, y en el
# de haber mas de un piso, todos son iguales.
# Pedir al usuario cantidad de pisos, filas y columnas, $inicial.
# Al ingresar un vehiculo guardar patente, tipo(auto o camioneta), hs de entrada, lugar donde estaciona.
# Marcar ocupado en los lugares donde estacionan autos.
# % de ocupacion por piso.
# Al retirarse un auto: desmarcar el lugar que deja libre y cobrar : (Auto: $100/hs, Camioneta: $150/hs)
# Cierre de caja: $inicial + ganancias
# % de ganancias por tipo de vehiculo.

from time import time
OPCION_INGRESO_VEHICULO = 1
OPCION_EGRESO_VEHICULO = 2
OPCION_PORCENTAJE_POR_PISO = 3
OPCION_PORCENTAJE_GANANCIA_TIPO_VEHICULO = 4
OPCION_CAJA_CERRADA = 5

def mostrar_menu_principal():
    print("¡MENU PRINCIPAL!")
    print("1- Ingreso de vehiculo.")
    print("2- Egreso de un vehiculo.")
    print("3- Porcentaje de ocupacion por piso.")
    print("4- Porcentaje de ganancia por tipos de vehiculos.")
    print("5- Caja al cierre del dia.")

def pedir_opcion(mayor_restriccion):
    #Pedir opcion de algún menu, debo pasarle la maxima opcion que puede poner.
    opcion = int(input("Por favor ingrese una opcion o 0 para salir: "))
    while ((opcion < 0) or (opcion > mayor_restriccion)):
        opcion = int(input("Por favor ingrese una opcion correcta: "))
    return opcion

def marcar_ocupado(estacionamiento):
    pass

def crear_vehiculo(patente, tipo, hs_ingreso, piso, fila, columna):
    vehiculo = {patente: {'Tipo': tipo, 'Hs_ingreso': hs_ingreso, 'Piso': piso, 'Fila': fila, 'Columna': columna}}
    return vehiculo

def ingreso_vehiculo():
    patente = input("Ingrese la patente del vehiculo: ")
    tipo = input("Ingrese el tipo de vehiculo (A/C): ")
    while tipo != 'A' and tipo != 'C':
        tipo = input("Tipo de vehiculo incorrecto, vuelva a intentarlo:")
    hs_ingreso = time()
    piso = int(input("Ingrese el piso donde estaciono el vehiculo: "))
    fila = int(input("Ingrese la fila donde estaciono el vehiculo: "))
    columna = int(input("Ingrese la columna donde estaciono el vehiculo: "))
    vehiculo = {patente: {'Tipo': tipo, 'Hs_ingreso': hs_ingreso, 'Piso': piso, 'Fila': fila, 'Columna': columna}}
    print(vehiculo)

def egreso_vehiculo():
    pass
def porcentaje_por_piso():
    pass
def porcentaje_ganancia_vehiculo():
    pass
def caja_cerrada():
    pass

def ir_opcion_elegida_menu_principal(opcion):
    # Voy a la opcion que eligio en el menu principal.
    if opcion == OPCION_INGRESO_VEHICULO:
        ingreso_vehiculo()
    elif opcion == OPCION_EGRESO_VEHICULO:
        egreso_vehiculo()
    elif opcion == OPCION_PORCENTAJE_POR_PISO:
        porcentaje_por_piso()
    elif opcion == OPCION_PORCENTAJE_GANANCIA_TIPO_VEHICULO:
        porcentaje_ganancia_vehiculo()
    else:
        caja_cerrada()

def generar_estacionamiento(filas, columnas, pisos = 1):
    #Creo el estacionamiento con los datos que me brinda el usuario.
    estacionamiento = []
    for i in range(pisos):
        estacionamiento.append([])
        for j in range(filas):
            estacionamiento[i].append([])
            for k in range(columnas):
                estacionamiento[i][j].append(False)
    return estacionamiento

def pedir_datos_estacionamiento():
    print("Por favor ingrese los datos del estacionamiento.")
    pisos = int(input("Cantidad de pisos: "))
    filas = int(input("Cantidad de filas que tiene cada piso: "))
    columnas = int(input("Cantidad de columas que tiene cada piso: "))
    dinero_inicial = float(input("Cantidad de dinero inicial: "))
    return generar_estacionamiento(filas, columnas, pisos)


def main():
    estacionamiento = pedir_datos_estacionamiento()
    mostrar_menu_principal()
    opcion_elegida = pedir_opcion(5)
    ir_opcion_elegida_menu_principal(opcion_elegida)

main()